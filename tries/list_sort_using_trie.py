"""
implement the sort_list() function which will sort the elements of a list of strings.

revisit: code is incomplete
"""
from trie import Trie


def get_words(root, result, level, word):
    # Leaf denotes end of a word
    if root.is_end_word:
        # current word is stored till the 'level' in the character array
        temp = ""
        for x in range(level):
            temp += word[x]
        result.append(temp)

    for i, (letter, child) in enumerate(root.children.items()):
        if child is not None:
            # Non-null child, so add that index to the character array
            word[level] = letter
            get_words(child, result, level + 1, word)


def sort_list(arr):
    result = []

    # Creating Trie and Inserting words from array
    trie = Trie()
    for word in arr:
        trie.insert(word)

    word = [''] * 20
    get_words(trie.root, result, 0, word)
    return result


def main():
    arr = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
    assert sort_list(arr) == ['a', 'abc','answer','any','by','bye','the','their','there']

main()