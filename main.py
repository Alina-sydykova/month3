import flet as ft
from datetime import datetime

def get_greeting(name):
    #time = datetime.now().hour
    time = 7
    if 6 <= time < 12:
        return f"Доброе утро, {name}!"
    elif 12 <= time < 18:
        return f"Добрый день, {name}!"
    elif 18 <= time < 24:
        return f"Добрый вечер, {name}!"
    else:
        return f"Доброй ночи, {name}!"

def main(page: ft.Page):
    page.title = "Моё первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text(get_greeting("гость"))  # приветствие при запуске

    greeting_history = []
    history_text = ft.Text("История приветствий:", style="bodyMedium")

    def on_button_click(e):
        name = name_input.value.strip()

        if name:
            greeting_text.value = get_greeting(name)
            greet_button.text = "Поздороваться снова"
            name_input.value = ""

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            greeting_history.append(f"{timestamp}: {name}")
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        else:
            greeting_text.value = "Пожалуйста, введите ваше имя!"

        page.update()

    name_input = ft.TextField(label="Введите ваше имя:", autofocus=True, on_submit=on_button_click)

    def clear_history(e):
        greeting_history.clear()
        history_text.value = "История приветствий:"
        page.update()

    def toggle_theme(e):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        page.update()

    theme_button = ft.IconButton(icon=ft.icons.BRIGHTNESS_6, tooltip="Сменить тему", on_click=toggle_theme)
    clear_button = ft.TextButton("Очистить историю", on_click=clear_history)
    clear_button_icon = ft.IconButton(icon=ft.icons.DELETE, tooltip="Очистка", on_click=clear_history)
    greet_button = ft.ElevatedButton("Поздороваться", on_click=on_button_click)

    page.add(
        ft.Row([theme_button, clear_button, clear_button_icon], alignment=ft.MainAxisAlignment.CENTER),
        greeting_text,
        name_input,
        greet_button,
        history_text
    )

ft.app(target=main)
