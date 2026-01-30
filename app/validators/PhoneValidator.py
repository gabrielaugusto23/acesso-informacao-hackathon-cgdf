import re

from app.validators.IValidator import IValidator
from app.validators.ValidationResult import ValidationResult


class PhoneValidator(IValidator):
    PHONE_REGEX = re.compile(r"(\(?\d{2}\)?\s*)?(\d{4,5})(?:[-\s]*)?(\d{4})")

    def __init__(self, next_handler=None):
        super().__init__(next_handler)

    def handle(self, text: str):
        match = self.PHONE_REGEX.search(text)

        if match:
            return ValidationResult(
                detected_value=match.group(),
                validators="PhoneValidator",
            )

        if self._next_handler is not None:
            return self._next_handler.handle(text)

        return None
