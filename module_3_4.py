def single_root_words(root_word, *other_words):
    same_words = []
    for words in other_words:
        if root_word.lower().count(words.lower()) or words.lower().count(root_word.lower()):
            same_words.append(words)
    return same_words



print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))

print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))

        
    