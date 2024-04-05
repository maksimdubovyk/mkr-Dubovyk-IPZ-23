import pytest

from main import get_most_common_words

class Test:
    def test_loading_unexist_files(self):   
        unexist_path = "unexist_path.txt"     
        with pytest.raises(FileExistsError):
            get_most_common_words(unexist_path, 10)