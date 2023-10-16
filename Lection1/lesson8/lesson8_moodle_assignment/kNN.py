import numpy as np
from collections import Counter
class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def euclidean_dis(self, x1, x2):
        x1 = np.array(x1)
        x2 = np.array(x2)
        return np.sqrt(np.sum((x1-x2) ** 2))

    def predict(self, X):
        y_predict = [self._predict(x) for x in X]
        return np.array(y_predict)

    def _predict(self, x):
        dists = [self.euclidean_dis(x, x_train) for x_train in self.X_train]

        k_indices = np.argsort(dists)[:self.k]

        k_nearest_labels = [self.y_train[i] for i in k_indices]

        most_common = Counter(k_nearest_labels).most_common(1)

        return most_common[0][0]
