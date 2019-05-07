#!/usr/bin/python3

# Imports
from requests_html import HTMLSession
import requests
from subprocess import call

# Products
cex = "https://uk.webuy.com/product-detail/?id="
productId = ["stabmics3i7256gwpa", "stabmics3i7512g1a", "stabmics3i7512g1c"] ## List of ProductIDs 

for product in productId:
    # create an HTML Session object
    session = HTMLSession()
    resp = session.get(cex + product)
    resp.html.render()

    # Get Class Details
    name = resp.html.find(".productNamecustm",first=True)
    name = name.text.split('\n', 1)[0]
    stock = resp.html.find(".buyNowButton",first=True)
    stock = stock.text

    # Print Results
    if stock.find("Out Of Stock") == -1:
        print("Item " +name + " is in stock! Emailing..")
        call(["python", "/working/sendmail.py", name, product])