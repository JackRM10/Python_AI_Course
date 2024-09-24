def Sorting(lst):
    lst.sort(key=len)
    return lst
     
# Driver code
lst = ["Jack", "Michael", "Susan", "Rachel", 
       "Richard", "Nick", "April"]
print(Sorting(lst))