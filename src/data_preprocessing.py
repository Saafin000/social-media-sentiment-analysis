import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
import numpy as np

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def clean_text(text):
    """Clean and preprocess text data"""
    if not isinstance(text, str):
        return ""
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove special characters and digits, keep only letters and spaces
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Remove stopwords
    text = " ".join([
        word for word in text.split()
        if word not in stop_words and len(word) > 2
    ])
    
    return text

def normalize_sentiment(sentiment):
    """Normalize all emotion labels to Positive, Negative, or Neutral"""
    if not isinstance(sentiment, str):
        return 'neutral'
    
    sentiment = sentiment.strip().lower()
    
    # POSITIVE EMOTIONS
    positive_emotions = {
        'positive', 'joy', 'happiness', 'happy', 'love', 'amusement', 'enjoyment', 
        'admiration', 'affection', 'awe', 'surprise', 'adoration', 'anticipation',
        'contentment', 'calmness', 'kind', 'kindness', 'pride', 'proud', 'excitement',
        'excitement', 'gratitude', 'grateful', 'hope', 'hopeful', 'inspiration', 'inspired',
        'accomplishment', 'elation', 'euphoria', 'confidence', 'confident', 'determination',
        'empowerment', 'empathetic', 'enthusiasm', 'creativity', 'creative inspiration',
        'acceptance', 'amazement', 'adrenaline', 'adventure', 'approval', 'appreciation',
        'arousal', 'blessed', 'breakthrough', 'celebration', 'charm', 'compassion',
        'compassionate', 'connection', 'coziness', 'culinary adventure', 'culinaryodyssey',
        'elegance', 'elation', 'enchantment', 'engagement', 'freedom', 'friendship',
        'fulfillment', 'grandeur', 'harmony', 'heartwarming', 'hope', 'iconic', 'imagination',
        'inspiration', 'inspired', 'joy in baking', 'joyfulreunion', 'playful', 'playfuljoy',
        'positivity', 'radiance', 'rejuvenation', 'resilience', 'reverence', 'romance',
        'satisfaction', 'serenity', 'solace', 'success', 'tenderness', 'thrill', 
        'thrilling journey', 'touched', 'tranquility', 'triumph', 'vibrancy', 'whimsy',
        'wonder', 'wonderment', 'zest', 'free-spirited', 'optimism', 'overjoyed',
        'engaged', 'energy', 'happiness', 'mindfulness', 'motivation', 'renewal',
        'renewed effort', 'celestial wonder', 'creative inspiration', 'dreamchaser',
        'envisioning history', 'festive joy', 'inner journey', 'nature beauty',
        'ocean freedom', 'runway creativity', 'winter magic', 'whispers of the past',
        'artistic burst', 'iconic', 'mellodic', 'mesmerizing', 'hypnotic', 'captivation',
        'contemplation', 'reflection', 'colorful', 'enchantment', 'colorful'
    }
    
    # NEGATIVE EMOTIONS
    negative_emotions = {
        'negative', 'anger', 'angry', 'fear', 'fearful', 'sadness', 'sad', 'disgust',
        'disappointed', 'disappointment', 'bitter', 'bitterness', 'confusion', 'shame',
        'despair', 'desperation', 'devastated', 'grief', 'heartache', 'heartbreak',
        'helplessness', 'jealous', 'jealousy', 'loneliness', 'loss', 'lostlove',
        'melancholy', 'numbness', 'regret', 'resentment', 'sorrow', 'suffering',
        'envy', 'envious', 'embarrassed', 'frustrated', 'frustration', 'anxiety',
        'anxious', 'apprehensive', 'hatred', 'hate', 'intimidation', 'isolation',
        'desolation', 'dismissive', 'bad', 'boredom', 'overwhelmed', 'pressure',
        'miscalculation', 'obstacle', 'nostalgia', 'pensive', 'yearning', 'betrayal',
        'emotional storm', 'exhaustion', 'emotionalstorm', 'darkness', 'dazzle',
        'ruins', 'dread', 'hazard', 'peril', 'wariness'
    }
    
    # NEUTRAL EMOTIONS
    neutral_emotions = {
        'neutral', 'ambivalence', 'indifference', 'curiosity', 'contemplation',
        'exploration', 'challenge', 'emotion', 'ambivalent', 'mischievous', 'engagement',
        'wonder', 'intrigue', 'immersion', 'solitude', 'sympathy', 'charming',
        'bittersweet', 'relaxation', 'connection', 'relaxing'
    }
    
    # Check if sentiment belongs to any category
    if sentiment in positive_emotions:
        return 'positive'
    elif sentiment in negative_emotions:
        return 'negative'
    elif sentiment in neutral_emotions:
        return 'neutral'
    
    # Default mapping based on keywords
    if any(word in sentiment for word in ['positive', 'joy', 'happy', 'love', 'good', 'great', 'excellent', 'amazing', 'wonderful', 'nice', 'beautiful', 'excellent', 'awesome']):
        return 'positive'
    elif any(word in sentiment for word in ['negative', 'sad', 'angry', 'hate', 'bad', 'terrible', 'awful', 'horrible', 'poor', 'fear', 'scared', 'angry', 'frustrated']):
        return 'negative'
    else:
        return 'neutral'

# Load the sentiment dataset
print("Loading dataset...")
df = pd.read_csv('../data/sentimentdataset.csv')

print(f"Original dataset shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")

# Use 'Text' and 'Sentiment' columns (case-sensitive as per dataset)
if 'Text' in df.columns and 'Sentiment' in df.columns:
    # Create a clean dataframe with required columns
    df_clean = pd.DataFrame()
    df_clean['text'] = df['Text'].apply(clean_text)
    df_clean['sentiment'] = df['Sentiment'].apply(normalize_sentiment)
    
    # Remove empty texts
    df_clean = df_clean[df_clean['text'].str.len() > 0]
    
    print(f"\nAfter preprocessing: {df_clean.shape}")
    print(f"\nSentiment distribution:")
    sentiment_counts = df_clean['sentiment'].value_counts()
    print(sentiment_counts)
    print(f"\nSentiment percentages:")
    print((sentiment_counts / len(df_clean) * 100).round(2))
    
    # Save cleaned data
    df_clean.to_csv('../data/cleaned_data.csv', index=False)
    
    print("\n[SUCCESS] Preprocessing Completed Successfully!")
    print(f"\nTotal samples: {len(df_clean)}")
    print(f"  - Positive: {(df_clean['sentiment'] == 'positive').sum()}")
    print(f"  - Negative: {(df_clean['sentiment'] == 'negative').sum()}")
    print(f"  - Neutral:  {(df_clean['sentiment'] == 'neutral').sum()}")
    
    print("\nSample cleaned data:")
    print(df_clean.head(20))
    print(f"\nCleaned data saved to: ../data/cleaned_data.csv")
else:
    print("Error: Expected 'Text' and 'Sentiment' columns not found!")
    print(f"Available columns: {df.columns.tolist()}")