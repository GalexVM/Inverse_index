from tensorflow.keras.preprocessing.text import text_to_word_sequence
import os
import time

def find_words_in_files(filenames):
    word_files_mapping = {}
    for filename in filenames:
        with open(filename, "r") as f:
            file_words = set(text_to_word_sequence(f.read()))
            for word in file_words:
                if word in word_files_mapping:
                    word_files_mapping[word].append(filename)
                else:
                    word_files_mapping[word] = [filename]
    return word_files_mapping

# Lista de nombres de archivos
file_list = [str(i)+"random_words.txt" for i in range(0,20)]

# Obtener el mapeo de palabras a archivos
start = time.time()
word_files_mapping = find_words_in_files(file_list)
end = time.time()
print("Time:", (end-start), "s")
# Imprimir el mapeo de palabras a archivos
print("writing to file...")
with open("output.txt","w") as file:
    for word, files in word_files_mapping.items():
        file.write(f"Palabra: {word}, Archivos: {files}\n")
