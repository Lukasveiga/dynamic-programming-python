# Write a function `canConstruct(target, wordBank)` that accepts a target string
# and an array of strings.

# The function should return a boolean indicating whether or note the target can
# be constructed by concatenating elements of the wordBank array.

# You may reuse elements of the wordBank as many times as needed.

from utils import checkFunctionResult, mesureFunctionTimeExecution;

def canConstruct(target, wordBank):
    table = [False for _ in range(len(target) + 1)]
    table[0] = True
    for i in range (0, len(target) + 1):
        if(table[i] == True):
            for word in wordBank:
                if(target[i: i + len(word)] == word): table[i + len(word)] = True
            
    return table[len(target)];



if __name__ == '__main__':
    
    errorMessage = "CanConstruct fuction did not return the correct value"
    
    checkFunctionResult(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]), True, errorMessage);
    
    target = "eeeeeeeeeeeeeeeeeeeeef";
    wordBank = ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"];
    
    results = {};
    
    results["canConstruct"] = mesureFunctionTimeExecution(canConstruct, target, wordBank);
    
    print(sorted(results.items(), key=lambda x: x[1]));