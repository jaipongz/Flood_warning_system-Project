from typing import Optional
from pydantic import BaseModel, Field


class WaterSchema(BaseModel):
    # name: str = Field(...)
    # year: int = Field(..., gt=1990, lt=2030)
    date: int = Field(..., gt=0, lt=32)
    # month: int = Field(..., gt=0, lt=13)
    waterfront: float = Field(..., ge=0.0)
    waterback: float = Field(..., ge=0.0)
    waterdrain: float = Field(..., ge=0.0)

    class Config:
        schema_extra = {
            "example": {
                # "name": "M7",
                # "year": 2020,
                # "month":12,
                "date":13,
                "waterfront":121.1,
                "waterback":111.3,
                "waterdrain":102.4,
            }
        }


class UpdateWaterModel(BaseModel):
    name: Optional[str]
    year: Optional[int]
    date: Optional[int]
    month: Optional[int]
    waterfront: Optional[float]
    waterback: Optional[float]
    waterdrain: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "name": "M7",
                "year": 2020,
                "month":12,
                "date":13,
                "waterfront":121.1,
                "waterback":111.3,
                "waterdrain":102.4,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}