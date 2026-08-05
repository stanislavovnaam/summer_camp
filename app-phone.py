from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.animation import Animation
import random

Window.clearcolor = (0.05, 0.0, 0.0, 1)


class MyApp(App):
    def build(self):
        btn = Button(
            text="Открыть",
            background_color=(0.35, 0.0, 0.0, 1),
            color=(1, 1, 1, 1)
        )
        btn.bind(on_press=self.show_popup)
        return btn

    def show_popup(self, instance):
        layout = BoxLayout(orientation="vertical", spacing=10, padding=15)

        self.label = Label(
            text="СИСТЕМА ОБНАРУЖИЛА [b]СБОЙ[/b]",
            markup=True,
            font_size="24sp",
            color=(1, 0.2, 0.2, 1)
        )

        close_btn = Button(
            text="Закрыть",
            size_hint_y=None,
            height=60,
            background_color=(0.2, 0, 0, 1),
            color=(1, 1, 1, 1),
            disabled=True
        )

        layout.add_widget(self.label)
        layout.add_widget(close_btn)

        self.popup = Popup(
            title="!!! WARNING !!!",
            content=layout,
            size_hint=(0.85, 0.45),
            auto_dismiss=False
        )

        self.popup.open()
        self.event = Clock.schedule_interval(self.glitch_step, 0.12)
        Clock.schedule_once(self.close_popup, 300)

    def glitch_step(self, dt):
        texts = [
            "СИСТЕМА ОБНАРУЖИЛА [b]СБОЙ[/b]",
            "СИСТЕМА ОБНАРУЖИЛА [b]S8Y[/b]",
            "СИСТЕМА ОБНАРУЖИЛА [b]▒▒▒[/b]",
            "[b]ERROR[/b] / CONNECTION LOST",
            "СИСТЕМА ОБНАРУЖИЛА [b]СБ0Й[/b]",
        ]

        self.label.text = random.choice(texts)
        self.label.color = (1, random.uniform(0.1, 0.6), random.uniform(0.1, 0.3), 1)

        dx = random.randint(-8, 8)
        dy = random.randint(-4, 4)
        self.label.pos_hint = {"center_x": 0.5 + dx / 500, "center_y": 0.65 + dy / 500}

    def close_popup(self, dt):
        if hasattr(self, "event"):
            self.event.cancel()
        if hasattr(self, "popup") and self.popup:
            self.popup.dismiss()


MyApp().run()