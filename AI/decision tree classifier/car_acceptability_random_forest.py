import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier

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

    clf = RandomForestClassifier(n_estimators=150, criterion='entropy')
    clf.fit(train_x, train_y)

    counter = 0
    for x, y in zip(test_x, test_y):
        prediction = clf.predict([x])[0]
        if prediction == y:
            counter += 1

    print(counter/len(test_set))