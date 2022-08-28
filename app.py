from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton


class PasswordCheckApp(MDApp):
    
    def check(self, args):
        print("TEST")

    def build(self):

        # SCREEN
        screen = MDScreen()

        # RESULTS
        self.label = MDLabel(
                halign="center",
                theme_text_color = "Primary",
                pos_hint = {"center_x": 0.5, "center_y": 0.7},
                font_style = "H5"
        )
        screen.add_widget(self.label)

        # INPUT
        self.input = MDTextField(
                text = "enter password",
                halign = "center",
                size_hint = (0.8, 1),
                pos_hint = {"center_x": 0.5, "center_y": 0.5},
                font_size = 22
                )
        screen.add_widget(self.input)

        # BUTTON
        screen.add_widget(MDFillRoundFlatButton(
            text = "CHECK",
            font_size = 17,
            pos_hint = {"center_x": 0.5, "center_y": 0.3},
            on_press = self.check
            ))

        return screen

if __name__ == "__main__":
    PasswordCheckApp().run()
