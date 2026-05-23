import flet as ft
import random
import time

def main(page: ft.Page):
    # Forzar el tema claro y fondo visible
    page.title = "JDM Car Memorama"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F8F9FA"
    page.padding = 20

    # Lista de autos (parejas)
    CARROS = ["🏎️", "🚗", "🚙", "🚓", "🚘", "🚨", "🏎️", "🚗", "🚙", "🚓", "🚘", "🚨"]
    random.shuffle(CARROS)

    state = {
        "tablero": CARROS,
        "seleccionadas": [],
        "parejas_encontradas": set(),
        "intentos": 0,
        "botones": []
    }

    # Marcador de intentos
    marcador = ft.Text(
        value="Intentos: 0 | Parejas: 0/6", 
        size=22, 
        color="#1A1D20", 
        weight=ft.FontWeight.BOLD
    )

    def tarjeta_click(e):
        btn = e.control
        idx = btn.data

        if len(state["seleccionadas"]) >= 2 or idx in state["seleccionadas"] or state["tablero"][idx] in state["parejas_encontradas"]:
            return

        # Mostrar el emoji del carro al hacer clic usando la propiedad content
        btn.content = ft.Text(state["tablero"][idx], size=30)
        btn.style = ft.ButtonStyle(bgcolor="#E9ECEF")
        state["seleccionadas"].append(idx)
        page.update()

        if len(state["seleccionadas"]) == 2:
            idx1, idx2 = state["seleccionadas"]
            state["intentos"] += 1
            marcador.value = f"Intentos: {state['intentos']} | Parejas: {len(state['parejas_encontradas'])}/6"
            page.update()

            if state["tablero"][idx1] == state["tablero"][idx2]:
                state["parejas_encontradas"].add(state["tablero"][idx1])
                state["seleccionadas"] = []
                if len(state["parejas_encontradas"]) == 6:
                    marcador.value = f"🏆 ¡Ganaste en {state['intentos']} intentos!"
                page.update()
            else:
                # Si no coinciden, esperamos un momento y ocultamos
                time.sleep(0.8)
                state["botones"][idx1].content = ft.Text("❓", size=30, color="#212529")
                state["botones"][idx1].style = ft.ButtonStyle(bgcolor="#FFFFFF")
                state["botones"][idx2].content = ft.Text("❓", size=30, color="#212529")
                state["botones"][idx2].style = ft.ButtonStyle(bgcolor="#FFFFFF")
                state["seleccionadas"] = []
                page.update()

    def reiniciar_juego(e):
        random.shuffle(CARROS)
        state["tablero"] = CARROS
        state["seleccionadas"] = []
        state["parejas_encontradas"] = set()
        state["intentos"] = 0
        marcador.value = "Intentos: 0 | Parejas: 0/6"
        for btn in state["botones"]:
            btn.content = ft.Text("❓", size=30, color="#212529")
            btn.style = ft.ButtonStyle(bgcolor="#FFFFFF")
        page.update()

    # Cuadrícula nativa de 4 columnas
    grid = ft.GridView(
        expand=True,
        runs_count=4,
        max_extent=90,
        spacing=10,
        run_spacing=10,
    )

    # Generamos los 12 botones usando .content en lugar de .text
    state["botones"] = []
    for i in range(12):
        btn = ft.ElevatedButton(
            content=ft.Text("❓", size=30, color="#212529"),
            data=i,
            on_click=tarjeta_click,
            style=ft.ButtonStyle(
                bgcolor="#FFFFFF",
                shape=ft.RoundedRectangleBorder(radius=12)
            )
        )
        state["botones"].append(btn)
        grid.controls.append(btn)

    # Agregamos todo a la vista de manera simplificada
    page.add(
        ft.Row([ft.Text("🚗 JDM Memorama", size=28, weight=ft.FontWeight.BOLD, color="#1A1D20")], alignment=ft.MainAxisAlignment.CENTER),
        ft.Container(height=10),
        ft.Row([ft.Container(content=grid, width=380, height=300)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([marcador], alignment=ft.MainAxisAlignment.CENTER),
        ft.Container(height=15),
        ft.Row([
            ft.ElevatedButton(
                content=ft.Text("🔄 Reiniciar Juego", color="#FFFFFF"), 
                on_click=reiniciar_juego,
                style=ft.ButtonStyle(bgcolor="#0D6EFD")
            )
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

if __name__ == "__main__":
    # Forzamos vista web para que corra perfecto dentro de GitHub Codespaces
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)