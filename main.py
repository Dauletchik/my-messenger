from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton

class ChatScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Главный вертикальный контейнер для всего экрана
        main_layout = MDBoxLayout(orientation='vertical')
        
        # 1. Область со скроллом, где будут отображаться сообщения
        scroll = MDScrollView()
        self.chat_list = MDList()
        scroll.add_widget(self.chat_list)
        main_layout.add_widget(scroll)
        
        # 2. Нижняя панель для ввода (текст + кнопка отправки)
        bottom_bar = MDBoxLayout(orientation='horizontal', size_hint_y=None, height="60dp", padding="10dp")
        
        self.text_input = MDTextField(hint_text="Напишите сообщение...", size_hint_x=0.8)
        send_btn = MDIconButton(icon="send", on_release=self.send_message)
        
        bottom_bar.add_widget(self.text_input)
        bottom_bar.add_widget(send_btn)
        
        main_layout.add_widget(bottom_bar)
        self.add_widget(main_layout)

    def send_message(self, instance):
        text = self.text_input.text.strip()
        if text:
            # Добавляем сообщение в список чата на экране
            self.chat_list.add_widget(OneLineListItem(text=f"Вы: {text}"))
            self.text_input.text = "" # Очищаем поле ввода после отправки

class MessengerApp(MDApp):
    def build(self):
        # Настраиваем тему (Dark — тёмная, как в Telegram)
        self.theme_cls.theme_style = "Dark"  
        self.theme_cls.primary_palette = "Blue"
        return ChatScreen()

if __name__ == "__main__":
    MessengerApp().run()
