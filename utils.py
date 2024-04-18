import time;

def mesureFunctionTimeExecution(function, *args):
    start = time.time();
    function(*args);
    end = time.time();
    return end - start;

def checkFunctionResult(given, expected, message):
    if (given != expected):
       raise Exception(message);