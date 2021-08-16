from fastapi import FastAPI, Response
from pydantic import BaseModel, validator, ValidationError

# import the types you need
from typing import Optional

app = FastAPI(openapi_url="/docs")
# TODO: load you model weights here

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
            raise ValidationError('Unknown value, must be a value in ["A", "B", "C"]')
        return v


@app.post("/predict")
def predict(req: PredictionRequest):
    """
    Prediction logic.
    """

    # TODO; call preprocessing function (if exists)

    # TODO: call model's predict function
    prediction = True # TODO: replace

    # TODO: call postprocessing function (if exists)

    return {"output": prediction}


@app.get("/healthz")
def healthz_func():
    """
    Health check for API server.
    """
    return Response(content="\n", status_code=200, media_type="text/plain")