from bs4 import BeautifulSoup
import requests


def handler(event, context):
    res = requests.get("https://wwfmarket.com/collections/basic-koleksiyonu")
    html_doc = res.text
    soup = BeautifulSoup(html_doc, "html.parser")
    product_card = soup.find_all("div", attrs={"class": "product-item"})
    products = {
        elem.find("p", attrs={"class": "product-item-title"}).text.replace("\n", ""): {
            e.text: not "color:silver !important;" in e.attrs.get("style", "")
            for e in elem.find_all("span", attrs={"class": "flex-container"})
        }
        for elem in product_card
    }
    desired_products = [
       "Basic Erkek T-Shirt - Siyah",
       "Basic Erkek T-Shirt - Açık Gri",
    ]
    notifications = [
        p for p in desired_products
        if products.get(p) and products.get(p).get("M")
    ]
    return notifications
