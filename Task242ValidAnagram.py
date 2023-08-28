# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

def isAnagram(s: str, t: str) -> bool:

     letters_s = list(s)
     letter_t = list(t)
     letter_t.sort()
     letters_s.sort()

     if (letter_t == letters_s):
         return True
     else:
         return False