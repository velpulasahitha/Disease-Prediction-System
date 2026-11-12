import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. Load dataset
data = pd.read_csv("Training.csv")


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

from doctor_mapping import DOCTOR_MAPPING

# 1. Load dataset
data = pd.read_csv("Training.csv")

# 2. Drop useless column
data = data.drop(columns=["Unnamed: 133"])

# 3. Separate features and target
X = data.drop("prognosis", axis=1)
y = data["prognosis"]

# 4. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 6. Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# 7. Test prediction (NO WARNING version)
sample = X.iloc[[0]]   # keep DataFrame
prediction = model.predict(sample)
disease = prediction[0]

doctor = DOCTOR_MAPPING.get(disease, "General Physician")

print("Predicted Disease:", disease)
print("Recommended Doctor:", doctor)