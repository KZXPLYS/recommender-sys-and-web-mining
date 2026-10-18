import gzip


import json


import dateutil.parser


import random


import numpy as np


from collections import defaultdict


from sklearn import linear_model


import math


def feat(d, catID, maxLength, includeCat = True, includeReview = True, includeLength = True):
    feat = []
    if includeCat:
        cat_feature = [0] * len(catID)

        cate = d['beer/style']

        if cate in catID:
            index = catID[cate]
            cat_feature[index] = 1

        feat = feat + cat_feature
    if includeReview:
        review_features = [
            d['review/appearance'],
            d['review/aroma'],
            d['review/palate'],
            d['review/taste'],
            d['review/overall']
        ]

        feat = feat + review_features
    if includeLength:
        length_feature = len(d['review/text']) / maxLength
        feat = feat + [length_feature]

    return feat + [1]


def pipeline(reg, catID, dataTrain, dataValid, dataTest, includeCat=True, includeReview=True, includeLength=True):
    mod = linear_model.LogisticRegression(C=reg, class_weight='balanced')

    maxLength = max([len(d['review/text']) for d in dataTrain])
    
    Xtrain = [feat(d, catID, maxLength, includeCat, includeReview, includeLength) for d in dataTrain]
    Xvalid = [feat(d, catID, maxLength, includeCat, includeReview, includeLength) for d in dataValid]
    Xtest = [feat(d, catID, maxLength, includeCat, includeReview, includeLength) for d in dataTest]
    
    yTrain = [d['beer/ABV'] > 7 for d in dataTrain]
    yValid = [d['beer/ABV'] > 7 for d in dataValid]
    yTest = [d['beer/ABV'] > 7 for d in dataTest]
    
    # (1) Fit the model on the training set
    mod.fit(Xtrain, yTrain)

    # (2) Compute validation BER
    predictions_valid = mod.predict(Xvalid)

    TP = 0
    TN = 0
    FP = 0
    FN = 0


    for i in range(len(yValid)):
        if predictions_valid[i] == True and yValid[i] == True:
            TP += 1
        elif predictions_valid[i] == False and yValid[i] == False:
            TN += 1
        elif predictions_valid[i] == True and yValid[i] == False:
            FP += 1
        else:
            FN += 1

    FPR = FP / (FP + TN)
    FNR = FN / (FN + TP)

    vBER = (FPR + FNR) / 2

    # (3) Compute test BER
    predictions_test = mod.predict(Xtest)

    TP = 0
    TN = 0
    FP = 0
    FN = 0


    for i in range(len(yTest)):
        if predictions_test[i] == True and yTest[i] == True:
            TP += 1
        elif predictions_test[i] == False and yTest[i] == False:
            TN += 1
        elif predictions_test[i] == True and yTest[i] == False:
            FP += 1
        else:
            FN += 1

    FPR = FP / (FP + TN)
    FNR = FN / (FN + TP)

    tBER = (FPR + FNR) / 2

    return mod, vBER, tBER


def Q1(catID, dataTrain, dataValid, dataTest):
    # No need to modify this if you've implemented the functions above
    mod, validBER, testBER = pipeline(10, catID, dataTrain, dataValid, dataTest, True, False, False)
    return mod, validBER, testBER


def Q2(catID, dataTrain, dataValid, dataTest):
    mod, validBER, testBER = pipeline(10, catID, dataTrain, dataValid, dataTest, True, True, True)
    return mod, validBER, testBER


def Q3(catID, dataTrain, dataValid, dataTest):
    bestMod = None
    bestValidBER = 1
    bestTestBER = 1

    for c in [0.001, 0.01, 0.1, 1, 10]:
        mod, validBER, testBER = pipeline(
            c,
            catID,
            dataTrain,
            dataValid,
            dataTest,
            True,
            True,
            True
        )

        if validBER < bestValidBER:
            bestValidBER = validBER
            bestTestBER = testBER
            bestMod = mod

    # Return the validBER and testBER for the model that works best on the validation set
    return bestMod, bestValidBER, bestTestBER


def Q4(C, catID, dataTrain, dataValid, dataTest):
    mod, validBER, testBER_noCat = pipeline(C, catID, dataTrain, dataValid, dataTest, False, True, True)
    mod, validBER, testBER_noReview = pipeline(C, catID, dataTrain, dataValid, dataTest, True, False, True)
    mod, validBER, testBER_noLength = pipeline(C, catID, dataTrain, dataValid, dataTest, True, True, False)
    return testBER_noCat, testBER_noReview, testBER_noLength


def Jaccard(s1, s2):
    intersection = len(s1.intersection(s2))
    union = len(s1.union(s2))

    if union == 0:
        return 0

    return intersection / union


def mostSimilar(i, N, usersPerItem):
    similarities = []

    users = usersPerItem[i] # 找到i这个item有哪些users买过

    for item in usersPerItem: #遍历所有item除了item自己
        if item == i:
            continue

        similarity = Jaccard(users, usersPerItem[item])

        similarities.append((similarity, item))

    similarities.sort(reverse=True)

    # Should be a list of (similarity, itemID) pairs
    return similarities[:N]


def MSE(y, ypred):
    errors = []

    for i in range(len(y)):
        error = (y[i] - ypred[i]) ** 2
        errors.append(error)

    return sum(errors) / len(errors)


def getMeanRating(dataTrain):
    total = 0

    for d in dataTrain:
        total += d['star_rating']

    meanRating = total / len(dataTrain)

    return meanRating


def getUserAverages(itemsPerUser, ratingDict): # 每个user对他自己评价过的所有item的平均评分
    userAverages = {}

    for user in itemsPerUser:
        total = 0

        for item in itemsPerUser[user]:
            total += ratingDict[(user, item)]

        average = total / len(itemsPerUser[user])

        userAverages[user] = average
    return userAverages


def getItemAverages(usersPerItem, ratingDict): #遍历每一个item，然后把所有给这个item打过分的用户找出来，计算这些人的平均评分
    itemAverages = {}

    for item in usersPerItem:
        total = 0

        for user in usersPerItem[item]:
            total += ratingDict[(user, item)]

        average = total / len(usersPerItem[item])

        itemAverages[item] = average
    return itemAverages


def predictRating(user,item,ratingMean,reviewsPerUser,usersPerItem,itemsPerUser,userAverages,itemAverages):
    # Solution for Q6, should return a rating

    # 如果这个 item 在 training set 里从来没出现过
    if item not in itemAverages:
        return ratingMean

    numerator = 0
    denominator = 0

    # 遍历这个 user 以前评价过的商品
    for review in reviewsPerUser[user]:

        j = review['product_id']

        # 不和目标商品自己比较
        if j == item:
            continue

        rating = review['star_rating']

        similarity = Jaccard(
            usersPerItem[item],
            usersPerItem[j]
        )

        numerator += (rating - itemAverages[j]) * similarity
        denominator += similarity

    # 如果没有任何相似商品
    if denominator == 0:
        return itemAverages[item]

    prediction = itemAverages[item] + numerator / denominator

    return prediction


def predictRatingQ7(user, item, ratingMean,
                    reviewsPerUser, usersPerItem, itemsPerUser,
                    userAverages, itemAverages):

    q6prediction = predictRating(
        user, item, ratingMean,
        reviewsPerUser, usersPerItem, itemsPerUser,
        userAverages, itemAverages
    )

    prediction = 0.2 * q6prediction + 0.8 * ratingMean

    return prediction
