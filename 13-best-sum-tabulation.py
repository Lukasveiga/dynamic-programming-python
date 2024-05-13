# Wirte a function `bestSum(targetSum, numbers)` that takes in a targetSum
# and an array of numbers as arguments.

# The function should return an array containing the shortest combination of
# numbers that add up to exactly the targetSum.

# If there is a tie for the shortest combination, you may return any one of the
# shortest.

from utils import checkFunctionResult, mesureFunctionTimeExecution

def bestSum(target, numbers):
    table = [None for _ in range(target + 1)]
    table[0] = []
    for i in range(0, target + 1):
        if(table[i] != None):
            for num in numbers:
                combination = [*table[i], num];
                if(i + num <= target and (table[i + num] == None or len(table[i + num]) > len(combination))):
                    table[i + num] = combination;
    return table[target];


if __name__ == '__main__':
    errorMessage = "BestSum fuction did not return the correct value";
    
    checkFunctionResult(bestSum(8, [1,4,5]), [4,4], errorMessage);
    
    targetSum = 25;
    numbers = [1,2,5,25];
    
    results = {};
    
    results["bestSum"] = mesureFunctionTimeExecution(bestSum,targetSum,numbers);
            
    print(sorted(results.items(), key=lambda x: x[1]));