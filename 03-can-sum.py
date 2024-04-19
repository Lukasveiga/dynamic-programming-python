# Write a function `canSum(targetSum, numbers)` that takes in a targetSum
# and a array of numbers as arguments.

# The function should return a boolean indicating whether or not it is 
# possible to generate the targetSum using numbers from the array.

# You may use an element of the array as many times as needed.
# You may assume that all input numbers are nonnegative.

# Example 1: canSum(7, [5,3,4,7]) -> true; 3 + 4 or 7
# Example 2: canSum(7, [2,4]) -> false;

from utils import checkFunctionResult, mesureFunctionTimeExecution;

# O(n^m) time: m = array length
# O(n) space
def canSum(targetSum, array):
    if targetSum == 0: return True;
    if targetSum < 0: return False;
    
    for n in array:
        if (canSum(targetSum - n, array) == True):
            return True;
    
    return False;

# O(m*n) time
# O(m) space
def canSumMemoization(targetSum, array, memo ={}):
    if targetSum in memo: return memo[targetSum];
    if targetSum == 0: return True;
    if targetSum < 0: return False;
    
    for n in array:
        reminder = targetSum - n
        if (canSumMemoization(reminder, array, memo) == True):
            memo[targetSum] = True;
            return True;
    
    memo[targetSum] = False;
    return False;

if __name__ == '__main__':
    errorMessage = "CanSum fuction did not return the correct value";
    
    checkFunctionResult(canSum(7, [5,3,4,7]), True, errorMessage);
    checkFunctionResult(canSumMemoization(7, [5,3,4,7]), True, errorMessage);
    
    targetSum = 200;
    array = [7,14]
    
    results = {}
    
    results["canSum"] = mesureFunctionTimeExecution(canSum, targetSum, array);
    results["canSumMemoization"] = mesureFunctionTimeExecution(canSumMemoization, targetSum, array);
    
    print(sorted(results.items(), key=lambda x: x[1]));
    
    