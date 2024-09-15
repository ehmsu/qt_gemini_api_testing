import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

class Gemini():
    def __init__(self) -> None:
        genai.configure(api_key=os.environ["API_KEY"])
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def text_prompt(self, text:str):
        # what's the difference between generate_content and send_message?
        response = model.generate_content(text, request_options={'timeout':10})
        return(response.text)
    
    def image_insert(self, image, text):
        result = model.generate_content(
            [image, "\n\n", text]
        )
        return(result)
    
    
    


    