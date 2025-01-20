import os
# Complete the solve function below.
def solve(s):
    result = ""
    for word in s.split(" "):  # Preserva espaços extras
        if word:  # Capitaliza somente palavras não vazias
            result += word.capitalize()
        result += " "  # Adiciona o espaço novamente
    return result.rstrip()  # Remove o último espaço extra

# Exemplo de uso
full_name = input("Enter a full name: ")
capitalized_name = solve(full_name)

print(capitalized_name)