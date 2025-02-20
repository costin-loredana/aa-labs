import time
import matplotlib.pyplot as plt

def negafib(n, r):
    """
    Adjusts the Fibonacci result for negative indices using:
        F(-n) = (-1)^(n+1) * F(n)
    """
    return (-1)**(n + 1) * r
    # """
    # Computes the nth Fibonacci number using a recursive method with dictionary memoization
    # and a unique approach via bit-shifting.
    
    # The method builds a dictionary F of necessary indices and then computes F[k] recursively.
    # Negative indices are handled via the negafib adjustment.
    # """
def fib(n):
    n0, n = n, abs(n)
    F = {}
    qinx = []
    qinx.append(n)
    F[n] = -1
    while qinx:
        k = qinx.pop() >> 1 
        if (k-1) not in F:
            F[k-1] = -1
            qinx.append(k-1)
        if k not in F:
            F[k] = -1
            qinx.append(k)
        if (k+1) not in F:
            F[k+1] = -1
            qinx.append(k+1)
    F[0], F[1], F[2] = 0, 1, 1
    keys_sorted = sorted(F.keys())
    for k in keys_sorted[3:]:
        k2 = k >> 1  # k2 = k//2
        f1, f2, f3 = F[k2 - 1], F[k2], F[k2 + 1]
        if k % 2 == 0:
            F[k] = f3 * f3 - f1 * f1
        else:
            F[k] = f3 * f3 + f2 * f2
    r = F[n]
    if n0 < 0:
        return negafib(n, r)
    return r

def measure_time_recursive(n):
    """
    Measures the execution time of computing fib(n) using the recursive method.
    Returns a tuple: (execution_time, fibonacci_result)
    """
    start = time.perf_counter()
    result = fib(n)
    end = time.perf_counter()
    return end - start, result

def main():
    try:
        input_str = input("Enter a list of Fibonacci term indices (comma separated, e.g., 5,10,15): ")
        terms = [int(item.strip()) for item in input_str.split(',')]
    except Exception as e:
        print("Invalid input:", e)
        return

    results = []
    for term in terms:
        exec_time, fib_val = measure_time_recursive(term)
        results.append((term, fib_val, exec_time))
    
    # Print the results in a table.
    print("\nTerm  | Fibonacci Value       | Execution Time (seconds)")
    print("----------------------------------------------------------")
    for term, fib_val, exec_time in results:
        print(f"{term:<5} | {fib_val:<21} | {exec_time:.6f}")
    
    # Plot a graph: Fibonacci term vs. execution time.
    x_vals = [item[0] for item in results]
    y_vals = [item[2] for item in results]
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, marker='o', linestyle='-', color='orange')
    plt.title("Execution Time for Recursive Fibonacci Calculations")
    plt.xlabel("Fibonacci Term (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
