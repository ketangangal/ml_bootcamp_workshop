from fastapi import FastAPI
from inference import preprocess, score, postprocess
import uvicorn

app = FastAPI()


@app.get("/get_schema")
async def schema():
    data = {
        'flag': {12: 0.997636306334699},
        'dst_host_serror_rate': {12: 0.0},
        'service': {12: 0.9997356245869135},
        'dst_host_srv_serror_rate': {12: 0.0},
        'protocol_type': {12: 0.9883398112159911},
        'srv_serror_rate': {12: 0.0},
        'same_srv_rate': {12: 1.0},
        'count': {12: 14},
        'src_bytes': {12: 215},
        'serror_rate': {12: 0.0}
        }
    return {"schema": data}


@app.post("/predict")
async def predict(data: dict):
    list_values = preprocess(data)
    scores = score(list_values)
    response = postprocess(scores)
    return {"Result": str(response)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
