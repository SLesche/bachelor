# Library
library(brms)

input <- list.files("./bachelor/models/model_comp", full.names = TRUE)
output <- paste0(stringr::str_remove(input, "\\.rda$"), "_waic.rda")

for (i in seq_along(input)){
  fit = rio::import(input[i])
  fit_waic = add_criterion(fit, "waic")
  save(fit_waic, file = output[i])
  print("done")
}