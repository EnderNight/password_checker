from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton


class PasswordCheckApp(MDApp):
    
    def check(self, args):
        password = self.input.text
        res = "cannot check data for this password"

        if len(password) < 7:
            res = "Too weak"

        else:
            if password.isdigit():
                if len(password) < 12:
                    res = "Too weak"
                else:
                    res = "Weak"

            else:
                if password.isalpha():
                    if password.islower():
                        if len(password) < 9:
                            res = "Too weak"
                        elif len(password) < 14:
                            res = "Weak"
                        elif len(password) < 18:
                            res = "Good"
                        else:
                            res = "Very good"
                    else:
                        if len(password) < 12:
                            res = "Weak"
                        elif len(password) < 15:
                            res = "Good"
                        elif len(password) < 18:
                            res = "Very good"
                        else:
                            res = "Perfect"
                else:
                    if any(c.isdigit() for c in password):
                        if any(not c.isalnum() for c in password):
                            if len(password) < 11:
                                res = "Weak"
                            elif len(password) < 13:
                                res = "Good"
                            elif len(password) < 16:
                                res = "Very good"
                            else:
                                res = "Perfect"
                        else:
                            if len(password) < 11:
                                res = "Weak"
                            elif len(password) < 14:
                                res = "Good"
                            elif len(password) < 17:
                                res = "Very good"
                            else:
                                res = "Perfect"

        self.label.text = "Password strengh : " + res


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
                hint_text = "Enter password",
                size_hint = (0.8, None),
                pos_hint = {"center_x": 0.5, "center_y": 0.5},
                font_size = 60
                )
        screen.add_widget(self.input)

        # BUTTON
        screen.add_widget(MDFillRoundFlatButton(
            text = "CHECK",
            font_size = 60,
            pos_hint = {"center_x": 0.5, "center_y": 0.3},
            on_press = self.check
            ))

        return screen

if __name__ == "__main__":
    PasswordCheckApp().run()
