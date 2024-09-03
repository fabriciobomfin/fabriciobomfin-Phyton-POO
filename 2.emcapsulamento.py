import os
os.system("cls || clear")  # Limpar terminal

# Criando sua própria exceção
class SaldoInsuficienteError(Exception):
    pass

class ValorNegativoError(Exception):
    pass 

class Conta:
    def __init__(self, numero_conta: int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 0  # Atributo protegido

    @property
    def saldo(self):
        return self._saldo
        
    def sacar(self, valor):
        # Try - except
        try:
            self._verificar_sacar(valor)
            self._saldo -= valor
        except SaldoInsuficienteError as error:
            return f"Erro: {error.mensagem}"
        return self._saldo
    
    def _verificar_sacar(self, valor):  # Método privado
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.")  # Lançando um erro
            
    def depositar(self, valor):
        try:
            self.__verificar__depositar(valor)
        except ValorNegativoError as erro:
            return f"Erro: {erro}"
        
    def _verificar_depositar(self, valor):
        if valor < 0:
            raise ValorNegativoError("Não é possovel depositar valor negati")
        
        self._saldo += valor
        return self._saldo 

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

# Instanciar classes
conta_corrente = ContaCorrente(222, 333)
conta_poupanca = ContaPoupanca(444, 555)

# Operações de conta
conta_corrente.depositar(500)
print(f"Saldo da conta corrente: {conta_corrente.saldo}")

print(conta_corrente.sacar(200))  # Deve funcionar
print(conta_corrente.sacar(400))  # Deve mostrar erro de saldo insuficiente
