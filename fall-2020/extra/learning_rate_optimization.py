# Created by dadajonjurakuziev at 2020/10/13 5:58 PM

import time
import warnings

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.exceptions import ConvergenceWarning
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

warnings.filterwarnings(action='ignore', category=ConvergenceWarning)


def train_MNIST(X, X_test, Y, Y_test):
    prange = [0.0000001, 0.000001, 0.00001, 0.0001, 0.001, 0.01, 0.1]
    accuracy = []

    for lr_rate in prange:
        mlp_test = MLPClassifier(hidden_layer_sizes=200,
                                 batch_size=32,
                                 max_iter=1000,
                                 learning_rate_init=lr_rate,
                                 solver='sgd')

        mlp_test.fit(X, Y)
        res = mlp_test.predict(X_test)

        conf = np.zeros((10, 10))
        for i in range(len(res)):
            conf[res[i]][Y_test[i]] += 1
        print(conf)

        no_correct = 0
        for i in range(10):
            no_correct += conf[i][i]
        current_accuracy = no_correct / len(res)
        accuracy.append(current_accuracy * 100)
        print(f"테스트 집합에 대한 정확률은 {str(round(current_accuracy * 100, 2))}% 입니다.")

    return prange, accuracy


def draw_graph(learning_rates, accuracies):
    # Find the best accuracy
    best_acc = max(acc)
    # Find the learning rate that gave us the best accuracy
    best_lr_rate = lr_rate[acc.index(best_acc)]

    plt.title("Learning rate optimization")
    plt.plot(lr_rate, acc)

    # Draw arrow and point the best result
    plt.annotate("best learning rate", xy=(best_lr_rate, best_acc), xytext=(best_lr_rate * 0.1, best_acc - 30), arrowprops=dict(facecolor='r'))
    plt.text(best_lr_rate * 0.1, best_acc - 40, f"lr_r : {'%.e' % best_lr_rate}\nacc : {round(best_acc, 2)}")

    plt.xlabel("Learning rate values")
    plt.ylabel("Accuracy")
    plt.xscale("log")
    plt.show()


if __name__ == "__main__":
    # Load MNIST dataset
    digit = datasets.load_digits()
    # Split dataset into train/test
    x_train, x_test, y_train, y_test = train_test_split(digit.data, digit.target, train_size=0.6)

    # start timer
    start = time.time()

    # train MNIST using Multi layer perceptron
    lr_rate, acc = train_MNIST(x_train, x_test, y_train, y_test)

    # draw graph
    draw_graph(lr_rate, acc)

    # sto timer
    end = time.time()
    print(f"\n학습률 최적화에 걸린 시간은 {round(end - start)}초 입니다.")
