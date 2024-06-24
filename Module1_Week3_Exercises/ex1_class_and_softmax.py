import torch
from torch.nn import Module


class Softmax(Module):
    def __init__(self, stable=False):
        super(Softmax, self).__init__()
        self.stable = stable

    def forward(self, x):
        if self.stable:
            # Softmax stable
            c = torch.max(x)
            exp_x = torch.exp(x - c)
            return exp_x / torch.sum(exp_x)
        else:
            # Softmax thường
            exp_x = torch.exp(x)
            return exp_x / torch.sum(exp_x)


if __name__ == "__main__":
    # Softmax thường
    data = torch.Tensor([1, 2, 3])
    softmax = Softmax()
    output = softmax(data)
    print("Softmax:", output)

    # Softmax stable
    data = torch.Tensor([1, 2, 3])
    softmax_stable = Softmax(stable=True)
    output_stable = softmax_stable(data)
    print("Softmax stable:", output_stable)
