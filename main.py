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

def write_words_in_file(file_path: str, most_common_words: list):
    """
    Write the most common words and their counts to a text file.

    Args:
        file_path (str): The path to the output text file.
        most_common_words (list): A list of tuples containing the most common words and their counts.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        for word, count in most_common_words:
            file.write(f"{word}-{count}\n")

def main():
    """
    Main function to execute the script.
    """
    input_file_path = "input.txt"
    output_file_path = "output.txt"

    most_common_words = get_most_common_words(input_file_path)

    write_words_in_file(output_file_path, most_common_words)

if __name__ == "__main__":
    main()
