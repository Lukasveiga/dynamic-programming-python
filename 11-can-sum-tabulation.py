# Write a function `canSum(targetSum, numbers)` that takes in a targetSum
# and a array of numbers as arguments.

# The function should return a boolean indicating whether or not it is 
# possible to generate the targetSum using numbers from the array.

# You may use an element of the array as many times as needed.
# You may assume that all input numbers are nonnegative.

# Example 1: canSum(7, [5,3,4,7]) -> true; 3 + 4 or 7

from utils import mesureFunctionTimeExecution, checkFunctionResult;

def canSum(target, numbers):
    table = [False for _ in range(target + 1)]
    table[0] = True
    for i in range(0, target + 1):
        if (table[i] == True):
            for num in numbers:
                if(i + num <= target): table[i + num] = True
                
    return table[target];
                
        
    

if __name__ == '__main__':
    errorMessage = "CanSum fuction did not return the correct value";
    
    checkFunctionResult(canSum(7, [5,3,4,7]), True, errorMessage);
    
    targetSum = 200;
    array = [7,14]
    
    results = {}
    
    results["canSum"] = mesureFunctionTimeExecution(canSum, targetSum, array);
    
    print(sorted(results.items(), key=lambda x: x[1]));