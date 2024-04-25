# Write a function `allConstruct(target, wordBank)` that accepts a target
# string and an array of strings.

# The function should return a 2D array containing all the ways that the
# `target` can be constructed by concatenating elements of the `wordBank` array.

# You may reuse elements of `wordBank` as many times as needed.

from utils import checkFunctionResult, mesureFunctionTimeExecution

# m = target.length
# n = wordBank.length
# time = O(n^m)
# space = O(m²)
def allConstruct(target, wordBank):
    if target == "": return [[]];
    
    allPossibilities = [];
    
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, wordBank);
            targetWays = list(map(lambda way: [word, *way], suffixWays));
            allPossibilities.extend(targetWays);
                
    return allPossibilities;


# time = O(n^m * m)
# space = O(m²)
def allConstructMemoization(target, wordBank, memo = {}):
    if target in memo: return memo[target];                                                    
    if target == "": return [[]];
    
    allPossibilities = [];
    
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffixWays = allConstructMemoization(suffix, wordBank, memo);
            targetWays = list(map(lambda way: [word, *way], suffixWays));
            allPossibilities.extend(targetWays);
            memo[target] = allPossibilities;
    
    memo[target] = allPossibilities;        
    return allPossibilities;
    

if __name__ == '__main__':
    
    errorMessage = "AllConstruct fuction did not return the correct value"

    checkFunctionResult(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]), [['purp', 'le'], ['p', 'ur', 'p', 'le']], errorMessage);
    checkFunctionResult(allConstructMemoization("purple", ["purp", "p", "ur", "le", "purpl"]), [['purp', 'le'], ['p', 'ur', 'p', 'le']], errorMessage);
    
    target = "eeeeeeeeeeeeeeeeeeeeef";
    wordBank = ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"];
    
    results = {};
    
    results["allConstruct"] = mesureFunctionTimeExecution(allConstruct, target, wordBank);
    results["allConstructMemoization"] = mesureFunctionTimeExecution(allConstructMemoization, target, wordBank);

    print(sorted(results.items(), key=lambda x: x[1]));