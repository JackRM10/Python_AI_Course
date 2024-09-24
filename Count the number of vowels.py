#Count the number of vowels
string = "Counting vowels is fun!"
vowels = "aeiouAEIOU"
 
count = sum(string.count(vowel) for vowel in vowels)
print(count)