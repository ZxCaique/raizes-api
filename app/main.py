from fastapi import FastAPI

app=FastAPI(title='Raizes API')

@app.get('/')
def root():
    return {'message':'Raizes API'}
