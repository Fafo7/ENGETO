from requests import get
from bs4 import BeautifulSoup
adresa = "https://www.pivovarclock.cz"
odpoved = get(adresa)

"""
* odpoved.text - objekt typu "str",
* feature - argument, který upřesní typ rozdělovače.
"""
rozdelene_html = BeautifulSoup(odpoved.text, features="html.parser")

print(rozdelene_html)

