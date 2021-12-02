from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty

from plyer import email

Builder.load_string('''
<EmailInterface>:
    orientation: 'vertical'
    BoxLayout:
        Label:
            text: 'Recipient:'
        TextInput:
            id: recipient
    BoxLayout:
        Label:
            text: 'Subject:'
        TextInput:
            id: subject
    BoxLayout:
        Label:
            text: 'text'
        TextInput:
            id: text
    IntentButton:
        email_recipient: recipient.text
        email_subject: subject.text
        email_text: text.text
        text: 'Send email'
        size_hint_y: None
        height: sp(40)
        on_release: self.send_email()
''')


class EmailInterface(BoxLayout):
    pass


class IntentButton(Button):
    email_recipient = StringProperty()
    email_subject = StringProperty()
    email_text = StringProperty()

    def send_email(self, *args):
        email.send(recipient=self.email_recipient,
                   subject=self.email_subject,
                   text=self.email_text,
                   create_chooser=False)


class EmailApp(App):
    def build(self):
        return EmailInterface()

    def on_pause(self):
        return True


if __name__ == "__main__":
    EmailApp().run()


