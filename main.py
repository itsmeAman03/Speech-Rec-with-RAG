from imports import LANGUAGES
import whisper 
from Translateionn import text_to_text_translate
import os
from dotenv import load_dotenv
from transformers import pipeline 
from summarization import summarization



def get_file_path(path: str = "") -> str:
    arr = os.listdir(path)
    print("List of files in artifacts:")
    list_file = {}

    for idx, value in enumerate(arr):
        print(f"{idx} - {value}")
        list_file[idx] = value

    while True:
        try:
            selected_file_idx = int(input("Enter the file index from the above list: "))
            selected_file = list_file[selected_file_idx]
            selected_file = str(path+selected_file)
            print(selected_file)
            return selected_file
        except (KeyError, ValueError):
            print("Invalid file index. Please try again.")

def get_text_from_audio(path: str = "") -> str:

    model = whisper.load_model("base")

   

    result = model.transcribe(path,fp16=False)
    return result["text"]


def detect_lang_audio(path: str = "") -> str :
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(path)
    audio = whisper.pad_or_trim(audio)
    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    # detect the spoken language
    _, probs = model.detect_language(mel)
    detected_lang = max(probs, key=probs.get)
    return detected_lang

def get_language(lang: str = "") -> str:
    languages = LANGUAGES
    code_lang = [code for code, language in languages.items() if language == selected_lang]
    print(code_lang[0])
    return code_lang




if __name__=='__main__':
    
    load_dotenv()

    # path = string(input("Enter the directory where your audio/video files are: "))
    path = "/home/meister/Projects/Speech-Rec-with-RAG/artifacts/"
    file_path = get_file_path(path)

    transciption_of_audio = get_text_from_audio(file_path)
    print(transciption_of_audio)

    option = int(input("Choose option from Below : \n 1. Audio summarization \n2. Audio translation in text"))

    if option==1:
        """ 
        Audio summarization in text
        """
        sum_text = summarization(transciption_of_audio)
        print(sum_text)

    elif option==2:
        """ 
        translation 
        """
        target_lang = str(input("Enter the target language"))
        out_lang = get_language(target_lang)
        in_lang = detect_lang_audio(file_path)
        text_trans = text_to_text_translate(in_lang,out_lang,transciption_of_audio)
        print(text_trans)
    
    else: 
        print("Wrong Input!!")
