import math


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def sigmoid(n):
    return 1 / (1 + math.exp(-n))


def relu(n):
    return max(0, n)


def elu(n, alpha=0.01):
    return n if n > 0 else alpha * (math.exp(n) - 1)


def exercise2():
    x = input('Input x = ')
    if not is_number(x):
        print(f'{x} is not a valid number')
        return None

    x = float(x)

    act_func = input('Input activation Function ( sigmoid | relu | elu ): ')
    if act_func not in ['sigmoid', 'relu', 'elu']:
        print(f'{act_func} is not supported')
        return None

    if act_func == 'sigmoid':
        print(f'sigmoid f({x}) = ', sigmoid(x))
    elif act_func == 'relu':
        print(f'relu f({x}) = ', relu(x))
    elif act_func == 'elu':
        print(f'elu f({x}) = ', elu(x))


if __name__ == '__main__':
    exercise2()
