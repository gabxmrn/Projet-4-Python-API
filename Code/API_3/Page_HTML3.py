from flask import Flask
from Toolboxs.html_toolbox import HTMLToolBox

def construction_API3():
    API3 = API_3_ContentGenerator()
    return API3.generate_page()
    
class API_3_ContentGenerator:
    def generate_page(self):
        def __init__(self):
            super().__init__()

    def generate_page(self):
        project_name = 'API d\'Uniformisation pour Échanges de Cryptomonnaies'
        title = HTMLToolBox.generate_title(project_name)
        project_subtitle = "Standardisez et uniformisez l'accès aux différentes plateformes d'échange."
        sub_title = HTMLToolBox.generate_subtitle(project_subtitle)

        form = """
        <form id="apiForm" action="" method="post">
            <h3>Visualisation des Données de Marché</h3>
            <label for="api_url">URL de l'API:</label><br>
            <input type="text" id="api_url" name="api_url" placeholder="Entrez l'URL de l'API"><br>
            <label for="api_key">Clé de l'API:</label><br>
            <input type="text" id="api_key" name="api_key" placeholder="Entrez votre clé d'API"><br>
            <label for="market_data_pair">Paire de Marché:</label><br>
            <input type="text" id="market_data_pair" name="market_data_pair" placeholder="Par exemple: BTC-USD"><br>
            <label for="action">Action:</label><br>
            <input type="text" id="action" name="action" placeholder="Par exemple: Get Price"><br>

            <h3>Passer un Ordre de Trade sur Binance</h3>
            <label for="trade_pair">Paire de Trade:</label><br>
            <input type="text" id="trade_pair" name="trade_pair" placeholder="Par exemple: BTC-USD"><br>
            <label for="trade_type">Type d'Ordre:</label><br>
            <select id="trade_type" name="trade_type">
                <option value="buy">Achat</option>
                <option value="sell">Vente</option>
            </select><br>
            <label for="quantity">Quantité:</label><br>
            <input type="text" id="quantity" name="quantity" placeholder="Quantité à trader"><br>
            <label for="price">Prix:</label><br>
            <input type="text" id="price" name="price" placeholder="Prix à laquelle trader"><br>
            
            <input type="submit" value="Envoyer">
        </form>
        """
        return title + sub_title + form
