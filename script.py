def count_inherit_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
    words = text.lower().split()
    inherit_words = [word for word in words if word.startswith('inherit')]
    word_counts = {}
    for word in inherit_words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    for word, count in word_counts.items():
        print("{}\t{}".format(count, word.capitalize()))

count_inherit_words('origin.txt')

	

