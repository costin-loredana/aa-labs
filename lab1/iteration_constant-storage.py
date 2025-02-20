import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(20000)
def negafib(n, r):
    """
    Adjusts the Fibonacci result for negative indices using the formula:
    F(-n) = (-1)^(n+1) * F(n)
    """
    return (-1)**(n+1) * r

def fib_iter(n):
    """
    Iteratively computes the nth Fibonacci number using constant space.
    Supports negative indices using the negafib function.
    """
    n0, n = n, abs(n)
    if n == 0:
        r = 0
    elif n == 1:
        r = 1
    else:
        f2, f1 = 1, 0
        for i in range(2, n+1):
            f2, f1 = f2 + f1, f2
        r = f2
    if n0 < 0:
        return negafib(n, r)
    return r

def measure_time_iter(n):
    """
    Measures the execution time of computing fib_iter(n).
    Returns a tuple: (execution_time_in_seconds, fibonacci_result)
    """
    start = time.perf_counter()
    result = fib_iter(n)
    end = time.perf_counter()
    return end - start, result

def main():
    try:
        input_str = input("Enter a list of Fibonacci term indices (comma separated, e.g., 5,10,15): ")
        # Convert input into a list of integers
        input_array = [int(item.strip()) for item in input_str.split(',')]
    except Exception as e:
        print("Invalid input. Please enter numbers separated by commas.")
        return

    results = []
    for term in input_array:
        exec_time, fib_val = measure_time_iter(term)
        results.append((term, fib_val, exec_time))
    
    # Print the results in a table format.
    print("\nTerm  | Fibonacci Value       | Execution Time (seconds)")
    print("----------------------------------------------------------")
    for term, fib_val, exec_time in results:
        print(f"{term:<5} | {fib_val:<21} | {exec_time:.6f}")

    # Plot a graph: term vs execution time.
    terms = [item[0] for item in results]
    times = [item[2] for item in results]
    plt.figure(figsize=(10, 6))
    plt.plot(terms, times, marker='o', linestyle='-', color='blue')
    plt.title("Execution Time for Iterative Fibonacci Calculations")
    plt.xlabel("Fibonacci Term (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
