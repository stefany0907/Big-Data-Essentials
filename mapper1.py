
import sys
import re

path = "stop_words_en.txt"

with open(path, "r") as file:
    stop_words = file.read().splitlines()

for line in sys.stdin:

    article_id, text = line.strip().split('\t', 1)

    try:
        words = re.split('\W*\s+\W*', text.strip())
        words = [word for word in words if (word not in stop_words) and word.isalpha()]
        
        for word in words:
            print("{}\t{}".format(word.lower(), 1))
            
    except Exception as e:
        print(e)
        continue