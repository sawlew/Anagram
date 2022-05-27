word = input("Enter your first word: ").lower()
anagram = input("Enter your second word: ").lower()

def check(word, anagram):
    if (sorted(word) == sorted(anagram)):
        return True
    else:
        return False

print(check(word, anagram))# Anagram
