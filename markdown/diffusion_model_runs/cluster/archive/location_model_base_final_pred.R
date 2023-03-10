library(dplyr)

fit <- rio::import("./bachelor/models/location_standard_bias_2023-03-07.rda")

pred <- predict(fit,
                negative_rt = TRUE,
                summary = FALSE,
                ndraws = 500)

save(pred, file = "./bachelor/predictions/prediction_location_base.rdata")
