import pandas as pd


df = pd.read_csv('C:\\Users\\victo\\Documents\\GitHub\\Projeto-tratamento-de-dados\\Data_base\\movies_1980_2020_30k.csv', sep= ',')
#print(df.shape)
#print(df.head)

#linhas_vazias = df.isnull().all() #Check1 linhas vazias
#print(linhas_vazias)

#replicas = df.value_counts() # Check2 Linhas repetidas
#if replicas is True:
#    print('não há duplicadas')
#else:
#    print(replicas)
#    print("entrou aqui")
#
#print(replicas.shape)


print(df.count()) # check 3 Linhas NA