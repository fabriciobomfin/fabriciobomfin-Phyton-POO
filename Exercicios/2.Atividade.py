import os

os.system("cls || clear")  # Limpar o terminal.
from enum import Enum

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Setor(Enum):
    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Funcionario:
    
    def __init__(self, id: int, nome: str, idade: int, salario: float, setor: Setor, sexo: Sexo) -> None:
        """Construtor."""
       
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.setor = setor
        self.sexo = sexo

    def __str__(self) -> str:
        return (f"\nID: {self.id}"
                f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nSalario: {self.salario}"
                f"\nSetor: {self.setor}"
                f"\nSexo: {self.sexo}")

funcionario_1 = Funcionario(87029922,"Marta", 22, 100.50,Setor.FINANCEIRO ,Sexo.FEMININO)
print(funcionario_1)


