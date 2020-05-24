import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier

if __name__ == '__main__':
    with open('car.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dataset = list(csv_reader)[1:]

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[:int(0.7 * len(dataset))]
    train_x = [t[:-1] for t in train_set]  # Atributi bez klasata
    train_x = encoder.transform(train_x)
    train_y = [t[-1] for t in train_set]  # Klasata

    test_set = dataset[int(0.7 * len(dataset)):]
    test_x = [t[:-1] for t in test_set]
    test_x = encoder.transform(test_x)
    test_y = [t[-1] for t in test_set]

    clf = DecisionTreeClassifier(criterion='entropy', random_state=0)
    clf.fit(train_x, train_y)

    print(f'Depth: {clf.get_depth()}')
    print(f'Number of leaves: {clf.get_n_leaves()}')

    counter = 0
    for x, y in zip(test_x, test_y):
        prediction = clf.predict([x])[0]
        if prediction == y:
            counter += 1

    print(counter / len(test_set))

    feature_importances = list(clf.feature_importances_)

    print(feature_importances)

    most_important_feature = feature_importances.index(max(feature_importances))
    print(most_important_feature)

    least_important_feature = feature_importances.index(min(feature_importances))
    print(least_important_feature)

    train_x_2 = list()
    for t in train_x:
        sample = [t[i] for i in range(len(t)) if i != most_important_feature]
        train_x_2.append(sample)

    test_x_2 = list()
    for t in test_x:
        sample = [t[i] for i in range(len(t)) if i != most_important_feature]
        test_x_2.append(sample)

