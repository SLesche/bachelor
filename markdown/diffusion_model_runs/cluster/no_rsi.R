## ----setup------------------------------------------------------------------------------------
# Diffusion model packages
library(brms)
# cmdstanr
library(cmdstanr)
library(dplyr)

## ----data-------------------------------------------------------------------------------------
data <- rio::import("./bachelor/data/diffusion_data_robust.rdata")


## ----formula
formula <- bf(
  # No intercepts, bc this estimates parameters for each combination of
  # rsi and error_factor
  rt | dec(decision) ~ 0 + error_factor:stimulus,
  bs ~ 0 + error_factor,
  # because rsi and error_factor are known they can be used here
  # pre-error is not technically "known", but should affect bs and ndt nonetheless
  ndt ~ 0 + error_factor,
  bias ~ 0 + error_factor:previous_stimulus
)


## ----set-prior--------------------------------------------------------------------------------
prior <- c(
  # drift rate
  prior("normal(0, 5)", class = "b"), # drift rate, population
  
  # boundary separation
  set_prior("gamma(10, 5)", class = "b", dpar = "bs"), 
  # bs restricted to > 0, lb = 0
  
  # Non-decision time
  set_prior("gamma(1, 5)", class = "b", dpar = "ndt"),
  
  # Bias
  set_prior("beta(4, 4)", class = "b", dpar = "bias")
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
    b_bs = runif(tmp_dat$K_bs, 1.5, 3.5),
    b_ndt = runif(tmp_dat$K_ndt, 0.05, 0.1),
    b_bias = runif(tmp_dat$K_bias, 0.4, 0.6)
  )
}



## ----setup-model------------------------------------------------------------------------------
n_iter <- 3000
n_warmup <- 1000
n_chains <- 4
n_cores <- 8
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
  # save_pars = save_pars(all = TRUE),
  control = list(max_treedepth = max_depth, adapt_delta = adapt_delta),
  refresh = 500,
  seed = seed # reproducibility
)

## ----saving-ddm-classic-----------------------------------------------------------------------
save(fit_wiener, file = paste0("./bachelor/models/no_rsi.rda"),
     compress = "xz")

fit_wiener <- add_criterion(fit_wiener, criterion = "loo")

save(fit_wiener, file = paste0("./bachelor/models/model_comp/no_rsi.rda"),
     compress = "xz")

## posterior-predict
pred <- predict(fit_wiener,
                summary = FALSE,
                negative_rt = TRUE,
                ndraws = 500)

save(pred, file = "./bachelor/predictions/pred_no_rsi.rda")

