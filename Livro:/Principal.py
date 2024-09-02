class Livro:
    def __init__(self, titulo, autor, num_paginas, preco):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        self.preco = preco

    def __str__(self):
        return (f"Título: {self.titulo}\n"
                f"Autor: {self.autor}\n"
                f"Número de Páginas: {self.num_paginas}\n"
                f"Preço: R${self.preco:.2f}")

def main():
    # Criando dois objetos Livro com as características fornecidas
    livro1 = Livro("O Alquimista", "Paulo Coelho", 208, 34.90)
    livro2 = Livro("A Guerra dos Tronos", "George R. R. Martin", 768, 89.90)

    # Exibindo os detalhes dos livros
    print("Detalhes do Livro 1:\n")
    print(livro1)
    
    print("\nDetalhes do Livro 2:\n")
    print(livro2)

if __name__ == "__main__":
    main()
