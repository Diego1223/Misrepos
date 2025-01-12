import flet as ft 

def main(page: ft.Page):
    page.title = "Checadores"
    def checadorEs(e):
        txtEs = "Hola amigo"
        txtEm = "Hello friend"

        if idiomaEs.value == True:
            textoOpcion.value = (
                f"Impresion: {txtEs}"
            )
        else:
            textoOpcion.value = (
                f"Impresion: {txtEm}"
            )
        page.update()
    textoOpcion = ft.Text()
    idiomaEs = ft.Checkbox(label="Espanol", value=False, on_change=checadorEs)
    idiomaEn = ft.Checkbox(label="Ingles", value=False, on_change=checadorEs)


    page.add(idiomaEs, idiomaEn, textoOpcion)
ft.app(main)