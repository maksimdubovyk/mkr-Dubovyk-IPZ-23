def get_most_common_words(file_path: str, n: int = 10):
    """
    Read the content of a text file, find the n most common words,
    and return them as a list of tuples (word, count).

    Args:
        file_path (str): The path to the input text file.
        n (int): Number of most common words to find (default is 10).

    Returns:
        list: A list of tuples containing the n most common words and their counts.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    words = text.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '').split()

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    most_common_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:n]

    return most_common_words
