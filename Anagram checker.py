from collections import Counter

# function to check if two strings are
# anagram or not
def check(s1, s2):
  
    # implementing counter function
    if(Counter(s1) == Counter(s2)):
        print("True")
    else:
        print("False")


# driver code
s1 = "listen"
s2 = "silent"
check(s1, s2)
