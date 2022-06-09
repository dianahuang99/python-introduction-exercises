def print_upper_words(words, must_start_with):
    """changes a word that starts with any letter that you pass in to uppercase"""
    for char in must_start_with:
        for word in words:
            if word[0] == char or word[0] == char.upper():
                print(word.upper())
