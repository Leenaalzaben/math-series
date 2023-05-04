def fibonacci(n):
    #  Docstring
    '''
    This function takes a non-negative integer n as input and returns a list
    of the first n terms of the Fibonacci sequence.
    
        input ==> value
        output ==> represnt the fibonacci series for the input number.
    * where the Fibonacci sequence is
    a series of numbers in which each number is the sum of the two preceding
    ones, starting from 0 and 1.
    '''
    if n <= 1:
        if n == 0:
            return 0
        else:
            return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    #  Docstring
    '''
    Also this function takes a non-negative integer n as input,and returns a list
    of the first n terms of the Lucas series.
    it's the same with fibonacci except that it starts with 2 and 1 instead of 0 and 1.
        input ==> value
        output ==> represnt the lucas series for the input number.
    '''
    if n <= 1:
        if n == 0:
            return 2
        else:
            return 1

    return lucas(n-1) + lucas(n-2)


def sum_series(n,f=0,s=1):
    '''
    function will check if the enters are either 'fibonacci' or 'lucas' or it will  do be sum.
    series_type : str
        The type of series to generate ("fibonacc", "lucas", or "sum").
    n : int
    '''
    if f == 2 and s == 1:
        return lucas(n)
    elif f == 0 and s == 1:
        return fibonacci(n)
    else:
        return fibonacci(n) + lucas(f)
    