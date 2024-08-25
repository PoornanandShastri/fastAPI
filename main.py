from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def first_example():
    '''
    FastAPI Example First Fast API app 
    '''
    return {"Fastapi Example": "FastAPI"}
