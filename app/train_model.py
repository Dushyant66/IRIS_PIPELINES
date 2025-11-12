import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Load data
df = pd.read_csv("app/iris.csv")

X = df.drop("species", axis=1)
y = df["species"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Save model
model_path = "app/model.pkl"
with open(model_path, "wb") as f:
    pickle.dump(clf, f)

print("✅ Model trained and saved as model.pkl")
