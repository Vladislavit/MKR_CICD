from text_processing.text_processing import count_words_and_sentences

file_path = "text.txt"
num_of_words, num_of_sentences = count_words_and_sentences(file_path)
print(f"кількість слів: {num_of_words}")
print(f"кількість реченнь: {num_of_sentences}")