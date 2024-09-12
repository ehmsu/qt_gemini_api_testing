import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.", request_options={'timeout':10})
# raises google.api_core.exceptions.DeadlineExceeded: 504 Deadline Exceeded if timeout exceeded
print(response.text)