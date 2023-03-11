library(dplyr)
library(tidybayes)

predict_ddm <- function(fit){
  pred = fit$data %>%
    select(-rt, -decision) %>%
    add_predicted_draws(model = fit,
                        negative_rt = TRUE,
                        n = 500) %>%
    mutate(decision = ifelse(.prediction > 0, 1, 0),
           rt = abs(.prediction))
  return(pred)
}

input <- list.files("./bachelor/models/", pattern = "no_rsi_", full.names = TRUE)
file_name <- list.files("./bachelor/models/", pattern = "no_rsi_", full.names = FALSE)
outut <- paste0("./bachelor/predictions/pred_", file_name)

for (i in seq_along(input)){
  fit = rio::import(input[i])
  pred = predict_ddm(fit)
  save(pred, file = output[i])
}