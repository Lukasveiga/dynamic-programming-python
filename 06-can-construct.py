# Write a function `canConstruct(target, wordBank)` that accepts a target string
# and an array of strings.

# The function should return a boolean indicating whether or note the target can
# be constructed by concatenating elements of the wordBank array.

# You may reuse elements of the wordBank as many times as needed.

from utils import checkFunctionResult, mesureFunctionTimeExecution;

# m = target.length
# n = wordBank.length
# time = O(n^m * m)
# space = O(m²)
def canConstruct(target, wordBank):
    if target == "": return True;
    
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank) == True:
                return True;
            
    return False;

# time = O(n * m²)
# space = O(m²)
def canConstructMemoization(target, wordBank, memo = {}):
    if target in memo: return memo[target];
    if target == "": return True;
    
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if canConstructMemoization(suffix, wordBank, memo) == True:
                memo[target] = True;
                return True;
    
    memo[target] = False; 
    return False;


if __name__ == '__main__':
    
    errorMessage = "CanConstruct fuction did not return the correct value"
    
    checkFunctionResult(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]), True, errorMessage);
    checkFunctionResult(canConstructMemoization("abcdef", ["ab", "abc", "cd", "def", "abcd"]), True, errorMessage);
    
    target = "eeeeeeeeeeeeeeeeeeeeef";
    wordBank = ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"];
    
    results = {};
    
    results["canConstruct"] = mesureFunctionTimeExecution(canConstruct, target, wordBank);
    results["canConstructMemoization"] = mesureFunctionTimeExecution(canConstructMemoization, target, wordBank);
    
    print(sorted(results.items(), key=lambda x: x[1]));