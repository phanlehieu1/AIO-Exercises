import gdown
import os


url = "https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko"
output = "data.txt"


def download_file_from_google_drive(url, output):
    gdown.download(url, output, quiet=False)


download_file_from_google_drive(url, output)


def word_count(file_path):
    word_count_dict = {}

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                if word in word_count_dict:
                    word_count_dict[word] += 1
                else:
                    word_count_dict[word] = 1

    return word_count_dict


result = word_count(output)
print(result)
