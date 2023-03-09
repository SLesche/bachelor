## ----setup------------------------------------------------------------------------------------
# Diffusion model packages
library(brms)

# cmdstanr
library(cmdstanr)

# Dplyr
library(dplyr)

## ----functions--------------------------------------------------------------------------------


## ----setup-model------------------------------------------------------------------------------
n_iter <- 3000
n_warmup <- 1000
n_chains <- 4
n_cores <- 32
n_threads <- floor(n_cores/n_chains)
max_depth <- 15
adapt_delta <- 0.95
seed <- 1234



## ----data-------------------------------------------------------------------------------------
data <- rio::import("./bachelor/data/diffusion_data_location.rdata")



## ----formula----------------------------------------------------------------------------------
formula <- bf(
  # No intercepts, bc this estimates parameters for each combination of
  # rsi and error_factor
  rt | dec(decision) ~ 0 + rsi:error_factor:stimulus,
  bs ~ 0 + rsi:error_factor,
  # because rsi and error_factor are known they can be used here
  # pre-error is not technically "known", but should affect bs and ndt nonetheless
  ndt ~ 0 + rsi:error_factor,
  bias ~ 0 + rsi:previous_stimulus:error_factor
)

output <- list()

run_ddm <- function(participant){
  # Get data
  part_data = data[which(data$id == participant),]
  min_rt = min(part_data$rt)
  
  # Run ddm
  prior = c(
    # drift rate
    prior("normal(0, 5)", class = "b"), # drift rate, population
    
    # boundary separation
    set_prior("normal(1.5, 1)", class = "b", dpar = "bs", lb = 0), 
    # bs restricted to > 0, lb = 0
    
    # Non-decision time
    set_prior("normal(0.10, 0.1)", class = "b", dpar = "ndt", lb = 0, ub = min_rt),
    
    # Bias
    set_prior("normal(0.5, 0.25)", class = "b", dpar = "bias", lb = 0, ub = 1)
  )
  
  tmp_dat = make_standata(
    formula, 
    family = wiener(
      link_bs = "identity", 
      link_ndt = "identity",
      link_bias = "identity"
    ),
    data = part_data,
    prior = prior
  )
  
  initfun = function() {# all pars in stancode need init here
    list(
      b = rnorm(tmp_dat$K), 
      b_bs = runif(tmp_dat$K_bs, 1, 2),
      b_ndt = runif(tmp_dat$K_ndt, 0.05, 0.1),
      b_bias = runif(tmp_dat$K_bias, 0.4, 0.6)
    )
  }
  
  fit_wiener = brm(
    formula, 
    data = part_data,
    family = wiener(
      link_bs = "identity", 
      link_ndt = "identity",
      link_bias = "identity"
    ),
    prior = prior, 
    init = initfun,
    iter = n_iter, 
    warmup = n_warmup, 
    chains = n_chains,
    backend = "cmdstanr",
    cores = n_cores,
    threads = threading(n_threads),
    control = list(max_treedepth = max_depth, adapt_delta = adapt_delta),
    refresh = 100,
    seed = seed # reproducibility
  )
  
  # store output
  return(fit_wiener)
}

ids = as.numeric(unique(data$id))

for (i in ids){
  output[i] = run_ddm(ids[i])
}

## ----saving-ddm-classic-----------------------------------------------------------------------
save(output, file = paste0("./bachelor/models/ids_model_", Sys.Date(), ".rda"),
     compress = "xz")