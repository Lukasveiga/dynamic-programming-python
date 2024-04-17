import time;

def mesureFunctionTimeExecution(function, input):
    start = time.time();
    function(input);
    end = time.time();
    return end - start;