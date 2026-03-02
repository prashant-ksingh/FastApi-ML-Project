from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predict_category: str = Field(
        ...,
        description="The predicted insurance premium category",
        examples="Heigh"
    )
    confidence: float = Field(
        ...,
        description="Model's confidence score for the predicted class(range : 0 to 1)",
        examples= 0.8432
    )
    class_probabilites: Dict[str, float] = Field(
        ...,
        description="Probability  distribution across all tpossible classes",
        examples={"low": 0.01, "Medium": 0.15, "heigh": 0.84}
    )