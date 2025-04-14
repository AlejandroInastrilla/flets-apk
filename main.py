# main.py
import flet as ft

def main(page: ft.Page):
    page.title = "Mi app con Flet"
    page.add(ft.Text("¡Hola desde Flet en Android!"))

ft.app(target=main)
