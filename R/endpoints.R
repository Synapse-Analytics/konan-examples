## R script using plumber to create an endpoint, expose a port with a function name to send model features
## and return model prediction
suppressMessages(library(tidyverse))
suppressMessages(library(jsonlite))
suppressMessages(source("credit_scoring_functions.R"))
suppressMessages(source("api_errors.R"))

#* Return the prediction of the credit scoring model between 0 and 100
#* @param BAD:int
#* @param LOAN:int
#* @param MORTDUE:numeric
#* @param VALUE:numeric
#* @param REASON
#* @param JOB
#* @param YOJ:numeric
#* @param DEROG:numeric
#* @param DELINQ:numeric
#* @param CLAGE:numeric
#* @param NINQ:numeric
#* @param CLNO:numeric
#* @param DEBTINC:numeric
#* @post /predict
#* @serializer json list(auto_unbox=TRUE)
endpoint.predict <- function(req, res, BAD = NULL,
                             LOAN, MORTDUE,
                             VALUE, REASON = "DebtCon",
                             JOB = "Other", YOJ,
                             DEROG, DELINQ,
                             CLAGE, NINQ,
                             CLNO, DEBTINC) {

  body <- jsonlite::fromJSON(req$postBody)
  json_input <- body
  input_df <- json_input %>% as.data.frame

  if (all(names(input_df) %in% predict_cols) == FALSE) {
    missing_params("Missing required parameters.")
  }

  model_rds_path = "credit_scoring_model.rds"
  y <- model.predict(input_df, model_rds_path)

  return (list(y = round(y, digits = 2)))
}

#* Health check for API server. Make sure it works with Kubernetes liveness probe
#* @get /healthz
#* @serializer json list(auto_unbox=TRUE)
endpoint.healthz <- function(req) {
  return("\n")
}
