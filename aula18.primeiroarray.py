import numpy as np

dados_vendas = np.array([12,15,17,20,22,25,28,30,35,150])

print (dados_vendas)

#calculando a media (sensivel a extremos)

media_vendas = np.mean(dados_vendas)

#calculando a mediana (robusta a extremos)

mediana_vendas = np.median(dados_vendas)


print(media_vendas)
print(mediana_vendas)

#---------------------------------------------------------------------#

#dados de exemplo

dados = np.array([12,15,17,20,22,25,28,30,35,40])

#calculando os quartis

Q1 = np.percentile(dados, 25)
Q2 = np.percentile(dados, 50)
Q3 = np.percentile(dados, 75)

print("\n")
print (Q1)
print(Q2)
print(Q3)


#-----------------------------------------------------------------------#

i = Q3 - Q1
Limite_inferior = Q1 - 1.5 * i

Limite_max = Q3 + 1.5 * i

outliers = dados[(dados < Limite_inferior) | (dados > Limite_max)]

dentro = dados[(dados >= Limite_inferior) & (dados <= Limite_max)]
bigode_inf = dentro.min()
bigode_sup = dentro.max()

print("Limite inferior: \n")
print(Limite_inferior)
print("\nLimite Superior: \n")
print(Limite_max)
print("\nOutliers: \n")
print(outliers)
print("\nBigode inferior: \n")
print(bigode_inf)
print("\nBigode superior: \n")
print(bigode_sup)