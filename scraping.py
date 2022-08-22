from bs4 import BeautifulSoup
import requests
import json

url = "http://45.65.200.38/publicaciones"
page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")

dates_tags = soup.find_all("h1")
authors_tags = soup.find_all("td", scope="row")
title_tags = soup.find_all("a", rel="noopener")
url_tags = title_tags

# Removing unnecessary H1 element of the list
dates_tags.pop(0)

publication_dic = []
list_title = []
list_authors = []
list_url = []
list_dates = []

for title in title_tags[:-2]:
    list_title.append(title.text)
    list_url.append(title["href"])

for authors in authors_tags:
    list_authors.append(authors.text)

for date in dates_tags:
    list_dates.append(date.text)

# Reversing the order of the lists.
list_title = list_title[::-1]
list_url = list_url[::-1]
list_authors = list_authors[::-1]
list_dates = list_dates[::-1]

# Checking if the length of the list of titles is equal to the length of the list of authors.
def add_dictionary_space():
    if len(title_tags[:-2]) == len(authors_tags):
        for i in range(len(authors_tags)):
            publication_dic.append({})


def add_information():
    dates = {
        list_dates[0]: [0, 2],
        list_dates[1]: [3, 4],
        list_dates[2]: [5, 8],
        list_dates[3]: [9, 9],
        list_dates[4]: [10, 16],
        list_dates[5]: [17, 20],
        list_dates[6]: [21, 21],
        list_dates[7]: [22, 30],
        list_dates[8]: [31, 45],
        list_dates[9]: [46, 55],
        list_dates[10]: [56, 59],
    }

    # Adding the values of the lists to the dictionary.
    for i in range(len(publication_dic)):
        publication_dic[i]["id"] = i
        publication_dic[i]["title"] = list_title[i]
        publication_dic[i]["authors"] = list_authors[i]
        publication_dic[i]["url"] = list_url[i]
        publication_dic[i]["date"] = ""

        for j in range(len(dates)):
            if dates[list_dates[j]][0] <= i and i <= dates[list_dates[j]][1]:
                publication_dic[i]["date"] = list_dates[j]


def write_json():
    publication_txt = open("publications.json", "w", encoding="utf-8")
    publications = str(json.dumps(publication_dic, ensure_ascii=False, indent=4))
    publication_txt.write(publications)


add_dictionary_space()
add_information()
write_json()
