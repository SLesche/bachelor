fit <- rio::import("./bachelor/models/hierarch_good_only_err.rda")

pred <- predict(fit,
                summary = FALSE,
                negative_rt = TRUE,
                ndraws = 200)

save(pred, file = "./bachelor/predictions/pred_hierarch_good_only_err.rda")