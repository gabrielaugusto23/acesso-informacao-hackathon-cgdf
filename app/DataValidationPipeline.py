from validators.CPFValidator import CPFValidator

class DataValidationPipeline:
    @staticmethod
    def build():

        cpf = CPFValidator()
        
        # cpf.set_next(phone)

        return cpf