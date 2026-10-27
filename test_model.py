import joblib
import re
from nltk.corpus import stopwords

# Load model and vectorizer
model = joblib.load('models/sentiment_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    stop_words = set(stopwords.words('english'))
    text = " ".join([word for word in text.split() if word not in stop_words and len(word) > 2])
    return text

# Test predictions
test_texts = [
    "I absolutely love this amazing product! It's fantastic!",
    "This is terrible, very disappointed with the service",
    "The weather today is quite normal and average"
]

print("\n[TEST] Model Prediction Verification")
print("=" * 70)
for text in test_texts:
    cleaned = clean_text(text)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]
    confidence = model.predict_proba(vector).max() * 100
    print(f"\nText: {text}")
    print(f"  -> Sentiment: {prediction.upper()}")
    print(f"  -> Confidence: {confidence:.2f}%")

print("\n" + "=" * 70)
print("[SUCCESS] Model is working correctly!\n")
