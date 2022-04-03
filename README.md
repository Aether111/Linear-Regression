# Linear-Regression
The linear regression problem has been solved by using an exhaustive search (brute force) approach. A grid search approach takes in a set of a datapoints and generates many candidate lines of different slopes and y-intercepts.
Each line is then tested by calculating the vertical distance from each datapoint to that line.
The verical distances are summed, squared, and halved to produce the mean-squared error of the line.
Out of all the candidate lines generated, the one with the least mean-squared error is selected to be the optimal line.
For more information, see https://en.wikipedia.org/wiki/Linear_regression.
