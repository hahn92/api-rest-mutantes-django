from django.shortcuts import render

# Create your views here.




def isMutant(dna):
  """
  Función que recibe un arreglo n*n de ADN y devuelve True si la cadena contiene mas de 4 letras consecutivas, verticalmente, horizontalmente o en diagonal
  """
  #Se recorre el arreglo
  longitud = len(dna)
  #print(longitud)
  for i in range(longitud):
    for j in range(len(dna[i])):
      #Se verifica si hay 4 letras consecutivas en vertical
      if j+3 < len(dna[i]):
        if dna[i][j] == dna[i][j+1] and dna[i][j] == dna[i][j+2] and dna[i][j] == dna[i][j+3]:
          #print(dna[i][j] + dna[i][j+1] + dna[i][j+2] + dna[i][j+3])
          return True
      #Se verifica si hay 4 letras consecutivas en horizontal
      if i+3 < len(dna):
        if dna[i][j] == dna[i+1][j] and dna[i][j] == dna[i+2][j] and dna[i][j] == dna[i+3][j]:
          #print(dna[i][j] + dna[i+1][j] + dna[i+2][j] + dna[i+3][j])
          return True
      #Se verifica si hay 4 letras consecutivas en diagonal
      if i+3 < len(dna) and j+3 < len(dna[i]):
        if dna[i][j] == dna[i+1][j+1] and dna[i][j] == dna[i+2][j+2] and dna[i][j] == dna[i+3][j+3]:
          #print(dna[i][j] + dna[i+1][j+1] + dna[i+2][j+2] + dna[i+3][j+3])
          return True
      if i-3 >= 0 and j+3 < len(dna[i]):
        if dna[i][j] == dna[i-1][j+1] and dna[i][j] == dna[i-2][j+2] and dna[i][j] == dna[i-3][j+3]:
          #print(dna[i][j] + dna[i-1][j+1] + dna[i-2][j+2] + dna[i-3][j+3])
          return True
  return False

#dna = ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]

#print(isMutant(dna))
