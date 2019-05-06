#!/usr/bin/python3

# Imports
from requests_html import HTMLSession
import requests
import ssl

# Bypass SSL error
ssl._create_default_https_context = ssl._create_unverified_context

# Product
cex = "https://uk.webuy.com/product-detail/?id="
productId = "stabmics3i7256gwpa" ## Not in Stock example
#productId = "5026555423045" ## In Stock example
 
# create an HTML Session object
session = HTMLSession()
resp = session.get(cex + productId)
resp.html.render()

# Get Class Details
name = resp.html.find(".productNamecustm",first=True)
name = name.text.split('\n', 1)[0]
stock = resp.html.find(".buyNowButton",first=True)
stock = stock.text

# Print Results
if stock.find("Out Of Stock") == -1:
    print("Success, Item " + name + " is in Stock")
else:
    print("Item " + name + " is not in Stock right now")