def find_missing_letter(chars):
    for i in range(1, len(chars)):
        if ord(chars[i]) - ord(chars[i - 1]) != 1:
            return chr(ord(chars[i - 1]) + 1)
    return None
