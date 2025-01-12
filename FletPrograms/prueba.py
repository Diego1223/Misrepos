import flet as ft
import random 


def main(page:ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "Tabs Flet"
    
    titulo = ft.Row(controls=[
        ft.Text("Ejemplo de tabs", size=24, color=ft.colors.WHITE)
    ], alignment=ft.MainAxisAlignment.CENTER)
    
    #Contenido Tareas
    def generar_tareas():
        tareas = ["Hacer la compra", "Llamar al medico", "Estudiar para el examen", "Hacer ejercicio", "Leer un libro", "estudiar C++"]
        return random.sample(tareas, 4)
    
    lista_tareas = ft.ListView(spacing=10, padding=20) 
    
    def actualizar_tareas():
        lista_tareas.controls.clear()
        for tarea in generar_tareas():
            lista_tareas.controls.append(ft.Text(tarea,color=ft.colors.WHITE))
        page.update()

    actualizar_tareas()
    btn_actualizar = ft.ElevatedButton("Actualizar tareas", on_click= lambda _: actualizar_tareas())
    contenido_tareas = ft.Column(controls=[lista_tareas, btn_actualizar])

    #CONTENIDO PERFIL  
    campo_nombre =ft.TextField(hint_text="Nombre", bgcolor=ft.colors.BLUE_GREY_700)
    campo_email = ft.TextField(hint_text="Email", bgcolor=ft.colors.BLUE_GREY_700)
    boton_guardar = ft.ElevatedButton("Guardar perfil")
    contenido_perfil = ft.Column
    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="Tareas", icon=ft.Icons.LIST_ALT, content=contenido_tareas),
            ft.Tab(text="Perfil", icon=ft.Icons.PERSON),
            ft.Tab(text="Configuracion", icon=ft.Icons.SETTINGS)
        ],
        expand=1
    )

    page.add(titulo, tabs)
ft.app(target=main)