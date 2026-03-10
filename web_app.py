import streamlit as st
import pickle

model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

st.title("Fake News Detection System")

news = st.text_area("Enter News Text")

if st.button("Check News"):

    news_vector = vectorizer.transform([news])
    prediction = model.predict(news_vector)

    if prediction[0] == 1:
        st.success("Real News")
    else:
        st.error("Fake News")