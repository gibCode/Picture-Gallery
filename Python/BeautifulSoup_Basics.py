import requests
from bs4 import BeautifulSoup


r = requests.get("http:/mypage.com/1")

r = requests.post("http:/mypage.com", data=dict(
    email="me@mypage.com",
    password="secret_value"
))


##Pass query arguments
r = requests.get("http:/mypage.com/page", params=dict(
    query="Data here",
    page=2
))

###
print r.text
##


##				BeautifulSoup

##====================================================

soup = BeautifulSoup(r.text, "html.parser")


links = soup.find_all("a")


tags = soup.find_all("li", "search-result")


tags = soup.find("div", id="search-results").find_all("a", "external-links")

tags = soup.select("#search-results .external-links")

inner_contents = soup.find("div", id="price").contents

inner_text = soup.find("div", id="price").text.strip()

inner_text = soup.find("div", id="price").text.strip().encode("utf-8")


anchor_href = soup.find("a")["href"]



for product in soup.find_all("div", "products"):
    product_title = product.find("h3").text
    product_price = product.find("span", "price").text
    product_url = product.find("a")["href"]
    print "{} is selling for {} at {}".format(product_title, product_price, product_url)


##

import csv
...
with open("C:/temp/output.csv", "w") as f:
    writer = csv.writer(f)

    # collected_items = [
    #   ["Product #1", "$10", "http://mypage.com/product-1"],
    #   ["Product #2", "$25", "http://mypage.com/product-2"],
    #   ...
    # ]

    for item_property_list in collected_items:
        writer.writerow(item_property_list)

###
import csv
...
field_names = ["Column 1", "Column 2", "Column 3"]
with open("~/Desktop/output.csv", "w") as f:
    writer = csv.DictWriter(f, field_names)

    # collected_items = [
    #   {
    #       "Column 1": "Product #1",
    #       "Column 2": "$10",
    #       "Column 3": "http://mypage.com/product-1"
    #   },
    #   ...
    # ]

    # Write a header row
    writer.writerow({x: x for x in field_names})

    for item_property_dict in collected_items:
        writer.writerow(item_property_dict)




###Sessions and Cookies
# create a session
session = requests.Session()

# make a login POST request, using the session
session.post("http://mypage.com/login", data=dict(
    email="me@mypage.com",
    password="secret_value"
))

# subsequent requests that use the session will automatically handle cookies
r = session.get("http://mypage.com/protected_page")



#Writing to a SQLite Database
import sqlite3

conn = sqlite3.connect("/tmp/output.sqlite")
cur = conn.cursor()
...
for item in collected_items:
    cur.execute("INSERT INTO scraped_data (title, price, url) values (?, ?, ?)",
        (item["title"], item["price"], item["url"])
    )

###



###

