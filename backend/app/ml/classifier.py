from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import numpy as np

class VerdictClassifier:
    def __init__(self):
        self.model = LogisticRegression(max_iter=200)
        self.encoder = LabelEncoder()

    def train(self, X, y):
        y_enc = self.encoder.fit_transform(y)
        X_train, X_val, y_train, y_val = train_test_split(X, y_enc, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        return self.model.score(X_val, y_val)

    def predict(self, X):
        preds = self.model.predict_proba(X)
        labels = self.encoder.inverse_transform(np.argmax(preds, axis=1))
        confidences = preds.max(axis=1)
        return list(zip(labels, confidences))

