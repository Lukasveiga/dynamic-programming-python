# Write a function `allConstruct(target, wordBank)` that accepts a target
# string and an array of strings.

# The function should return a 2D array containing all the ways that the
# `target` can be constructed by concatenating elements of the `wordBank` array.

# You may reuse elements of `wordBank` as many times as needed.

from utils import checkFunctionResult, mesureFunctionTimeExecution

def allConstruct(target, wordBank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]];
    
    for i in range (0, len(target) + 1):
        for word in wordBank:
            if(target[i: i + len(word)] == word): 
                newCombinations = map(lambda subArray: [*subArray, word], table[i]);
                table[i + len(word)].extend(newCombinations);

    return table[len(target)];
    

if __name__ == '__main__':
    errorMessage = "AllConstruct fuction did not return the correct value"

    checkFunctionResult(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]), [['purp', 'le'], ['p', 'ur', 'p', 'le']], errorMessage);
    
    target = "eeeeeeeeeeeeeeeeeeeeef";
    wordBank = ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"];
    
    results = {};
    
    results["allConstruct"] = mesureFunctionTimeExecution(allConstruct, target, wordBank);

    print(sorted(results.items(), key=lambda x: x[1]));