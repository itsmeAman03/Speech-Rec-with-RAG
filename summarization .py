import torch
import transformers
from transformers import pipeline

def summarization(result:str)-> str:
    prompt = f"There's some text that you want to summarize. This could be an article, a news story, a podcast ,a conversation between people, or any other kind of text that you want to get the gist of.: \n {result}"  
    summarizer = pipeline("summarization", model="google-t5/t5-base", tokenizer="google-t5/t5-base", framework="tf",token=userdata.get('HF_TOKEN'))
    summ = summarizer(prompt, min_length=150, max_length=500)
    summ = summ['summary_text']
    return summ
