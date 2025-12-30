def solution(s):
    answer = True
    
    stack = []
    
    #문자열 s크기만큼 반복  
    for i in s:
        if i == '(':
            stack.append('(')
        
        else:
        	
            if stack == []:
                return False
            
            else:
                stack.pop()
    
    if stack != []:
        return False
    
    return True