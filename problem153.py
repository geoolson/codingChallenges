"""
Find an efficient algorithm to find the smallest distance (measured in number of words) 
between any two given words in a string.

For example, given words "hello", and "world" and a text content of "dog cat hello cat dog dog hello cat 
world", return 1 because there's only one word "cat" in between the two words.
"""
import sys

def wordCount(sentence, first, end):
    count = 0
    initialWord = False
    for i in sentence:
        if (i == first):
            if(initialWord):
                count = 0
            else:
                initialWord = True
        elif(initialWord and i == end):
            return count
        elif (initialWord):
            count += 1

if __name__ == "__main__":
    if(len(sys.argv) == 4):
        sentence = sys.argv[1].split(" ")
        count = wordCount(sentence, sys.argv[2], sys.argv[3])
        print(count)
    else:
        print("error")