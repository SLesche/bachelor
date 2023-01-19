library(brms) # for the analysis
library(haven) # to load the SPSS .sav file
library(tidyverse) # needed for data manipulation.
library(RColorBrewer) # needed for some extra colours in one of the graphs
library(ggmcmc)
library(ggthemes)
library(ggridges)

popular2data <- read_sav(file = "https://github.com/MultiLevelAnalysis/Datasets-third-edition-Multilevel-book/blob/master/chapter%202/popularity/SPSS/popular2.sav?raw=true")

interceptonlymodeltest <- brm(popular ~ 1 + (1 | class), 
                              data   = popular2data, 
                              warmup = 100, 
                              iter   = 200, 
                              chains = 2, 
                              inits  = "random",
                              cores  = 2)  #the cores function tells STAN to make use of 2 CPU cores simultaneously instead of just 1.

interceptonlymodel <- brm(popular ~ 1 + (1|class),  
                          data = popular2data, 
                          warmup = 1000, iter = 3000, 
                          cores = 2, chains = 2, 
                          seed = 123,
                          refresh = 10) #to run the model
