library(rio)
library(dplyr)
library(tidyr)
library(ggplot2)
library(forcats)
library(data.table)
library(purrr)
library(stringr)

# Filter out NA rows
not_all_na <- function(x) any(!is.na(x))

setwd(dirname(rstudioapi::getSourceEditorContext()$path))

r_dir <- paste0(getwd(), "/collective_data/BAT/")

psychopy_dir <- paste0(str_replace(getwd(), "/r", "/psychopy/data/"))

list.files(path = r_dir)
import_custom <- function(x){
  import(x) %>% 
    select(-contains("end_screen"),
           -starts_with("V"))
}

data_bat <- list.files(r_dir,
                       "csv",
                       full.names = T
) %>%
  map(import_custom) %>%
  rbindlist(
    use.names = TRUE
  ) %>% 
  mutate(key_resp_trial.rt = ifelse(participant %in% 1:3,
                                    key_resp_trial.rt,
                                    key_resp_trial.rt + 0.1))

# data_bat_1 <- import(paste0(r_dir, "1_00_bat_bachelor_2022-12-14_13h57.43.768.csv")) %>% 
#   select(-contains("end_screen"), -)
# data_bat_2 <- import(paste0(r_dir, "2_00_bat_bachelor_2022-12-14_13h58.16.622.csv")) %>% 
#   select(-contains("end_screen"), -starts_with("V"))
# data_bat_3 <- import(paste0(r_dir, "3_00_bat_bachelor_2022-12-14_14h24.57.588.csv")) %>% 
#   select(-contains("end_screen"), -starts_with("V"))
# 
# data_bat <- rbind(data_bat_1, data_bat_2, data_bat_3)
# anti_join(tibble(name = colnames(data_bat_3)), tibble(name = colnames(data_bat_2)))

answers <- data_bat %>% 
  filter(!is.na(loop_exp.thisN)) %>% 
  select(where(not_all_na)) %>% 
  group_by(participant, loop_exp.thisN) %>% 
  mutate(acc = key_resp_trial.corr,
         rt = key_resp_trial.rt,
         prev_acc = lag(key_resp_trial.corr)) %>% 
  ungroup()

answers %>% 
  count(trial_type)

answers %>% 
  filter(lag(correct == "None"), correct != "None") %>% 
  group_by(rsi, prev_acc) %>% 
  summarize(mean_rt = mean(key_resp_trial.rt, na.rm = TRUE),
            count = n())

# robust
answers <- answers %>% 
  mutate(error_type = case_when(
    lag(correct == "None") & correct == "None" & lead(correct != "None") & acc == 0 ~ "e_double_lure",
    lag(correct != "None") & correct == "None" & lead(correct != "None") & acc == 0 ~ "e_single_lure"
  )) %>% 
  mutate(error_type = case_when(
    lag(error_type) == "e_single_lure" ~ "e+1",
    lag(error_type) == "e_double_lure" ~ "e+1",
    lead(error_type) == "e_single_lure" ~ "e-1",
    lead(error_type, 2) == "e_double_lure" ~ "e-1",
    error_type == "e_single_lure" ~ "e",
    error_type == "e_double_lure" ~ "e",
    TRUE ~ "other"
  )) %>% 
  mutate(error_type = fct_relevel(factor(error_type), "e-1", "e", "e+1", "other"))
answers %>% 
  group_by(rsi, error_type) %>% 
  summarize(mean_rt = mean(rt, na.rm = TRUE),
            count = n()) %>% 
  ungroup() %>% 
  ggplot(
    aes(x = error_type,
        y = mean_rt,
        group = rsi, color = factor(rsi))
  ) +
  geom_line()+
  theme_classic()
answers %>% 
  group_by(participant, trial_type, rsi) %>% 
  count(key_resp_trial.corr) %>% 
  View()

answers %>% 
  group_by(rsi, trial_type) %>%
  count(key_resp_trial.corr)

answers %>% 
  group_by(participant, rsi) %>% 
  summarize(mean_rt = mean(key_resp_trial.rt, na.rm = TRUE))

answers %>% 
  filter(key_resp_trial.rt < 0.1) %>% 
  count(participant)
