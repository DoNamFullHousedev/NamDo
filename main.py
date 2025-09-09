import flet as ft
from speech import recognize_speech
from tts import speak
from dictionary import search_anh_viet, search_viet_anh, extract_en_word
def main(page: ft.Page):
    page.title = "Bài thi cuối kì python"
    page.window.height = 800
    page.window.width = 400
    page.window.left = 200
    page.window.top = 50
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.PINK_50

    txt = ft.TextField(
        hint_text="Nhập từ tiếng Anh...",
        border_radius=20,
        border_color=ft.Colors.INDIGO_300,
        bgcolor=ft.Colors.WHITE,
        expand=True
    )
    meaning = ft.Text()
    speech = ft.Text()
    mode = ft.Switch(label="Anh -> Việt", value=True)
    last_eng_word = ft.Text(value="")  # Lưu từ tiếng Anh để phát âm

    speak_btn = ft.ElevatedButton("Phát âm", on_click=lambda e: speak(last_eng_word.value), disabled=True)

    def handle_search(event):
        word = txt.value.strip().lower()
        found = False
        last_eng_word.value = ""
        speak_btn.disabled = True
        if mode.value:  # Anh Việt
            key, mean = search_anh_viet(word)
            if key is not None:
                meaning.value = f"{key}: {mean}"
                last_eng_word.value = extract_en_word(key)
                speak_btn.disabled = False
                found = True
        else:  # Việt Anh
            mean, eng = search_viet_anh(word)
            if mean is not None:
                meaning.value = f"{mean}: {eng}"
                last_eng_word.value = extract_en_word(eng)
                speak_btn.disabled = False
                found = True
        if not found:
            meaning.value = "Không tìm thấy từ"
            speak_btn.disabled = True
        page.update()

    def handle_micro(event):
        txt.value = ""
        meaning.value = ""
        speech.value = "Hãy nói vào micro..."
        page.update()
        try:
            lang = "en-US" if mode.value else "vi-VN"
            text = recognize_speech(language=lang)
            txt.value = text
            speech.value = ""
        except:
            meaning.value = 'Không nhận diện được, vui lòng thử lại '
            speech.value = ""
        page.update()

    def handle_mode_change(e):
        meaning.value = ""
        txt.value = ""
        last_eng_word.value = ""
        speak_btn.disabled = True
        if mode.value:
            mode.label = "Anh -> Việt"
            txt.hint_text = "Nhập từ tiếng Anh..."
        else:
            mode.label = "Việt -> Anh"
            txt.hint_text = "Nhập từ tiếng Việt..."
        page.update()

    btn = ft.ElevatedButton("Tìm kiếm", on_click=handle_search)
    btn_mic = ft.IconButton(icon="mic", icon_color=ft.Colors.RED, on_click=handle_micro)
    result_card = ft.Card(
        content=ft.Container(
            content=ft.Column([meaning, speak_btn], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            bgcolor=ft.Colors.AMBER_50,
            border_radius=20,
            alignment=ft.alignment.center
        ),
        margin=10,
        elevation=5
    )

    mode.on_change = handle_mode_change

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    mode,
                    ft.Row([txt, btn_mic], alignment=ft.MainAxisAlignment.CENTER),
                    btn,
                    result_card,
                    speech
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                expand=True
            ),
            padding=20,
            alignment=ft.alignment.top_center,
            expand=True
        )
    )

ft.app(target=main)