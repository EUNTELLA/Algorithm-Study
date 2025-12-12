def solution(n):
    result = 0
    
    n_str = str(n)
    
    for number in n_str :
        result += int(number)
    
    return result