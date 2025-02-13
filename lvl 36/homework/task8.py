def find_hello_index(string):
    return string.lower().find("hello")
string = "Hello world! This is a test. Hello again!"
index = find_hello_index(string)
print(f"The word 'hello' appears first at index: {index}" if index != -1 else "The word 'hello' was not found.")