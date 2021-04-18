#=================================
#  State 1: Data Pre-processing
#=================================

# Load some packages for data manipulation:
library(tidyverse)
library(magrittr)
library(purrr)
source("credit_scoring_functions.R")

# Import data:
hmeq <- read.csv("http://www.creditriskanalytics.net/uploads/1/9/5/1/19511601/hmeq.csv")

df <- model.preprocess(hmeq)

# Fitting

# Split our data:

df_train <- df %>%
  group_by(BAD) %>%
  sample_frac(0.7) %>%
  ungroup() # Use 50% data set for training model.

df_test <- dplyr::setdiff(df, df_train) # Use 50% data set for validation.

# Data frame for training Logistic Regression:
df_train_aic <- df_train %>% select(all_of(predict_cols), "BAD")

log.model <- glm(BAD ~., data = df_train_aic, family = binomial(link = "logit"))

saveRDS(log.model, file = "credit_scoring_model.rds")

log.predictions <- predict(log.model, df_test, type="response")
log.predictions <-  log.predictions * 100

df_test$score <- log.predictions
