# Library
library(brms)

input <- list.files("./bachelor/models/model_comp", full.names = TRUE)
input_no_path <- list.files("./bachelor/models/model_comp", full.names = FALSE)
output <- paste0("./bachelor/models/model_comp/waic/", input_no_path)

for (i in seq_along(input)){
  fit = rio::import(input[i])
  fit_waic = add_criterion(fit, "waic")
  save(fit_waic, file = output[i])
  print("done")
}