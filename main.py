import os  #ortam değişkenleri okunur
import google.generativeai as genai  # gemini apı kullanmak için 
from dotenv import load_dotenv # env dosyasını yüklemek için

load_dotenv() #env dosyasını yükler 
api_key = os.getenv("GEMINI_API_KEY") #api_key değişkeninin içinde benim key imi atıyor 

genai.configure(api_key=api_key) #configure: Anahtarı sisteme tanıtır (yetkilendirme).
model = genai.GenerativeModel("gemini-2.0-flash") #  Kullanmak istediğimiz Gemini modelini seçer.

print("Melike'nin Chatbot'a hoş geldiniz! (Çıkmak için 'exit' yazın)\n")

while True:
    prompt = input("Kullanıcı:")
    if prompt.lower() == "exit":
        print("Görüşmek Üzere :)")
        break
    response = model.generate_content(prompt)
    print("Bot:", response.text)    
