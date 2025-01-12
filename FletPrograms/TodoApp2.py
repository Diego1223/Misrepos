#Hacer que si la tarea es true se borre y si es false se quede ahi 
import flet as ft


def main(page: ft.Page):
    page.title = "App Bar"
    def agregarTarea(e):
        valorTarea = ft.Checkbox(label=nuevaTarea.value)
        page.add(valorTarea)
        valorTarea.value = ""
        page.update()

    #AppBar
    appBar = ft.Row(
        controls = [
        ft.Text("Navegacion principal"),
        ft.Container(
            width=975, 
        ),
        ft.Row(controls= [
            ft.IconButton(icon=ft.icons.ADD),
            ft.IconButton(icon=ft.icons.SETTINGS),
            ft.IconButton(icon=ft.icons.INFO)
        ], alignment=ft.MainAxisAlignment.END)
    ], alignment= ft.MainAxisAlignment.START)

    #Creacion de tareas (Main Application)
    #Focused border color funciona cuandop la persona oprime el campo de texto
    nuevaTarea = ft.TextField(label="Que necesitas hacer hoy?", focused_border_color='blue')

    page.add(appBar, nuevaTarea, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=agregarTarea))
ft.app(target=main)