# Wirte a function `bestSum(targetSum, numbers)` that takes in a targetSum
# and an array of numbers as arguments.

# The function should return an array containing the shortest combination of
# numbers that add up to exactly the targetSum.

# If there is a tie for the shortest combination, you may return any one of the
# shortest.

from utils import checkFunctionResult, mesureFunctionTimeExecution

# m = targetSum; n = numbers.length;
# O(n^m * m) time
# O(m²) space
def bestSum(targetSum, numbers):
    if targetSum == 0: return [];
    if targetSum < 0: return None;
    
    shortestComb = None;
    
    for n in numbers:
        remainder = targetSum - n;
        remainderComb = bestSum(remainder, numbers);
        
        if remainderComb != None:
            comb =[*remainderComb, n];
            if shortestComb == None or (len(comb) < len(shortestComb)):
                shortestComb = comb;
            
    return shortestComb;

# m = targetSum; n = numbers.length;
# O(m² * n) time
# O(m²) space
def bestSumMemoization(targetSum, numbers, memo = {}):
    if targetSum in memo: return memo[targetSum];
    if targetSum == 0: return [];
    if targetSum < 0: return None;
    
    shortestComb = None;
    
    for n in numbers:
        remainder = targetSum - n;
        remainderComb = bestSumMemoization(remainder, numbers, memo);
        
        if remainderComb != None:
            comb =[*remainderComb, n];
            if shortestComb == None or (len(comb) < len(shortestComb)):
                shortestComb = comb;
            
    memo[targetSum] = shortestComb;
    return shortestComb;

if __name__ == '__main__':
    errorMessage = "BestSum fuction did not return the correct value";
    
    checkFunctionResult(bestSum(8, [1,4,5]), [4,4], errorMessage);
    checkFunctionResult(bestSumMemoization(8, [1,4,5]), [4,4], errorMessage);
    
    targetSum = 25;
    numbers = [1,2,5,25];
    
    results = {};
    
    results["bestSum"] = mesureFunctionTimeExecution(bestSum,targetSum,numbers);
    results["bestSumMemoization"] = mesureFunctionTimeExecution(bestSumMemoization,targetSum,numbers);
            
    print(sorted(results.items(), key=lambda x: x[1]));