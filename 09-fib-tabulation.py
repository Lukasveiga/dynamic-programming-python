# Write a function `fib(n)` that takes in a number as an argument.
# The function should return the n-th number of the Fibonacci sequence.
from utils import mesureFunctionTimeExecution, checkFunctionResult;

# O(n) time
# O(n) space
def fib(n):
    # 0 1 1 ...
    second = 1;
    third = 1;
    fibNumber = 0;
    
    for i in range(0, n - 2):
        fibNumber = second + third;
        second = third;
        third = fibNumber;
    
    return fibNumber;

def fibSecondAproach(n):
    table = [0] * (n + 1);
    table[1] = 1;
    for i in range(n):
        table[i + 1] += table[i]
        if i + 2 <= n:
            table[i + 2] += table[i]
    return table[n]

if __name__ == '__main__':
    errorMessage = "Fib fuction did not return the correct value";
    checkFunctionResult(fib(7), 13, errorMessage);
    checkFunctionResult(fibSecondAproach(7), 13, errorMessage);
    
    input = 30;
    
    results = {};
    results["fib"] = mesureFunctionTimeExecution(fib, input);
    results["fibSecondAproach"] = mesureFunctionTimeExecution(fibSecondAproach, input);
    fibSecondAproach(6);
    print(sorted(results.items(), key=lambda x: x[1]));
