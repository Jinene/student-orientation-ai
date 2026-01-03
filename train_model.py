# train_model.py
"""
Train AI model to classify student orientation based on scores.
Saves model to orientation_model.pkl
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load data
df = pd.read_csv("data/students.csv")

# Features & target
X = df[["Math","Physics","Chemistry","English","History"]]
y = df["Orientation"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print(f"✅ Model Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")

# Save model
joblib.dump(clf, "orientation_model.pkl")
print("✅ Model saved as orientation_model.pkl")

# Predict example
example = [[85,80,78,70,65]]  # new student scores
pred = clf.predict(example)
print("Predicted Orientation for example student:", pred[0])
