library(brms)
fit <- rio::import("./bachelor/models/no_rsi_2023-03-11.rda")

predict_ddm <- function(fit){
  pred = predict(fit,
                 summary = FALSE,
                 negative_rt = TRUE,
                 ndraws = 500)
  return(pred)
}

pred <- predict_ddm(fit)

save(pred, "./bachelor/predictions/pred_no_rsi.rda")

fit <- add_criterion(fit, "loo")

save(fit, "./bachelor/models/model_comp/loo_no_rsi.rda")