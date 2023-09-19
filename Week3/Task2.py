# Given an unbalanced bracket sequence of ‘(‘ and ‘)’, convert it into a balanced
# sequence by adding the minimum number of ‘(‘ at the beginning of the string and ‘)’ at the
# end of the string by dynamic programming.


def unbalanced_bracket_sequence(String):
    start  = 0
    end = 0
    for  i in range(0,len(String)):
        if(String[i] == '('):
            start = start + 1
            end = end - 1  
        if(String[i] == ')'):
            end = end + 1
            start = start - 1    
    if(start<0):
        return ('(' *-start) + String
    if(end<0):
         return String + ')' * (-end) 
    return 'String is Balance'     
print(unbalanced_bracket_sequence('(a+b(c)'))  