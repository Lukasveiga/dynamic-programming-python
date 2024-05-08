# Say that you are a traveler on a 2D grid. You begin in the top-left
# corner and your goal is to travel to the bottom-right corner. You may
# only mov down or right.

# In how many ways you travel to the goal on a grid with dimensions m * n?
# Write a fuction `gridTraveler(m,n)` that calculates this.

from utils import mesureFunctionTimeExecution, checkFunctionResult;

def gridTraveler(m, n):
    table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    table[1][1] = 1;
    for i in range(0, m + 1):
        for j in range(0, n + 1):
            current = table[i][j]
            if(j + 1 <= n): table[i][j + 1] += current;
            if(i + 1 <= m):table[i + 1][j] += current;
            
    return table[m][n]

if __name__ == '__main__':
    errorMessage = "Grid traveler fuction did not return the correct value";
    
    checkFunctionResult(gridTraveler(2,3), 3, errorMessage);
    
    m = 12;
    n = 12;
    
    results = {};
    results["gridTraveler"] = mesureFunctionTimeExecution(gridTraveler, m,n);

    print(sorted(results.items(), key=lambda x: x[1]));
