import os
from joblib import load


def preprocess(data: dict) -> list:
    """ This Function preprocess the data before scoring the model """
    path = os.path.join(os.getcwd(), "model_store", "scaler.pkl")
    scaler = load(path)
    scaler.transform()
    return list(data.values())


def score(data: list) -> int:
    """ This Function score the model """
    path = os.path.join(os.getcwd(), "model_store", "model.pkl")
    model = load(path)
    response = model.predict([data])
    return response


def postprocess(result: list) -> str:
    """ This Function converts the model ouput into human readable format """
    path = os.path.join(os.getcwd(), "model_store", "encoder.pkl")
    decoder = load(path)
    response = decoder.inverse_transform(result)
    return response
