from fastapi import APIRouter
from app.ml.result import predict_ppd_risk

router = APIRouter(prefix="/ml", tags=["ML Risk Prediction"])

@router.post("/predict")
def predict_risk(data: dict):
    """
    Input JSON example :
    {
        "age": 28,
        "partner_support": 7,
        "sleep_quality": 3,
        "epds_10": 0
    }
    """
    result = predict_ppd_risk(data)
    return result
