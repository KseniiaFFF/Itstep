def clam_word(x):

    with open('tewq.txt', 'r') as file:
        lines = [line.strip() for line in file]

    result = '' 
    for n in x:
        index = n - 1
        result += lines[index]

    with open('word.txt', 'w') as file:
        file.write(result)

    return result