## ----setup------------------------------------------------------------------------------------
# Diffusion model packages
library(brms)

# cmdstanr
library(cmdstanr)


## ----functions--------------------------------------------------------------------------------



## ----data-------------------------------------------------------------------------------------
data_location <- rio::import("./bachelor/data/diffusion_data_robust_good.rdata")


## ----set-formula------------------------------------------------------------------------------
# Add no intercorr here ||
formula <- bf(
  # No intercepts, bc this estimates parameters for each combination of
  # rsi and error_factor
  rt | dec(decision) ~ 0 + rsi:error_factor:stimulus + (0 + rsi:error_factor:stimulus||id),
  bs ~ 0 + rsi:error_factor + (0 + rsi:error_factor||id),
  # because rsi and error_factor are known they can be used here
  # pre-error is not technically "known", but should affect bs and ndt nonetheless
  ndt ~ 0 + rsi:error_factor + (0 + rsi:error_factor||id),
  bias ~ 0 + previous_stimulus:error_factor + (0 + previous_stimulus:error_factor||id) # no reason for bias to vary TODO: intercept for bias
  # just want to estimate intercept for bias?
  # TODO: maybe estimate intercept for bias? 
)


## ----set-prior--------------------------------------------------------------------------------
prior <- c(
  # drift rate
  prior("normal(0, 5)", class = "b"), # drift rate, population
  
  # boundary separation
  set_prior("gamma(10, 5)", class = "b", dpar = "bs", lb = 0), 
  # bs restricted to > 0, lb = 0
  
  # Non-decision time
  set_prior("gamma(1, 5)", class = "b", dpar = "ndt", lb = 0),
  
  # Bias
  set_prior("beta(4, 4)", class = "b", dpar = "bias", lb = 0, ub = 1),
  
  # Group level
  set_prior("gamma(2, 4)", class = "sd", lb = 0)
)

## ----temp-starting-values---------------------------------------------------------------------
tmp_dat_location <- make_standata(
  formula, 
  family = wiener(
    link_bs = "identity", 
    link_ndt = "identity",
    link_bias = "identity"
  ),
  data = data_location,
  prior = prior
)


## ----init-function----------------------------------------------------------------------------
initfun_location <- function() {# all pars in stancode need init here
  list(
    b = rnorm(tmp_dat_location$K),
    b_bs = runif(tmp_dat_location$K_bs, 1, 2),
    b_ndt = runif(tmp_dat_location$K_ndt, 0.05, 0.1), # rep for each dim in ndt
    b_bias = runif(tmp_dat_location$K_bias, 0.4, 0.6),
    sd_1 = runif(tmp_dat_location$M_1, 0.5, 1),
    z_1 = matrix(rnorm(tmp_dat_location$M_1*tmp_dat_location$N_1, 0, 0.01),
                 tmp_dat_location$M_1, tmp_dat_location$N_1),
    sd_2 = runif(tmp_dat_location$M_2, 0.5, 1),
    z_2 = matrix(rnorm(tmp_dat_location$M_2*tmp_dat_location$N_2, 0, 0.01),
                 tmp_dat_location$M_2, tmp_dat_location$N_2),
    sd_3 = runif(tmp_dat_location$M_3, 0.5, 1),
    z_3 = matrix(rnorm(tmp_dat_location$M_3*tmp_dat_location$N_3, 0, 0.01),
                 tmp_dat_location$M_3, tmp_dat_location$N_3),
    sd_4 = runif(tmp_dat_location$M_4, 0.5, 1),
    z_4 = matrix(rnorm(tmp_dat_location$M_4*tmp_dat_location$N_4, 0, 0.01),
                 tmp_dat_location$M_4, tmp_dat_location$N_4)    
  )
}


## ----setup-model------------------------------------------------------------------------------
n_iter <- 2000
n_warmup <- 1000
n_chains <- 4
n_cores <- 16
n_threads <- floor(n_cores/n_chains)
max_depth <- 15
adapt_delta <- 0.95
seed <- 1234

## ----fitting-model-location-------------------------------------------------------------------
fit_wiener_location <- brm(
  formula, 
  data = data_location,
  family = wiener(
    link_bs = "identity", 
    link_ndt = "identity",
    link_bias = "identity"
  ),
  prior = prior, 
  init = initfun_location,
  iter = n_iter, 
  # init_r = 0.1,
  warmup = n_warmup, 
  chains = n_chains,
  backend = "cmdstanr",
  cores = n_cores,
  threads = threading(n_threads), 
  control = list(max_treedepth = max_depth, adapt_delta = adapt_delta),
  refresh = 200,
  seed = seed # reproducibility
)


## ----saving-ddm-classic-----------------------------------------------------------------------
save(fit_wiener_location, file = paste0("./bachelor/models/hierarch_model_good.rda"),
     compress = "xz")

