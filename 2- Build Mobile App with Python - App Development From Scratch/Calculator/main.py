from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        self.icon = "calculator.png"
        self.operators = ["/", "*", "+", "-"]
        self.last_operator = None
        self.last_button = None

        # Creating Layout
        main_layout = BoxLayout(orientation="vertical")
        self.solutionField = TextInput(background_color="black", foreground_color="white",
                                       multiline=False, halign="right", font_size=50,
                                       readonly=True)

        main_layout.add_widget(self.solutionField)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label, font_size=30, background_color="grey",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_btn_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equal_btn = Button(
            text="=", font_size=30, background_color="grey",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        equal_btn.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_btn)

        return main_layout

    # When user presses a button updates text on solution field
    def on_btn_press(self, instance):
        current = self.solutionField.text
        btn_text = instance.text

        if btn_text == 'C':
            self.solutionField.text = ""
        else:
            if current and (
                    self.last_operator and btn_text in self.operators):
                return
            elif current == "" and btn_text in self.operators:
                return
            else:
                new_text = current + btn_text
                self.solutionField.text = new_text
        self.last_button = btn_text
        self.last_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solutionField.text
        if text:
            solution = str(eval(self.solutionField.text))
            self.solutionField.text = solution


if __name__ == "__main__":
    app = MainApp()
    app.run()
