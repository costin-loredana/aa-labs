import time
import matplotlib.pyplot as plt

def negafib(n, r):
    """
    Adjusts the Fibonacci result for negative indices using:
        F(-n) = (-1)^(n+1) * F(n)
    """
    return (-1)**(n + 1) * r

def mat_mul_opt(A, B):
    """
    Multiplies two 2x2 matrices A and B.
    """
    return [
        [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
        [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
    ]

def mat_pow_opt_iter(power):
    """
    Computes the (1,1) Fibonacci transformation matrix
        F = [[1, 1],
             [1, 0]]
    raised to the given power using repeated squaring.
    """
    # Start with the identity matrix.
    result = [[1, 0], [0, 1]]
    base = [[1, 1], [1, 0]]
    while power > 0:
        if power % 2 == 1:
            result = mat_mul_opt(result, base)
        base = mat_mul_opt(base, base)
        power //= 2
    return result

def fib(n):
    n0 = n
    n = abs(n)
    if n == 0:
        r = 0
    else:
        m = mat_pow_opt_iter(n - 1)
        r = m[0][0]
    if n0 < 0:
        return negafib(n, r)
    return r

def measure_time_matrix(n):
    """
    Measures the execution time of computing fib(n) using the repeated-squaring method.
    Returns a tuple: (execution_time, fibonacci_result)
    """
    start = time.perf_counter()
    result = fib(n)
    end = time.perf_counter()
    return end - start, result

def main():
    try:
        input_str = input("Enter a list of Fibonacci term indices (comma separated, e.g., 5,10,15): ")
        input_array = [int(item.strip()) for item in input_str.split(',')]
    except Exception as e:
        print("Invalid input. Please enter numbers separated by commas.")
        return

    results = []
    for term in input_array:
        exec_time, fib_val = measure_time_matrix(term)
        results.append((term, fib_val, exec_time))
    
    # Print the results in a table.
    print("\nTerm  | Fibonacci Value       | Execution Time (seconds)")
    print("----------------------------------------------------------")
    for term, fib_val, exec_time in results:
        print(f"{term:<5} | {fib_val:<21} | {exec_time:.6f}")
    
    # Plot a graph: term vs. execution time.
    terms = [item[0] for item in results]
    times = [item[2] for item in results]
    plt.figure(figsize=(10, 6))
    plt.plot(terms, times, marker='o', linestyle='-', color='purple')
    plt.title("Execution Time for Matrix Exponentiation Fibonacci Calculations")
    plt.xlabel("Fibonacci Term (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
