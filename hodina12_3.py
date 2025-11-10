from bs4 import BeautifulSoup

html_doc = """
<div class="center">
<div class="floatnone">
    <a href="https://commons.wikimedia.org/wiki/File:Cadmium-crystal_bar.jpg" class="image" title="Kadmium je měkký stříbřitě bílý kov, používaný zejména k povrchové ochraně kovů a také k 
    výrobě různých slitin a sloučenin">
        <img alt="Kadmium je měkký stříbřitě bílý kov, používaný zejména k povrchové ochraně kovů a 
        také k výrobě různých slitin a sloučenin" decoding="async" data-file-width="5220" data-file-height="3378" width="400" height="259">
    </a>
</div>
</div> 
"""
rozdelene_html = BeautifulSoup(html_doc, features="html.parser")

print(
    rozdelene_html.select_one(
        ".floatnone > a:nth-child(1) > img:nth-child(1)"
    ).attrs["alt"]
)
print(rozdelene_html.select("div"))