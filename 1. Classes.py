import os

os.system("cls || clear")  # Limpar o terminal.

class Aluno:
    # Construtor.
    def __init__(self, nome: str, idade: int) -> None:
        # Atributos
        self.nome = nome
        self.idade = idade

    def exibir_dados(self) -> str:
            return f"Nome: {self.nome} \nIdade: {self.idade}"


# Instanciar a classe.
aluno = Aluno("Marta", 22)

# Imprimir os atributos.
print(f"Nome: {aluno.nome}")
print(f"Idade: {aluno.idade}")
print(aluno.exibir_dados())


    