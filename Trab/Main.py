from Graph import Graph


i = 1
while(i != 0):
    print('\nOpções: ( TOY.csv,  SJM.csv,  FFL.csv,  MDOP.csv )')
    escolha = input('Informe o arquivo (0 para sair ): ')
    if(escolha == '0'):
        print('Saindo...')
        break
    else:
        g1 = Graph(ListaDe_Adjacencia=[], ListaDe_Vertices=[])
        g1.read_file("Datasets/"+escolha)
        g1.add_Aresta()
        g1.Ordenar_ListaDe_Adjacencia()
        aux = g1.Caminho_Critico()
        print('\nProcessando...')
        print('\nCaminho Crítico:')
        for i in range(len(aux[2])):
            print('-',aux[2][i])
        print('\nTempo Mínimo: ', end="")
        print(aux[0])