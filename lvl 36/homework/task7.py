def count_word_occurrences(text, word):
    words = text.lower().split()
    return words.count(word.lower())
text = "The cat sat on the mat. The cat is happy."
word = input("Enter the word to search for: ")
count = count_word_occurrences(text, word)
print(f"The word '{word}' appears {count} times in the text.")
