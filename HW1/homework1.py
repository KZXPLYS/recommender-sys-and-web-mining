from collections import defaultdict


from sklearn import linear_model


import numpy


import math


import gzip


import json


import dateutil.parser


import random


def getMaxLen(dataset):
    # Find the longest review (number of characters)
    maxLen = 0
    for data in dataset:
        maxLen = max(maxLen, len(data['review_text']))
    return maxLen


def featureQ1(datum, maxLen):
    # Feature vector for one data point
    return [len(datum['review_text']) / maxLen if maxLen > 0 else 0]


def Q1(dataset):
    maxLen = getMaxLen(dataset)
    X = [[len(d['review_text']) / maxLen] for d in dataset]
    Y = [d['rating'] for d in dataset]

    model = linear_model.LinearRegression()
    model.fit(X, Y)

    theta = [model.intercept_, model.coef_[0]]

    predictions = model.predict(X)

    MSE = numpy.mean((numpy.array(Y) - predictions) ** 2)
    return theta, MSE


def featureQ2(datum, maxLen):
    scaled_length = len(datum['review_text']) / maxLen if maxLen > 0 else 0

    weekday = datum['parsed_date'].weekday()   # 0~6
    month = datum['parsed_date'].month        # 1~12

    weekday_features = [int(weekday == i) for i in range(1, 7)]
    month_features = [int(month == i) for i in range(2, 13)]

    return [1, scaled_length] + weekday_features + month_features


def Q2(dataset):
    maxLen = getMaxLen(dataset)
    X2 = [featureQ2(d, maxLen) for d in dataset]
    Y2 = [d['rating'] for d in dataset]

    model = linear_model.LinearRegression(fit_intercept=False)

    model.fit(X2, Y2)

    predictions = model.predict(X2)

    MSE2 = numpy.mean((numpy.array(Y2) - predictions) ** 2)
    return X2, Y2, MSE2


def featureQ3(datum, maxLen):
    scaled_length = len(datum['review_text']) / maxLen if maxLen > 0 else 0
    weekday = datum['parsed_date'].weekday()
    month = datum['parsed_date'].month

    return [1, scaled_length, weekday, month]


def Q3(dataset):
    maxLen = getMaxLen(dataset)
    X3 = [featureQ3(d, maxLen) for d in dataset]
    Y3 = [d['rating'] for d in dataset]

    model = linear_model.LinearRegression(fit_intercept=False)

    model.fit(X3, Y3)

    predictions = model.predict(X3)

    MSE3 = numpy.mean((numpy.array(Y3) - predictions) ** 2)
    return X3, Y3, MSE3


def Q4(dataset):
    n = len(dataset)
    train = dataset[: n//2]
    test = dataset[n//2:]

    maxLen = getMaxLen(train)

    # mse2
    X2_train = [featureQ2(d, maxLen) for d in train]
    Y2_train = [d['rating'] for d in train]

    model = linear_model.LinearRegression(fit_intercept=False)

    model.fit(X2_train, Y2_train)

    X2_test = [featureQ2(d, maxLen) for d in test]
    Y2_test = [d['rating'] for d in test]
    predictions_2 = model.predict(X2_test)

    test_mse2 = numpy.mean((numpy.array(Y2_test) - predictions_2) ** 2)

    # mse3
    X3_train = [featureQ3(d, maxLen) for d in train]
    Y3_train = [d['rating'] for d in train]
    model = linear_model.LinearRegression(fit_intercept=False)

    model.fit(X3_train, Y3_train)

    X3_test = [featureQ3(d, maxLen) for d in test]
    Y3_test = [d['rating'] for d in test]
    predictions_3 = model.predict(X3_test)

    test_mse3 = numpy.mean((numpy.array(Y3_test) - predictions_3) ** 2)

    return test_mse2, test_mse3


def featureQ5(datum):
    return [len(datum['review/text'])]


def Q5(dataset, feat_func):
    X = [feat_func(d) for d in dataset]
    Y = [d['review/overall'] >= 4 for d in dataset]

    model = linear_model.LogisticRegression(class_weight='balanced')
    model.fit(X, Y)

    predictions = model.predict(X)

    TP = 0
    TN = 0
    FP = 0
    FN = 0

    for i in range(len(Y)):
        if predictions[i] == True and Y[i] == True:
            TP += 1
        elif predictions[i] == False and Y[i] == False:
            TN += 1
        elif predictions[i] == True and Y[i] == False:
            FP += 1
        else:
            FN += 1

    FPR = FP / (FP + TN)
    FNR = FN / (FN + TP)

    BER = (FPR + FNR) / 2
    return TP, TN, FP, FN, BER


def Q6(dataset):
    X = [featureQ5(d) for d in dataset]
    Y = [d['review/overall'] >= 4 for d in dataset]

    model = linear_model.LogisticRegression(class_weight='balanced')
    model.fit(X, Y)

    probabilities = model.predict_proba(X)

    results = []

    for i in range(len(Y)):
        positive_probability = probabilities[i][1]
        true_label = Y[i]

        results.append([positive_probability, true_label])
    results.sort(reverse=True)

    Ks = [1, 100, 1000, 10000]
    precs = []

    for K in Ks:
        positive_count = 0

        for i in range(K):
            if results[i][1] == True:
                positive_count += 1

        precision = positive_count / K
        precs.append(precision)

    return precs


def featureQ7(datum):
    return [
        len(datum['review/text']),
        datum['review/appearance'],
        datum['review/aroma'],
        datum['review/palate'],
        datum['review/taste'],
        datum['beer/ABV']
    ]
