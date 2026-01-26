import re

from validators.IValidator import IValidator

class EmailValidator(IValidator):
    EMAIL_REGEX = re.compile(r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})")

    def handle(self, text: str):
        match = self.EMAIL_REGEX.search(text)

        if match:
            return {
                "tipo": "DADO_PESSOAL",
                "campo": "email",
                "valor_detectado": match.group(),
                "validators": "EmailValidator",
            }
        if self.__next_handler:
            return self.__next_handler.handle(text)

        return None