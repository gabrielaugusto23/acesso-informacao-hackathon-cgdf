import re

from validators.IValidator import IValidator
from validators.ValidationResult import ValidationResult


class EmailValidator(IValidator):
    EMAIL_REGEX = re.compile(r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})")

    def handle(self, text: str):
        match = self.EMAIL_REGEX.search(text)

        if match:
            return ValidationResult(
                detected_value=match.group(),
                validators="EmailValidator",
            )

        if self._next_handler:
            return self._next_handler.handle(text)

        return None
