
import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')  # required to convert to unicode

path = 'stop_words_en.txt'

# Your code for reading stop words here
with open(path, "r") as f:
    stop_words = f.read().split('\n')

for line in sys.stdin:
    try:
        article_id, text = unicode(line.strip()).split('\t', 1)
    except ValueError as e:
        continue

    words = re.split("\W*\s+\W*", text, flags=re.UNICODE)
    words = [word for word in words if (word not in stop_words) and word.isalpha()]
    # Your code for mapper here.
    for word in words:
        print >> sys.stderr, "reporter:counter:Wiki stats,Total words,%d" % 1
        print "%s\t%d" % (word.lower(), 1)