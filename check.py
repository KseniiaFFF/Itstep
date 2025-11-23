def check_word(result):
    with open('bad_words.txt', 'r') as file:
        bad_text = file.read().replace(",", " ")

    bad_words = bad_text.split()

    if result.lower() in bad_words:
        print("Bad word")
        return True
    return False