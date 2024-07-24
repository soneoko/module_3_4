def single_root_words(root_word, *other_words):
    same_words = [i for i in other_words if i.lower() in root_word.lower() or root_word.lower() in i.lower()]
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)