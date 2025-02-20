import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(20000)
def fib_memo(n, F):
    if F[n] is None:
        if n == 0:
            F[n] = 0
        elif n == 1:
            F[n] = 1
        else:
            F[n] = fib_memo(n - 1, F) + fib_memo(n - 2, F)
    return F[n]

def fib(n):
    if n < 0:
        # Negafibonacci: F(-n) = (-1)**(-n+1) * F(n)
        return (-1)**(-n+1) * fib(-n)
    F = [None] * (n + 1)
    return fib_memo(n, F)

def measure_time(n):
    start = time.perf_counter()
    result = fib(n)
    end = time.perf_counter()
    return end - start, result

def main():
    # Option 1: Use a predefined array of term indices.
    # input_array = [5, 10, 15, 20, 25, 30]
    
    # Option 2: Allow user to input a comma-separated list of terms.
    try:
        input_str = input("Enter a list of Fibonacci term indices (comma separated, e.g., 5,10,15): ")
        input_array = [int(item.strip()) for item in input_str.split(',')]
    except Exception as e:
        print("Invalid input. Please enter numbers separated by commas.")
        return

    results = []
    for term in input_array:
        t, fib_val = measure_time(term)
        results.append((term, fib_val, t))

    # Print the results in a table.
    print("\nTerm  | Fibonacci Value       | Execution Time (seconds)")
    print("----------------------------------------------------------")
    for term, fib_val, t in results:
        print(f"{term:<5} | {fib_val:<21} | {t:.6f}")

    # Plot the graph: term vs. execution time.
    terms = [item[0] for item in results]
    times = [item[2] for item in results]
    
    plt.figure(figsize=(10, 6))
    plt.plot(terms, times, marker='o', linestyle='-', color='blue')
    plt.title("Execution Time for Fibonacci Calculations")
    plt.xlabel("Fibonacci Term (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
