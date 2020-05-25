from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def read_dataset():
    data = []
    with open('winequality.csv') as f:
        _ = f.readline()
        while True:
            line = f.readline().strip()
            if line == '':
                break
            parts = line.split(';')
            data.append(list(map(float, parts[:-1])) + parts[-1:])

    return data


def divide_sets(dataset):
    bad_classes = [d for d in dataset if d[-1] == 'bad']
    good_classes = [d for d in dataset if d[-1] == 'good']

    train_set = bad_classes[:int(len(bad_classes) * 0.7)] + good_classes[:int(len(good_classes) * 0.7)]
    val_set = bad_classes[int(len(bad_classes) * 0.7):int(len(bad_classes) * 0.8)] + \
              good_classes[int(len(good_classes) * 0.7):int(len(good_classes) * 0.8)]
    test_set = bad_classes[int(len(bad_classes) * 0.8):] + good_classes[int(len(good_classes) * 0.8):]

    return train_set, val_set, test_set


if __name__ == '__main__':
    dataset = read_dataset()
    train_set, val_set, test_set = divide_sets(dataset)

    train_x = [x[:-1] for x in train_set]
    train_y = [x[-1] for x in train_set]

    val_x = [x[:-1] for x in val_set]
    val_y = [x[-1] for x in val_set]

    test_x = [x[:-1] for x in test_set]
    test_y = [x[-1] for x in test_set]

    scaler = StandardScaler()
    scaler.fit(train_x)
    scaler2 = MinMaxScaler()
    scaler2.feature_range = (-1, 1)
    scaler2.fit(train_x)

    clf1 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    clf2 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    clf3 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)

    clf1.fit(train_x, train_y)
    clf2.fit(scaler.transform(train_x), train_y)
    clf3.fit(scaler2.transform(train_x), train_y)

    val_acc1 = 0
    val_predictions = clf1.predict(val_x)
    for x, y in zip(val_predictions, val_y):
        if x == y:
            val_acc1 += 1

    val_acc1 = val_acc1 / len(val_y)

    print("Tochnost bez normalizacija:", val_acc1)

    val_acc1 = 0
    val_predictions = clf2.predict(scaler.transform(val_x))
    for x, y in zip(val_predictions, val_y):
        if x == y:
            val_acc1 += 1

    val_acc1 = val_acc1 / len(val_y)

    print("Tochnost so standardna normalizacija:", val_acc1)

    val_acc1 = 0
    val_predictions = clf3.predict(scaler2.transform(val_x))
    for x, y in zip(val_predictions, val_y):
        if x == y:
            val_acc1 += 1

    val_acc1 = val_acc1 / len(val_y)

    print("Tochnost so MinMax normalizacija:", val_acc1)

    tp, fp, tn, fn = 0, 0, 0, 0
    predictions = clf3.predict(scaler2.transform(test_x))
    for x, y in zip(predictions, test_y):
        if y == 'good':
            if x == y:
                tp += 1
            else:
                fn += 1
        else:
            if x == y:
                tn += 1
            else:
                fp += 1

    acc = (tp + tn) / (tp + tn + fp + fn)
    prediznost = tp / (tp + fp)
    odziv = tp / (tp + fn)

    print("Accuracy:", acc)
    print("Preciznost:", prediznost)
    print("Odziv:", odziv)

    # acc = (tp + tn) / (tp + fp + tn + fn)
    # precision = tp / (tp + fp)
    # recall = tp / (tp + fn)
    #
    # print('Evaluacija:')
    # print(f'Tochnost: {acc}')
    # print(f'Preciznost: {precision}')
    # print(f'Odziv: {recall}')