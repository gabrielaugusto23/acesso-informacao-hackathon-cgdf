import re

from app.validators.IValidator import IValidator
from app.validators.ValidationResult import ValidationResult


class RGValidator(IValidator):
    RG_REGEX = re.compile(
        r"(\d{2}\.\d{3}\.\d{3}-[0-9X]|SP\d{8}|RJ-\d{2}\.\d{3}\.\d{3}-\d)"
    )

    def __init__(self, next_handler=None):
        super().__init__(next_handler)

    def handle(self, text: str):
        match = self.RG_REGEX.search(text)

        if match:
            return ValidationResult(
                detected_value=match.group(),
                validators="RGValidator",
            )

        if self._next_handler is not None:
            return self._next_handler.handle(text)

        return None
