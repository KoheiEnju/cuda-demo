import numpy as np


def main_np():
    N = 1 << 28
    x = np.ones((N,), dtype=float)
    y = np.full((N,), 2.0, dtype=float)
    y = x + y
    maxError = np.min(np.abs(y - 3.0))
    return maxError


def main_pure():
    # TODO: 64bitの浮動小数点数を使っているため、他のベンチマークよりも不利になっている
    N = 1 << 28
    x = [1.0 for _ in range(N)]
    y = [2.0 for _ in range(N)]
    for i in range(N):
        y[i] = x[i] + y[i]
    maxError = 0.0
    for i in range(N):
        maxError = max(maxError, abs(y[i] - 3.0))
    return maxError


if __name__ == "__main__":
    maxError = main_pure()
    print(f"Max Error: {maxError}")
