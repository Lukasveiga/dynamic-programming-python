# Write a function `countConstruct(target, wordBank)` that accepts a target
# string and an array of strings.

# The function should return the number of ways that the target can be constructed
# by concatenating elements of the `wordBank` array.

from utils import checkFunctionResult, mesureFunctionTimeExecution

# m = target.length
# n = wordBank.length
# time = O(n^m * m)
# space = O(m²)
def countConstruct(target, wordBank):
    if target == "": return 1;
    totalCount = 0;
    
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            totalCount += countConstruct(suffix, wordBank)
            
    return totalCount;

# time = O(n * m²)
# space = O(m²)
def countConstructMemoization(target, wordBank, memo = {}):
    if target in memo: return memo[target];
    if target == "": return 1;
    totalCount = 0;
    
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            totalCount += countConstructMemoization(suffix, wordBank, memo)
            
    memo[target] = totalCount;  
    return totalCount;
    

if __name__ == '__main__':
    
    errorMessage = "CanConstruct fuction did not return the correct value"

    checkFunctionResult(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]), 2, errorMessage);
    checkFunctionResult(countConstructMemoization("purple", ["purp", "p", "ur", "le", "purpl"]), 2, errorMessage);

    target = "eeeeeeeeeeeeeeeeeeeeef";
    wordBank = ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"];

    results = {};

    results["countConstruct"] = mesureFunctionTimeExecution(countConstruct, target, wordBank);
    results["countConstructMemoization"] = mesureFunctionTimeExecution(countConstructMemoization, target, wordBank);

    print(sorted(results.items(), key=lambda x: x[1]));