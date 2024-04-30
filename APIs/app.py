# GET WAY
from fastapi import FastAPI

app = FastAPI()

@app.get('/predict')
def predict_model(age:int, sex:str):
    # Assume a complex ML model
    if age<15 or sex=='F':
        return {'Survived':1}
    else:
        return {'Survived':0}