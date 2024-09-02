from abc import ABC, abstractmethod
import os
os.system("cls || clear")  # Limpar o terminal.

class Funcionario(ABC):
    # Construtor ---------------------------------------------------
    def __init__(self, nome: str, telefone: int, email:str, endereco:str, salario:str) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.salario = salario


    @abstractmethod  # Método abstrato
    def salario_final(self) -> float:
        pass

    class Endereço(Funcionario):
    def calcular_salario(self) -> float:
       logradouro: str
       numero: str
       complemento: str
       cep: str
       cidade: str
