
def read_file_content(filename):
    with open(filename) as data:
        data_file = data.read()
        return data_file


def count_words():
    text = read_file_content("./story.txt").lower()
    word = text.split()

    dict_text = {}
    for words in word:
        if words in dict_text:
            dict_text[words] += 1
        else:
            dict_text[words] = 0
            dict_text[words] += 1
    return dict_text

print(count_words())




