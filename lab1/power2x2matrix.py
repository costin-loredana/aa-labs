import time
import matplotlib.pyplot as plt

def negafib(n, r):
    """
    Adjusts the Fibonacci result for negative indices using:
       F(-n) = (-1)^(n+1) * F(n)
    """
    return (-1)**(n + 1) * r

def mat_mul_opt(m):
    """
    Multiplies a 2x2 matrix m by the Fibonacci transformation matrix:
       F = [[1, 1],
            [1, 0]]
    Given m = [[a, b],
               [c, d]],
    the result is:
       m * F = [[a+b, a],
                [c+d, c]]
    """
    a, b = m[0][0], m[0][1]
    c, d = m[1][0], m[1][1]
    return [[a + b, a],
            [c + d, c]]

def fib(n):
    n0, n = n, abs(n)
    if n == 0:
        r = 0
    else:
        # Start with the identity matrix.
        m = [[1, 0], [0, 1]]
        # Multiply m by F = [[1,1],[1,0]] (n-1) times.
        for i in range(1, n):
            m = mat_mul_opt(m)
        r = m[0][0]
    if n0 < 0:
        return negafib(n, r)
    return r

def measure_time_matrix(n):
    """Measures the execution time of computing fib(n) via matrix iteration."""
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
    
    # Print the results in a table format.
    print("\nTerm  | Fibonacci Value       | Execution Time (seconds)")
    print("----------------------------------------------------------")
    for term, fib_val, exec_time in results:
        print(f"{term:<5} | {fib_val:<21} | {exec_time:.6f}")

    # Plot the graph: term vs. execution time.
    terms = [item[0] for item in results]
    times = [item[2] for item in results]
    
    plt.figure(figsize=(10, 6))
    plt.plot(terms, times, marker='o', linestyle='-', color='green')
    plt.title("Execution Time for Matrix Iteration Fibonacci Calculations")
    plt.xlabel("Fibonacci Term (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
