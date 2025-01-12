import flet as ft

def main(page: ft.Page):
    #REcibe un evento y luego muestra la variable 
    def Impresion(e):
        print(f"La impresion que se mostro fue: {nombre.value}")
        txtIm = ft.Text(value=f"Tu nombre es: {nombre.value}")
        page.add(
            ft.Row([
                txtIm 
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ))
    #Text field es el campo de entrada
    nombre = ft.TextField(label="Escribe tu nombre", focused_border_color="green")
    impresion = ft.ElevatedButton(text="Imprimir tu nombre", on_click=Impresion) 

    page.add(
        nombre, impresion 
    )
ft.app(target=main)