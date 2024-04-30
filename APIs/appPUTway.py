from fastapi import FastAPI
from pydantic import BaseModel

class Input(BaseModel):
    age:int
    sex:str

app = FastAPI()

@app.put('/predict')
def predict_model(d:Input):
    if d.age<10 or d.sex=='M':
        return {'survived':1}
    else:
        return {'survived':0}