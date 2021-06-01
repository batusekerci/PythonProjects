import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-0.005*x))

def sigmoid_derivative(x):
    return 0.005 * x * (1 - x )



def read_and_divide_into_train_and_test():
    df=pd.read_csv("breast-cancer-wisconsin.csv")
    df = df.replace(to_replace="?", value="5")
    df.astype(int)
    training_inputs= df.iloc[:560,1:-1]
    test_inputs = df.iloc[560:,1:-1]
    training_labels= df.iloc[:560,[-1]]
    test_labels= np.array(df.iloc[560:,[-1]])
    core = pd.DataFrame(training_inputs)
    corre = core.corr()

    plt.imshow(corre, cmap='hot', interpolation='nearest')
    plt.xticks(range(len(corre.columns)), corre.columns, rotation = 90)
    plt.yticks(range(len(corre.columns)), corre.columns)
    plt.title("Correlation Heatmap")
    for i in range(len(corre)):
        for j in range(len(corre)):
            plt.text(j, i, "{:.2f}".format(corre.iloc[i, j]),
                           ha="center", va="center", color="b")
    plt.show()
    return training_inputs, training_labels, test_inputs, test_labels



def run_on_test_set(test_inputs, test_labels, weights):
    tp = 0
    test_predictions = sigmoid(np.dot(test_inputs.astype(int),weights))

    for val in range(len(test_predictions)):
        if test_predictions[val] > 0.5:
            test_predictions[val] = 1
        else:
            test_predictions[val] = 0
    
    for predicted_val, label in zip(test_predictions, test_labels):
        if predicted_val == label:

            tp += 1
    accuracy = tp / len(test_labels)

    return accuracy


def plot_loss_accuracy(accuracy_array, loss_array):
    plt.figure()
    plt.subplot(211)
    plt.plot(accuracy_array)
    plt.title("Accuracy")
    plt.subplot(212)
    plt.plot(loss_array)
    plt.title("Loss")
    plt.show()

def main():

    iteration_count = 2500
    np.random.seed(1)
    weights = 2 * np.random.random((9, 1)) - 1
    accuracy_array = []
    loss_array = []
    training_inputs, training_labels, test_inputs, test_labels = read_and_divide_into_train_and_test()

    for iteration in range(iteration_count):
        outputs = np.dot(training_inputs.astype(int),weights)
        outputs = sigmoid(outputs)
        loss = training_labels-outputs
        tuning = loss*sigmoid_derivative(outputs)
        weights += np.dot((np.transpose(training_inputs.astype(int))), tuning)
        loss_array.append(np.mean(loss))
        accuracy_array.append(run_on_test_set(test_inputs, test_labels, weights))

    plot_loss_accuracy(accuracy_array, loss_array)

main()