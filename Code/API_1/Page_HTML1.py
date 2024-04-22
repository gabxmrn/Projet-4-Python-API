from flask import Flask
from Toolboxs.html_toolbox import HTMLToolBox

def construction_API1():
    """
    Fonction qui génère le contenu de la page API1.

    Returns:
        str: Le contenu HTML de la page API1.
    """
    
    API1 = API_1_ContentGenerator()
    return API1.generate_page()

class API_1_ContentGenerator: 

    def __init__(self) -> None:
        """
        Initialise une nouvelle instance de la classe API_1_ContentGenerator.
        """
        super().__init__()

    def generate_page(self):
        """
        Génére le contenu de l'API1 sur une page HTML

        Returns:
            str : contenu de la page HTML
        """

        # Mise en place du titre
        line_break = HTMLToolBox.generate_line_break()
        project_name = 'API pour Backtesting de Stratégies de Trading Algorithmique'
        title = HTMLToolBox.generate_title(project_name)

        # Descriptif du projet
        project_description = """Cette API permet aux utilisateurs de soumettre leurs propres stratégies de trading algorithmique pour backtesting. 
        Le système doit être capable d’exécuter ces stratégies sur des données de marché historiques et de fournir des analyses de performance sur la période spécifiée.
        """
        description = HTMLToolBox.generate_paragraph(project_description)
        
        # Nom de la requête
        rqt_input_box = HTMLToolBox.generate_str_input_box("rqt","Nom de votre requête pour l'identification :")

        # Sélection de la fonction de trading
        function_title = HTMLToolBox.generate_input_selection("Sélection de la fonction de trading à utiliser (renvoie les poids) :")
        remarque = HTMLToolBox.generate_paragraph("Pour tester le code, veuillez entrer : fnc1, fnc2 ou fnc3.")
        fnc = HTMLToolBox.generate_str_input_box("fnc","")

        # Tickers à sélectionner pour la stratégie à backtester
        data_ticker = ["AAPL", "MSFT", "AMZN", "NVDA", "GOOGL", "TSLA", "META", "GOOG", "BRK.B", "UNH"]
        dropdown_data_type = "<label for='type' style='font-family: Helvetica, sans-serif; font-weight: bold; display: block;'>Sélection des tickers : </label>"
        dropdown_data_type += HTMLToolBox.generate_dropdown_menu("dataticker", data_ticker, True)

        # Boite de saisie des dates de calibrage
        date1_input_box_cal = HTMLToolBox.generate_date_input_box("startDateCal", "Date de début de calibrage :")
        date2_input_box_cal = HTMLToolBox.generate_date_input_box("endDateCal", "Date de fin de calibrage :")

        # Boite de saisie des dates de test
        date1_input_box_test = HTMLToolBox.generate_date_input_box("startDateTest", "Date de début de test :")
        date2_input_box_test = HTMLToolBox.generate_date_input_box("endDateTest", "Date de fin de test :")

        # Fréquences des observations considérées 
        freq_input_box = HTMLToolBox.generate_str_input_box("freq","Fréquence des observations (ex. 1s, 1min, 1h, 1d, 1w, 1m ou 1y) :")
        
        # Montant initial
        amt_input_box = HTMLToolBox.generate_str_input_box("amt","Montant initial du portefeuille :")
    
        # Bouton pour lancer le code
        button_code = """
        <div style="display: flex; justify-content: center;">
            <button id="BtnAPI1" style="background-color: lightgreen; padding: 10px 20px; font-size: 16px;">Importation des paramètres :</button>
        </div>
        <div id="result"></div>
        """
        
        # Récupération des données entrées par l'utilisateur
        script = """
        <script>
            document.getElementById("BtnAPI1").addEventListener("click", function() {
                var startDateCal = document.getElementById("startDateCal").value;
                var endDateCal = document.getElementById("endDateCal").value;
                var startDateTest = document.getElementById("startDateTest").value;
                var endDateTest = document.getElementById("endDateTest").value;
                var freq = document.getElementById("freq").value;
                var dataTicker = Array.from(document.getElementById("dataticker").selectedOptions).map(option => option.value);
                var amt = document.getElementById("amt").value;
                var rqt = document.getElementById("rqt").value;
                var fnc = document.getElementById("fnc").value;

                var xhr = new XMLHttpRequest();
                xhr.open("POST", "/run_code_api2", true);
                xhr.setRequestHeader('Content-Type', 'application/json');
                xhr.onload = function () {
                    if (xhr.status === 200) {
                        document.getElementById("result").innerHTML = xhr.responseText;
                    }
                };
                xhr.send(JSON.stringify({fnc:fnc, startDateCal: startDateCal, endDateCal: endDateCal, startDateTest: startDateTest, endDateTest: endDateTest, dataticker:dataTicker, freq: freq, amt: amt}));
            });
        </script>
        """

        return line_break + title + description + rqt_input_box + function_title + remarque + fnc + dropdown_data_type + \
            date1_input_box_cal + date2_input_box_cal + date1_input_box_test + date2_input_box_test + \
            freq_input_box + amt_input_box + button_code + script