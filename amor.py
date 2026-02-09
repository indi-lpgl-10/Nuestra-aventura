import flet as ft
from datetime import datetime
import os
import logging

# Configurar logging para ver errores en Render
logging.basicConfig(level=logging.INFO)

def main(page: ft.Page):
    # --- CONFIGURACIÓN PARA RENDER/WEB ---
    page.title = "Nuestro 1er Año ❤️"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#FFF0F5"
    
    # Para Render: no usar window dimensions (no aplica en web)
    # page.window_width = 390  # Comentar para web
    # page.window_height = 844  # Comentar para web
    
    # --- TUS DATOS (PERSONALIZA AQUÍ) ---
    FECHA_ANIVERSARIO = datetime(2025, 2, 14) 
    NOMBRE_PAREJA = "Mi Amor"

    # --- MÚSICA DE FONDO (CON MANEJO DE ERRORES) ---
    try:
        musica = ft.Audio(
            src="https://assets.mixkit.co/music/preview/mixkit-loving-you-117.mp3",  # URL alternativa si no tienes cancion.mp3
            autoplay=False,  # Cambiado a False para evitar problemas en móviles
            volume=0.7,
        )
        page.overlay.append(musica)
        tiene_musica = True
    except Exception as e:
        print(f"Error cargando música: {e}")
        tiene_musica = False

    def toggle_musica(e):
        if tiene_musica:
            if musica.autoplay:
                musica.autoplay = False
                musica.pause()
                e.control.icon = ft.icons.MUSIC_OFF
                e.control.tooltip = "Activar música"
            else:
                musica.autoplay = True
                musica.play()
                e.control.icon = ft.icons.MUSIC_NOTE
                e.control.tooltip = "Silenciar música"
            page.update()

    # --- COMPONENTE DE CABECERA REUTILIZABLE ---
    def crear_cabecera(titulo):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        on_click=lambda _: cambiar_pantalla(menu_principal),
                        tooltip="Volver al menú"
                    ),
                    ft.Text(titulo, size=22, weight="bold", color="#D63384", expand=True),
                    ft.IconButton(
                        icon=ft.icons.MUSIC_OFF if tiene_musica else ft.icons.MUSIC_OFF,
                        on_click=toggle_musica if tiene_musica else None,
                        tooltip="Controlar música" if tiene_musica else "Música no disponible",
                        disabled=not tiene_musica
                    )
                ],
                alignment=ft.MainAxisAlignment.START
            ),
            padding=ft.padding.only(left=10, right=10, top=10),
            bgcolor="#FFE4E9"
        )

    # --- NAVEGACIÓN MEJORADA ---
    def cambiar_pantalla(nueva_pantalla):
        page.controls.clear()
        page.add(nueva_pantalla)
        page.update()

    # ==========================================
    # 1. ESTADÍSTICAS MEJORADAS
    # ==========================================
    def ver_estadisticas(e):
        ahora = datetime.now()
        diferencia = ahora - FECHA_ANIVERSARIO
        dias_juntos = diferencia.days
        horas_juntos = dias_juntos * 24
        semanas_juntos = dias_juntos // 7
        
        contenido = ft.Column(
            controls=[
                crear_cabecera("📈 Nuestro Tiempo"),
                ft.Container(height=20),
                
                # Tarjeta principal de días
                ft.Container(
                    content=ft.Column([
                        ft.Icon("favorite", size=50, color="white"),
                        ft.Text(f"{dias_juntos}", size=60, weight="bold", color="white"),
                        ft.Text("DÍAS JUNTOS", size=18, color="white", weight="bold")
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=30,
                    bgcolor="#D63384",
                    border_radius=20,
                    alignment=ft.alignment.center,
                    width=300
                ),
                
                ft.Container(height=20),
                
                # Estadísticas adicionales
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Column([
                                ft.Icon("schedule", size=30, color="#D63384"),
                                ft.Text(f"{horas_juntos:,}", size=20, weight="bold"),
                                ft.Text("horas", size=12)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            padding=15,
                            bgcolor="white",
                            border_radius=15,
                            expand=True
                        ),
                        ft.Container(width=10),
                        ft.Container(
                            content=ft.Column([
                                ft.Icon("calendar_today", size=30, color="#D63384"),
                                ft.Text(f"{semanas_juntos}", size=20, weight="bold"),
                                ft.Text("semanas", size=12)
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            padding=15,
                            bgcolor="white",
                            border_radius=15,
                            expand=True
                        ),
                    ]
                ),
                
                ft.Container(height=25),
                ft.Text("Cada día a tu lado es un regalo 💝", size=16, italic=True, color="#666"),
                ft.Container(height=20),
                
                # Contador en tiempo real
                ft.Container(
                    content=ft.Column([
                        ft.Text("Contador en vivo:", size=14, color="#888"),
                        ft.Text(f"Desde el {FECHA_ANIVERSARIO.strftime('%d/%m/%Y')}", size=12),
                    ]),
                    padding=10
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO
        )
        
        pantalla = ft.Container(content=contenido, padding=20, expand=True)
        cambiar_pantalla(pantalla)

    # ==========================================
    # 2. HISTORIAS INTERACTIVAS
    # ==========================================
    def ver_historias(e):
        historias = [
            {
                "titulo": "Nuestro Primer Viaje ✈️",
                "icono": "airplane_ticket",
                "color": "#4A90E2",
                "texto": "¿Recuerdas cuando nos perdimos en aquel pueblo? Fue el mejor 'error' de nuestras vidas. Aprendimos que lo importante no es el destino, sino estar juntos.",
                "fecha": "Marzo 2025"
            },
            {
                "titulo": "Esa Cena Especial 🍕",
                "icono": "restaurant",
                "color": "#FF9500",
                "texto": "La mejor pizza del mundo, no por su sabor, sino por la compañía. Tus risas hicieron que esa noche fuera mágica.",
                "fecha": "Abril 2025"
            },
            {
                "titulo": "El Día que Todo Cambió 💘",
                "icono": "favorite",
                "color": "#FF2D55",
                "texto": "14 de febrero de 2025. El día en que nuestros caminos se unieron para siempre. Prometo hacerte feliz cada día de mi vida.",
                "fecha": "14 Feb 2025"
            }
        ]
        
        tarjetas = []
        for historia in historias:
            tarjeta = ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Icon(historia["icono"], color=historia["color"], size=30),
                        ft.Text(historia["titulo"], size=18, weight="bold", expand=True),
                    ]),
                    ft.Container(height=10),
                    ft.Text(historia["texto"], size=14),
                    ft.Container(height=10),
                    ft.Text(historia["fecha"], size=12, color="#888", italic=True)
                    ]),
                padding=20,
                bgcolor="white",
                border_radius=15,
                border=ft.border.all(1, "#EEE")
            )
            tarjetas.append(tarjeta)
            tarjetas.append(ft.Container(height=15))
        
        contenido = ft.Column(
            controls=[
                crear_cabecera("📸 Nuestras Historias"),
                ft.Container(height=20),
                *tarjetas,
                ft.Container(
                    content=ft.Text("Todavía estamos escribiendo nuestra historia... 💌", 
                                   size=16, italic=True, text_align=ft.TextAlign.CENTER),
                    padding=20
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        
        cambiar_pantalla(ft.Container(content=contenido, padding=20))

    # ==========================================
    # 3. CARTAS PERSONALIZADAS
    # ==========================================
    def ver_cartas(e):
        cartas = [
            {
                "titulo": "Para el Amor de Mi Vida 💌",
                "contenido": """Querida amor mío,

Este primer año a tu lado ha sido el más hermoso de mi vida. Cada risa, cada abrazo, cada momento contigo es un tesoro que guardo en mi corazón.

Eres mi razón para sonreír cada mañana y mi paz en cada atardecer. Gracias por ser exactamente como eres, por tu paciencia, tu ternura y tu amor incondicional.

Prometo amarte cada día más, apoyarte en tus sueños y construir juntos un futuro lleno de felicidad.

Con todo mi amor,
Para siempre tuyo.""",
                "firma": "Tu Media Naranja 🍊"
            }
        ]
        
        contenido = ft.Column(
            controls=[
                crear_cabecera("💌 Cartas de Amor"),
                ft.Container(height=20),
                
                ft.Container(
                    content=ft.Column([
                        ft.Text(cartas[0]["titulo"], size=22, weight="bold", color="#D63384"),
                        ft.Divider(height=20),
                        ft.Text(cartas[0]["contenido"], size=16, selectable=True),
                        ft.Divider(height=20),
                        ft.Text(cartas[0]["firma"], size=18, italic=True, weight="bold", color="#D63384")
                    ]),
                    padding=25,
                    bgcolor="#FFF9FA",
                    border_radius=15,
                    border=ft.border.all(2, "#FFD1DC")
                ),
                
                ft.Container(height=30),
                
                # Botón para añadir más cartas (funcionalidad futura)
                ft.Container(
                    content=ft.Column([
                        ft.Icon(ft.icons.ADD_CIRCLE_OUTLINE, size=40, color="#D63384"),
                        ft.Text("Próximamente: Más cartas sorpresa", size=14, color="#666"),
                        ft.Text("(Sigue deslizando hacia abajo 👇)", size=12, color="#999")
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=20
                )
            ],
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        
        pantalla = ft.Container(content=contenido, padding=20, expand=True)
        cambiar_pantalla(pantalla)

    # ==========================================
    # MENÚ PRINCIPAL REDISEÑADO
    # ==========================================
    opciones_menu = [
        {"icono": "photo_library", "texto": "Nuestras Historias", "color": "#FF69B4", "accion": ver_historias},
        {"icono": "timeline", "texto": "Tiempo Juntos", "color": "#FF1493", "accion": ver_estadisticas},
        {"icono": "love_and_relationship", "texto": "Cartas de Amor", "color": "#C71585", "accion": ver_cartas},
    ]
    
    botones_menu = []
    for opcion in opciones_menu:
        boton = ft.Container(
            content=ft.Column([
                ft.Icon(opcion["icono"], size=40, color="white"),
                ft.Text(opcion["texto"], size=16, color="white", weight="bold")
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10),
            on_click=opcion["accion"],
            padding=25,
            bgcolor=opcion["color"],
            border_radius=20,
            width=280,
            height=120,
            alignment=ft.alignment.center,
            animate=ft.animation.Animation(300, ft.AnimationCurve.EASE_IN_OUT)
        )
        botones_menu.append(boton)
        botones_menu.append(ft.Container(height=15))

    menu_principal = ft.Column(
        controls=[
            # Encabezado con nombre personalizado
            ft.Container(
                content=ft.Column([
                    ft.Text(f"Para {NOMBRE_PAREJA}", 
                           size=28, weight="bold", color="#D63384", 
                           text_align=ft.TextAlign.CENTER),
                    ft.Text("❤️ Nuestro Primer Año ❤️", 
                           size=18, color="#666", text_align=ft.TextAlign.CENTER),
                    ft.Container(height=10),
                    ft.Divider(height=1, color="#FFD1DC")
                ]),
                padding=ft.padding.only(top=40, bottom=20)
            ),
            
            ft.Container(height=20),
            
            # Botones del menú
            *botones_menu,
            
            ft.Container(height=30),
            
            # Pie de página
            ft.Container(
                content=ft.Column([
                    ft.Text("Hecho con 💖 para ti", size=14, color="#999"),
                    ft.Text(f"Actualizado: {datetime.now().strftime('%d/%m/%Y')}", size=12, color="#CCC")
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                padding=20
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO
    )

    # ==========================================
    # PANTALLA DE PORTADA MEJORADA
    # ==========================================
    def ir_a_menu_desde_portada(e):
        if tiene_musica:
            musica.autoplay = True
            musica.play()
        cambiar_pantalla(menu_principal)

    portada = ft.Column(
        controls=[
            # Espacio superior
            ft.Container(height=100),
            
            # Corazón animado
            ft.Container(
                content=ft.Stack([
                    ft.Icon("favorite", size=180, color="#FF6B9D"),
                    ft.Container(
                        content=ft.Text("I²", size=70, weight="bold", color="white"),
                        width=180, height=180,
                        alignment=ft.alignment.center,
                    )
                ]),
                animate_scale=ft.animation.Animation(1000, ft.AnimationCurve.BOUNCE_OUT)
            ),
            
            ft.Container(height=40),
            
            # Texto de bienvenida
            ft.Column([
                ft.Text("Bienvenida", 
                       size=42, weight="bold", color="#D63384"),
                ft.Text("a Nuestra Historia", 
                       size=24, color="#333", weight="bold"),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            
            ft.Container(height=40),
            
            # Mensaje romántico
            ft.Container(
                content=ft.Text(
                    '"El mejor amor es aquel que despierta el alma\n'
                    'y nos hace alcanzar más, que enciende el corazón\n'
                    'y nos trae paz a la mente."',
                    size=16, italic=True, color="#666",
                    text_align=ft.TextAlign.CENTER
                ),
                padding=20,
                bgcolor="#FFF9FA",
                border_radius=15,
                width=300
            ),
            
            ft.Container(height=40),
            
            # Botón de entrada
            ft.Container(
                content=ft.ElevatedButton(
                    content=ft.Row([
                        ft.Icon(ft.icons.FAVORITE, color="white"),
                        ft.Text("Descubre Nuestro Amor", size=18, color="white")
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    on_click=ir_a_menu_desde_portada,
                    bgcolor="#D63384",
                    height=60,
                    width=280,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=15),
                    )
                ),
                animate_opacity=ft.animation.Animation(1000, ft.AnimationCurve.EASE_IN)
            ),
            
            # Instrucción para móvil
            ft.Container(
                content=ft.Text("Presiona el corazón ❤️", 
                               size=14, color="#999", italic=True),
                padding=ft.padding.only(top=20)
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True
    )
    
    portada_container = ft.Container(
        content=portada,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=["#FFF0F5", "#FFE4E9", "#FFD1DC"]
        ),
        expand=True
    )

    # Inicializar con portada
    page.add(portada_container)

# ==========================================
# CONFIGURACIÓN PARA RENDER (VERSIÓN CORREGIDA)
# ==========================================
if __name__ == "__main__":
    # Configuración específica para Render
    port = int(os.environ.get("PORT", 8080))
    
    # Usar la API correcta de Flet para la versión actual
    # En versiones más recientes, ft.app funciona sin parámetro view
    ft.app(
        target=main,
        port=port,
        host="0.0.0.0",
        assets_dir="assets"
    )
