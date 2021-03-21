predict_cols <- c('LOAN', 'MORTDUE', 'VALUE', 'YOJ', 'DEROG',
                  'DELINQ', 'CLAGE', 'NINQ', 'CLNO', 'DEBTINC')

decision_col <- 'BAD'

na_rate <- function(x) {
  x %>%
    is.na() %>%
    sum() / length(x)
}

# Function replaces NA by mean:
replace_by_mean <- function(x) {
  x[is.na(x)] <- mean(x, na.rm = TRUE)
  return(x)
}

# A function imputes NA observations for categorical variables:
replace_na_categorical <- function(x) {
  x %>%
    table() %>%
    as.data.frame() %>%
    arrange(-Freq) ->> my_df

  n_obs <- sum(my_df$Freq)
  pop <- my_df$. %>% as.character()
  set.seed(29)
  x[is.na(x)] <- sample(pop, sum(is.na(x)), replace = TRUE, prob = my_df$Freq)
  return(x)
}


model.preprocess <- function(raw_dataframe) {
  sapply(raw_dataframe, na_rate) %>% round(2)
  # Use the two functions:
  processed_df <-
    raw_dataframe %>%
    mutate_if(is.factor, as.character) %>%
    mutate(REASON = case_when(REASON == "" ~ NA_character_, TRUE ~ REASON),
           JOB = case_when(JOB == "" ~ NA_character_, TRUE ~ JOB)) %>%
    mutate_if(is_character, as.factor) %>%
    mutate_if(is.numeric, replace_by_mean) %>%
    mutate_if(is.factor, replace_na_categorical)

  return(processed_df)
}


model.predict <- function(input_df, model_rds_path) {

  library(tidyverse)
  library(magrittr)
  library(purrr)
  # library(jsonlite)
  #
  # json_input <- '{"LOAN":21600,"MORTDUE":154991.0,"VALUE":101776.0487414501,"YOJ":8.9222681359,"DEROG":2.0,"DELINQ":4.0,"CLAGE":165.60083001,"NINQ":0.0,"CLNO":43.0,"DEBTINC":38.014917273}'
  # model_rds_path = "credit_scoring_model.rds"
  #
  # input_df <- fromJSON(json_input) %>% as.data.frame

  credit_scoring_model <- readRDS(model_rds_path)
  log.predictions <- predict(credit_scoring_model, input_df, type="response")
  log.predictions <- log.predictions * 100

  return(log.predictions)
}

