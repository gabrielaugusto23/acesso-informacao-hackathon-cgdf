import spacy

from app.validators.IValidator import IValidator
from app.validators.ValidationResult import ValidationResult

nlp = spacy.load("pt_core_news_sm")


class NameValidator(IValidator):
    def __init__(self, next_handler=None):
        super().__init__(next_handler)

    def handle(self, text: str):
        doc = nlp(text)
        for ent in doc.ents:
            if ent.label_ == "PER":
                if len(ent.text.split()) >= 2:
                    return ValidationResult(
                        detected_value=ent.text,
                        validators="NameValidator",
                    )

        if self._next_handler is not None:
            return self._next_handler.handle(text)

        return None
