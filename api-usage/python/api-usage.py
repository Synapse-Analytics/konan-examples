# Refer to https://docs.konan.ai for a detailed walkthrough

import requests

def login(email, password):
    """Logging in and retrieving a new pair of access and refresh tokens

    :param email: the email you registered with to konan
    :param password: your konan password
    """
    r_login = requests.post(
        'https://auth.konan.ai/api/auth/login',
        data={
            'email': email,
            'password': password
        }
    )

    if r_login.status_code == 200: # successfully logged in
        resp_data = r_login.json()
        konan_access = resp_data['access'] # access token to be used for authentication
        konan_refresh = resp_data['refresh'] # refresh token to issue another access token later on
    else: # an error has occurred
        print(r_login.status_code, r_login.reason)


def refresh_token(konan_refresh):
    """Refresh an access token

    :param konan_refresh: refresh token retrieved from login
    """
    # retrieving a new access token
    r_refresh = requests.post(
        'https://auth.konan.ai/api/auth/token/refresh',
        data={
            'refresh': konan_refresh, # refresh token obtained in the logging in section
        }
    )

    if r_refresh.status_code == 200: # successfully generated a new access token
        konan_access = r_refresh.json()['access'] # new access token
    else: # an error has occurred
        print(r_refresh.status_code, r_refresh.reason)

def logout(konan_refresh):
    """Logging out

    param konan_refresh: refresh token retrieved from login() or refresh_token()
    """
    # logging out
    r_logout = requests.post(
        'https://auth.konan.ai/api/auth/logout',
        data={
            'refresh': konan_refresh, # refresh token obtained in the logging in section
            'all_devices': False, # whether to logout this user from all their devices and sessions
        }
    )

    if r_logout.status_code == 204: # successfully logged out
        print("You have successfully logged out")
    else: # an error has occurred
        print(r_logout.status_code, r_logout.reason)


def get_docs(konan_access, project_uuid):
    """
    Get openapi json docs of deployment
    """
    PROJECT_UUID = project_uuid

    # retrieving ml-docs
    r_ml_docs = requests.get(
        "https://api.konan.ai/ml-docs/%s" %(PROJECT_UUID),
        headers={
            'Authorization': 'Bearer ' + konan_access
        }
    )

    if r_ml_docs.status_code == 200: # successfully retrieved the ml-docs
        ml_docs = r_ml_docs.json()
    else: # an error has occurred
        print(r_ml_docs.status_code, r_ml_docs.reason)


def predict(project_uuid, input_feats, konan_access):
    """Hit deployment's prediction endpoint.

    :param project_uuid: project uuid
    :param input_feats: dict of model inputs ex: {'input-1': 'value-1', 'input-2': 'value-2'}
    :param konan_access: konan access token
    """

    PROJECT_UUID = project_uuid
    predict_inputs = input_feats

    # hitting the predict endpoint
    r_predict = requests.post(
        "https://api.konan.ai/mlservices/%s/predict" % (PROJECT_UUID),
        headers={
            'Authorization': 'Bearer ' + konan_access
        },
        data=predict_inputs
    )

    if r_predict.status_code == 201: # successfully created a prediction
        predict_outputs = r_predict.json()
    else: # an error has occurred
        print(r_predict.status_code, r_predict.reason)