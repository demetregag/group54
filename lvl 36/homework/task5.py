def count_word_the(paragraph):
    words = paragraph.lower().split()
    return words.count("the")
paragraph = """The quick brown fox jumps over the lazy dog. 
The dog barked at the stranger."""
count = count_word_the(paragraph)
print(f"The word 'the' appears {count} times.")