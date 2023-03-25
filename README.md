# student-entries-generator
program to insert random student entries on mongodb and update redis


Criei funções para gerar cpfs válidos, um ano de 2000 a 2023.
Baixei arquivos CSV com dados de nomes e cursos e atribuí o valor aleatóriamente toda vez que um objeto estudante era instanciado.
Fiz uma função que organiza os atributos do objeto estudante em um json para ser inserido no mongo.
Deixei a string de conexão com mongoDB num arquivo separado para não deixar exposto no repo de versionamento.
Foram inseridos 5000 arquivos no mongo na primeira vez que rodei o programa, mas para fim de testes removi a ordem 
de inserção fixa para um input de usuário.
Assim que é terminada a inserção no mongo, removo todas as entries existentes no redis e insiro a collection atual.
