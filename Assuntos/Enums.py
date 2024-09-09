import os
from enum import Enum
os.system("cls || clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"


class Pessoa:
    
    def __init__(self,nome: str, idade: int, sexo: Sexo) -> None:
        """Construtor."""
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __str__(self) -> str:
        '''Equivalente ao toString() do java'''
        return (f"\nNome: {self.nome}" f"\nIdade: {self.idade}" f"\nSexo{self.sexo}")
    
    # Instanciar classe Pessoa.
    pessoa_1 = Pessoa("Marta", 22, Sexo.FEMININO)

    print(pessoa_1)
#corrigir