from fastapi import FastAPI
from inference import preprocess, score, postprocess
import uvicorn

app = FastAPI()


@app.get("/get_schema")
async def schema():
    """ This is Schema of the code"""
    data = {'count': {12: 14},
            'dst_host_srv_serror_rate': {12: 0.0},
            'dst_host_serror_rate': {12: 0.0},
            'same_srv_rate': {12: 1.0},
            'diff_srv_rate': {12: 0.0},
            'src_bytes': {12: 215},
            'srv_count': {12: 14},
            'srv_serror_rate': {12: 0.0},
            'dst_host_srv_diff_host_rate': {12: 0.0},
            'dst_host_srv_count': {12: 255},
            'dst_host_count': {12: 255}
            }
    return {"schema": data}


@app.post("/predict")
async def predict(data: dict):
    list_values = preprocess(data)
    scores = score(list_values)
    response = postprocess(scores)
    return {"Result": str(response)}

@app.get("/done")
async def done():
    """ This is Schema of the code. hello world"""
    data = {"response": "done"}
    return {"schema": data}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
