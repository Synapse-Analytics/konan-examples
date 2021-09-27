#!/bin/bash

# Refer to https://docs.konan.ai for a detailed walkthrough

source .synapse-id.env

## LOGGING IN ##
sid_login_response=$(curl \
    --header "Content-Type: application/json" \
    --request POST \
    --data "{\"email\":\"$SID_EMAIL\",\"password\":\"$SID_PASSWORD\"}" \
    https://auth.konan.ai/api/auth/login \
    )

export KONAN_ACCESS=$(echo $sid_login_response | jq -r .access)
export KONAN_REFRESH=$(echo $sid_login_response | jq -r .refresh)

## REFRESH TOKEN ##
sid_refresh_response=$(curl \
    --header "Content-Type: application/json" \
    --request POST \
    --data "{\"refresh\":\"$KONAN_REFRESH\"}" \
    https://auth.konan.ai/api/auth/token/refresh \
    )

export KONAN_ACCESS=$(echo $sid_refresh_response | jq -r .access)


## LOGOUT ##
curl \
    --header "Content-Type: application/json" \
    --request POST \
    --data "{\"refresh\":\"$KONAN_REFRESH\",\"all_devices\":\"false\"}" \
    https://auth.konan.ai/api/auth/logout


## GET OPENAPI JSON DOCS ##
export PROJECT_UUID=<your-project-uuid-here>
project_ml_docs=$(curl \
    --header "Content-Type: application/json" \
    --request GET \
    --headers "{Authorization: Bearer \"$KONAN_ACCESS\"}" \
    https://api.konan.ai/ml-docs/"$PROJECT_UUID" \
    )

## HIT PREDICTION ENDPOINT ##
export PROJECT_UUID=<your-project-uuid-here>

predict_output=$(curl \
    --header "Content-Type: application/json" \
    --request POST \
    --headers "{Authorization: Bearer \"$KONAN_ACCESS\"}" \
    --data "<predict-inputs-dictionary>" \ # don't forget to write your project's predict endpoint's input dictionary here
    https://api.konan.ai/mlservices/"$PROJECT_UUID"/predict \
    )
