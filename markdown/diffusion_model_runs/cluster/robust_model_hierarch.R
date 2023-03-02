## ----setup-------------------------------------------------------------------------------------
# Diffusion model packages
library(brms)

# Rstan
library(rstan)


## ----functions---------------------------------------------------------------------------------



## ----data--------------------------------------------------------------------------------------
data_robust <- rio::import("./bachelor/data/diffusion_data_robust.rdata")


## ----set-formula-------------------------------------------------------------------------------
# Add no intercorr here ||
formula <- bf(
  # No intercepts, bc this estimates parameters for each combination of
  # rsi and error_factor
  rt | dec(decision) ~ 0 + rsi:error_factor:stimulus + (0 + rsi:error_factor:stimulus||id),
  bs ~ 0 + rsi:error_factor + (0 + rsi:error_factor||id),
    # because rsi and error_factor are known they can be used here
    # pre-error is not technically "known", but should affect bs and ndt nonetheless
  ndt ~ 0 + rsi:error_factor + (0 + rsi:error_factor||id),
  bias = 0.5 # no reason for bias to vary TODO: intercept for bias
    # just want to estimate intercept for bias?
    # TODO: maybe estimate intercept for bias? 
)


## ----set-prior---------------------------------------------------------------------------------
prior <- c(
 # drift rate
 prior("normal(0, 5)", class = "b"), # drift rate, population

 # boundary separation
 set_prior("normal(1.5, 1)", class = "b", dpar = "bs", lb = 0), 
  # bs restricted to > 0, lb = 0
 
 # Non-decision time
 set_prior("normal(0.15, 0.1)", class = "b", dpar = "ndt", lb = 0),
 
 # Group-level
 set_prior("normal(0, 0.3)", class = "sd")
)


## ----temp-starting-values----------------------------------------------------------------------
tmp_dat_robust <- make_standata(
  formula, 
  family = wiener(
    link_bs = "identity", 
    link_ndt = "identity",
    link_bias = "identity"
    ),
  data = data_robust,
  prior = prior
  )


## ----init-function-----------------------------------------------------------------------------
initfun_robust <- function() {# all pars in stancode need init here
  list(
    b = rnorm(tmp_dat_robust$K),
    b_bs = runif(tmp_dat_robust$K_bs, 1, 2),
    b_ndt = runif(tmp_dat_robust$K_ndt, 0.05, 0.1), # rep for each dim in ndt
    sd_1 = runif(tmp_dat_robust$M_1, 0.5, 1),
    z_1 = matrix(rnorm(tmp_dat_robust$M_1*tmp_dat_robust$N_1, 0, 0.01),
                 tmp_dat_robust$M_1, tmp_dat_robust$N_1),
    sd_2 = runif(tmp_dat_robust$M_2, 0.5, 1),
    z_2 = matrix(rnorm(tmp_dat_robust$M_2*tmp_dat_robust$N_2, 0, 0.01),
                 tmp_dat_robust$M_2, tmp_dat_robust$N_2),
    sd_3 = runif(tmp_dat_robust$M_3, 0.5, 1),
    z_3 = matrix(rnorm(tmp_dat_robust$M_3*tmp_dat_robust$N_3, 0, 0.01),
                 tmp_dat_robust$M_3, tmp_dat_robust$N_3)
  )
}


## ----setup-model-------------------------------------------------------------------------------
n_iter <- 2000
n_warmup <- 1000
n_chains <- 4
n_cores <- 4
max_depth <- 15
adapt_delta <- 0.95
seed <- 1234

model_setup_values <- data.frame(n_iter, n_warmup, n_chains, n_cores, max_depth,
                                 adapt_delta, seed)


## ----fitting-model-location--------------------------------------------------------------------
fit_wiener_robust <- brm(
  formula, 
  data = data_robust,
  family = wiener(
    link_bs = "identity", 
    link_ndt = "identity",
    link_bias = "identity"
    ),
  prior = prior, 
  init = initfun_robust,
  iter = n_iter, 
  # init_r = 0.1,
  warmup = n_warmup, 
  chains = n_chains,
  cores = n_cores, 
  control = list(max_treedepth = max_depth, adapt_delta = adapt_delta),
  seed = seed # reproducibility
  )


## ----saving-ddm-classic------------------------------------------------------------------------
save(fit_wiener_robust, file = paste0("./bachelor/models/full_effect_robust_", Sys.Date(), ".rda"),
     compress = "xz")

