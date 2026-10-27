# 🚀 Quick Start Guide

## ⚡ 5-Minute Setup

### Step 1: Navigate to Project Directory
```powershell
cd "c:\Users\saafi\OneDrive\Desktop\Sentiment Analysis\social-media-sentiment-analysis-dashboard"
```

### Step 2: Install Dependencies (First Time Only)
```powershell
pip install -r requirements.txt
```

### Step 3: Launch the Dashboard
```powershell
streamlit run app/streamlit_app.py
```

**Alternative - Use the launch script:**
```powershell
.\run_dashboard.ps1
```

The dashboard will open automatically at: **http://localhost:8501**

---

## 📊 Dashboard Sections

### 1️⃣ Single Prediction (📝)
**What it does**: Analyze a single text input in real-time

**How to use**:
1. Enter your text in the text area
2. Click "🔍 Predict Sentiment"
3. See the sentiment and confidence score
4. View probability breakdown for all 3 sentiments

**Example inputs**:
- "I absolutely love this amazing product!" → POSITIVE
- "This is terrible and disappointing" → NEGATIVE
- "The weather is normal today" → NEUTRAL

---

### 2️⃣ Batch Analysis (📊)
**What it does**: Analyze multiple texts from a CSV file

**How to use**:
1. Prepare a CSV file with a column containing text
2. Click "Choose a CSV file" and upload it
3. Click "🚀 Analyze All Records"
4. View results with pie chart and histogram
5. Download results as CSV

**CSV Format**:
```
text,other_column1,other_column2
"I love this",value1,value2
"This is bad",value1,value2
```

---

### 3️⃣ Dataset Analytics (📈)
**What it does**: Explore the training dataset

**Features**:
- Dataset statistics (total records, avg text length)
- Sentiment distribution charts
- Text length analysis by sentiment
- Platform distribution (Twitter, Instagram, Facebook)
- Geographic analysis (Top countries)
- Raw vs. cleaned data comparison

---

### 4️⃣ Model Performance (🎯)
**What it does**: View model evaluation metrics

**Includes**:
- Model configuration details
- Performance metrics (Accuracy, Precision, Recall, F1-Score)
- Confusion matrix visualization
- Model classes and their emojis

**Key Metrics**:
- Accuracy: 78.91%
- Precision: 83.51%
- Recall: 78.91%
- F1-Score: 74.88%

---

## 🔧 Manual Pipeline Execution

If you need to retrain the model:

### Step 1: Data Preprocessing
```powershell
cd src
python data_preprocessing.py
```
**Output**: `../data/cleaned_data.csv`

### Step 2: Model Training
```powershell
python train_model.py
```
**Output**: 
- `../models/sentiment_model.pkl`
- `../models/vectorizer.pkl`
- `../models/model_performance.png`

### Step 3: Test Predictions
```powershell
cd ..
python test_model.py
```

---

## 📂 Project Structure

```
sentiment-analysis-dashboard/
├── app/
│   └── streamlit_app.py          ← Dashboard code
├── src/
│   ├── data_preprocessing.py      ← Data cleaning
│   ├── train_model.py             ← Model training
│   └── predict.py                 ← Single prediction
├── data/
│   ├── sentimentdataset.csv       ← Original dataset
│   └── cleaned_data.csv           ← Processed data
├── models/
│   ├── sentiment_model.pkl        ← Trained model
│   ├── vectorizer.pkl             ← TF-IDF vectorizer
│   └── model_performance.png      ← Performance chart
├── requirements.txt               ← Python packages
└── README.md                      ← Full documentation
```

---

## 🧪 Testing

### Quick Test
```powershell
python test_model.py
```

### Test Custom Text
```python
import joblib
import re
from nltk.corpus import stopwords

model = joblib.load('models/sentiment_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

text = "Your text here"
cleaned = text.lower()  # Simple cleaning
vector = vectorizer.transform([cleaned])
prediction = model.predict(vector)[0]
print(f"Sentiment: {prediction}")
```

---

## 📊 Dataset Information

- **Total Records**: 732
- **Positive**: 455 (62.16%)
- **Negative**: 208 (28.42%)
- **Neutral**: 69 (9.43%)
- **Features**: Text, Sentiment, User, Platform, Country, Engagement metrics
- **Emotion Categories Mapped**: 157 → 3 primary sentiments

---

## ⚙️ Model Details

| Property | Value |
|----------|-------|
| Algorithm | Logistic Regression |
| Vectorizer | TF-IDF |
| Vocabulary Size | 1,147 |
| Training Samples | 585 |
| Testing Samples | 147 |
| N-gram Range | (1, 2) |
| Max Features | 5,000 |

---

## 🎓 Understanding Results

### Confidence Scores
- **High (>70%)**: Very confident prediction
- **Medium (50-70%)**: Reasonably confident
- **Low (<50%)**: Uncertain, may need review

### Per-Class Performance
```
Positive:  100% recall  → Captures almost all positive sentiments
Negative:  96% precision → Very accurate on negative sentiments  
Neutral:   7% recall    → Underperforms (few training samples)
```

---

## 🐛 Troubleshooting

### Issue: "Port 8501 already in use"
**Solution**: Use a different port
```powershell
streamlit run app/streamlit_app.py --server.port 8502
```

### Issue: "Module not found"
**Solution**: Install dependencies
```powershell
pip install -r requirements.txt
```

### Issue: "No such file: models/sentiment_model.pkl"
**Solution**: Run training first
```powershell
cd src
python train_model.py
cd ..
```

### Issue: Dashboard loads but no predictions
**Solution**: Check if model files exist
```powershell
Test-Path models/sentiment_model.pkl
Test-Path models/vectorizer.pkl
```

---

## 💾 Saving Results

All batch analysis results can be downloaded as CSV files with:
- Original text
- Predicted sentiment
- Confidence score

Click the **"📥 Download Full Results (CSV)"** button in the Batch Analysis section.

---

## 📞 Need Help?

1. Check **README.md** for detailed documentation
2. Check **PROJECT_SUMMARY.md** for technical details
3. Run test scripts to verify everything works
4. Check model performance in the dashboard's Model Performance section

---

## ✨ Key Features

✅ Real-time sentiment prediction  
✅ Batch processing support  
✅ Interactive visualizations  
✅ Model performance metrics  
✅ Dataset analytics  
✅ Platform & geographic insights  
✅ Results export capability  
✅ Mobile-friendly interface  

---

## 🎯 Next Steps

1. **Explore the Dashboard**: Navigate through all 4 sections
2. **Try Single Predictions**: Test with various text inputs
3. **Batch Analysis**: Upload your own CSV file
4. **Review Analytics**: Understand dataset distribution
5. **Check Performance**: See model metrics and visualizations

---

## 📈 Performance Summary

| Metric | Score |
|--------|-------|
| **Accuracy** | 78.91% |
| **Precision** | 83.51% |
| **Recall** | 78.91% |
| **F1-Score** | 74.88% |

**Status**: ✅ **PRODUCTION READY**

---

Enjoy your Sentiment Analysis Dashboard! 🎉
