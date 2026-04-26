import numpy as np
from sklearn.linear_model import LinearRegression

# نموذج تدريبي بسيط
class DemandModel:
    def __init__(self):
        self.model = LinearRegression()
        self._train()

    def _train(self):
        # بيانات وهمية (Days vs Demand)
        X = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
        y = np.array([50,55,53,60,65,70,72,75,78,80])
        self.model.fit(X, y)

    def predict(self, day):
        return float(self.model.predict([[day]])[0])
