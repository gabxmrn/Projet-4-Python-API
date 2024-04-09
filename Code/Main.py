from API_Global import Application

# Instancier l'application
app = Application()

# On centre les boutons dans la fenêtre
app.update_idletasks()
largeur_fenetre = app.winfo_width()
for widget in app.winfo_children():
    widget.pack_configure(anchor='n', padx=(largeur_fenetre - widget.winfo_reqwidth()) // 2)

# Lancer l'application
app.mainloop()
