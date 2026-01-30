from app.validators.CPFValidator import CPFValidator
from app.validators.EmailValidator import EmailValidator
from app.validators.NameValidator import NameValidator
from app.validators.PhoneValidator import PhoneValidator
from app.validators.RGValidator import RGValidator


class DataValidationPipeline:
    @staticmethod
    def build():
        return PhoneValidator(
            RGValidator(CPFValidator(EmailValidator(NameValidator(None))))
        )
