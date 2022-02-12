# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# driver = webdriver.Chrome('./chromedriver')
# driver.get("https://www.pccomponentes.com")
#
# driver.maximize_window()
# driver.implicitly_wait(10)

#### Lancer recherche carte Geforce GTX
# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
#
# s = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)
# driver.maximize_window()
# driver.get('https://www.pccomponentes.com/buscar/?query=GeForce%20GTX&page=1&or-relevance')

# driver.find_element(By.NAME, 'q').send_keys('Yasser Khalil')

# time.sleep(10)

# from bs4 import BeautifulSoup as bs
# import urllib.request
#
# # url = 'https://www.amazon.com/b'
# # url ='https://www.jessops.com/drones'
# url ='https://www.amazon.fr/s?k=GeForce+GTX+1060+6GB&__mk_fr_FR=ÅMÅŽÕÑ&crid=1EK7BLGK37KEQ&sprefix=geforce+gtx+1060+6gb%2Caps%2C168&ref=nb_sb_noss_1'
#
# page = urllib.request.urlopen(url, timeout=5)
#
# soup = bs(page, 'html.parser')

# print(soup)
# from bs4 import BeautifulSoup
# import requests
#
# File = open("out.csv", "a")
# URL = 'https://www.amazon.fr/EVGA-GeForce-1060-Gaming-GDDR5/dp/B01LYN9KK6/ref=sr_1_1?__mk_fr_FR=ÅMÅŽÕÑ&keywords' \
#       '=GeForce+GTX+1060+6GB&qid=1644177043&sr=8-1 '
#
# HEADERS = ({'User-Agent':
#                 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 '
#                 'Safari/537.36 '
#                 'OPR/83.0.4254.27',
#             'Accept-Language': 'en-US, en;q=0.5'})
#
# webpage = requests.get(URL, headers=HEADERS)
# soup = BeautifulSoup(webpage.content, "lxml")
#
# # print(soup)
#
# try:
#     title = soup.find("span", attrs={"id": 'productTitle'})
#     title_value = title.string
#     title_string = title_value.strip().replace(',', '')
#
# except AttributeError:
#     title_string = "NA"
#     print("product Title = ", title_string)

# File.write(f"{title_string},")
#
# File.write(f"{available},\n")
#
# # closing the file
# File.close()

# if __name__ == '__main__':
#     # opening our url file to access URLs
#     file = open("url.txt", "r")
#
#     # iterating over the urls
#     for links in file.readlines():
#         main(links)


# importing libraries
from bs4 import BeautifulSoup
import requests


def main(URL):
    # opening our output file in append mode
    File = open("out.csv", "a")

    # specifying user agent, You can use other user agents
    # available on the internet

    HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 '
                    'Safari/537.36 '
                    'OPR/83.0.4254.27',
                'Accept-Language': 'en-US, en;q=0.5'})

    # Making the HTTP Request
    webpage = requests.get(URL, headers=HEADERS)

    # Creating the Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "lxml")

    # retrieving product title
    try:
        # Outer Tag Object
        title = soup.find("span",
                          attrs={"id": 'productTitle'})

        # Inner NavigableString Object
        title_value = title.string

        # Title as a string value
        title_string = title_value.strip().replace(',', '')

    except AttributeError:
        title_string = "NA"
    print("product Title = ", title_string)

    # saving the title in the file
    File.write(f"{title_string},")

    # retrieving price
    try:
        price = soup.find("span", attrs={'class': 'a-offscreen'}).string.strip().replace(',', '.')
        # price = soup.find("span", attrs={'class': 'a-size-base a-color-price'}).string.strip().replace(',', '.')
        # price = soup.find("span", attrs={'id': 'priceblock_ourprice'}).string.strip().replace(',', '')

    except AttributeError:
        price = "NA"
    print("Products price = ", price)

    # saving
    File.write(f"{price},")

    # retrieving product rating
    try:
        rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip().replace(',', '')

    except AttributeError:

        try:
            rating = soup.find(
                "span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
        except:
            rating = "NA"
    print("Overall rating = ", rating)

    File.write(f"{rating},")

    try:
        review_count = soup.find(
            "span", attrs={'id': 'acrCustomerReviewText'}).string.strip().replace(',', '')

    except AttributeError:
        review_count = "NA"
    print("Total reviews = ", review_count)
    File.write(f"{review_count},")

    # print availablility status
    try:
        available = soup.find("div", attrs={'id': 'availability'})
        available = available.find("span").string.strip().replace(',', '')

    except AttributeError:
        available = "NA"
    print("Availability = ", available)

    # saving the availability and closing the line
    File.write(f"{available},\n")

    # closing the file
    File.close()


if __name__ == '__main__':
    # opening our url file to access URLs
    file = open("url.txt", "r")

    # iterating over the urls
    for links in file.readlines():
        main(links)
