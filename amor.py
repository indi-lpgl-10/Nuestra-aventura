import flet as ft
from datetime import datetime
import os

def main(page: ft.Page):
    # --- CONFIGURACIÓN BÁSICA ---
    page.title = "Para Mi Amor ❤️"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # --- TUS DATOS ---
    FECHA_ANIVERSARIO = datetime(2025, 2, 14) 
    NOMBRE_PAREJA = "Mi Amor"
    
    # --- FUNCIÓN SIMPLE DE NAVEGACIÓN ---
    def cambiar_pantalla(nueva_pantalla):
        page.controls.clear()
        page.add(nueva_pantalla)
        page.update()
    
    # ==========================================
    # 1. ESTADÍSTICAS (SIN ft.alignment)
    # ==========================================
    def ver_estadisticas(e):
        dias_juntos = (datetime.now() - FECHA_ANIVERSARIO).days
        
        pantalla = ft.Column([
            ft.Text("📈 Nuestro Tiempo", size=25, weight="bold", color="#D63384"),
            ft.Divider(),
            
            ft.Container(
                ft.Column([
                    ft.Icon("favorite", size=50, color="white"),
                    ft.Text(f"{dias_juntos} Días", size=40, weight="bold", color="white"),
                    ft.Text("juntos ❤️", size=16, color="white")
                ]),
                padding=20,
                bgcolor="#D63384",
                border_radius=15,
                width=300
            ),
            
            ft.Container(height=20),
            ft.Text("Cada día contigo es especial", size=18, italic=True),
            ft.Container(height=20),
            
            ft.ElevatedButton(
                "Volver al Menú",
                on_click=lambda _: cambiar_pantalla(menu_principal),
                bgcolor="#D63384",
                color="white"
            )
        ])
        
        cambiar_pantalla(ft.Container(pantalla, padding=20))
    
    # ==========================================
    # 2. HISTORIAS (SIN ft.alignment)
    # ==========================================
    def ver_historias(e):
        pantalla = ft.Column([
            ft.Text("📸 Nuestras Historias", size=25, weight="bold", color="#D63384"),
            
            ft.Container(
                ft.Column([
                    ft.Text("Nuestro primer viaje", size=18, weight="bold"),
                    ft.Icon("airplane_ticket", size=50, color="blue"),
                    ft.Text("¿Recuerdas cuando nos perdimos?", size=14)
                ]),
                padding=15,
                bgcolor="white",
                border_radius=10
            ),
            
            ft.Container(
                ft.Column([
                    ft.Text("Esa cena especial", size=18, weight="bold"),
                    ft.Icon("restaurant", size=50, color="orange"),
                    ft.Text("La mejor pizza del mundo", size=14)
                ]),
                padding=15,
                bgcolor="white",
                border_radius=10
            ),
            
            ft.Container(height=20),
            
            ft.ElevatedButton(
                "Volver al Menú",
                on_click=lambda _: cambiar_pantalla(menu_principal),
                bgcolor="#D63384",
                color="white"
            )
        ])
        
        cambiar_pantalla(ft.Container(pantalla, padding=20))
    
    # ==========================================
    # 3. CARTAS (SIN ft.alignment)
    # ==========================================
    def ver_cartas(e):
        pantalla = ft.Column([
            ft.Text("💌 Carta para ti", size=25, weight="bold", color="#D63384"),
            
            ft.Container(
                ft.Text(
                    "Mi amor,\n\n"
                    "Este año a tu lado ha sido el más feliz de mi vida. "
                    "Gracias por cada sonrisa, cada abrazo y cada momento juntos.\n\n"
                    "Te amo con todo mi corazón.\n\n"
                    "Para siempre tuyo/a ❤️",
                    size=16
                ),
                padding=20,
                bgcolor="white",
                border_radius=10
            ),
            
            ft.Container(height=20),
            
            ft.ElevatedButton(
                "Volver al Menú",
                on_click=lambda _: cambiar_pantalla(menu_principal),
                bgcolor="#D63384",
                color="white"
            )
        ])
        
        cambiar_pantalla(ft.Container(pantalla, padding=20))
    
    # ==========================================
    # MENÚ PRINCIPAL (SIN ft.alignment)
    # ==========================================
    menu_principal = ft.Container(
        ft.Column([
            ft.Text(f"Para {NOMBRE_PAREJA} ❤️", size=30, weight="bold", color="#D63384"),
            ft.Text("Nuestro Primer Año", size=18),
            ft.Container(height=30),
            
            ft.ElevatedButton(
                "📸 Nuestras Historias",
                on_click=ver_historias,
                bgcolor="#FF69B4",
                color="white",
                width=250,
                height=50
            ),
            
            ft.ElevatedButton(
                "📈 Tiempo Juntos",
                on_click=ver_estadisticas,
                bgcolor="#FF1493",
                color="white",
                width=250,
                height=50
            ),
            
            ft.ElevatedButton(
                "💌 Cartas de Amor",
                on_click=ver_cartas,
                bgcolor="#C71585",
                color="white",
                width=250,
                height=50
            ),
            
            ft.Container(height=30),
            ft.Text("Hecho con amor 💖", size=14, color="#999")
        ]),
        padding=20
    )
    
    # ==========================================
    # PORTADA (SIN ft.alignment)
    # ==========================================
    def ir_a_menu(e):
        cambiar_pantalla(menu_principal)
    
    portada = ft.Container(
        ft.Column([
            ft.Container(height=100),
            ft.Icon("favorite", size=150, color="#FF6B9D"),
            ft.Container(height=30),
            ft.Text("Bienvenida", size=40, weight="bold", color="#D63384"),
            ft.Text("a Nuestra Historia", size=24, weight="bold"),
            ft.Container(height=40),
            
            ft.Container(
                ft.Text(
                    "Un año de amor,\n"
                    "risas y momentos\n"
                    "inolvidables ❤️",
                    size=18,
                    text_align="center"
                ),
                padding=20,
                bgcolor="#FFF9FA",
                border_radius=15,
                width=300
            ),
            
            ft.Container(height=40),
            
            ft.ElevatedButton(
                "Entrar ❤️",
                on_click=ir_a_menu,
                bgcolor="#D63384",
                color="white",
                width=200,
                height=50
            )
        ]),
        bgcolor="#FFF0F5",
        padding=20,
        expand=True
    )
    
    # Iniciar
    page.add(portada)

# ==========================================
# CONFIGURACIÓN MÍNIMA PARA RENDER
# ==========================================
if __name__ == "__main__":
    ft.app(
        target=main,
        port=int(os.environ.get("PORT", 8080)),
        host="0.0.0.0"
    )
