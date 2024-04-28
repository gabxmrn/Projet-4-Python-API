import sys

sys.path.append("C:/Users/bossd/OneDrive/Dauphine/M2/Python API/Projet-4-Python-API-main/Code/Toolboxs")

from html_toolbox import HTMLToolBox


def construction_API2() -> str:
    API2 = API_2_ContentGenerator()
    return API2.generate_page()


class API_2_ContentGenerator:
    def __init__(self) -> None:
        super().__init__()

    def generate_page(self) -> str:
        # Sections de la page
        websocket_section = self.generate_websocket_section()
        specified_indicators_section = self.generate_specified_indicators_section()
        custom_indicators_section = self.generate_custom_indicators_section()

        # Génération de la page HTML
        return websocket_section + specified_indicators_section + custom_indicators_section

    def generate_websocket_section(self) -> str:
        # Contenu pour la section Websocket
        title = HTMLToolBox.generate_title("Websocket : Données en direct")
        description1 = HTMLToolBox.generate_paragraph(
            "Cette section permet de recevoir des données en temps réel via WebSocket.")

        # Sélection des paramètres de marché
        parameter_title = HTMLToolBox.generate_input_selection("Sélection des paramètres de marché :")

        # Liste des tickers de crypto-actifs (USDT quote-asset)
        ticker_input_box = HTMLToolBox.generate_tick_input_box("tickers",
                                                               "Ticker des crypto-actifs (USDT quote-asset) :")

        description2 = HTMLToolBox.generate_paragraph(
            "Exemple : pour le BTC, veuillez écrire BTCUSDT.")

        # Type de données à récupérer
        data_type = ["Open", "High", "Low", "Close", "Volume"]
        dropdown_data_type = "<label for='type' style='font-family: Helvetica, sans-serif; font-weight: bold; display: block;'>Type de données à récupérer : </label>"
        dropdown_data_type += HTMLToolBox.generate_dropdown_menu("datatype", data_type, True)

        # Boite de saisie des dates
        date1_input_box = HTMLToolBox.generate_date_input_box("startDate", "Date de début :")
        date2_input_box = HTMLToolBox.generate_date_input_box("endDate", "Date de fin :")

        # Fréquence
        freq_input_box = HTMLToolBox.generate_str_input_box("freq",
                                                            "Fréquence entre les points de données (ex. 1s, 1min, 1h, 1d, 1w, 1m ou 1y) :")
        # Boîte de saisie pour la durée de la période
        period_input_box = HTMLToolBox.generate_str_input_box("period", "Durée de la période de calcul :")

        # Boutons pour les analyses techniques via WebSocket
        button_code = """
        <div style="display: flex; justify-content: center; gap: 10px;">
            <button id="BtnSMA" style="background-color: lightblue; padding: 10px 20px; font-size: 16px;">SMA</button>
            <button id="BtnEMA" style="background-color: lightblue; padding: 10px 20px; font-size: 16px;">EMA</button>
            <button id="BtnMACD" style="background-color: lightblue; padding: 10px 20px; font-size: 16px;">MACD</button>
            <button id="BtnRSI" style="background-color: lightblue; padding: 10px 20px; font-size: 16px;">RSI</button>
            <button id="BtnBBands" style="background-color: lightblue; padding: 10px 20px; font-size: 16px;">Bollinger Bands</button>
        </div>
        <div id="result"></div>
        """

        # Script pour gérer les clics des boutons
        script = """
        <script>
        document.getElementById("BtnRSI").addEventListener("click", function() {
    // Fonction pour reformater les dates en format attendu par l'API
    function formatDate(dateStr) {
        const parts = dateStr.split('-'); // suppose que la date est en format JJ-MM-AAAA
        return parts[2] + '-' + parts[1] + '-' + parts[0]; // reformatage en AAAA-MM-JJ
    }

    var tickers = document.getElementById("tickers").value;
    var dataType = Array.from(document.getElementById("datatype").selectedOptions).map(option => option.value)[0]; // suppose que le datatype est un seul élément
    var frequency = document.getElementById("freq").value;
    var startDate = formatDate(document.getElementById("startDate").value);
    var endDate = formatDate(document.getElementById("endDate").value);
    var n = parseInt(document.getElementById("period").value); // assurez-vous que c'est un entier

    var params = {
        tickers: tickers,
        ohlcv: dataType,
        freq: frequency,
        start_date: startDate,
        end_date: endDate,
        n: n
    };

    fetch(`/api/v1/ta/rsi?` + new URLSearchParams(params), {
        method: 'GET'
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        document.getElementById("result").innerHTML = JSON.stringify(data);
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById("result").innerHTML = 'Error: ' + error;
    });
});

        </script>

        """

        return title + description1 + parameter_title + \
            ticker_input_box + description2 + dropdown_data_type + \
            date1_input_box + date2_input_box + freq_input_box + period_input_box + button_code + script

    def generate_specified_indicators_section(self) -> str:
        # Contenu pour la section des indicateurs spécifiés
        title = HTMLToolBox.generate_title("Indicateurs spécifiés : Données historiques")
        description = HTMLToolBox.generate_paragraph(
            "Cette section permet de calculer des indicateurs techniques spécifiés à partir de données historiques.")
        # Ajouter plus de contenu ici si nécessaire

        return title + description

    def generate_custom_indicators_section(self) -> str:
        # Contenu pour la section des indicateurs personnalisés
        title = HTMLToolBox.generate_title("Indicateurs personnalisés : Données historiques")
        description = HTMLToolBox.generate_paragraph(
            "Cette section permet à l'utilisateur de définir et appliquer ses propres fonctions d'analyse sur des données historiques.")
        # Ajouter plus de contenu ici si nécessaire

        return title + description

# Ceci est une simplification, ajoutez les éléments de formulaire, les scripts et autres détails nécessaires.
