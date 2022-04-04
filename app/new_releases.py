import requests


def new_release():
    url = "https://netflix-weekly-top-10.p.rapidapi.com/api/movie"

    headers = {
        "X-RapidAPI-Host": "netflix-weekly-top-10.p.rapidapi.com",
        "X-RapidAPI-Key": "edc00c985cmsh7b06df24941523ep19e99djsnc60dfb97072a"
    }

    response = requests.request("GET", url, headers=headers)
    # print(response.text)
    return response.text
