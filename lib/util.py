def print_progress(
    message: str,
    current: float,
    target: float,
    precision: int = 2
) -> None:
    '''
        Prints a message with a progress indicator appended (% progress)
        
        message: str
            The message that you would like to print
        current: float
            The current amount of progress
        target: float
            The target amount of progress
        precision: int
            The number of decimal places to include in the progress indicator
    '''
    
    percent = (current * 10**(2 + precision) // target) / 10**precision
    print(f'\r{message} {percent}%', end="")
