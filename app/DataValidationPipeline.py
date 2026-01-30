from validators.PhoneValidator import PhoneValidator


class DataValidationPipeline:
    @staticmethod
    def build():
        phone = PhoneValidator()
        return phone
