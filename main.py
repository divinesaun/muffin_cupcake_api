import joblib
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import numpy as np
import warnings
warnings.filterwarnings("ignore")


app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="templates"), name="static")

# Set up templates
templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or '*' to allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

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
async def home(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


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
