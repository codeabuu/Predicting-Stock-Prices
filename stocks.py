#!/usr/bin/python3
import csv
import numpy
from sklearn.svm import SVR
import matplotlib.pyplot as plt

dates = []
prices = []

def get_data(file):
    with open(file, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        new(csvFileReader)
        for row in csvFileReader:
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[1]))
    return

def predict_price(dates, prices, x):
    dates = np.reshape(dates, (len(dates), 1))

    '''linear support vector regression'''
    svr_lin = SVR(kernel= 'linear', C=1e3)
    svr_poly = SVR(kernel= 'poly', C=1e3, degree = 2)
    svr_rbf = SVR(kernel= 'rbf', C=1e3, gamma=0.1)
    svr_lin.fit(dates, prices)
    svr_poly.fit(dates, prices)
    svr_rbf.fit(dates, prices)

    plt.scatter(dates,prices, color='black', label="Data")
    plt.plot(dates, svr_rbf.predict(dates), color = 'red', label= 'RBF MODEL')
    plt.plot(dates, svr_lin.predict(dates), color = 'green', label= 'Linear Model')
    plt.plot(dates, svr_poly.predict(dates), color = 'blue', label="Polynomial Model")
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support vector regression')
    plt.legend()
    plt.show()

    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

get_data('safshares.csv')
predicted_prices = predicted_price(dates, prices, 29)
print(predicted_prices)
