# The edit distance between two strings refers to the minimum number of character
# insertions, deletions, and substitutions required to change one string to the other. For example,
# the edit distance between "kitten" and "sitting" is three: substitute the "k" for "s", substitute
# the "e" for "i", and append a "g".
# Write a Python program to compute the edit distance between two given strings.

def Edit_Distance(string1, string2):
    max_string = max(string1, string2, key=lambda x: len(x))
    mini_string = ""
    result = "" 
    if (max_string == string1):
        mini_string = string2
    else:
        mini_string = string1
    for i in range(0, len(max_string)):
        if(i<len(mini_string) and max_string[i] != mini_string[i]  ):
            result = result + max_string[i] 
        elif(i>=len(mini_string)):
            result = result + max_string[i] 
    return len(result) 
 
string1 = "kitten"
string2 = "sitting"
print(Edit_Distance(string1, string2))
   

