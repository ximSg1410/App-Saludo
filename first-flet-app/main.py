import flet as ft 

def main(page: ft.Page ):
    page.title = "App de Saludo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    nombre_input = ft.TextField(label="Escribe tu nobre", widht=300)
    resultado = ft.Text(value="", size=20, color="blue)

    def saludar(e):
        if nombre_input.value.strip():
            resultado.value = f"¡Hola {nombre_input.value}!😊"
        else:
            resultado.value = "Por favor escribe tu nombre."
        page.update()
    
    boton = ft.ElevatedButton("Saludar", on_click=saludar)

    page.add(
        ft.Column(
            [
                ft.Text("Bienvenido a la app de saludo🙈", size=24, weight=ft.FontWeight.BOLD),
                NOMBRE_INPUT,
                boton,
                resultado,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)