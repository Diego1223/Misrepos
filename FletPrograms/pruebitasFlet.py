#Tiene las dimensiones de una aplicacion de celular
import flet as ft
import random

class Programa(ft.Container):
    def generar_tareas(self):
        self.tareas = ["hacer la compra", "Llamar al medico", "Estudiar para el examen", "Hacer ejercicio",
                  "Leer un libro", "Preparar la cena", "Estudiar C++"]
        #Random .choice escoge al azar las tareas y con el for le damos que van a ser 5 tareas que escogera al azar
        #COn .salmple es lo mismo pero aqui no se repiten las tareas
        return list(random.sample(self.tareas, 5))
    
    def actualizar_tarea(self):
        #con esta funcion limpiamos la lista
        self.lista_tareas.controls.clear()
        #Aqui estamos volviendo a agregar las tareas que se retornan en la funcion generar tarea
        for self.tarea in self.generar_tareas():
            self.lista_tareas.controls.append(ft.Text(self.tarea, color=ft.colors.WHITE))

    def __init__(self, page):
        super().__init__()
        self.page = page
        self.page.title = "Reservacion"
        self.page.bgcolor = ft.colors.BLUE_GREY_800
        self.page.window_width = 400       
        self.titulo = ft.Row(controls=[
            ft.Text("Ejemplo de tabs", size=24, color=ft.colors.WHITE)
        ], alignment=ft.MainAxisAlignment.CENTER)

        self.actualizar_tarea()
        self.botonActualizar = ft.ElevatedButton("Actualizar tarea", on_click=lambda _: self.actualizar_tarea())
        self.contenido_tareas = ft.Column([self.lista_tareas, self.botonActualizar])


        self.tabs = ft.Tabs(
            #Significa que se inicia en la primer pestana (1 es en la segunda y asi)
            selected_index=0,
            animation_duration=300, #300 milisegundos (lo que dura la animacion en lo que cambiamos de pestanas)
            tabs=[
                ft.Tab(text="Tareas", icon=ft.icons.LIST_ALT, content=self.contenido_tareas),
                ft.Tab(text="Perfil", icon=ft.icons.PERSON),
                ft.Tab(text="Configuracion",icon=ft.icons.SETTINGS)
            ],
            #El contenedor debe ajustarse a todo el ancho de su contenedor padre que es la pagina 
            expand=1 
        )
        #spacing es el espaciado hacia abajo
        #padding va a ser el espaciado de los lados
        self.lista_tareas = ft.ListVIew(
            spacing= 10,
            padding=20,
            
        )

        self.page.add(self.titulo, self.tabs)



    
ft.app(target=Programa)