def word_count(filename):
    script = open(filename)

    word_counts = {}
    
    for line in script:
        lines = line.rstrip()
        words = lines.split(" ")
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

print(word_count("twain.txt"))




