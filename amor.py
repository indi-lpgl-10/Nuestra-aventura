import flet as ft
from datetime import datetime
import os

def main(page: ft.Page):
    # --- CONFIGURACIÓN GENERAL ---
    page.title = "Nuestro 1er Año"
    page.bgcolor = "#FFF0F5"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0 
    
    # --- TUS DATOS ---
    FECHA_ANIVERSARIO = datetime(2025, 2, 14) 
    NOMBRE_PAREJA = "Mi Amor"

    # --- MÚSICA DE FONDO 🎵 ---
    try:
        musica = ft.Audio(
            src="cancion.mp3", 
            autoplay=True,     
            volume=1.0,        
            balance=0,         
        )
        page.overlay.append(musica)
    except Exception:
        print("No se pudo cargar la música")

    # --- NAVEGACIÓN ---
    def cambiar_pantalla(nueva_pantalla):
        page.clean()
        page.add(nueva_pantalla)
        page.update()

    # ==========================================
    # 1. ESTADÍSTICAS
    # ==========================================
    def ver_estadisticas(e):
        ahora = datetime.now()
        diferencia = ahora - FECHA_ANIVERSARIO
        dias_juntos = diferencia.days
        
        pantalla = ft.Column(
            controls=[
                ft.Container(height=20),
                ft.Text("Nuestras Estadísticas 📈", size=25, weight="bold", color="#D63384"),
                ft.Divider(),
                ft.Container(
                    content=ft.Column([
                        ft.Icon("timer", size=40, color="white"),
                        ft.Text(f"{dias_juntos} Días", size=40, weight="bold", color="white"),
                        ft.Text("compartiendo risas", size=15, color="white")
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    # CAMBIO: ft.Alignment(0, 0) en lugar del atajo .center
                    padding=20, bgcolor="#D63384", border_radius=15, alignment=ft.Alignment(0, 0)
                ),
                ft.Container(height=10),
                ft.Text("Y contando... ❤️", size=18, italic=True),
                ft.Container(height=20),
                ft.ElevatedButton("Volver al Menú", on_click=lambda _: cambiar_pantalla(menu_principal))
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
        # CAMBIO: ft.Alignment(0, 0)
        vista = ft.Container(content=pantalla, alignment=ft.Alignment(0, 0), expand=True)
        cambiar_pantalla(vista)

    # ==========================================
    # 2. HISTORIAS
    # ==========================================
    def ver_historias(e):
        pantalla = ft.Column(
            controls=[
                ft.Container(height=20),
                ft.Text("Nuestras Historias 📸", size=25, weight="bold", color="#D63384"),
                
                ft.Container(
                    content=ft.Column([
                        ft.Text("Nuestro primer viaje", size=18, weight="bold"),
                        ft.Icon("airplane_ticket", size=50, color="blue"), 
                        ft.Text("¿Recuerdas cuando nos perdimos en aquel pueblo?", size=14)
                    ]),
                    padding=15, bgcolor="white", border_radius=10
                ),
                
                ft.Container(
                    content=ft.Column([
                        ft.Text("Esa cena especial", size=18, weight="bold"),
                        ft.Icon("restaurant", size=50, color="orange"), 
                        ft.Text("La mejor pizza del mundo.", size=14)
                    ]),
                    padding=15, bgcolor="white", border_radius=10
                ),

                ft.ElevatedButton("Volver al Menú", on_click=lambda _: cambiar_pantalla(menu_principal))
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO,
            height=700
        )
        cambiar_pantalla(pantalla)

    # ==========================================
    # 3. CARTAS
    # ==========================================
    def ver_cartas(e):
        pantalla = ft.Column(
            controls=[
                ft.Container(height=20),
                ft.Text("Cartas para ti 💌", size=25, weight="bold", color="#D63384"),
                ft.Container(
                    content=ft.Text(
                        "Querido/a ...\n\n"
                        "Te escribo esto porque este año ha sido increíble...",
                        size=16
                    ),
                    padding=20, bgcolor="white", border_radius=10
                ),
                ft.ElevatedButton("Volver al Menú", on_click=lambda _: cambiar_pantalla(menu_principal))
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO,
            height=700
        )
        cambiar_pantalla(pantalla)

    # ==========================================
    # MENÚ PRINCIPAL
    # ==========================================
    menu_principal = ft.Column(
        controls=[
            ft.Text(f"Hola, {NOMBRE_PAREJA} ❤️", size=25, weight="bold", color="#D63384"),
            ft.Text("Elige una sorpresa:", size=16),
            ft.Container(height=10),
            ft.ElevatedButton("📸 Nuestras Historias", on_click=ver_historias, bgcolor="#FF69B4", color="white", width=250, height=50),
            ft.ElevatedButton("📈 Tiempo Juntos", on_click=ver_estadisticas, bgcolor="#FF1493", color="white", width=250, height=50),
            ft.ElevatedButton("💌 Cartas de Amor", on_click=ver_cartas, bgcolor="#C71585", color="white", width=250, height=50),
            ft.Container(height=20),
            ft.OutlinedButton("Volver a la Portada", on_click=lambda _: cambiar_pantalla(portada_container))
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
    )

    # ==========================================
    # PANTALLA INICIAL
    # ==========================================
    def ir_a_menu_desde_portada(e):
        cambiar_pantalla(menu_principal)

    portada = ft.Column(
        controls=[
            ft.Text("Bienvenida", size=35, weight="bold", color="#D63384"),

            ft.Stack(
                controls=[
                    ft.Icon("favorite_border", size=140, color="red"),
                    ft.Container(
                        content=ft.Text("I²", size=50, weight="bold", color="#D63384"),
                        width=140, height=140,
                        # CAMBIO: ft.Alignment(0, 0)
                        alignment=ft.Alignment(0, 0),
                        padding=ft.padding.only(bottom=10)
                    )
                ],
            ),

            ft.Text("a nuestra historia", size=25, weight="bold", color="black"),
            ft.Container(height=20),
            ft.ElevatedButton("Empezar ❤️", on_click=ir_a_menu_desde_portada, bgcolor="#D63384", color="white")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )
    
    portada_container = ft.Container(
        content=portada,
        # CAMBIO: ft.Alignment(0, 0)
        alignment=ft.Alignment(0, 0),
        expand=True
    )

    page.add(portada_container)

# --- INICIO PARA RENDER ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    # CAMBIO: Usamos ft.AppView.WEB_BROWSER que es lo correcto ahora
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=port, host="0.0.0.0", assets_dir="assets")
