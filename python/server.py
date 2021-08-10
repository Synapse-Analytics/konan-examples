"""
References:
fastapi docs: https://fastapi.tiangolo.com/
more on types: https://fastapi.tiangolo.com/python-types/
fastapi vs flask: https://testdriven.io/blog/moving-from-flask-to-fastapi/#:~:text=Its%20popularity%20is%20fueled%20by,amongst%20the%20machine%20learning%20community.&text=Unlike%20Flask%2C%20FastAPI%20is%20an,fastest%20Python%2Dbased%20web%20frameworks.
pydantic validation: https://pydantic-docs.helpmanual.io/usage/
"""

from fastapi import FastAPI, Response
from pydantic import BaseModel, validator, ValidationError

# import the types you need
from typing import Optional

app = FastAPI(openapi_url="/docs")

# TODO: create your request serializer, insert all fields and types
# example request seralizer
class PredictionRequest(BaseModel):
    """
    Request serializer for input format validation.
    """

    some_feat: str
    other_feat: int
    optional_field: Optional[bool] = None  # default value

    # TODO: add validators to enforce value ranges
    @validator("some_feat")
    def in_values(cls, v):
        """
        Validates prediction score is in ranges or limits.
        """
        if v not in ["A", "B", "C"]:
            raise ValidationError('Unkown value, must be a value in ["A", "B", "C"]')
        return v


class PredictionResponse(BaseModel):
    """
    Response serializer for response format validation.
    All responses to credit scoring should abide by this format.
    """

    prediction_result: bool # could be int or other types

    @validator("prediction_score")
    def between_0_and_100(cls, v):
        """
        Validates prediction score is in range.
        """
        if not 0 <= v <= 100:
            raise ValidationError("must be a value between 0 and 100")
        return v


@app.post("/predict", response_model=PredictionResponse)
def predict():
    """This is the prediction endpoint that Konan will communicate with.

    :return: Response
    """
    # TODO: call your preprocessing function (check example below)
    # TODO: call your model's predict function (loaded at top of file)

    return {"prediction_result": True}


# A health check endpoint for backend purposes. Must be included!
@app.get("/healthz")
def healthz_func():
    """
    Health check for API server.
    """
    return Response(content="\n", status_code=200, media_type="text/plain")
