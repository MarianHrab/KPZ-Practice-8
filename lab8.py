import requests
from bs4 import BeautifulSoup


def parse_ukd_data():
    url = 'https://ukd.edu.ua/'
    page = requests.get(url)  # getting GET request from variable URL
    soup = BeautifulSoup(page.content, "html.parser")  # taking page content and parser specifier

    class_with_tags = soup.find("div", class_='col-lg-9 col-md-12')  # finding class with tags of professions
    ul_tag = class_with_tags.find('ul')  # finding tag 'ul'
    prof_names = ul_tag.find_all('li')  # in tag ul find tag 'li' where placed professions names

    prof_list = []
    for element in prof_names:
        speciality_name = element.text.strip()  # taking all string from tag and add to list
        prof_list.append(speciality_name)
    print("List of professions:")
    print()
    for item in prof_list:  # print list of professions
        print(item)

    return prof_list


parse_ukd_data()

