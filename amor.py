import flet as ftimport flet as ft
from datetime import datetime
import os

def main(page: ft.Page):
    # --- CONFIGURACIÓN DE LA PÁGINA ---
    page.title = "Nuestro Aniversario"
    page.bgcolor = "#FFF0F5" 
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    # Alineación central forzada (esto arregla que se vea gris o vacío)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    
    # --- TUS DATOS ---
    FECHA_ANIVERSARIO = datetime(2025, 2, 14) 
    NOMBRE_PAREJA = "Mi Amor"

    # --- MÚSICA 🎵 ---
    try:
        musica = ft.Audio(src="cancion.mp3", autoplay=True)
        page.overlay.append(musica)
    except:
        pass 

    # --- NAVEGACIÓN ---
    def cambiar_pantalla(contenido_nuevo):
        page.clean()
        # Reforzamos la alineación al cambiar de pantalla
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.add(contenido_nuevo)
        page.update()

    # ==========================================
    # 1. ESTADÍSTICAS
    # ==========================================
    def ver_estadisticas(e):
        ahora = datetime.now()
        diferencia = ahora - FECHA_ANIVERSARIO
        dias_juntos = diferencia.days
        
        contenido = ft.Column(
            [
                ft.Text("Nuestras Estadísticas 📈", size=25, weight="bold", color="#D63384"),
                ft.Container(height=20),
                ft.Container(
                    content=ft.Column([
                        # CORREGIDO: Sin 'name=', directo el string
                        ft.Icon("timer", size=40, color="white"),
                        ft.Text(f"{dias_juntos} Días", size=40, weight="bold", color="white"),
                        ft.Text("juntos", size=15, color="white")
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=30, bgcolor="#D63384", border_radius=20
                ),
                ft.Container(height=20),
                ft.ElevatedButton("Volver", on_click=lambda _: cambiar_pantalla(pantalla_menu))
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
        cambiar_pantalla(contenido)

    # ==========================================
    # 2. HISTORIAS
    # ==========================================
    def ver_historias(e):
        contenido = ft.Column(
            [
                ft.Text("Momentos 📸", size=25, weight="bold", color="#D63384"),
                ft.Container(height=10),
                
                # Historia 1
                ft.Container(
                    content=ft.Column([
                        # CORREGIDO: Sin 'name='
                        ft.Icon("airplane_ticket", size=40, color="blue"),
                        ft.Text("Primer Viaje", weight="bold"),
                        ft.Text("Esa vez que nos perdimos...", size=14)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=15, bgcolor="white", border_radius=10
                ),
                
                # Historia 2
                ft.Container(
                    content=ft.Column([
                        # CORREGIDO: Sin 'name='
                        ft.Icon("restaurant", size=40, color="orange"),
                        ft.Text("Cena Especial", weight="bold"),
                        ft.Text("La mejor pizza.", size=14)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=15, bgcolor="white", border_radius=10
                ),

                ft.Container(height=10),
                ft.ElevatedButton("Volver", on_click=lambda _: cambiar_pantalla(pantalla_menu))
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
        cambiar_pantalla(contenido)

    # ==========================================
    # 3. CARTAS
    # ==========================================
    def ver_cartas(e):
        contenido = ft.Column(
            [
                ft.Text("Para ti 💌", size=25, weight="bold", color="#D63384"),
                ft.Container(
                    content=ft.Text(
                        "Querido/a ...\n\nEres lo mejor que me ha pasado...",
                        text_align=ft.TextAlign.CENTER
                    ),
                    padding=20, bgcolor="white", border_radius=10, width=300
                ),
                ft.Container(height=20),
                ft.ElevatedButton("Volver", on_click=lambda _: cambiar_pantalla(pantalla_menu))
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        cambiar_pantalla(contenido)

    # ==========================================
    # PANTALLAS PRINCIPALES
    # ==========================================
    
    # MENÚ
    pantalla_menu = ft.Column(
        [
            ft.Text(f"Hola, {NOMBRE_PAREJA} ❤️", size=28, weight="bold", color="#D63384"),
            ft.Text("Elige un regalo:", size=16),
            ft.Container(height=20),
            ft.ElevatedButton("📸  Historias", on_click=ver_historias, bgcolor="#FF69B4", color="white", width=200, height=45),
            ft.ElevatedButton("📈  Tiempo Juntos", on_click=ver_estadisticas, bgcolor="#FF1493", color="white", width=200, height=45),
            ft.ElevatedButton("💌  Carta", on_click=ver_cartas, bgcolor="#C71585", color="white", width=200, height=45),
            ft.Container(height=20),
            ft.TextButton("Volver al inicio", on_click=lambda _: cambiar_pantalla(pantalla_portada))
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )

    # PORTADA
    pantalla_portada = ft.Column(
        [
            ft.Text("Feliz Aniversario", size=32, weight="bold", color="#D63384", text_align=ft.TextAlign.CENTER),
            ft.Container(height=10),
            # CORREGIDO: Sin 'name='
            ft.Icon("favorite", size=100, color="red"),
            ft.Text("1 Año Juntos", size=20, weight="bold"),
            ft.Container(height=30),
            ft.ElevatedButton("ENTRAR ❤️", on_click=lambda _: cambiar_pantalla(pantalla_menu), bgcolor="#D63384", color="white", width=180, height=50)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(pantalla_portada)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    # Usamos la configuración de vista correcta para la nueva versión
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=port, host="0.0.0.0", assets_dir="assets")
