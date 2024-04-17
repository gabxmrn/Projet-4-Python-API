class HTMLToolBox:

    def generate_title(title_txt):
        title_style = "font-family: Helvetica, sans-serif; text-align: center; border: 2px solid black; padding: 10px;"
        return f"<h1 style='{title_style}'>{title_txt}</h1>"
    
    def generate_subtitle(subtitle_text):
        subtitle_style = "font-family: Helvetica, sans-serif; text-align: center; font-size: 16px;"
        return f"<h2 style='{subtitle_style}'>{subtitle_text}</h2>"

    def generate_paragraph(paragraph_text):
        paragraph_style = "font-family: Helvetica, sans-serif; text-align: left; font-size: 14px; margin-bottom: 10px;"
        return f"<p style='{paragraph_style}'>{paragraph_text}</p>"
    
    def generate_line_break():
        return "<br>"
    
    def generate_input_selection(text):
        text_style = "font-family: Helvetica, sans-serif; text-align: left; font-size: 14px; text-decoration: underline;"
        return f"<h3 style='{text_style}'>{text}</h3>"
    
    def generate_dropdown_menu(options, multiple):
        dropdown_html = "<select"
        
        if multiple:
            dropdown_html += " multiple"
        
        dropdown_html += " style='padding: 10px; border: 1px solid #ccc; border-radius: 4px; background-color: #fff; color: #333; font-size: 16px; font-family: Helvetica, sans-serif;'>"
        
        for option in options:
            dropdown_html += f"<option style='background-color: #fff; color: #333;'>{option}</option>"
        
        dropdown_html += "</select>"
        
        return dropdown_html
    
    @staticmethod
    def generate_date_input_box(id, title):
        input_box_style = "padding: 5px; border: 1px solid #ccc; border-radius: 4px; font-size: 14px; font-family: Helvetica, sans-serif; margin-bottom: 10px;"
        title_style = "font-family: Helvetica, sans-serif; text-align: left; font-size: 14px; font-weight: bold; margin-bottom: 5px;"
        date_input = f"<div><p style='{title_style}'>{title}</p><input type='date' id='{id}' style='{input_box_style}' name='{title}'></div>"
        return date_input
    
    def generate_str_input_box(id, title):
        input_box_style = "padding: 5px; border: 1px solid #ccc; border-radius: 4px; font-size: 14px; font-family: Helvetica, sans-serif; margin-bottom: 10px;"
        title_style = "font-family: Helvetica, sans-serif; text-align: left; font-size: 14px; font-weight: bold; margin-bottom: 5px;"
        str_input_box = f"<div><p style='{title_style}'>{title}</p><input type='text' id='{id}' style='{input_box_style}' name='{title}'></div>"
        return str_input_box

