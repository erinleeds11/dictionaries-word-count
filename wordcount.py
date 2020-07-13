import sys
filename = sys.argv[1]

# def word_count(filename):
#     #open file
#     word_counts = Counter()
#     script = open(filename, "r")
#     contents = script.read()
#     contents = contents.replace("\n", " ").rstrip()
#     words = contents.split(" ")
#     for word in words:
#         word = word.rstrip('?!,.').lower()
#         word_counts[word] += 1

#     for word, count in word_counts.items():
#         print(word, count)

def word_count(filename):

    #create empty dictionary
    word_counts = {}
    script = open(filename)
    for line in script:
        lines = line.rstrip()
        words = lines.split(" ")
        for word in words:
            word = word.rstrip('?!,.').lower()
            word_counts[word] = word_counts.get(word, 0) + 1

    word_counts = sorted(word_counts.items(), key = lambda x: x[0], x[1], reverse = True)
    for word, word_counts in word_counts:
        print(word, word_counts)


word_count(filename)



