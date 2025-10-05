
def count_words(text):
    words = len(text.split())
    return words

def words_counter(text):
    text = text.lower()
    count = {}
    
    for ch in text:
        if(ch.isalpha()):    
            count[ch] = count.get(ch, 0) +1

    char_list = []
    for ch, n in count.items():
        char_list.append({"char": ch, "num": n})
    return char_list


def sort_on(items):
    return items["num"]


