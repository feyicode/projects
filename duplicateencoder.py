def duplicate_encode(word):
    for i in range (len(word)):
        if word.count(word[i]) > 1:
            word = word[:i] + word[i] + word[i+1:]
'''        else:
            word.replace(word[i],"(")
    return word'''

print(duplicate_encode("test"))