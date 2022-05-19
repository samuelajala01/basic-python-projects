print("Welcome to Python CLI word counter")
print("Paste or type a sentence and let python talk to your device.")

words = input("Enter a sentence or paste some words: ")

count = len(words.split())

if count > 0 and count < 2:
  print(count, "word was found")
elif count > 1:
  print(count, "words were found in total")
else:
 print(" no word was found")





