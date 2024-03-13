import re
# import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords

def remove_special_characters(text):
    pattern =r'[^\w\s.,;!?]'
    clean_text = re.sub(pattern, '', text)
    return clean_text

def remove_stop_words(splittedText):
    STOPWORDS = set(stopwords.words('vietnamese'))
    text =  ' '.join([word for word in splittedText if word not in STOPWORDS])
    return text

def remove_one_character_words(splittedText):
    text =  ' '.join([word for word in splittedText if len(word) > 1]) 
    return text

try:
    with open('data.txt', "r", encoding="utf-8") as file:
        file_content = file.read()
        removedSpecialCharacter=remove_special_characters(file_content)
        convertToLowerCase=removedSpecialCharacter.lower()
        splittedText=removedSpecialCharacter.split(" ")
        removedStopWords=remove_stop_words(splittedText)
        removedOneCharacterWords=remove_one_character_words(splittedText)
        print("file_content:", file_content)
        print("removedSpecialCharacter:", removedSpecialCharacter)
        print('convertToLowerCase:', convertToLowerCase)
        print('removedStopWords:', removedStopWords)
        print('splittedText:', splittedText)
        print('removedOneCharacterWords:', removedOneCharacterWords)
except FileNotFoundError:
    print(f"File '{'data.txt'}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")