from validators.PhoneValidator import PhoneValidator
from validators.RGValidator import RGValidator

class DataValidationPipeline:
    @staticmethod
    def build():
        phone = PhoneValidator()
        rg = RGValidator(phone)
        return rg
