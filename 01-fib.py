# Write a function `fib(n)` that takes in a number as an argument.
# The function should return the n-th number of the Fibonacci sequence.
from utils import mesureFunctionTimeExecution, checkFunctionResult;

# O(n) time
# O(n) space
def fib(n):
    first = 1;
    second = 1;
    fibNumber = 0;
    
    for i in range(0, n - 2):
        fibNumber = first + second;
        first = second;
        second = fibNumber;
    
    return fibNumber;

# O(2^n) time
# O(n) space
def fibRecursion(n):
    if (n <= 2): return 1;
    return fibRecursion(n - 1) + fibRecursion(n - 2);

# O(n) time
# O(n) space
def fibRecursionMemoization(n, memo = {}):
    if n in memo: return memo[n];
    if (n <= 2): return 1;
    memo[n] = fibRecursionMemoization(n - 1, memo) + fibRecursionMemoization(n - 2, memo);
    return memo[n];
    

if __name__ == '__main__':
    errorMessage = "Fib fuction did not return the correct value";
    
    checkFunctionResult(fib(7), 13, errorMessage);
    checkFunctionResult(fibRecursion(7), 13, errorMessage);
    checkFunctionResult(fibRecursionMemoization(7), 13, errorMessage);
    
    input = 30;
    
    results = {};
    results["fib"] = mesureFunctionTimeExecution(fib, input);
    results["fibRecursion"] = mesureFunctionTimeExecution(fibRecursion, input);
    results["fibRecursionMemoization"] = mesureFunctionTimeExecution(fibRecursionMemoization, input);
    
    print(sorted(results.items(), key=lambda x: x[1]));
    