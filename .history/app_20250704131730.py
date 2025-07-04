import streamlit as st
import joblib

# Title and description
st.title("🎯 YouTube Comment Sentiment Classifier")
st.write("Enter a YouTube comment and see if it's Positive or Negative.")

# Load model and vectorizer
@st.cache_resource
def load_model():
    model = joblib.load("SVM_Linear_SVC_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_model()

# Text input from user
user_input = st.text_area("✏️ Enter your comment here:")

# Predict button
if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a comment.")
    else:
        # Vectorize and predict
        X = vectorizer.transform([user_input])
        prediction = model.predict(X)[0]
        sentiment = "👍 Positive" if prediction == 1 else "👎 Negative"
        
        st.success(f"Predicted Sentiment: {sentiment}")
