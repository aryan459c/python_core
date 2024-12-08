str = "i am sunil i am loking for a job"
def word_occ(string):
    words = string.split()
    word_count = {}
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
print(word_occ(str))
