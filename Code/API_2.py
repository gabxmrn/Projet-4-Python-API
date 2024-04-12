from flask import Flask
from toolbox import HTMLToolBox

def construction_API2():
    API2 = API_2_ContentGenerator()
    return API2.generate_page()

class API_2_ContentGenerator: 

    def __init__(self):
        super().__init__()
    
    def generate_page(self):
        project_name = 'Création d’Analytics de Trading Personnalisés via API'
        title = HTMLToolBox.generate_title(project_name)
        project_subtitle = "ceci est un sous titre"
        sub_title = HTMLToolBox.generate_subtitle(project_subtitle)
        return title + sub_title