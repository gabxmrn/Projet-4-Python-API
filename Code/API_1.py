from flask import Flask
from toolbox import HTMLToolBox

def construction_API1():
    API1 = API_1_ContentGenerator()
    return API1.generate_page()

class API_1_ContentGenerator: 

    def __init__(self):
        super().__init__()

    def generate_page(self):
        project_name = 'API pour Backtesting de Stratégies de Trading Algorithmique'
        title = HTMLToolBox.generate_title(project_name)
        project_subtitle = "ceci est un sous titre"
        sub_title = HTMLToolBox.generate_subtitle(project_subtitle)
        return title + sub_title

    def generate_dropdown_menu(options):
        dropdown_html = "<select>"
        for option in options:
            dropdown_html += f"<option value='{option}'>{option}</option>"
        dropdown_html += "</select>"
        return dropdown_html