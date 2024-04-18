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

        # Saut de ligne
        line_break = HTMLToolBox.generate_line_break()

        # Titre du projet
        project_name = 'Création d’Analytics de Trading Personnalisés via API'
        title = HTMLToolBox.generate_title(project_name)

        # Descriptif du projet
        project_description = """API qui permet à l'utilisateur de créer et de recevoir des analytics de trading personnalisés. 
                            Cet API fournit une large gamme d'indicateurs d'analyse technique appliqués aux marchés de crypto-actifs.
                            Les utilisateurs peuvent également soumettre et appliquer leurs propres fonctions d'analyse Python3 personalisées aux données historiques et à celles en temps réel. """
        description = HTMLToolBox.generate_paragraph(project_description)

        # Sélection de la fonction
        function_title = HTMLToolBox.generate_input_selection("Sélection de la fonction à utiliser :")
        fnc = HTMLToolBox.generate_str_input_box("fnc","")
    
        # Sélection des paramètres de marché
        parameter_title = HTMLToolBox.generate_input_selection("Sélection des paramètres de marché :")

        # Liste des tickers de crypto-actifs (USDT quote-asset)
        ticker_input_box = HTMLToolBox.generate_tick_input_box("tickers","Ticker des crypto-actifs (USDT quote-asset) :")

        # Type de données à récupérer
        data_type = ["Open","High", "Low", "Close", "Volume"]
        dropdown_data_type = "<label for='type' style='font-family: Helvetica, sans-serif; font-weight: bold; display: block;'>Type de données à récupérer : </label>"
        dropdown_data_type += HTMLToolBox.generate_dropdown_menu("datatype", data_type, True)

        # Boite de saisie des dates
        date1_input_box = HTMLToolBox.generate_date_input_box("startDate", "Date de début :")
        date2_input_box = HTMLToolBox.generate_date_input_box("endDate", "Date de fin :")

        # Fréquence
        freq_input_box = HTMLToolBox.generate_str_input_box("freq","Fréquence entre les points de données (ex. 1s, 1min, 1h, 1d, 1w, 1m or 1y) :")

        # Bouton pour lancer le code
        button_code = """
        <div style="display: flex; justify-content: center;">
            <button id="BtnAPI2" style="background-color: lightgreen; padding: 10px 20px; font-size: 16px;">Importation des paramètres :</button>
        </div>
        <div id="result"></div>
        """
        
        # Récupération des données entrées par l'utilisateur
        script = """
        <script>
            document.getElementById("BtnAPI2").addEventListener("click", function() {
                var startDate = document.getElementById("startDate").value;
                var endDate = document.getElementById("endDate").value;
                var freq = document.getElementById("freq").value;
                var dataType = Array.from(document.getElementById("datatype").selectedOptions).map(option => option.value);
                var tick = document.getElementById("tickers").value;
                var fnc = document.getElementById("fnc").value;

                var xhr = new XMLHttpRequest();
                xhr.open("POST", "/run_code_api2", true);
                xhr.setRequestHeader('Content-Type', 'application/json');
                xhr.onload = function () {
                    if (xhr.status === 200) {
                        document.getElementById("result").innerHTML = xhr.responseText;
                    }
                };
                xhr.send(JSON.stringify({startDate: startDate, endDate: endDate, dataType:dataType, freq: freq, tickers:tick}));
            });
        </script>
        """
        
        # Génération de la page HTML
        return title + description + \
            function_title + fnc + parameter_title + \
            ticker_input_box + dropdown_data_type + \
            date1_input_box + date2_input_box + freq_input_box + \
            line_break + button_code + script + line_break + line_break
    