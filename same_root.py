def single_root_words(root_word, *other_words):
    same_word = []
    for i in range(len(other_words)):
        if root_word.lower() in other_words[i].lower() or other_words[i].lower() in root_word.lower():
            same_word.append(other_words[i])            
    print(same_word)
    
single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')