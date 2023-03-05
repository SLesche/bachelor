## ----setup------------------------------------------------------------------------------------
# Diffusion model packages
library(brms)

# cmdstanr
library(cmdstanr)


## ----functions--------------------------------------------------------------------------------



## ----data-------------------------------------------------------------------------------------
data <- rio::import("./bachelor/data/diffusion_data_location.rdata")


## ----formula----------------------------------------------------------------------------------
formula <- bf(
  # No intercepts, bc this estimates parameters for each combination of
  # rsi and error_factor
  rt | dec(decision) ~ 0 + rsi:error_factor:stimulus,
    # TODO: Implement this! Model comparison?
  bs ~ 0 + rsi:error_factor,
    # because rsi and error_factor are known they can be used here
    # pre-error is not technically "known", but should affect bs and ndt nonetheless
  ndt ~ 0 + rsi:error_factor,
  bias ~ 0 + previous_stimulus:previous_trial_type:previous_acc # no reason for bias to vary TODO: intercept for bias
    # just want to estimate intercept for bias?
    # TODO: maybe estimate intercept for bias? 
)


## ----set-prior--------------------------------------------------------------------------------
prior <- c(
 # drift rate
 prior("normal(0, 5)", class = "b"), # drift rate, population

 # boundary separation
 set_prior("normal(1.5, 1)", class = "b", dpar = "bs", lb = 0), 
  # bs restricted to > 0, lb = 0
 
 # Non-decision time
 set_prior("normal(0.15, 0.1)", class = "b", dpar = "ndt", lb = 0),
 
 # Bias
 set_prior("normal(0.5, 0.25)", class = "b", dpar = "bias", lb = 0, ub = 1)
)


## ----stan-code-check--------------------------------------------------------------------------
# Check that all parameters listed
make_stancode(formula, # default transformations
              family = wiener(link_bs = "identity", 
                              link_ndt = "identity",
                              link_bias = "identity"),
              data = data, 
              prior = prior)



## ----temp-starting-values---------------------------------------------------------------------
tmp_dat <- make_standata(
  formula, 
  family = wiener(
    link_bs = "identity", 
    link_ndt = "identity",
    link_bias = "identity"
    ),
  data = data,
  prior = prior
  )


## ----init-function----------------------------------------------------------------------------
initfun <- function() {# all pars in stancode need init here
  list(
    b = rnorm(tmp_dat$K), 
    b_bs = runif(tmp_dat$K_bs, 1, 2),
    b_ndt = runif(tmp_dat$K_ndt, 0.05, 0.1),
    b_bias = runif(tmp_dat$K_bias, 0.4, 0.6)
  )
}



## ----setup-model------------------------------------------------------------------------------
n_iter <- 3000
n_warmup <- 1000
n_chains <- 4
n_cores <- 16
n_threads <- floor(n_cores/n_chains)
max_depth <- 15
adapt_delta <- 0.99
seed <- 1234

model_setup_values <- data.frame(n_iter, n_warmup, n_chains, n_cores, n_threads, max_depth,
                                 adapt_delta, seed)


## ----fitting-model-classic--------------------------------------------------------------------
fit_wiener <- brm(
  formula, 
  data = data,
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
  refresh = 20,
  seed = seed # reproducibility
  )


## ----saving-ddm-classic-----------------------------------------------------------------------
save(fit_wiener, file = paste0("./bachelor/models/location_standard_bias_", Sys.Date(), ".rda"),
     compress = "xz")

