import os
import pytest


@pytest.fixture(autouse=True)
def prepare_input_text_file(tmp_path):
    target_file = os.path.join(tmp_path, 'input_test.txt')
    with open(target_file, 'w') as file:
        lines = ['Word1 Word2 Word3\n',
                 'Word1, Word1, Word2,\n',
                 'Word1. Word2. Word1.\n',
                 'Word1! Word2? Word3 \n',
                 ]
        file.writelines(lines)
    return target_file

@pytest.fixture(autouse=True)
def prepare_output_text_file(tmp_path):
    target_file = os.path.join(tmp_path, 'output_test.txt')
    open(target_file, 'a').close()
    return target_file