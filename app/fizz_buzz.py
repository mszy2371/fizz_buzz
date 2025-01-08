
def fizz_buzz(start: int, end: int):
    if not (1 <= start <= 100 and 1 <= end <= 100):
        raise ValueError("Both start and end must be between 1 and 100 inclusive.")
    if start > end:
        raise ValueError("Start must be less than or equal to end.")
    
    results = []
    for i in range(start, end + 1):
        output = ""
        if i % 3 == 0:
            output += str(i) + " fizz "
        if i % 5 == 0:
            output += str(i) + " buzz "
        results.append(output or str(i))
    return results
    
# usage example:
# print(fizz_buzz(1, 5))  # ['1', '2', '3 fizz ', '4', '5 buzz ']
