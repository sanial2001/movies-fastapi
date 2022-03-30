import streamlit
import requests
import json


def run():
    streamlit.title("Movie prediction list")
    if streamlit.button("Netflix top10 weekly"):
        resp = requests.get("http://127.0.0.1:8000/get_movies")
        top10 = resp.text
        streamlit.success(top10)

    movie = streamlit.text_input("Enter the movie you have watched")
    data = {
        "movie": movie
    }
    if streamlit.button("Predict"):
        resp = requests.post("http://127.0.0.1:8000/predict_movies", json=data)
        prediction = resp.text
        streamlit.success(f"Movies recommended are : {prediction}")


if __name__ == "__main__":
    run()
