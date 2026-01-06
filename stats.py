def sort_on(item):
    return item['num']

def get_file_as_text(_path_to_file):
    with open(_path_to_file) as f:
        content_ = f.read()
    return content_

def count_words(text_):
    words_ = text_.split()
    return len(words_)

def list_most_common_words(text, number_of_words):
    text_ = text.lower()
    words_ = text_.split()
    words_dict_ = {}
    dict_list_ = []
    for word_ in words_:
        if word_ in words_dict_:
            words_dict_[word_] += 1
        else:
            words_dict_[word_] = 1
    for entry_ in words_dict_:
        dict_list_.append({'word': entry_, 'num': words_dict_[entry_]})
    dict_list_.sort(key=sort_on, reverse=True)
    return dict_list_[:number_of_words:1]

def count_letters(text_):
    text_lowercase_ = text_.lower()
    character_dictionary_ = {}

    for character in text_lowercase_:
        if character in character_dictionary_:
            character_dictionary_[character] += 1
        else:
            character_dictionary_[character] = 1
    return character_dictionary_

def sort_by_number(dict_):
    new_list_ = []
    for entry_ in dict_:
        #if entry_.isalpha():
        new_list_.append({'char': entry_, 'num': dict_[entry_]})
    new_list_.sort(key=sort_on, reverse=True)
    return new_list_
    