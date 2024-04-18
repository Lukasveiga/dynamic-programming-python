# Say that you are a traveler on a 2D grid. You begin in the top-left corner
# and your goal is to travel to the bottom-right corner. You may only move down
# or right.
# In how many ways can you travel to the goal on a grid with dimensions m * n?
# Write a fuction `gridTraveler(m,n)` that calculates this.

from utils import mesureFunctionTimeExecution, checkFunctionResult;

# O(2^n+m) time
# O(n+m) space
def gridTraveler(m,n):
    if m == 1 and n == 1: return 1;
    if m == 0 or n == 0: return 0;
    return gridTraveler(m - 1, n) + gridTraveler(m, n - 1);

# O(m*n) time
# O(m+n) space
def gridTravelerMemoization(m,n, memo = {}):
    key = str(m) + "," + str(n);
    
    if key in memo: return memo[key];
    
    if m == 1 and n == 1: return 1;
    if m == 0 or n == 0: return 0;
    
    memo[key] = gridTravelerMemoization(m - 1, n, memo) + gridTravelerMemoization(m, n - 1, memo);
    return memo[key];


if __name__ == '__main__':
    errorMessage = "Grid traveler fuction did not return the correct value";
    
    checkFunctionResult(gridTraveler(2,3), 3, errorMessage);
    
    m = 12;
    n = 12;
    
    results = {};
    results["gridTraveler"] = mesureFunctionTimeExecution(gridTraveler, m,n);
    results["gridTravelerMemoization"] = mesureFunctionTimeExecution(gridTravelerMemoization, m,n);

    print(sorted(results.items(), key=lambda x: x[1]));