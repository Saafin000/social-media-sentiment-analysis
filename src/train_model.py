import pandas as pd
import joblib
import numpy as np
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

print("="*60)
print("SENTIMENT ANALYSIS MODEL TRAINING")
print("="*60)

# Load cleaned data
print("\n1. Loading cleaned data...")
df = pd.read_csv('../data/cleaned_data.csv')

print(f"   Dataset shape: {df.shape}")
print(f"   Sentiment distribution:\n{df['sentiment'].value_counts()}")

# Prepare features and labels
X = df['text']
y = df['sentiment']

print(f"\n2. Splitting data (80/20 train-test split)...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print(f"   Training samples: {len(X_train)}")
print(f"   Testing samples: {len(X_test)}")

# TF-IDF Vectorization
print(f"\n3. Applying TF-IDF Vectorization...")
vectorizer = TfidfVectorizer(
    max_features=5000,
    min_df=2,
    max_df=0.8,
    ngram_range=(1, 2),
    lowercase=True
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

print(f"   Feature matrix shape: {X_train_vec.shape}")
print(f"   Vocabulary size: {len(vectorizer.get_feature_names_out())}")

# Train Logistic Regression Model
print(f"\n4. Training Logistic Regression Model...")
model = LogisticRegression(
    max_iter=1000,
    random_state=42,
    multi_class='multinomial',
    solver='lbfgs'
)

model.fit(X_train_vec, y_train)

# Make predictions
print(f"\n5. Evaluating Model Performance...")
predictions = model.predict(X_test_vec)

# Calculate metrics
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions, average='weighted', zero_division=0)
recall = recall_score(y_test, predictions, average='weighted', zero_division=0)
f1 = f1_score(y_test, predictions, average='weighted', zero_division=0)

print(f"\n   ┌─ Model Performance Metrics ─┐")
print(f"   │ Accuracy:  {accuracy*100:6.2f}%")
print(f"   │ Precision: {precision*100:6.2f}%")
print(f"   │ Recall:    {recall*100:6.2f}%")
print(f"   │ F1-Score:  {f1*100:6.2f}%")
print(f"   └──────────────────────────────┘")

# Detailed classification report
print(f"\n6. Classification Report:")
print(classification_report(y_test, predictions))

# Confusion Matrix
cm = confusion_matrix(y_test, predictions)
print(f"\n7. Confusion Matrix:")
print(cm)

# Save model and vectorizer
print(f"\n8. Saving Model and Vectorizer...")
model_path = Path('../models')
model_path.mkdir(exist_ok=True)

joblib.dump(model, model_path / 'sentiment_model.pkl')
joblib.dump(vectorizer, model_path / 'vectorizer.pkl')

print(f"   ✓ Model saved to: ../models/sentiment_model.pkl")
print(f"   ✓ Vectorizer saved to: ../models/vectorizer.pkl")

# Create visualization
print(f"\n9. Creating performance visualization...")
try:
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Confusion Matrix Heatmap
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=model.classes_, 
                yticklabels=model.classes_,
                ax=axes[0], cbar_kws={'label': 'Count'})
    axes[0].set_title('Confusion Matrix')
    axes[0].set_ylabel('True Label')
    axes[0].set_xlabel('Predicted Label')
    
    # Metrics comparison
    metrics = [accuracy, precision, recall, f1]
    metric_names = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
    colors = ['#2ecc71', '#3498db', '#e74c3c', '#f39c12']
    
    bars = axes[1].bar(metric_names, metrics, color=colors, alpha=0.7, edgecolor='black')
    axes[1].set_ylim([0, 1.0])
    axes[1].set_ylabel('Score')
    axes[1].set_title('Model Performance Metrics')
    axes[1].grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        axes[1].text(bar.get_x() + bar.get_width()/2., height,
                    f'{height*100:.1f}%',
                    ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('../models/model_performance.png', dpi=100, bbox_inches='tight')
    print(f"   ✓ Performance visualization saved to: ../models/model_performance.png")
except Exception as e:
    print(f"   ⚠ Could not save visualization: {e}")

print(f"\n" + "="*60)
print(f"✓ MODEL TRAINING COMPLETED SUCCESSFULLY!")
print(f"="*60)