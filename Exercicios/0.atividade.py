from abc import ABC, abstractmethod
import os

# Limpa o terminal (útil para visualização em alguns sistemas operacionais)
os.system("cls || clear")  

# Classe para representar um endereço
class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        # Inicializa os atributos do endereço
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def exibir_endereco(self) -> str:
        # Retorna uma string formatada com os detalhes do endereço
        return (f"Logradouro: {self.logradouro}\n"
                f"Número: {self.numero}\n"
                f"Complemento: {self.complemento}\n"
                f"CEP: {self.cep}\n"
                f"Cidade: {self.cidade}")

# Classe abstrata para representar um funcionário
class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        # Inicializa os atributos comuns de um funcionário
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    @abstractmethod
    def calcular_salario(self) -> float:
        # Método abstrato que deve ser implementado por subclasses
        pass

    def __str__(self) -> str:
        # Retorna uma string formatada com os detalhes do funcionário, incluindo o endereço
        return (f"Nome: {self.nome}\n"
                f"Telefone: {self.telefone}\n"
                f"Email: {self.email}\n"
                f"{self.endereco.exibir_endereco()}")

# Classe para representar um médico, que é um tipo de funcionário
class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, salario_base: float, crm: str) -> None:
        # Inicializa atributos específicos do médico além dos comuns
        super().__init__(nome, telefone, email, endereco)
        self.salario_base = salario_base
        self.crm = crm

    def calcular_salario(self) -> float:
        # Retorna o salário base do médico (sem cálculos adicionais)
        return self.salario_base

    def __str__(self) -> str:
        # Retorna uma string formatada com detalhes do médico
        return (f"== Dados Médico ==\n"
                f"{super().__str__()}\n"
                f"Salário Base: {self.salario_base}\n"
                f"CRM: {self.crm}")

# Classe para representar um engenheiro, que também é um tipo de funcionário
class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, salario_base: float, crea: str) -> None:
        # Inicializa atributos específicos do engenheiro além dos comuns
        super().__init__(nome, telefone, email, endereco)
        self.salario_base = salario_base
        self.crea = crea

    def calcular_salario(self) -> float:
        # Retorna o salário base do engenheiro (sem cálculos adicionais)
        return self.salario_base

    def __str__(self) -> str:
        # Retorna uma string formatada com detalhes do engenheiro
        return (f"== Dados Engenheiro ==\n"
                f"{super().__str__()}\n"
                f"Salário Base: {self.salario_base}\n"
                f"CREA: {self.crea}")

# Criando instâncias e imprimindo informações
# Instância de Engenheiro
engenheiro = Engenheiro("Fabricio", "71983169204", "ducorte99@gmail.com", 
                        Endereco("Rua A", "7", "casa", "41180600", "Salvador"), 5000, "422")

# Instância de Médico
medico = Medico("Silvestre", "5484984", "dmwqomdwq@dmwqodm,wqo", 
                Endereco("Rua B", "77", "dqwdwq", "321321", "Salvador"), 5000, "321")

# Imprimindo detalhes dos funcionários
print(engenheiro)
print(medico)
