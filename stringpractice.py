# From https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00-introduction-to-computer-science-and-programming-fall-2008/assignments/pset3.pdf

# In this assignment we will use the .find() method of a string. This method returns the index of the first substring
#  found in the string. For instance, 'abcdefg'.find('cde') will return 2 because the substring 'cde' starts in the 2nd
#  position of the string 'abcdefg'. Recall that in python indices start at 0. We can provide a second argument to the
#  .find() method to search only for substrings after the index provided. For example, 'abcdefgcde'.find('cde', 3) returns
#  7 since it starts looking at index 3 of the string and misses the first matching substring.

# Write a function called countSubStringMatch(target, key) that returns the number of times the substring key appears
#  in the longer string target. Use an iterative solution.
def countSubStringMatch(target, key):
    pass

# print(countSubStringMatch("atgacatgcacaagtatgcat", "ca"))
# Expected output:
# 4

# print(countSubStringMatch("atgacatgcacaagtatgcat", "eieieo"))
# Expected output:
# 0

# Write a function called subStringMatchExact(target, key) that returns a string listing all starting indices of a
#  substring key in a the longer string target. Recall you can cast ints as strings using str() concatenate strings using
#  the + symbol.
def subStringMatchExact(target, key):
    pass

# print(subStringMatchExact("atgacatgcacaagtatgcat", "ca"))
# Expected output:
# "4 8 10 18"

# print(subStringMatchExact("atgacatgcacaagtatgcat", "eieieo"))
# Expected output:
# ""

# print(subStringMatchExact("atgacatgcacaagtatgcat", "a"))
# Expected output:
# "0 3 5 9 11 12 15 19"

# Write a function called subStringMatchExactlyOneSub(target, key) that returns a string listing all starting indices of
#  a substring key in the longer string target where exactly one character within the substring is wrong. For instance,
#  if the target is "cag" then positive examples could be "caa", "aag", or "ctg" among others. Do not return indices of
#  exact matches! Use the same strategy as before to return a concatenated string.
def subStringMatchExactlyOneSub(target, key):
    pass

# print(subStringMatchExactlyOneSub("atgacatgcacaagtatgcat", "cat"))
# Expected output:
# "8 10 14"
