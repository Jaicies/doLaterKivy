from plyer import email


class Email:
    recipient = 'abc@gmail.com'
    subject = 'Hi'
    text = 'This is an example.'
    create_chooser = False
    email.send(recipient=recipient, subject=subject, text=text,
               create_chooser=create_chooser)

    def send(self, recipient=None, subject=None, text=None, create_chooser=None):
        self._send(recipient=recipient, subject=subject, text=text,
                   create_chooser=create_chooser)

    def _send(self, **kwargs):
        raise NotImplementedError()



