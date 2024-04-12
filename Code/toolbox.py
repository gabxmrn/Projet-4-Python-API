class HTMLToolBox:
    def generate_title(title_txt):
        title_style = "font-family: Helvetica, sans-serif; text-align: center; border: 2px solid black; padding: 10px;"
        return f"<h1 style='{title_style}'>{title_txt}</h1>"
    
    def generate_subtitle(subtitle_text):
        subtitle_style = "font-family: Helvetica, sans-serif; text-align: center; font-size: 16px;"
        return f"<h2 style='{subtitle_style}'>{subtitle_text}</h2>"


