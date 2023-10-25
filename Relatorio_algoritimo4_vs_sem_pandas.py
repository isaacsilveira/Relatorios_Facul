# Defina listas para armazenar as notas dos alunos
alunos = ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4', 'Aluno5']
nota1 = [10, 8.5, 7.5, 9.5, 10]
nota2 = [9, 7.5, 8, 9, 9.5]
nota3 = [8.5, 9, 7, 8, 9]
nota4 = [9, 8, 8.5, 9, 8.5]
nota5 = [8.5, 9.5, 7, 8.5, 9]

# Crie uma tabela exibindo as notas dos alunos
print("Aluno\tNota1\tNota2\tNota3\tNota4\tNota5")
for i in range(len(alunos)):
    print(f"{alunos[i]}\t{nota1[i]}\t{nota2[i]}\t{nota3[i]}\t{nota4[i]}\t{nota5[i]}")