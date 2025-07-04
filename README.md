# 🎯 YouTube Video Comment Sentiment Classifier

This project analyzes YouTube video comments and classifies them into **Positive** or **Negative** sentiments using **Natural Language Processing (NLP)** and **Machine Learning**. It also includes a deployed **Streamlit web app** that allows users to test the model in real-time.

---

## 🚀 Project Features

✅ Fetch comments from YouTube videos using **YouTube Data API v3**  
✅ Preprocess and clean text data  
✅ Perform **sentiment analysis** using **VADER** and custom labeling  
✅ Generate **WordClouds** to visualize frequent words  
✅ Train and compare multiple ML models:
- Logistic Regression
- Naive Bayes
- SVM
- Random Forest
✅ Save best model and TF-IDF vectorizer  
✅ Deploy using **Streamlit** for real-time prediction

---

## 📊 Tech Stack

| Tool/Library      | Purpose                         |
|-------------------|----------------------------------|
| `python`          | Programming Language             |
| `streamlit`       | App interface & deployment       |
| `googleapiclient` | Fetching YouTube comments        |
| `nltk`            | VADER Sentiment Analysis         |
| `sklearn`         | ML Models, TF-IDF, Evaluation    |
| `joblib`          | Saving & Loading Models          |
| `matplotlib`/`seaborn` | EDA and Visualization     |
| `wordcloud`       | Visualize frequent words         |

---

## 📁 Folder Structure

yt_video_sentiment-app/
├── app.py # Streamlit Web App
├── tfidf_vectorizer.pkl # Saved TF-IDF vectorizer
├── SVM_Linear_SVC_model.pkl # Best-performing ML model
├── requirements.txt # Python dependencies
└── README.md # Project overview (this file)

---

## ⚙️ Installation & Usage (Local)

### 1️⃣ Clone the Repository
git clone https://github.com/A289shek2004/yt_video_sentiment-app.git

cd yt_video_sentiment-app

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the App Locally
streamlit run app.py
Your app will open at: http://localhost:8501

🌐 Live Demo
🔗 Streamlit App: [Coming soon – add link after deployment]
🔗 Project Walkthrough (YouTube/LinkedIn): 

📈 Example Input/Output
Input Comment:
This video is so helpful, thank you!
Predicted Sentiment:

👍 Positive
💡 Future Improvements
Add Neutral class for 3-way sentiment

Add comment filters (by likes, recency)

Visual sentiment summary for full video

Deploy as a full web API (Flask/FastAPI)

🙋‍♂️ Author
Abhishek Harendra Gupta
📫 LinkedIn
🎓 Data Science Student | Aspiring ML Engineer

📜 License
This project is licensed under the MIT License – feel free to use and modify.

---

## ✅ What You Should Do Next:

1. **Create this file** in your project folder as `README.md`
2. Commit & push:
```bash
git add README.md
git commit -m "Added complete professional README"
git push
