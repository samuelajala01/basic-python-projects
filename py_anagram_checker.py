print("Welcome to my Python Anagram Checker")

first_word = input("Enter first word: ")
second_word = input("Enter second word: ")

def checker():
  sort_first = len(sorted(first_word))
  sort_second = len(sorted(second_word))

  if(sort_first == sort_second):
    print(first_word, "and", second_word, "are anagrams")
  else:
    print(first_word, "and", second_word, "are not anagrams")

checker()
