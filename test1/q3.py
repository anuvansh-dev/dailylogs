from datetime import datetime

def time_difference(ts1, ts2, T):
    """
    The function takes two timestamps of different zones in 'Day dd Mon yyyy hh:mm:ss +xxxx' format, 
    where xxxx is the timezone and returns the absolute difference between the two in seconds.
    
    Args:
        ts1 and ts2 (str): The input timestamps in the specified format.

    Returns:
        int: Absolute difference between the two given timestamps in seconds.
    """
    
    # Expected time format
    time_format = "%a %d %b %Y %H:%M:%S %z"
    
    # Converting timestamps to datetime objects
    dt1 = datetime.strptime(ts1, time_format)
    dt2 = datetime.strptime(ts2, time_format)
    
    # Absolute difference bw the above two in seconds
    return abs(int((dt1 - dt2).total_seconds()))
    
# Testing
testcases = int(input("Enter number of testcases: "))

for i in range(testcases):
    timestamp1 = input('Enter first time stamp: ').strip()
    timestamp2 = input('Enter second time stamp: ').strip()
    
    result = time_difference(timestamp1, timestamp2, testcases)
    print(result)
    print(type(result))
