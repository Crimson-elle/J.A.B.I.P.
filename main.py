import customtkinter
import json
import os


def load_theme(path: str):
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


theme = load_theme(os.path.join(os.path.dirname(__file__), "theme.json"))
colors = theme.get("color", {})
widget_colors = theme.get("widget", {})

try:
    customtkinter.set_appearance_mode("Dark")
except Exception:
    pass


def button_callback():
    status_var.set("Cargando")
    app.after(2000, lambda: status_var.set("Activo"))


app = customtkinter.CTk()
app.title("J.A.B.I.P.")
app.geometry("400x150")

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(2, weight=1)

btn_colors = widget_colors.get("button", {})
footer_colors = widget_colors.get("footer", {})

button = customtkinter.CTkButton(
    app,
    text="Alertas",
    command=button_callback,
    fg_color=btn_colors.get("fg_color", colors.get("primary", None)),
    hover_color=btn_colors.get("hover_color", None),
    text_color=btn_colors.get("text_color", None),
)
button.grid(row=0, column=0, padx=20, pady=8, sticky="w")
button = customtkinter.CTkButton(
    app,
    text="Ingresar",
    command=button_callback,
    fg_color=btn_colors.get("fg_color", colors.get("primary", None)),
    hover_color=btn_colors.get("hover_color", None),
    text_color=btn_colors.get("text_color", None),
)
button.grid(row=1, column=0, padx=20, pady=8, sticky="w")

status_var = customtkinter.StringVar(value="Activado")
footer = customtkinter.CTkFrame(app, height=24, corner_radius=0, fg_color=footer_colors.get("bg", colors.get("background", None)))
footer.grid(row=3, column=0, columnspan=1, sticky="ew")

status_label = customtkinter.CTkLabel(footer, textvariable=status_var, anchor="w", text_color=footer_colors.get("text", colors.get("foreground", None)))
status_label.pack(side="left", fill="both", padx=8)

guest_label = customtkinter.CTkLabel(footer, text="Ha ingresado como invitado.", anchor="e", text_color=footer_colors.get("muted", colors.get("muted", None)))
guest_label.pack(side="right", padx=8)

app.mainloop()
