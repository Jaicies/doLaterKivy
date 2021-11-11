from plyer import sms


class Sms:
    recipient = 9999222299
    message = 'This is an example.'
    sms.send(recipient=recipient, message=message)

    def send(self, recipient, message):
        self._send(recipient=recipient, message=message)

    def _send(self, **kwargs):
        raise NotImplementedError()

