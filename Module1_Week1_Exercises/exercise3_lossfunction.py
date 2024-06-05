import math
import random


def mae(y_target: list, y_predict: list) -> float:
    total = 0
    for i in range(len(y_target)):
        total += abs(y_target[i] - y_predict[i])
    return total / len(y_target)


def mse(y_target: list, y_predict: list) -> float:
    total = 0
    for i in range(len(y_target)):
        total += (y_target[i] - y_predict[i])**2
    return total / len(y_target)


def rmse(y_target: list, y_predict: list) -> float:
    return math.sqrt(mse(y_target, y_predict))


def exercise3():
    num_samples = input(
        "Input number of samples (integer number) which are generated: ")
    if not num_samples.isnumeric():
        print("Number of samples must be an integer number")
        return
    num_samples = int(num_samples)
    loss = input("Input loss function (MAE|MSE|RMSE): ")
    if loss not in ['MAE', 'MSE', 'RMSE']:
        print(f"{loss} is not supported")
        return
    list_y_target = []
    list_y_pred = []
    if loss == 'MAE':
        for i in range(num_samples):
            y_pred = random.uniform(0, 10)
            y_target = random.uniform(0, 10)
            print(
                f"loss name: {loss}, sample: {i}, pred: {y_pred}, target: {y_target}, loss: {mae([y_target], [y_pred])}")
            list_y_target.append(y_target)
            list_y_pred.append(y_pred)
        print(f"final {loss}: {mae(list_y_target, list_y_pred)}")
    elif loss == 'MSE':
        for i in range(num_samples):
            y_pred = random.uniform(0, 10)
            y_target = random.uniform(0, 10)
            print(
                f"loss name: {loss},sample: {i}, pred: {y_pred}, target: {y_target}, loss: {mse([y_target], [y_pred])}")
            list_y_target.append(y_target)
            list_y_pred.append(y_pred)
        print(f"final {loss}: {mse(list_y_target, list_y_pred)}")
    else:
        for i in range(num_samples):
            y_pred = random.uniform(0, 10)
            y_target = random.uniform(0, 10)
            print(
                f"loss name: {loss},sample: {i}, pred: {y_pred}, target: {y_target}, loss: {rmse([y_target], [y_pred])}")
            list_y_target.append(y_target)
            list_y_pred.append(y_pred)
        print(f"final {loss}: {rmse(list_y_target, list_y_pred)}")


if __name__ == '__main__':
    exercise3()
