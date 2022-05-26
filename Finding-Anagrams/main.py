# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here


    sort_first = len(sorted(word))
    sort_second = len(sorted(anagram))

    
    if(sort_first == sort_second):
        print(word, "and", anagram, "are anagrams")
        return True
    else:
        print(word, "and", anagram, "are not anagrams")
        return False

    

word = input("Enter first word: ")
anagram = input("Enter second word: ")

find_anagram(word, anagram)
