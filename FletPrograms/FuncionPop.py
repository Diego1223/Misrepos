import flet as ft
import time
def main(page:ft.Page):
    for i in range(10):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            #Hace una actualizacion desde el rango 0
            #Parece que va subiendo 

            page.controls.pop(0)
        page.update()
        time.sleep(0.3)
        

ft.app(target=main)