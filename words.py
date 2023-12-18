#Simple story generator

from urllib.request import urlopen

story_words = []

def getWords():
    story = urlopen("http://sixty-north.com/c/t.txt")
    for line in story:
        line_words = line.decode("utf-8").split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def printWords(story_words):
    for i in story_words:
        print(i)

def main():
    words = getWords()
    printWords(words)


if __name__ == "__main__":
    main()
