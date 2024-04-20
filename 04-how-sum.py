# Write a function `howSum(targetSum, numbers)` that takes in a targetSum and an array of numbers
# as arguments.

# The function should return an array containing any combination of elements that add up to exactly
# the targetSum. If there is no combination that adds up to the targetSum, then return null.

from utils import mesureFunctionTimeExecution, checkFunctionResult;

# O(m^n * n) time: m = array length
# O(n) space
def howSum(targetSum, numbers):
    if targetSum == 0: return [];
    if targetSum < 0: return None;
    
    for n in numbers:
        remainder = targetSum - n;
        remainderResult = howSum(remainder, numbers);
        if remainderResult != None:
            return [*remainderResult, n];
        
    return None;

# O(m*n²) time: m = array length
# O(n²) space
def howSumMemoization(targetSum, numbers, memo = {}):
    if targetSum in memo: return memo[targetSum];
    if targetSum == 0: return [];
    if targetSum < 0: return None;
    
    for n in numbers:
        remainder = targetSum - n;
        remainderResult = howSumMemoization(remainder, numbers, memo);
        if remainderResult != None:
            memo[targetSum] = [*remainderResult, n];
            return memo[targetSum];
        
    memo[targetSum] = None;
    return None;

if __name__ == '__main__':
    errorMessage = "HowSum fuction did not return the correct value";
    
    checkFunctionResult(howSum(7, [2,3]), [3,2,2], errorMessage);
    checkFunctionResult(howSum(7, [2,4]), None, errorMessage);
    
    checkFunctionResult(howSumMemoization(7, [2,3]), [3,2,2], errorMessage);
    checkFunctionResult(howSumMemoization(7, [2,4], {}), None, errorMessage);
    
    targetSum = 200;
    array = [7,14]
    
    results = {}
    
    results["canSum"] = mesureFunctionTimeExecution(howSum, targetSum, array);
    results["canSumMemoization"] = mesureFunctionTimeExecution(howSumMemoization, targetSum, array);
    
    print(sorted(results.items(), key=lambda x: x[1]));