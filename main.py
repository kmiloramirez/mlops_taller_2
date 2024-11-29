from pandas import DataFrame
from joblib import load
from pydantic import BaseModel, ValidationError
from fastapi import FastAPI, HTTPException
import pickle

# model = load("pipeline.joblib")

# with open('pipeline_new.pkl', 'rb') as f:
#     model = pickle.load(f)


app = FastAPI()

class DataPredict(BaseModel):
    data_to_predict: list[list] = [['SE', '18', 'US', 'Remoto', 'CA', 'M'], ['MI', '36', 'ES', 'Presencial', 'ES', 'L']]

@app.post("/predict")
def predict(request: DataPredict):
    """
        Diccionario de mapeo para las posiciones de trabajo:

        AI Developer: 0,  AI Scientist: 1,  Analytics Engineer: 2,  Applied Data Scientist: 3,  Applied Machine Learning Engineer: 4,  
        Applied Machine Learning Scientist: 5,  Applied Scientist: 6,  BI Analyst: 7,  BI Data Analyst: 8,  
        BI Data Engineer: 9,  BI Developer: 10,  Big Data Architect: 11,  Big Data Engineer: 12,  
        Business Data Analyst: 13,  Business Intelligence Engineer: 14,  Cloud Database Engineer: 15,  Computer Vision Engineer: 16,  
        Computer Vision Software Engineer: 17,  Data Analyst: 18,  Data Analytics Consultant: 19,  Data Analytics Engineer: 20,  
        Data Analytics Manager: 21,  Data Analytics Specialist: 22,  Data Architect: 23,  Data Engineer: 24,  
        Data Infrastructure Engineer: 25,  Data Lead: 26,  Data Manager: 27,  Data Modeler: 28,  
        Data Operations Analyst: 29,  Data Operations Engineer: 30,  Data Quality Analyst: 31,  Data Science Consultant: 32,  
        Data Science Engineer: 33,  Data Science Lead: 34,  Data Science Manager: 35,  Data Scientist: 36,  
        Data Scientist Lead: 37,  Data Specialist: 38,  Data Strategist: 39,  Deep Learning Engineer: 40,  
        Director of Data Science: 41,  ETL Developer: 42,  ETL Engineer: 43,  Financial Data Analyst: 44,  
        Head of Data: 45,  Head of Data Science: 46,  Head of Machine Learning: 47,  Insight Analyst: 48,  
        Lead Data Analyst: 49,  Lead Data Engineer: 50,  Lead Data Scientist: 51,  Lead Machine Learning Engineer: 52,  
        ML Engineer: 53,  MLOps Engineer: 54,  Machine Learning Developer: 55,  Machine Learning Engineer: 56,  
        Machine Learning Infrastructure Engineer: 57,  Machine Learning Manager: 58,  Machine Learning Research Engineer: 59,  Machine Learning Researcher: 60,  
        Machine Learning Scientist: 61,  Machine Learning Software Engineer: 62,  Manager Data Management: 63,  Marketing Data Analyst: 64,  
        NLP Engineer: 65,  Principal Data Analyst: 66,  Principal Data Architect: 67,  Principal Data Scientist: 68,  
        Principal Machine Learning Engineer: 69,  Product Data Analyst: 70,  Research Engineer: 71,  Research Scientist: 72

    """
    try:
        list_data = request.data_to_predict
        df_data = DataFrame(list_data, columns=['experience_level', 'job_title', 'employee_residence', 'remote_ratio', 'company_location', 'company_size'])

        prediction = model.predict(df_data)
        return {"prediction": prediction.tolist()}
    except ValidationError as ve:
        raise HTTPException(status_code=400, detail=ve.errors())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/sum")
def sum(param1: float, param2: float):
    try:
        result = param1 + param2
        return {"param1": param1, "param2": param2, "sum": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home():
    return {'Universidad EIA': 'MLOps'}
