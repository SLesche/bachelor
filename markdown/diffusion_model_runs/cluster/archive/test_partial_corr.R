## ----setup------------------------------------------------------------------------------------
# Diffusion model packages
library(brms)

# cmdstanr
library(cmdstanr)

library(dplyr)

## ----functions--------------------------------------------------------------------------------



## ----data-------------------------------------------------------------------------------------
data <- rio::import("./bachelor/data/diffusion_data_robust.rdata")

data <- data %>% 
  filter(as.numeric(id) < 45)

## ----set-formula------------------------------------------------------------------------------
# Add no intercorr here ||
formula <- bf(
  # No intercepts, bc this estimates parameters for each combination of
  # rsi and error_factor
  rt | dec(decision) ~ 0 + rsi:error_factor:stimulus + (0 + rsi:error_factor:stimulus|id),
  bs ~ 0 + rsi:error_factor + (0 + rsi:error_factor|id),
  # because rsi and error_factor are known they can be used here
  # pre-error is not technically "known", but should affect bs and ndt nonetheless
  ndt ~ 0 + rsi:error_factor + (0 + rsi:error_factor|id),
  bias ~ 0 + previous_stimulus:error_factor + (0 + previous_stimulus:error_factor|id) # no reason for bias to vary TODO: intercept for bias
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
  set_prior("normal(0.5, 0.25)", class = "b", dpar = "bias", lb = 0, ub = 1),
  
  # Group-level
  set_prior("normal(0, 0.3)", class = "sd"),
  
  # Corr
  set_prior("lkj(1)", class = "cor")
)


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
    b_ndt = runif(tmp_dat$K_ndt, 0.05, 0.1), # rep for each dim in ndt
    b_bias = runif(tmp_dat$K_bias, 0.4, 0.6),
    sd_1 = runif(tmp_dat$M_1, 0.5, 1),
    z_1 = matrix(rnorm(tmp_dat$M_1*tmp_dat$N_1, 0, 0.01),
                 tmp_dat$M_1, tmp_dat$N_1),
    L_1 = diag(tmp_dat$M_1),
    sd_2 = runif(tmp_dat$M_2, 0.5, 1),
    z_2 = matrix(rnorm(tmp_dat$M_2*tmp_dat$N_2, 0, 0.01),
                 tmp_dat$M_2, tmp_dat$N_2),
    L_2 = diag(tmp_dat$M_2),
    sd_3 = runif(tmp_dat$M_3, 0.5, 1),
    z_3 = matrix(rnorm(tmp_dat$M_3*tmp_dat$N_3, 0, 0.01),
                 tmp_dat$M_3, tmp_dat$N_3),
    L_3 = diag(tmp_dat$M_3),
    sd_4 = runif(tmp_dat$M_4, 0.5, 1),
    z_4 = matrix(rnorm(tmp_dat$M_4*tmp_dat$N_4, 0, 0.01),
                 tmp_dat$M_4, tmp_dat$N_4),
    L_4 = diag(tmp_dat$M_4)
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


## ----fitting-model-location-------------------------------------------------------------------
fit_wiener_location <- brm(
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
  # init_r = 0.1,
  warmup = n_warmup, 
  chains = n_chains,
  backend = "cmdstanr",
  cores = n_cores,
  threads = threading(n_threads), 
  control = list(max_treedepth = max_depth, adapt_delta = adapt_delta),
  seed = seed # reproducibility
)


## ----saving-ddm-classic-----------------------------------------------------------------------
save(fit_wiener_location, file = paste0("./bachelor/models/test_partial_corr_", Sys.Date(), ".rda"),
     compress = "xz")

