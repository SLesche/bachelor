library(dplyr)
library(tidybayes)

predict_ddm <- function(fit){
  pred = fit$data %>%
    select(rsi, error_factor, stimulus, previous_stimulus) %>%
    add_predicted_draws(model = fit,
                        negative_rt = TRUE,
                        n = 500) %>%
    mutate(decision = ifelse(.prediction > 0, 1, 0),
           rt = abs(.prediction))
  return(pred)
}

input <- list.files("./bachelor/models/", pattern = "no_rsi_")


for (i in input){
  fit = rio::import(input)
  pred = predict_ddm(fit)
  output = 
  save(pred, paste0("./bachelor/predictions/"))
}