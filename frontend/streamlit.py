import streamlit as st
import requests
import json
import pandas as pd
import base64


@st.cache
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="file.csv">Download CSV File</a>'
    return href


def run():
    st.title("Movie Maniac")

    menu = ["Home", "Netflix weekly top10", "Predict movies to watch", "Find Movies", "Find nearby theatres", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Movie-Series Feeds Section")
        option = st.radio("Select to see the new releases", ["Movies", "Series"])
        if option == "Movies":
            resp = requests.get("http://127.0.0.1:8000/movies_feed")
            json_data = json.loads(resp.text)
            col1, col2 = st.columns((1, 1))
            flag = 1
            for key in json_data:
                if flag == 1:
                    col1.subheader(key)
                    col1.write(f'* **Release Date:** {json_data[key]["release_date"]}')
                    col1.write(f'* **About:** {json_data[key]["about"]}')
                    flag = 2
                else:
                    col2.subheader(key)
                    col2.write(f'* **Release Date:** {json_data[key]["release_date"]}')
                    col2.write(f'* **About:** {json_data[key]["about"]}')
                    flag = 1
        else:
            resp = requests.get("http://127.0.0.1:8000/series_feed")
            json_data = json.loads(resp.text)
            col1, col2 = st.columns((1, 1))
            flag = 1
            for key in json_data:
                if flag == 1:
                    col1.subheader(key)
                    col1.write(f'* **Release Date:** {json_data[key]["release_date"]}')
                    col1.write(f'* **About:** {json_data[key]["about"]}')
                    flag = 2
                else:
                    col2.subheader(key)
                    col2.write(f'* **Release Date:** {json_data[key]["release_date"]}')
                    col2.write(f'* **About:** {json_data[key]["about"]}')
                    flag = 1

    if choice == "Netflix weekly top10":
        st.subheader("Netflix weekly top10")
        resp = requests.get("http://127.0.0.1:8000/get_movies")
        json_data = json.loads(resp.text)
        # print(type(json_data))
        json_data = eval(json_data)
        df = pd.DataFrame(json_data)
        st.dataframe(df)
        st.markdown(filedownload(df), unsafe_allow_html=True)

    if choice == "Predict movies to watch":
        st.subheader("Predict movies to watch")

        df_movies = pd.read_csv("../app/dataset/movies.csv")
        movies_list = list(df_movies['title'])
        movie_selected = st.selectbox("Enter the movie you have watched", movies_list)
        movie_selected = movie_selected.split(" ")
        if movie_selected[-1][0] == "(":
            movie_selected.pop()
        movie_selected = ' '.join(movie_selected)
        data = {
            "movie": movie_selected
        }
        if st.button("Predict"):
            resp = requests.post("http://127.0.0.1:8000/predict_movies", json=data)
            json_data = json.loads(resp.text)
            if not json_data:
                st.write("Oops!!! No movies found")
            else:
                df = pd.DataFrame(json_data.values(), columns=['movies'])
                st.dataframe(df)
                st.markdown(filedownload(df), unsafe_allow_html=True)

    if choice == "Find Movies":
        st.subheader("Finding best Movies by genres")
        resp = requests.get("http://127.0.0.1:8000/get_movies_genres")
        df = pd.read_csv("../app/dataset/movie_ratings.csv")
        json_data = json.loads(resp.text)
        options = st.multiselect("Select genres to watch", json_data)
        df_filtered = df[(df['genres'].isin(options))]
        df2 = df_filtered.drop(['movieId', 'Unnamed: 0'], axis=1)
        df2.sort_values('avg_ratings', ascending=False, inplace=True)
        st.dataframe(df2)
        st.markdown(filedownload(df2), unsafe_allow_html=True)

    if choice == "Find nearby theatres":
        st.subheader("Find nearby theatres")
        address = st.text_input("Enter the locality where you live")
        data = {
            "address": address
        }
        if st.button("Find"):
            resp = requests.post("http://127.0.0.1:8000/get_nearby_theatres", json=data)
            json_data = json.loads(resp.text)
            # print(type(json_data))
            df = pd.DataFrame(json_data, columns=['name', 'rating', 'vicinity'])
            df.sort_values('rating', ascending=False, inplace=True)
            st.dataframe(df)
            st.markdown(filedownload(df), unsafe_allow_html=True)

    if choice == "About":
        st.subheader("About")
        frameworks_expand = st.expander("Frameworks used")
        frameworks_expand.markdown("""
        * **Python libraries:** base64, googlemaps, requests, json, time
        * **Front-end:** streamlit
        * **Back-end:** FastAPI
        * **ML:** collaborative based filtering to predict movies using sklearn, scipy, numpy, pandas 
        * **Web-scraping:** Beautifulsoup4
        """)

        data_source = st.expander("Data Source")
        data_source.markdown("""
        * **Movies and series feeds:** [Movies-Series feeds](https://moviesdaily.com/)
        * **Netflix weekly top 10:** [Rapid API netflix weekly top 10](https://rapidapi.com/mhtdy/api/netflix-weekly-top-10/)
        * **Find nearby theatres:** [Google maps API](https://developers.google.com/maps/documentation/places/web-service/search-nearby)
        """)

        about_me = st.expander("Source code and connectivity")
        about_me.markdown("""
        * **Github:** [Github repo](https://github.com/sanial2001/movies_fastapi)
        * **LinkedIn:** [LinkedIn](https://www.linkedin.com/in/sanial-das-b65594184/)
        """)


if __name__ == "__main__":
    run()
