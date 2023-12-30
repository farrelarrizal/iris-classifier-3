import pickle
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    result = {
        "status": 200,
        "message": "Hello World" 
    }
    return result

# check model loading
@app.get('/check-model')
def check_model():
    try:
        # try to load model
        with open('model/classifier.pkl', 'rb') as file:
            model = pickle.load(file)
        result = {
            "status": 200,
            "message": "Model loaded successfully"
        }
        return result
    except Exception as e:
        result = {
            "status": 500,
            "message": "Model loading failed",
            "error": str(e)
        }
        return result

# Predict
@app.post('/predict')
async def predict(request: Request):
    # get data from request
    data = await request.json()
    
    sepal_length = data['sepal_length']
    sepal_width = data['sepal_width']
    petal_length = data['petal_length']
    petal_width = data['petal_width']
    
    # load model
    with open('model/classifier.pkl', 'rb') as file:
        model = pickle.load(file)
        
    # label 
    label = ['Iris Setosa', 'Iris Versicolor', 'Iris Virginica']
        
    # validation input
    if sepal_length < 0.0 or sepal_width < 0.0 or petal_length < 0.0 or petal_width < 0.0:
        result = {
            "status": 400,
            "message": "Input value cannot be negative"
        }
        return result
    
    # prediction
    try:
        prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        result = {
            "status": 200,
            "message": "Prediction success",
            "prediction": label[prediction[0]]
        }
        return result
    except Exception as e:
        result = {
            "status": 500,
            "message": "Prediction failed",
            "error": str(e)
        }
        return result
    
# Run API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)