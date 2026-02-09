import flet as ft
from datetime import datetime
import os

def main(page: ft.Page):
    # --- CONFIGURACIÓN BÁSICA ---
    page.title = "Nuestro 1er Año ❤️"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#FFF0F5"
    page.padding = 0
    
    # --- TUS DATOS ---
    FECHA_ANIVERSARIO = datetime(2025, 2, 14) 
    NOMBRE_PAREJA = "Mi Amor"
    
    # --- MÚSICA (OPCIONAL, PUEDE FALLAR) ---
    try:
        musica = ft.Audio(
            src="https://assets.mixkit.co/music/preview/mixkit-loving-you-117.mp3",
            autoplay=False,
            volume=0.5,
        )
        page.overlay.append(musica)
        tiene_musica = True
    except:
        tiene_musica = False
    
    # --- FUNCIÓN DE NAVEGACIÓN SIMPLE ---
    def cambiar_pantalla(nueva_pantalla):
        page.controls.clear()
        page.add(nueva_pantalla)
        page.update()
    
    # ==========================================
    # 1. PANTALLA DE ESTADÍSTICAS
    # ==========================================
    def ver_estadisticas(e):
        dias_juntos = (datetime.now() - FECHA_ANIVERSARIO).days
        
        pantalla = ft.Column(
            controls=[
                ft.Text("📈 Nuestro Tiempo Juntos", 
                       size=25, weight="bold", color="#D63384"),
                ft.Divider(),
                
                ft.Container(
                    content=ft.Column([
                        ft.Icon("favorite", size=60, color="white"),
                        ft.Text(f"{dias_juntos}", size=70, weight="bold", color="white"),
                        ft.Text("Días de felicidad", size=18, color="white")
                    ], horizontal_alignment="center"),
                    padding=30,
                    bgcolor="#D63384",
                    border_radius=20,
                    width=300,
                    alignment=ft.alignment.center
                ),
                
                ft.Container(height=30),
                
                ft.Text("Cada día contigo es un regalo 💝", 
                       size=18, italic=True, color="#666"),
                
                ft.Container(height=30),
                
                ft.ElevatedButton(
                    "Volver al Menú",
                    on_click=lambda _: cambiar_pantalla(menu_principal),
                    bgcolor="#D63384",
                    color="white",
                    width=200
                )
            ],
            horizontal_alignment="center",
            spacing=20
        )
        
        cambiar_pantalla(ft.Container(
            content=pantalla,
            padding=20,
            alignment=ft.alignment.top_center
        ))
    
    # ==========================================
    # 2. PANTALLA DE HISTORIAS
    # ==========================================
    def ver_historias(e):
        pantalla = ft.Column(
            controls=[
                ft.Text("📸 Nuestras Historias", 
                       size=25, weight="bold", color="#D63384"),
                ft.Divider(),
                
                ft.Container(
                    content=ft.Column([
                        ft.Icon("airplane_ticket", size=50, color="blue"),
                        ft.Text("Nuestro primer viaje", size=20, weight="bold"),
                        ft.Text("¿Recuerdas cuando nos perdimos en aquel pueblo?", 
                               size=14, text_align="center")
                    ], horizontal_alignment="center"),
                    padding=20,
                    bgcolor="white",
                    border_radius=15,
                    width=300
                ),
                
                ft.Container(height=20),
                
                ft.Container(
                    content=ft.Column([
                        ft.Icon("restaurant", size=50, color="orange"),
                        ft.Text("Esa cena especial", size=20, weight="bold"),
                        ft.Text("La mejor pizza del mundo.", 
                               size=14, text_align="center")
                    ], horizontal_alignment="center"),
                    padding=20,
                    bgcolor="white",
                    border_radius=15,
                    width=300
                ),
                
                ft.Container(height=30),
                
                ft.ElevatedButton(
                    "Volver al Menú",
                    on_click=lambda _: cambiar_pantalla(menu_principal),
                    bgcolor="#D63384",
                    color="white",
                    width=200
                )
            ],
            horizontal_alignment="center",
            spacing=20,
            scroll="auto"
        )
        
        cambiar_pantalla(ft.Container(
            content=pantalla,
            padding=20
        ))
    
    # ==========================================
    # 3. PANTALLA DE CARTAS
    # ==========================================
    def ver_cartas(e):
        pantalla = ft.Column(
            controls=[
                ft.Text("💌 Cartas de Amor", 
                       size=25, weight="bold", color="#D63384"),
                ft.Divider(),
                
                ft.Container(
                    content=ft.Text(
                        "Querida amor mío,\n\n"
                        "Este primer año a tu lado ha sido el más hermoso de mi vida. "
                        "Cada risa, cada abrazo, cada momento contigo es un tesoro "
                        "que guardo en mi corazón.\n\n"
                        "Te amo más cada día.\n\n"
                        "Con todo mi corazón,\n"
                        "Para siempre tuyo ❤️",
                        size=16
                    ),
                    padding=25,
                    bgcolor="white",
                    border_radius=15,
                    width=350
                ),
                
                ft.Container(height=30),
                
                ft.ElevatedButton(
                    "Volver al Menú",
                    on_click=lambda _: cambiar_pantalla(menu_principal),
                    bgcolor="#D63384",
                    color="white",
                    width=200
                )
            ],
            horizontal_alignment="center",
            spacing=20,
            scroll="auto"
        )
        
        cambiar_pantalla(ft.Container(
            content=pantalla,
            padding=20
        ))
    
    # ==========================================
    # MENÚ PRINCIPAL
    # ==========================================
    menu_principal = ft.Column(
        controls=[
            ft.Text(f"Para {NOMBRE_PAREJA} ❤️", 
                   size=28, weight="bold", color="#D63384"),
            ft.Text("Nuestro Primer Año", size=18, color="#666"),
            
            ft.Container(height=40),
            
            ft.ElevatedButton(
                "📸 Nuestras Historias",
                on_click=ver_historias,
                bgcolor="#FF69B4",
                color="white",
                width=250,
                height=50
            ),
            
            ft.Container(height=15),
            
            ft.ElevatedButton(
                "📈 Tiempo Juntos",
                on_click=ver_estadisticas,
                bgcolor="#FF1493",
                color="white",
                width=250,
                height=50
            ),
            
            ft.Container(height=15),
            
            ft.ElevatedButton(
                "💌 Cartas de Amor",
                on_click=ver_cartas,
                bgcolor="#C71585",
                color="white",
                width=250,
                height=50
            ),
            
            ft.Container(height=40),
            
            ft.Text("Hecho con 💖 para ti", size=14, color="#999")
        ],
        horizontal_alignment="center",
        spacing=10
    )
    
    menu_principal = ft.Container(
        content=menu_principal,
        padding=20,
        alignment=ft.alignment.center
    )
    
    # ==========================================
    # PANTALLA DE PORTADA
    # ==========================================
    def ir_a_menu(e):
        if tiene_musica:
            musica.autoplay = True
            musica.play()
        cambiar_pantalla(menu_principal)
    
    portada = ft.Column(
        controls=[
            ft.Container(height=50),
            
            ft.Icon("favorite", size=150, color="#FF6B9D"),
            
            ft.Container(height=30),
            
            ft.Text("Bienvenida", 
                   size=40, weight="bold", color="#D63384"),
            ft.Text("a Nuestra Historia", 
                   size=24, weight="bold", color="#333"),
            
            ft.Container(height=40),
            
            ft.Text(
                '"El mejor amor es aquel que\n'
                'despierta el alma y hace\n'
                'que todo valga la pena."',
                size=16,
                italic=True,
                color="#666",
                text_align="center"
            ),
            
            ft.Container(height=40),
            
            ft.ElevatedButton(
                "Descubre Nuestro Amor ❤️",
                on_click=ir_a_menu,
                bgcolor="#D63384",
                color="white",
                width=250,
                height=50
            ),
            
            ft.Container(height=20),
            
            ft.Text("Toca el corazón para comenzar", 
                   size=14, color="#999", italic=True)
        ],
        horizontal_alignment="center",
        spacing=10
    )
    
    portada = ft.Container(
        content=portada,
        bgcolor="#FFF0F5",
        padding=20,
        alignment=ft.alignment.center,
        expand=True
    )
    
    # Iniciar con la portada
    cambiar_pantalla(portada)

# ==========================================
# CONFIGURACIÓN PARA RENDER
# ==========================================
if __name__ == "__main__":
    # Esto funcionará seguro en Render
    ft.app(
        target=main,
        port=int(os.environ.get("PORT", 8080)),
        host="0.0.0.0"
    )
