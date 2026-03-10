import tkinter as tk
import pickle

# Load model and vectorizer
model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

# Function to predict news
def check_news():
    news = text_box.get("1.0", tk.END)
    news_vector = vectorizer.transform([news])
    prediction = model.predict(news_vector)

    if prediction[0] == 1:
        result_label.config(text="Real News", fg="green")
    else:
        result_label.config(text="Fake News", fg="red")

# Create window
window = tk.Tk()
window.title("Fake News Detection")
window.geometry("500x400")

title = tk.Label(window, text="Fake News Detector", font=("Arial", 18))
title.pack(pady=10)

text_box = tk.Text(window, height=10, width=50)
text_box.pack()

check_button = tk.Button(window, text="Check News", command=check_news)
check_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 16))
result_label.pack(pady=10)

window.mainloop()