from trie import Trie


def total_number_of_words_in_a_trie(root: Trie):
    """
    1. we need to count all the instances of is_end_word
    2. we could use DFS to traverse all the nodes and
        increment a counter
    3. do this recursively
    4. we will visit all the letters
    """
    if not root:
        return None
    # at each loop set word count at 0
    word_count = 0

    # increment the counter if the node is the end of the word
    if root.is_end_word:
        word_count += 1

    for curr_letter, curr_child in root.children.items():
        # continue to recursively increment the counter for each child
        word_count += total_number_of_words_in_a_trie(curr_child)

    return word_count


def main():
    t = Trie()
    words = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
    for word in words:
        t.insert(word)

    result = total_number_of_words_in_a_trie(t.root)
    assert result == len(words)

main()