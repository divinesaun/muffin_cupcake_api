import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import warnings
warnings.filterwarnings("ignore")


app = FastAPI()

def load_pickle(filename):
    with open(filename, 'rb') as file:
        contents = joblib.load(file)
    return contents

model = load_pickle("ml_components/model.joblib")

class Data(BaseModel):
    Flour: int
    Milk: int
    Sugar: int
    Butter: int
    Egg: int
    Baking_Powder: int
    Vanilla: int
    Salt: int

@app.get("/")
async def home():
    return {"message": "This is an API for Muffin vs Cupcake classification"}


@app.post("/predict")
async def predict(data: Data):
    input_data = np.array([[data.Flour, data.Milk, data.Sugar, data.Butter,
                            data.Egg, data.Baking_Powder, data.Vanilla, data.Salt]])
    prediction = model.predict(input_data)
    feature_names = ["Cupcake", "Muffin"]
    return {"prediction": feature_names[prediction[0]]}


@app.get('/model-info')
async def model_info():
    model_name = model.__class__.__name__
    model_params = model.get_params()
    model_information =  {'model info': {
            'model name ': model_name,
            'model parameters': model_params}
            }
    return model_information
