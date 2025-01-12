import flet as ft
#Video crear tu propia biblioteca digital con python
class Programa(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.page.title = "Biblioteca Linux"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.titulo = ft.Text("Biblioteca Personal")
        self.iconoTema = ft.IconButton(
            icon=ft.icons.LIGHT_MODE,
            tooltip= "Cambiar tema",
            on_click= self.cambiarTema
        )

        self.appBar = ft.AppBar(
            title=self.titulo,
            center_title=True,
            bgcolor=ft.colors.SURFACE_VARIANT, #Constante de flet que se utiliza para mantener la coherencia visual
            actions=[self.iconoTema]
        )

        self.page.add(self.appBar)
    
    def cambiarTema(self, e):
        self.page.theme_mode = ft.ThemeMode.LIGHT if self.page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        self.iconoTema.icon = ft.icons.DARK_MODE if self.page.theme_mode == ft.ThemeMode.LIGHT else ft.icons.LIGHT_MODE
        self.page.update()
ft.app(target=Programa)