# Write a function `howSum(targetSum, numbers)` that takes in a targetSum and an array of numbers
# as arguments.

# The function should return an array containing any combination of elements that add up to exactly
# the targetSum. If there is no combination that adds up to the targetSum, then return null.

from utils import mesureFunctionTimeExecution, checkFunctionResult;

def howSum(target, numbers):
    table = [None for _ in range(target + 1)]
    table[0] = []
    for i in range(0, target + 1):
        if(table[i] != None):
            for num in numbers:
                if(i + num <= target): table[i + num] = [*table[i], num];
    print(table)
    return table[target];  
        
        
if __name__ == '__main__':
    errorMessage = "HowSum fuction did not return the correct value";
    
    checkFunctionResult(howSum(7, [2,3]), [3,2,2], errorMessage);
    
    targetSum = 200;
    array = [7,14]
    
    results = {}
    
    results["canSum"] = mesureFunctionTimeExecution(howSum, targetSum, array);
    
    print(sorted(results.items(), key=lambda x: x[1]));