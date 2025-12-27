import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Input data
n_samples = int(input("Enter number of samples: "))
n_features = int(input("Enter number of features: "))

X = []
y = []

for i in range(n_samples):
    X.append(list(map(float, input(f"Features of sample {i+1}: ").split())))

for i in range(n_samples):
    y.append(int(input(f"Target of sample {i+1} (0/1): ")))

X = np.array(X)
y = np.array(y)

# Train-test split
test_size = float(input("Enter test size (e.g. 0.2): "))
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, random_state=42
)

# Model training
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Predicted Probabilities:\n", y_prob)
