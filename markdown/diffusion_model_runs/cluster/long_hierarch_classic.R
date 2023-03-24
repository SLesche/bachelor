## ----setup------------------------------------------------------------------------------------
# Diffusion model packages
library(brms)

# cmdstanr
library(cmdstanr)
## ----data-------------------------------------------------------------------------------------
data <- rio::import("./bachelor/data/diffusion_data_classic_long.rdata")


## ----set-formula------------------------------------------------------------------------------
formula <- bf(
  rt | dec(acc) ~ 0 + error_factor + (0 + error_factor||id),
  bs ~ 0 + error_factor + (0 + error_factor||id),
  ndt ~ 0 + error_factor + (0 + error_factor||id),
  bias ~ 0 + error_factor + (0 + error_factor||id)
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
  set_prior("gamma(2, 4)", class = "sd", lb = 0),
  set_prior("gamma(2, 4)", class = "sd", dpar = "bs", lb = 0),
  set_prior("gamma(2, 4)", class = "sd", dpar = "ndt", lb = 0),
  set_prior("gamma(2, 4)", class = "sd", dpar = "bias", lb = 0)
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
    sd_2 = runif(tmp_dat$M_2, 0.5, 1),
    z_2 = matrix(rnorm(tmp_dat$M_2*tmp_dat$N_2, 0, 0.01),
                 tmp_dat$M_2, tmp_dat$N_2),
    sd_3 = runif(tmp_dat$M_3, 0.5, 1),
    z_3 = matrix(rnorm(tmp_dat$M_3*tmp_dat$N_3, 0, 0.01),
                 tmp_dat$M_3, tmp_dat$N_3),
    sd_4 = runif(tmp_dat$M_4, 0.5, 1),
    z_4 = matrix(rnorm(tmp_dat$M_4*tmp_dat$N_4, 0, 0.01),
                 tmp_dat$M_4, tmp_dat$N_4)     
  )
}


## ----setup-model------------------------------------------------------------------------------
n_iter <- 3000
n_warmup <- 1000
n_chains <- 4
n_cores <- 64
n_threads <- n_cores
max_depth <- 15
adapt_delta <- 0.95
seed <- 1234

## ----fitting-model-location-------------------------------------------------------------------
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
  # init_r = 0.1,
  warmup = n_warmup, 
  chains = n_chains,
  backend = "cmdstanr",
  threads = threading(n_threads), 
  control = list(max_treedepth = max_depth, adapt_delta = adapt_delta),
  refresh = 200,
  seed = seed # reproducibility
)


## ----saving-ddm-classic-----------------------------------------------------------------------
save(fit_wiener, file = paste0("./bachelor/models/hierarch_model_long_classic.rda"),
     compress = "xz")

pred <- predict(fit_wiener,
                summary = FALSE,
                negative_rt = TRUE,
                ndraws = 200)

save(pred, file = "./bachelor/predictions/pred_hierarch_classic.rda")