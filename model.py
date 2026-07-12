import os
import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv("dataset/crop_recommendation.csv")

# Features and target
X = data.drop("label", axis=1)
y = data["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Test accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Create models directory if it doesn't exist
os.makedirs("models", exist_ok=True)

# Save trained model
model_path = "models/crop_model.pkl"

with open(model_path, "wb") as file:
    pickle.dump(model, file)

print(f"Model saved successfully at: {model_path}")
