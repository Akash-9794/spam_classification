
import streamlit as st
import joblib
import re
import nltk
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

model = joblib.load('models/spam_model.pkl')
tfidf = joblib.load('models/spam_vectorizer.pkl')

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", '', text)
    text = ' '.join([w for w in text.split() if w not in stop_words])
    return text

st.set_page_config(page_title="SMS Spam Classifier", page_icon="📱")
st.title("📱 SMS Spam Classifier")
st.write("Enter any SMS message to check if it is spam or not.")

user_input = st.text_area("✉️ Enter SMS message here:")

if st.button("Check Message"):
    if user_input.strip() == "":
        st.warning("Please enter a message!")
    else:
        cleaned = clean_text(user_input)
        vector = tfidf.transform([cleaned])
        result = model.predict(vector)[0]
        prob = model.predict_proba(vector)[0]
        confidence = round(max(prob) * 100, 2)
        
        if result == 1:
            st.error(f"🚨 SPAM DETECTED — Confidence: {confidence}%")
        else:
            st.success(f"✅ LEGITIMATE MESSAGE — Confidence: {confidence}%")
