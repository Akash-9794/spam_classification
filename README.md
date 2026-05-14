# 📱 SMS Spam Classifier

A machine learning web app that detects whether an SMS message is spam or legitimate — built and deployed end-to-end.

🔗 **Live App:** [spamclassificationak.streamlit.app](https://spamclassificationak.streamlit.app)

---

## 🤔 What Does It Do?

You paste any SMS message, click a button, and it tells you:

- 🚨 **SPAM DETECTED** — with a confidence score
- ✅ **LEGITIMATE MESSAGE** — with a confidence score

---

## 🛠️ What I Used

| Tool | Why I Used It |
|------|--------------|
| Python 3.11+ | Main programming language |
| Pandas | Data loading and cleaning |
| NLTK | Stopword removal and text preprocessing |
| Scikit-learn | TF-IDF vectorization + Naive Bayes model |
| Joblib | Saving and loading trained model |
| Streamlit | Building and deploying the web app |
| GitHub | Code versioning and hosting |

---

## 🧠 How It Works

1. Loaded 5,572 real SMS messages (ham + spam) from UCI dataset
2. Kept only useful columns — renamed to `label` and `message`
3. Converted labels — ham = 0, spam = 1
4. Text preprocessing — lowercase, punctuation removal, stopword removal
5. TF-IDF vectorization (max 3000 features)
6. Trained Naive Bayes (MultinomialNB) model
7. Saved model and vectorizer using Joblib
8. Built Streamlit app for live predictions

---

## 📊 Results

| Metric | Score |
|--------|-------|
| Accuracy | **97.48%** |
| Precision | **1.00** |
| Recall | **0.81** |
| F1 Score | **0.90** |
| Total Samples | 5,572 |
| Ham (Legitimate) | 4,825 |
| Spam | 747 |

---

## 🔍 Interesting Observations

- **Precision = 1.0** — Every message flagged as spam was actually spam. Zero false positives.
- **Recall = 0.81** — 19% of actual spam was missed. This is due to class imbalance (747 spam vs 4825 ham).
- **Class Imbalance** — Dataset had significantly more ham than spam, which affected recall.

---

## 🌋 Problems I Faced

### 1. Class Imbalance
**Problem:** 4825 ham vs only 747 spam — model was biased toward ham.  
**Observation:** Recall suffered (0.81) because model missed some spam messages.  
**Learning:** Class imbalance is a real-world problem — can be fixed with oversampling (SMOTE) in future.

### 2. Model File Not Found on Streamlit Cloud
**Problem:** `models/` folder was not uploaded correctly to GitHub — app crashed on deploy.  
**Fix:** Re-uploaded files maintaining proper `models/` folder structure on GitHub.  
**Learning:** Always verify folder structure before deploying.

---

## 📁 Project Structure
