# Write a function `countConstruct(target, wordBank)` that accepts a target
# string and an array of strings.

# The function should return the number of ways that the target can be constructed
# by concatenating elements of the `wordBank` array.

from utils import checkFunctionResult, mesureFunctionTimeExecution

def countConstruct(target, wordBank):
    table = [0 for _ in range(len(target) + 1)]
    table[0] = 1
    for i in range (0, len(target) + 1):
        if(table[i] > 0):
            for word in wordBank:
                if(target[i: i + len(word)] == word): table[i + len(word)] += table[i];
    return table[len(target)];


if __name__ == '__main__':
    
    errorMessage = "CanConstruct fuction did not return the correct value"

    checkFunctionResult(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]), 2, errorMessage);

    target = "eeeeeeeeeeeeeeeeeeeeef";
    wordBank = ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"];

    results = {};

    results["countConstruct"] = mesureFunctionTimeExecution(countConstruct, target, wordBank);

    print(sorted(results.items(), key=lambda x: x[1]));