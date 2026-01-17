import re

from IHandler import IHandler


class PhoneHandler(IHandler):
    PHONE_REGEX = re.compile(r"(\(?\d{2}\)?\s?)?(\d{4,5})[-\s]?(\d{4})")

    def handle(self, text: str):
        match = self.PHONE_REGEX.search(text)

        if match:
            return {
                "tipo": "DADO_PESSOAL",
                "campo": "telefone",
                "valor_detectado": match.group(),
                "handlers": "PhoneHandler",
            }

        if self.__next_handler:
            return self.__next_handler.handle(text)

        return None
