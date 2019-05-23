
import sys

word_set = ()
current_key = None
total_words = 0

for line in sys.stdin:
    try:
        sorted_key, key, count = line.strip().split('\t', 2)
        count = int(count)
    except ValueError as e:
        continue
    if current_key != sorted_key:
        if current_key:
            #7823    eghilns 5   english,helsing,hesling,shengli,shingle
            print("{0}\t{1}\t{2}\t{3}".format(total_words, current_key, len(word_set), ",".join(sorted(word_set))))
            
        total_words = 0
        current_key = sorted_key
        word_set = ()
        
    word_set.add(key)
    total_words += count
    
if current_key:
    print("{0}\t{1}\t{2}\t{3}".format(total_words, current_key, len(word_set), ",".join(sorted(word_set))))