class HTMLToolBox:
    """
    Classe contenant des méthodes statiques pour générer les éléments d'une page HTML.
    """

    @staticmethod
    def generate_title(title_txt: str) -> str:
        """
        Génère un titre HTML (texte en gras et centré).

        Args:
            title_txt (str): Texte du titre.

        Returns:
            str: Balise HTML représentant le titre.
        """
        title_style = "font-family: Helvetica, sans-serif; text-align: center; border: 2px solid black; padding: 10px; font-weight: bold;"
        return f"<h1 style='{title_style}'>{title_txt}</h1>"

    @staticmethod
    def generate_subtitle(subtitle_text: str) -> str:
        """
        Génère un sous-titre HTML (texte centré).

        Args:
            subtitle_text (str): Texte du sous-titre.

        Returns:
            str: Balise HTML représentant le sous-titre.
        """
        subtitle_style = "font-family: Helvetica, sans-serif; text-align: center; font-size: 16px;"
        return f"<h2 style='{subtitle_style}'>{subtitle_text}</h2>"

    @staticmethod
    def generate_paragraph(paragraph_text: str) -> str:
        """
        Génère un paragraphe HTML (texte aligné à gauche).

        Args:
            paragraph_text (str): Texte du paragraphe.

        Returns:
            str: Balise HTML représentant le paragraphe.
        """
        paragraph_style = "font-family: Helvetica, sans-serif; text-align: left; font-size: 14px; margin-bottom: 10px;"
        return f"<p style='{paragraph_style}'>{paragraph_text}</p>"
    
    @staticmethod
    def generate_line_break() -> str:
        """
        Génère une balise HTML de saut de ligne.

        Returns:
            str: Balise HTML représentant un saut de ligne.
        """
        return "<br>"
    
    @staticmethod
    def generate_input_selection(text: str) -> str:
        """
        Génère une sélection d'entrée HTML (texte souligné, aligné à gauche).

        Args:
            text (str): Texte de la sélection.

        Returns:
            str: Balise HTML représentant la sélection.
        """
        text_style = "font-family: Helvetica, sans-serif; text-align: left; font-size: 14px; text-decoration: underline;"
        return f"<h3 style='{text_style}'>{text}</h3>"
    
    @staticmethod
    def generate_dropdown_menu(id: str, options: str, multiple: bool) -> str:
        """
        Génère un menu déroulant HTML.

        Args:
            id (str): ID du menu déroulant.
            options (list): Liste des options du menu.
            multiple (bool): Indique si le menu doit permettre la sélection multiple.

        Returns:
            str: Balise HTML représentant le menu déroulant.
        """
        dropdown_html = f"<select id='{id}'"
        
        if multiple:
            dropdown_html += " multiple"
        
        dropdown_html += " style='padding: 10px; border: 1px solid #ccc; border-radius: 4px; background-color: #fff; color: #333; font-size: 16px; font-family: Helvetica, sans-serif;'>"
        
        for option in options:
            dropdown_html += f"<option style='background-color: #fff; color: #333;'>{option}</option>"
        
        dropdown_html += "</select>"
        
        return dropdown_html
    
    
    @staticmethod
    def generate_date_input_box(id: str, title: str):
        """
        Génère une boîte de saisie de date HTML.

        Args:
            id (str): ID de la boîte de saisie de date.
            title (str): Titre de la boîte de saisie de date.

        Returns:
            str: Balise HTML représentant la boîte de saisie de date.
        """
        input_box_style = "padding: 5px; border: 1px solid #ccc; border-radius: 4px; font-size: 14px; font-family: Helvetica, sans-serif; margin-bottom: 10px;"
        title_style = "font-family: Helvetica, sans-serif; text-align: left; font-size: 14px; font-weight: bold; margin-bottom: 5px;"
        date_input = f"<div><p style='{title_style}'>{title}</p><input type='date' id='{id}' style='{input_box_style}' name='{title}'></div>"
        return date_input
    
    @staticmethod
    def generate_str_input_box(id: str, title: str):
        """
        Génère une boîte de saisie de texte HTML.

        Args:
            id (str): ID de la boîte de saisie de texte.
            title (str): Titre de la boîte de saisie de texte.

        Returns:
            str: Balise HTML représentant la boîte de saisie de texte.
        """
        input_box_style = "padding: 5px; border: 1px solid #ccc; border-radius: 4px; font-size: 14px; font-family: Helvetica, sans-serif; margin-bottom: 10px;"
        title_style = "font-family: Helvetica, sans-serif; text-align: left; font-size: 14px; font-weight: bold; margin-bottom: 5px;"
        str_input_box = f"<div><p style='{title_style}'>{title}</p><input type='text' id='{id}' style='{input_box_style}' name='{title}'></div>"
        return str_input_box
    
    @staticmethod
    def generate_tick_input_box(id: str, title: str):
        """
        Génère une boîte de saisie de ticker HTML.

        Args:
            id (str): ID de la boîte de saisie de ticker.
            title (str): Titre de la boîte de saisie de ticker.

        Returns:
            str: Balise HTML représentant la boîte de saisie de ticker.
        """
        input_box_style = "padding: 5px; border: 1px solid #ccc; border-radius: 4px; font-size: 14px; font-family: Helvetica, sans-serif; margin-bottom: 10px;"
        title_style = "font-family: Helvetica, sans-serif; text-align: left; font-size: 14px; font-weight: bold; margin-bottom: 5px;"
        str_input_box = f"<div><p style='{title_style}'>{title}</p><input type='text' id='{id}' style='{input_box_style}' name='{title}'></div>"

        script = """
        <script>
            document.getElementById('%s').addEventListener('keydown', function(event) {
                if (event.keyCode === 32) {
                    event.preventDefault();
                    var input = document.getElementById('%s');
                    var value = input.value.trim();
                    if (value !== '') { input.value = value + '/'; }
                }
            });
        </script>
        """ % (id, id)

        return str_input_box + script

