import streamlit as st
from openai import OpenAI
from deep_translator import GoogleTranslator

# 🔑 Paste your NEW OpenAI API key here (keep quotes)
API_KEY_IS ="API_KEY"
client = OpenAI(api_key=API_KEY_IS)


st.title("🌾 Farming Assistant (English ↔ Malayalam)")
st.text(st.secrets['API_KEY'])
user_question = st.text_input("Ask your farming question:")

def safe_translate(text, source_lang, target_lang):
    """Translate with graceful fallback if translator has an issue."""
    try:
        return GoogleTranslator(source=source_lang, target=target_lang).translate(text)
    except Exception as e:
        return None  # caller decides what to do

if st.button("Get Answer"):
    if not user_question:
        st.warning("Please enter a question.")
    else:
        # Detect Malayalam (unicode range)
        is_malayalam = any('\u0d00' <= ch <= '\u0d7f' for ch in user_question)

        # Malayalam → English if needed
        if is_malayalam:
            question_en = safe_translate(user_question, 'ml', 'en') or user_question
        else:
            question_en = user_question

        # Ask OpenAI (English prompt)
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": question_en}]
            )
            answer_en = response.choices[0].message.content
        except Exception as e:
            st.error(f"OpenAI error: {e}")
            st.stop()

        # Show in both languages
        if is_malayalam:
            answer_ml = safe_translate(answer_en, 'en', 'ml')
            if answer_ml:
                st.success(answer_ml)  # Malayalam answer
                st.markdown("---")
                st.info("**English Answer:**\n\n" + answer_en)
            else:
                st.success(answer_en)
                st.caption("Translator unavailable; showing English only.")
        else:
            st.success(answer_en)     # English answer
            answer_ml = safe_translate(answer_en, 'en', 'ml')
            if answer_ml:
                st.markdown("---")
                st.info("**Malayalam Answer:**\n\n" + answer_ml)
            else:
                st.caption("Translator unavailable; Malayalam not shown.")




