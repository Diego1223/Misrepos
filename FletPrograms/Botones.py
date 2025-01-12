import flet as ft

def main(page: ft.Page):
    texto = ft.Text('Primer aplicacion con flet')
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def cambiar(e):
        texto.value  = "Suscribete"
        page.update()

    boton = ft.FilledButton(text='Cambiar texto', on_click=cambiar)

    page.add(texto, boton)
ft.app(target=main)
