from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class doLater(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6,0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        # add widgets to window

        #image widget
        self.window.add_widget(Image(source="doLaterLogo.png"))

        self.choice = Label(
                        text= "Would you like to send a text or email?",
                        font_size = 18,
                        color = '#00FFCE'
                            )
        self.window.add_widget(self.choice)

        self.user = TextInput(
                    multiline=False,
                    padding_y = (20,20),
                    size_hint = (1, 0.5))


        self.window.add_widget(self.user)

        self.emailbutton = Button(text="Email",
                                  size_hint = (1,0.5),
                                  bold = True,
                                  background_color = '#00FFCE',
                                  background_normal ="")
        self.emailbutton.bind(on_press=self.callback)
        self.window.add_widget(self.emailbutton)

        self.textbutton = Button(text="text",
                                 size_hint=(1, 0.5),
                                 bold=True,
                                 background_color='#00FFCE',
                                 background_normal="")
        self.textbutton.bind(on_press=self.callback)
        self.window.add_widget(self.textbutton)

        return self.window

    def callback(self, button):
        self.choice.text = self.user.text



if __name__ == "__main__":
    doLater().run()




