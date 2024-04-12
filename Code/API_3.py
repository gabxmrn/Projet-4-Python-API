from flask import Flask
from toolbox import HTMLToolBox

def construction_API3():
    API3 = API_3_ContentGenerator()
    return API3.generate_page()

class API_3_ContentGenerator: 

    def __init__(self):
        super().__init__()

    def generate_page(self):
        project_name = 'API d’Uniformisation pour Échanges de Cryptomonnaies'
        title = HTMLToolBox.generate_title(project_name)
        project_subtitle = "ceci est un sous titre"
        sub_title = HTMLToolBox.generate_subtitle(project_subtitle)
        return title + sub_title