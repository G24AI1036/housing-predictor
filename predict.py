import joblib
from sklearn.datasets import fetch_california_housing

model = joblib.load("housing_model.joblib")
print("model loaded")

data = fetch_california_housing()
X, y = data.data, data.target

sample = X[0].reshape(1, -1)
prediction = model.predict(sample)

print(f"Predictions: {prediction[0]:.4f}")