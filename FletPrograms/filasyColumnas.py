import flet as ft

def main(page: ft.Page):
    page.title = "Titulo"
    text = ft.Text(value='Texto1', size=24, color = ft.colors.GREEN)
    text2 = ft.Text(value='Texto2', size=23, color= ft.colors.RED)
    
    #Las filas(ROW), son de izquierda a derecha acostadas
    filaTextos = ft.Row(
        #El controls es como una lista que estamos usando de nuestra fila
        controls=[text, text2],
        #Centra los elementos
        alignment = ft.MainAxisAlignment.CENTER,
        spacing = 50 #Espaciado de 50 pixeles
    )
    
    page.add(filaTextos)
    
    boton1 = ft.FilledButton(text='Boton1')
    boton2 = ft.FilledButton(text='Boton2')
    filadeBotones = ft.Row(
        controls = [boton1, boton2],
        alignment = ft.MainAxisAlignment.CENTER
    )

    #Columnas (de abajo hacia arriba)
    textosColumnas = [
        ft.Text('columna 1 - fila 1', size=18, color=ft.colors.GREEN),
        ft.Text('Columna1 - Fila 2', size=18, color=ft.colors.RED)
    ]
    columnaTextos = ft.Column(
        controls = textosColumnas
    )
    page.add(columnaTextos)



    page.add(filadeBotones)
                
ft.app(target=main)
