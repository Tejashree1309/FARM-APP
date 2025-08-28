# 🌾 Farming Assistant (English ↔ Malayalam)

This is a **Streamlit web app** that helps farmers ask questions in either **English or Malayalam**.  
It uses **OpenAI GPT model** for answers and **Google Translator** for language translation.

## 🚀 Features
- Ask farming questions in English or Malayalam.
- Automatically translates between the two languages.
- Uses AI (GPT-4o-mini) to provide answers.
- Runs on Streamlit Cloud with a public link.

---

## 🔧 Installation (Run Locally)

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/farming-assistant.git
   cd farming-assistant
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your OpenAI API key to `secrets.toml` (for local testing):
   Create a folder `.streamlit/` and inside it, make a file `secrets.toml`:
   ```toml
   OPENAI_API_KEY = "your_api_key_here"
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## 🌍 Deployment (Streamlit Cloud)

1. Push this repo to **GitHub**.  
2. Go to [Streamlit Cloud](https://share.streamlit.io).  
3. Select your repo → choose `app.py`.  
4. In **Secrets Manager**, add:
   ```
   OPENAI_API_KEY = your_api_key_here
   ```
5. Click **Deploy**. You’ll get a link like:
   ```
   https://your-app-name.streamlit.app
   ```

---

## 📷 Preview
Example interface:  

```
🌾 Farming Assistant (English ↔ Malayalam)

[Ask your farming question: ______________________ ]
[ Get Answer ]

✔ Answer shown in Malayalam / English
```

---

## 👨‍💻 Author
Developed with ❤️ using **Python, Streamlit, OpenAI, and Google Translator**.
