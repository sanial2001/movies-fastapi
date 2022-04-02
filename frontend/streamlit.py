import streamlit as st
import requests
import json


def run():
    st.title("Movie Maniac")

    menu = ["Netflix weekly top10", "Predict movies to watch", "Find nearby theatres"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Netflix weekly top10":
        st.subheader("Netflix weekly top10")
        resp = requests.get("http://127.0.0.1:8000/get_movies")
        top10 = resp.text
        st.success(top10)

    if choice == "Predict movies to watch":
        st.subheader("Predict movies to watch")

        movie = st.text_input("Enter the movie you have watched")
        data = {
            "movie": movie
        }
        if st.button("Predict"):
            resp = requests.post("http://127.0.0.1:8000/predict_movies", json=data)
            prediction = resp.text
            st.success(f"Movies recommended are : {prediction}")

    if choice == "Find nearby theatres":
        st.subheader("Find nearby theatres")
        address = st.text_input("Enter the locality where you live")
        data = {
            "address": address
        }
        if st.button("Find"):
            resp = requests.post("http://127.0.0.1:8000/get_nearby_theatres", json=data)
            st.success(f"Places are : {resp.text}")


if __name__ == "__main__":
    run()
