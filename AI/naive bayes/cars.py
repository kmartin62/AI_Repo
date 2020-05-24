#kategoriski tip

import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
import math

if __name__ == '__main__':
    with open("cars.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dataset = list(csv_reader)[1:]

        encoder = OrdinalEncoder()
        encoder.fit([dataset[i][:-1] for i in range(len(dataset))])
        # dataset = encoder.transform(dataset)

        train_set = dataset[0:math.ceil(0.7*len(dataset))]
        test_set = dataset[math.ceil(0.7*len(dataset)):]

        X = [train_set[i][:-1] for i in range(len(train_set))]
        X = encoder.transform(X)
        Y = [train_set[i][-1] for i in range(len(train_set))]

        clf = CategoricalNB()
        clf.fit(X, Y)

        # print(clf.predict_proba([test_set[0][0:-1]]))

        test_set_x = encoder.transform([test_set[i][:-1] for i in range(len(test_set))])
        counter = 0
        for i in range(len(test_set)):
            predict = clf.predict([test_set_x[i]])
            if predict == test_set[i][-1]:
                counter += 1

        print(counter)
        print(counter/len(test_set))

        entry = [el for el in input().split(' ')]
        entry = encoder.transform([entry])

        print(clf.predict(entry))
