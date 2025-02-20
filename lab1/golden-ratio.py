import math
import time
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(20000)
def negafib(n, r):
    """
    Adjusts the Fibonacci result for negative indices using:
       F(-n) = (-1)^(n+1) * F(n)
    """
    return (-1)**(n + 1) * r

def fib_golden_ratio(n):
    """
    Computes the nth Fibonacci number using the closed-form expression (Binet's Formula)
    with the Golden Ratio.
    
    Supports negative indices via the Negafibonacci rule.
    """
    n0, n = n, abs(n)
    if n == 0:
        r = 0
    elif n == 1:
        r = 1
    else:
        try:
            sqrt_5 = math.sqrt(5)
        except Exception as msg:
            print("Error computing sqrt(5):", msg)
            exit(1)
            
        phi = (1 + sqrt_5) / 2.0
        try:
            phi_n = math.pow(phi, n)
        except Exception as msg:
            print("Error computing phi^n:", msg)
            exit(1)
        psi_n = 1.0 / phi_n
        if n % 2 == 1:
            psi_n = -psi_n
        r = round((phi_n - psi_n) / sqrt_5)
        r = int(r)
    if n0 < 0:
        return negafib(n, r)
    return r

def measure_time_golden(n):
    """Measures the execution time of computing fib_golden_ratio(n)."""
    start = time.perf_counter()
    result = fib_golden_ratio(n)
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
        exec_time, fib_val = measure_time_golden(term)
        results.append((term, fib_val, exec_time))
    
    print("\nTerm  | Fibonacci Value       | Execution Time (seconds)")
    print("----------------------------------------------------------")
    for term, fib_val, exec_time in results:
        print(f"{term:<5} | {fib_val:<21} | {exec_time:.6f}")

    terms = [item[0] for item in results]
    times = [item[2] for item in results]
    
    plt.figure(figsize=(10, 6))
    plt.plot(terms, times, marker='o', linestyle='-', color='red')
    plt.title("Execution Time for Fibonacci (Golden Ratio) Calculations")
    plt.xlabel("Fibonacci Term (n)")
    plt.ylabel("Execution Time (seconds)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
