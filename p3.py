# solve the problem using Linear Regression

# import the lib
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# load the data
data = pd.read_csv("hpnov23.csv")
print(data)

# feature and target
feature = data[["area"]]
target = data["price"]

# model
model = LinearRegression()
model.fit(feature, target)

plt.scatter(data["area"], data["price"], color="red")
plt.plot(data["area"], model.predict(data[["area"]]), color="blue")
plt.show()
