import pickle

# Load model
model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

print("Fake News Detection System")

news = input("Enter news text: ")

news_vector = vectorizer.transform([news])

prediction = model.predict(news_vector)

if prediction[0] == 1:
    print("Real News")
else:
    print("Fake News")