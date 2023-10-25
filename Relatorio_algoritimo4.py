import pandas as pd

# Crie listas para armazenar as notas dos alunos
notas = {
    'Aluno': ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4', 'Aluno5'],
    'Nota1': [10, 8.5, 7.5, 9.5, 10],
    'Nota2': [9, 7.5, 8, 9, 9.5],
    'Nota3': [8.5, 9, 7, 8, 9],
    'Nota4': [9, 8, 8.5, 9, 8.5],
    'Nota5': [8.5, 9.5, 7, 8.5, 9],
}

# Crie um DataFrame a partir das listas
tabela_notas = pd.DataFrame(notas)

# Exiba a tabela
print(tabela_notas)