import flet as ft

class Program(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.dropdown  = ft.Dropdown(
            label="Color",
            options=[
                ft.dropdown.Option("Uno"),
                ft.dropdown.Option("DOs")
            ]
        )
        self.boton = ft.ElevatedButton("Enviar", on_click=self.Valor)
        self.page.add(self.dropdown,self.boton)

    def Valor(self, e):
        print(self.dropdown.value)
ft.app(target=Program)