class e_commerce:
    def __init__(self, taxa = 0.02, estorno = True, limite = None):
        self.taxa = taxa
        self.limite = limite
    
    def processar_pagamento(self, valor):
        pass

class PayPal(e_commerce):
    def __init__(self, taxa = 0.02):
        super().__init__(taxa = taxa)

    def processar_pagamento(self, valor):
        custo_processamento = valor * (1 + self.taxa)
        print(f"Processado pelo PayPal. Valor total: R${custo_processamento:.2f}")
        return custo_processamento
    
class MercadoPago(e_commerce):
    def __init__(self, limite = 10000):
        super()__init__(limite = limite)
        self.token_valido = 7337

    def processar_pagamento(self, valor, token = None):
        if valor > self.limite:
            if token != self.token_valido:
                print("Erro: token invalido. Transação não autorizada.")
                return None
            print
            

    