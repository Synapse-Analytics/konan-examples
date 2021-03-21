# https://unconj.ca/blog/structured-errors-in-plumber-apis.html
api_error <- function(message, status) {
  err <- structure(
    list(message = message, status = status),
    class = c("api_error", "error", "condition")
  )
  signalCondition(err)
}

error_handler <- function(req, res, err) {
  if (!inherits(err, "api_error")) {
    res$status <- 500
    res$body <- "{\"status\":500,\"message\":\"Internal server error.\"}"

    # Print the internal error so we can see it from the server side. A more
    # robust implementation would use proper logging.
    print(err)
  } else {
    # We know that the message is intended to be user-facing.
    res$status <- err$status
    res$body <- sprintf(
      "{\"status\":%d,\"message\":\"%s\"}", err$status, err$message
    )
  }
  res
}

not_found <- function(message = "Not found.") {
  api_error(message = message, status = 404)
}

missing_params <- function(message = "Missing required parameters.") {
  api_error(message = message, status = 400)
}

invalid_params <- function(message = "Invalid parameter value(s).") {
  api_error(message = message, status = 400)
}
