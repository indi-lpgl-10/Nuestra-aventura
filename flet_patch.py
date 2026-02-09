# flet_patch.py
import flet as ft

# Definir constantes de alineación si no existen
if not hasattr(ft.alignment, 'center'):
    ft.alignment.center = ft.alignment.Alignment(0, 0)
if not hasattr(ft.alignment, 'top_center'):
    ft.alignment.top_center = ft.alignment.Alignment(0, -1)
if not hasattr(ft.alignment, 'bottom_center'):
    ft.alignment.bottom_center = ft.alignment.Alignment(0, 1)
