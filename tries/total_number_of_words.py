from trie import Trie


def total_number_of_words_in_a_trie(root: Trie, words=None):
    """
    1. we need to count all the instances of is_end_word
    2. we could use DFS to traverse all the nodes and
        increment a counter
    3. do this recursively
    4. we will visit all the letters
    """
    if not root:
        return len(words)

    if words is None:
        words = []

    for curr_letter, curr_child in root.children.items():
        if curr_child.is_end_word:
            words.append(curr_letter)
        total_number_of_words_in_a_trie(curr_child, words)

    return len(words)



def main():
    t = Trie()
    words = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
    for word in words:
        t.insert(word)

    result = total_number_of_words_in_a_trie(t.root)
    assert result == len(words)

main()