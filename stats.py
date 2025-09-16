
def count_words(text):
    words = len(text.split())
    return words

def words_counter(words):
    character = words.lower()
    count = {}
    for ch in character:
        count[ch] = count.get(ch, 0) +1
        pass
    return count

