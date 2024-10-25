![Screenshot (297)](https://github.com/user-attachments/assets/afe2fa57-7a68-45fd-a57e-af9c9a13fdd8)

1) import pandas as pd:
- Imports the pandas library, which is used for data manipulation and analysis.
We use pd as an alias for easy reference throughout the code.
from sklearn.

2) linear_model import LinearRegression:
- Imports the LinearRegression class from the sklearn (Scikit-Learn) library.
This class allows us to create and use linear regression models.

3) import matplotlib.pyplot as plt:
- Imports matplotlib.pyplot, a plotting library, for creating visualizations.
We use plt as an alias to make it easier to call plotting functions.

These libraries are essential for reading data (pandas), creating and training the linear regression model (sklearn), and visualizing the data and model predictions (matplotlib).

4) data = pd.read_csv("hpnov23.csv"):
- Loads the dataset from a CSV file named "hpnov23.csv" and stores it in a variable called data.
pd.read_csv() is a pandas function that reads data from a CSV file into a DataFrame, which is a two-dimensional data structure similar to a table in a database.

5) print(data):
- Prints the content of the loaded dataset to the console for quick inspection.
This helps verify that the data has been loaded correctly.

![Screenshot (298)](https://github.com/user-attachments/assets/bc0eeff1-4523-4fa0-be9d-e2654129b1b3)

6) feature = data[["area"]]:
- Extracts the area column from the dataset and stores it as feature.
The double square brackets [[ ]] ensure that the extracted data is in a two-dimensional format (DataFrame), which is required for the model.

7) target = data["price"]:
- Extracts the price column from the dataset and stores it as target.
This will be the value that the model is trying to predict.

8) model = LinearRegression():
- Creates an instance of the LinearRegression class and stores it in the variable model.
This instance will be used to train the linear regression model.

9) model.fit(feature, target):
- Trains (or fits) the linear regression model using the feature (area) and target (price) data.
The .fit() method adjusts the model parameters (slope and intercept) to minimize the difference between the predicted values and actual target values.

10) plt.scatter(data["area"], data["price"], color="red"):
- Creates a scatter plot of the original data points, with area on the x-axis and price on the y-axis.
The color="red" parameter sets the color of the data points to red, making them easily distinguishable.

11) plt.plot(data["area"], model.predict(data[["area"]]), color="blue"):
- Draws the best-fit line calculated by the linear regression model.

12) model.predict(data[["area"]])
- generates predicted price values based on the area data.
The color="blue" parameter sets the color of the line to blue.
plt.show():

Displays the scatter plot and the regression line together in a single plot.
![Screenshot (299)](https://github.com/user-attachments/assets/e716e34d-ba58-468f-aab6-9a101b2e2fab)
