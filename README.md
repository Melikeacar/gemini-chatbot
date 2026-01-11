# Gemini Chatbot 🤖  
_Basit Bir Chatbot ile Google Gemini API’yi Öğren_

Gemini Chatbot, **Google Gemini API** kullanarak geliştirilmiş **terminal tabanlı** bir yapay zekâ sohbet uygulamasıdır.  
Bu proje, **Gemini API kullanımını öğrenmek**, API anahtarı yönetimini kavramak ve Python ile temel bir chatbot mantığını anlamak amacıyla geliştirilmiştir.

Sistem, kullanıcıdan aldığı metni Gemini modeline gönderir ve gerçek zamanlı olarak **AI destekli yanıtlar** üretir.

---

## 🧩 Teknik Mimari

Gemini Chatbot’un mimarisi aşağıdaki bileşenlerden oluşur:

| Bileşen               | Teknoloji / Dil            | Sorumluluklar                                                     |
|-----------------------|----------------------------|------------------------------------------------------------------|
| **Chatbot Uygulaması**| Python                     | Kullanıcıdan girdi alma, sohbet döngüsü                          |
| **AI Model Katmanı**  | Google Gemini API          | Metin üretimi ve yanıt oluşturma                                 |
| **Model Seçimi**      | gemini-2.0-flash           | Hızlı ve verimli metin üretimi                                   |
| **Ortam Yönetimi**    | python-dotenv              | API anahtarının güvenli şekilde yüklenmesi                       |
| **Bağımlılık Yönetimi** | requirements.txt         | Proje bağımlılıklarının tanımlanması                             |

---

## ✨ Özellikler

### 💬 Terminal Tabanlı Sohbet
- Kullanıcıdan anlık girdi alma  
- Sürekli sohbet (while loop)  
- `exit` komutu ile güvenli çıkış  

### 🤖 Gemini API Entegrasyonu
- Google Gemini API ile doğrudan iletişim  
- **gemini-2.0-flash** modeli kullanımı  
- Gerçek zamanlı AI yanıt üretimi  

### 🔐 Güvenli API Anahtarı Yönetimi
- `.env` dosyası ile gizli anahtar kullanımı  
- API key’in kod içinde tutulmaması  
- GitHub için `.gitignore` yapılandırması  

---

## ⚙️ Kurulum

### 1. Depoyu Klonla

    git clone https://github.com/Melikeacar/gemini-chatbot.git
    cd gemini-chatbot

---

### 2. Sanal Ortam Oluştur

    python -m venv venv
    .\venv\Scripts\activate   # Windows
    source venv/bin/activate # macOS / Linux

---

### 3. Bağımlılıkları Kur

    pip install -r requirements.txt

---

### 4. Ortam Değişkenlerini Ayarla

Proje kök dizininde `.env` dosyası oluştur ve içine aşağıdaki satırı ekle:

    GEMINI_API_KEY=your_api_key_here

---

### 5. Chatbot’u Çalıştır

    python main.py

Terminalde şu mesaj görüntülenir:

    Melike'nin Chatbot'a hoş geldiniz! (Çıkmak için 'exit' yazın)

---

## 🧠 Çalışma Süreci

1. **Kullanıcı**, terminal üzerinden metin girdisi sağlar  
2. **Python uygulaması**, kullanıcı girdisini Gemini API’ye gönderir  
3. **Gemini (gemini-2.0-flash)** modeli girdiyi işler  
4. **AI**, anlamlı bir metin yanıtı üretir  
5. **Chatbot**, yanıtı terminal ekranında gösterir  
6. Süreç, kullanıcı `exit` yazana kadar devam eder  

---

## 📦 Kullanılan Teknolojiler

### Core / Backend
- Python  
- Google Gemini API  
- google-generativeai  

### Ortam & Yapılandırma
- python-dotenv  
- Virtual Environment (venv)  

### Model
- gemini-2.0-flash  
