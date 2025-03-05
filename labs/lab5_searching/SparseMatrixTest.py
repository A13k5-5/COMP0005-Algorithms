import numpy as np
import time
from SparseMatrix import SparseMatrix


class DenseMatrix:
    def __init__(self, rows, cols):
        self.data = np.zeros((rows, cols))
        self.rows = rows
        self.cols = cols

    def add_val(self, val, row, col):
        self.data[row][col] = val

    def __mul__(self, other):
        return DenseMatrix.from_numpy(self.data @ other.data)

    @classmethod
    def from_numpy(cls, array):
        matrix = cls(array.shape[0], array.shape[1])
        matrix.data = array
        return matrix


def performance_test():
    # Test parameters
    sizes = [10, 100, 1000]
    sparsity = 0.01  # 1% non-zero elements

    print("Performance Comparison: SparseMatrix vs DenseMatrix")
    print("=" * 50)

    for n in sizes:
        print(f"\nMatrix size: {n}x{n}")

        # Create matrices
        sparse1 = SparseMatrix()
        sparse2 = SparseMatrix()
        dense1 = DenseMatrix(n, n)
        dense2 = DenseMatrix(n, n)

        # Fill matrices with same random values
        non_zero_count = int(n * n * sparsity)
        for _ in range(non_zero_count):
            row = np.random.randint(0, n)
            col = np.random.randint(0, n)
            val = np.random.random()
            sparse1.add_val(val, row, col)
            sparse2.add_val(val, row, col)
            dense1.add_val(val, row, col)
            dense2.add_val(val, row, col)
        sparse1.add_val(1, n - 1, n - 1)
        sparse2.add_val(1, n - 1, n - 1)

        # Test multiplication
        print("\nMultiplication test:")

        # Sparse multiplication
        start = time.time()
        sparse_result = sparse1 * sparse2
        sparse_time = time.time() - start
        print(f"SparseMatrix: {sparse_time:.4f} seconds")

        # Dense multiplication
        start = time.time()
        dense_result = dense1 * dense2
        dense_time = time.time() - start
        print(f"DenseMatrix:  {dense_time:.4f} seconds")

        speedup = dense_time / sparse_time
        print(f"Speedup: {speedup:.2f}x")


if __name__ == "__main__":
    performance_test()
