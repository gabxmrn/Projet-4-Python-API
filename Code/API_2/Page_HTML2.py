import sys

sys.path.append("C:/Users/bossd/OneDrive/Dauphine/M2/Python API/Projet-4-Python-API-main/Code/Toolboxs")

from Toolboxs.html_toolbox import HTMLToolBox


def construction_API2() -> str:
    """
    Fonction qui génère le contenu de la page API2.

    Returns:
        str: Le contenu HTML de la page API2.
    """
    API2 = API_2_ContentGenerator()
    return API2.generate_page()


class API_2_ContentGenerator:
    """
    Classe pour générer le contenu de la page API2.
    """

    def __init__(self) -> None:
        """
        Initialise une nouvelle instance de la classe API_2_ContentGenerator.
        """
        super().__init__()

    def generate_page(self) -> str:
        """
        Génère le contenu HTML de la page API2.

        Returns:
            str: Le contenu HTML de la page API2.
        """

        # Line break
        lb = HTMLToolBox.generate_line_break()

        # Titre de la page
        title = HTMLToolBox.generate_title('Création d’Analytics de Trading Personnalisés via API')

        # Description de l'API
        project_description = """API qui permet à l'utilisateur de créer et de recevoir des analytics de trading personnalisés. 
                            Cet API fournit une large gamme d'indicateurs d'analyse technique appliqués aux marchés de crypto-actifs.
                            Les utilisateurs peuvent également soumettre et appliquer leurs propres fonctions d'analyse Python3 personalisées aux données historiques et à celles en temps réel. """
        description = HTMLToolBox.generate_paragraph(project_description)

        # Sections de la page
        websocket_section = self.generate_websocket_section()
        indicators_section = self.generate_indicators_section()
        
        # Génération de la page HTML
        return title + description + lb + \
            websocket_section + lb + lb + \
            indicators_section + lb + lb

    def generate_websocket_section(self) -> str:
        """
        Génère le contenu HTML de la première section de la page API2.

        Returns:
            str: Le contenu de la section Websockets de la page API2.
        """

        # Contenu pour la section Websocket
        title = HTMLToolBox.generate_subtitle("Websocket : Données en direct")
        description1 = HTMLToolBox.generate_paragraph(
            "Cette section permet de recevoir des données en temps réel via WebSocket.")

        # Liste des tickers de crypto-actifs (USDT quote-asset)
        ticker_input_box = HTMLToolBox.generate_tick_input_box("tickers",
                                                               "Ticker des crypto-actifs (USDT quote-asset) :")

        description2 = HTMLToolBox.generate_paragraph(
            "Exemple : pour le BTC, veuillez écrire BTCUSDT.")

        # Fréquence
        freq_input_box = HTMLToolBox.generate_str_input_box("f",
                                                            "Fréquence entre les points de données (ex. 1s, 1min, 1h, 1d, 1w, 1m ou 1y) :")
        
        # Boîte de saisie pour la durée de la période
        period_input_box = HTMLToolBox.generate_str_input_box("period", "Durée de la période de calcul :")

        # Indicateur à sélectionner
        indicators = ["SMA","EMA", "MACD", "RSI", "BBands"]
        dropdown_indicators = "<label for='type' style='font-family: Helvetica, sans-serif; font-weight: bold; display: block;'>Indicateur à calculer : </label>"
        dropdown_indicators += HTMLToolBox.generate_dropdown_menu("indic", indicators, False)

        # Boutons pour les analyses techniques via WebSocket
        button_code = """
        <div style="display: flex; justify-content: center;">
            <button id="BtnWebsocket" style="background-color: lightblue; padding: 10px 20px; font-size: 16px;">Données réelles - Calcul de l'indicateur :</button>
        </div>
        <div id="result"></div>
        """

        # Script pour gérer les clics des boutons
        script = """
        <script>
            document.getElementById("BtnWebsocket").addEventListener("click", function() {

            var tickers = document.getElementById("tickers").value;
            var f = document.getElementById("f").value;
            var n = parseInt(document.getElementById("period").value);
            var indic = Array.from(document.getElementById("indic").selectedOptions).map(option => option.value);

            var xhr = new XMLHttpRequest();
            xhr.open("POST", "/run_code_api2", true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onload = function () {
                if (xhr.status === 200) {
                    document.getElementById("result").innerHTML = xhr.responseText;
                }
            };
            xhr.send(JSON.stringify({hist_rt:"rt", fnc: indic, tickers: tickers, freq: f, n:n}));
        });

        </script>
        """

        return title + description1 + \
            ticker_input_box + description2 + \
            freq_input_box + period_input_box + dropdown_indicators + \
            button_code + script

    def generate_indicators_section(self) -> str:
        """
        Génère le contenu HTML de la seconde section de la page API2.

        Returns:
            str: Le contenu de la section Données Historiques de la page API2.
        """

        # Contenu pour la section des indicateurs spécifiés
        title = HTMLToolBox.generate_subtitle("Données historiques - Calcul d'indicateur")

        # Descriptif
        description = "Cette section permet de calculer des indicteurs à l'aide de données historiques."

        # Indicateur existant ou personnalisé
        indic_title = HTMLToolBox.generate_input_selection("Entre l'indicateur à calculer :")
        rq = HTMLToolBox.generate_paragraph("""Les indicteurs implémentés sont : SMA, EMA, MACD, RSI, BBANDS.
                                            Si vous souhaitez calculer un indicateur personnalisé, veuillez entrer le nom de la fonction.
                                            Pour tester une fonction personnalisée, veuillez entrer test. """)
        fnc = HTMLToolBox.generate_str_input_box("fnc","")

        # Paramètres de marchés

        ## Liste des tickers de crypto-actifs (USDT quote-asset)
        ticker_input_box = HTMLToolBox.generate_tick_input_box("tick","Ticker des crypto-actifs (USDT quote-asset) :")

        ## Type de données à récupérer
        data_type = ["Open","High", "Low", "Close", "Volume"]
        dropdown_data_type = "<label for='type' style='font-family: Helvetica, sans-serif; font-weight: bold; display: block;'>Type de données à récupérer : </label>"
        dropdown_data_type += HTMLToolBox.generate_dropdown_menu("datatype", data_type, True)

        ## Boite de saisie des dates
        date1_input_box = HTMLToolBox.generate_date_input_box("startDate", "Date de début :")
        date2_input_box = HTMLToolBox.generate_date_input_box("endDate", "Date de fin :")

        ## Fréquence
        freq_input_box = HTMLToolBox.generate_str_input_box("freq","Fréquence entre les points de données (ex. 1s, 1min, 1h, 1d, 1w, 1m ou 1y) :")

        # Boutons pour les indicateurs
        button_code = """
        <div style="display: flex; justify-content: center;">
            <button id="BtnHisto" style="background-color: lightblue; padding: 10px 20px; font-size: 16px;">Données historiques - Calcul de l'indicateur :</button>
        </div>
        <div id="result"></div>
        """

        # Code du bouton
        script = """
        <script>
        document.getElementById("BtnHisto").addEventListener("click", function() {
                
            var startDate = document.getElementById("startDate").value;
            var endDate = document.getElementById("endDate").value;
            var freq = document.getElementById("freq").value;
            var dataType = Array.from(document.getElementById("datatype").selectedOptions).map(option => option.value);
            var tick = document.getElementById("tick").value;
            var fnc = document.getElementById("fnc").value;
        
            var xhr = new XMLHttpRequest();
            xhr.open("POST", "/run_code_api2", true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.onload = function () {
                if (xhr.status === 200) {
                    document.getElementById("result").innerHTML = xhr.responseText;
                }
            };
            xhr.send(JSON.stringify({hist_rt:"hist", fnc:fnc, startDate: startDate, endDate: endDate, dataType:dataType, freq: freq, tickers:tick}));
        });
        </script>
        """

        return title + description + \
            indic_title + rq + fnc + \
            ticker_input_box + dropdown_data_type + \
            date1_input_box + date2_input_box + freq_input_box + \
            button_code + script
