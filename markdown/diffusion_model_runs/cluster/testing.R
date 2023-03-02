library(brms)
library(cmdstanr)

fit <- brm(count ~ zAge + zBase * Trt + (1|patient),
           data = epilepsy, family = negbinomial(),
           chains = 1, threads = threading(2, grainsize = 100),
           backend = "cmdstanr")

