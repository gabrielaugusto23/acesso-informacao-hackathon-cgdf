
from validators.PhoneValidator import PhoneValidator
from validators.RGValidator import RGValidator
from validators.CPFValidator import CPFValidator

class DataValidationPipeline:
    @staticmethod
    def build():
        phone = PhoneValidator()
        rg = RGValidator(phone)
        cpf = CPFValidator(rg)
        return cpf
