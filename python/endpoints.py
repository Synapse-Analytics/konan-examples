"""
References:
fastapi docs: https://fastapi.tiangolo.com/
more on types: https://fastapi.tiangolo.com/python-types/
fastapi vs flask: https://testdriven.io/blog/moving-from-flask-to-fastapi/#:~:text=Its%20popularity%20is%20fueled%20by,amongst%20the%20machine%20learning%20community.&text=Unlike%20Flask%2C%20FastAPI%20is%20an,fastest%20Python%2Dbased%20web%20frameworks.
"""

import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

# import the types you need
from typing import Optional, List, Set, Tuple, Dict

app = FastAPI()

# TODO: load your model *here*
# model = pickle.load(file_path)

# TODO: create your request serializer, insert all fields and types
# example request seralizer
class Request(BaseModel):
    """
    Request serializer for input format validation.
    """
    some_feat: str
    other_feat: int
    optional_field: Optional[bool] = None # default value


class Response(BaseModel):
    """
    Response serializer for response format validation.
    All responses to credit scoring should abide by this format.
    """
    prediction_score : int


@app.post("/predict", response_model=Response)
def predict():
    """This is the prediction endpoint that Konan will communicate with.

    :return: Response
    """
    # TODO: call your preprocessing function (check example below)
    # TODO: call your model's predict function (loaded at top of file)

    return {"prediction_score": "50"}

"""
# example of what your predict endpoint might look like.

@app.post("/predict", reponse_model=Response)
def predict(req: Request):

    # call preprocess function
    clean_data = preprocess(req) # import and call your preprocessing function

    # call predict function
    predictions = model.predict(clean_data)

    # format predictions to the expected response format
    formatted_predictions = format_preds(predictions['y'])

    return formatted_predictions
"""

