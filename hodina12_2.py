from bs4 import BeautifulSoup

html_doc = """
<div class="mainpage-headline">
<a href="/wiki/Wikipedie:%C4%8Cl%C3%A1nek_t%C3%BDdne" title="Wikipedie:Článek týdne">Článek týdne</a>
</div>
"""

rozdelene_html = BeautifulSoup(html_doc, features="html.parser")
print(
    # jméno tagu
    rozdelene_html.div.name,  
    # text v tagu
    rozdelene_html.div.text,  
    # dostupné atributy
    rozdelene_html.div.attrs, 
    sep="\n"
)

rozdelene_html = BeautifulSoup(html_doc, features="html.parser")
print(rozdelene_html.a["title"])