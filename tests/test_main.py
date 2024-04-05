import pytest
from tests.conftest import prepare_input_text_file, prepare_output_text_file

from main import get_most_common_words, write_words_in_file

class Test:
    def test_loading_unexist_files(self):   
        unexist_path = "unexist_path.txt"     
        with pytest.raises(FileExistsError):
            get_most_common_words(unexist_path, 10)

    @pytest.mark.parametrize("n, expected_result", [
        (3, [('word1', 6), ('word2', 4), ('word3', 2)]),
        (2, [('word1', 6), ('word2', 4)]),
        (1, [('word1', 6)]),
    ])
    def test_get_most_common_words(self, prepare_input_text_file, n, expected_result):
        actual_result = get_most_common_words(prepare_input_text_file, n)

        assert actual_result == expected_result

    def test_write_words_in_file(self, prepare_output_text_file):
        most_common_words = [('word1', 5), ('word2', 3), ('word3', 2)]

        write_words_in_file(prepare_output_text_file, most_common_words)

        with open(prepare_output_text_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        assert len(lines) == len(most_common_words)

        for line, (word, count) in zip(lines, most_common_words):
            assert line.strip() == f"{word}-{count}"