predict_ddm <- function(fit){
  pred = predict(fit,
                 summary = FALSE,
                 negative_rt = TRUE,
                 ndraws = 500)
  return(pred)
}
fit <- rio::import("./bachelor/models/base_model_robust_2023-03-11.rda")
pred <- predict_ddm(fit)

save(pred, "./bachelor/predictions/pred_base_model_robust.rda")