import flet as ft 

def main(page: ft.Page):
    txt_name = ft.TextField(label="Your name")
    page.add(txt_name, ft.ElevatedButton("Say hello", on_click=btnClick))

    def btnClick(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(ft.Text(f"Hello, {name}"))
        txt_name = ft

ft.app(main)