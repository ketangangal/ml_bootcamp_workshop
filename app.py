from fastapi import FastAPI
from fastapi import Request
from inference import preprocess, score, postprocess
import uvicorn

app = FastAPI()


@app.get("/get_schema")
async def schema():
    data = {'service': 0.9910802775024777,
            'flag': 0.997636306334699,
            'src_bytes': 491,
            'dst_bytes': 0,
            'count': 2,
            'same_srv_rate': 1.0,
            'diff_srv_rate': 0.0,
            'dst_host_srv_count': 25,
            'dst_host_same_srv_rate': 0.17,
            'dst_host_same_src_port_rate': 0.17
            }
    return {"schema": data}


@app.post("/predict")
async def predict(request: Request):
    data = dict(await request.json())
    print(data)
    print(type(data))
    # list_values = preprocess(data)
    # result = score(list_values)
    # response = postprocess(result)
    # return {"Result": response[0]}
    return {"Result": data}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
