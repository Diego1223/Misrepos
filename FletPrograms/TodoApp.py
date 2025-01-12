import flet as ft

def main(page:ft.Page):
    def agregar(e):
      page.add(ft.Checkbox(label=nuevaTarea.value))
      nuevaTarea.value = ""
      nuevaTarea.update()

    nuevaTarea = ft.TextField(hint_text="Tareas por hacer", width=300)
    page.add(
        ft.Row( controls= [
            nuevaTarea, ft.ElevatedButton("Agregar", on_click=agregar)
        ])
    )
ft.app(main)