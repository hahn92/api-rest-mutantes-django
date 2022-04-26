from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import status

# Serializer
from .serializers import MutantSerializer

# Models
from .models import Mutant

# Create your views here.

@api_view(['POST'])
def Validador(request):
  """
  Recibe una cadena de ADN y valida si es o no una secuencia mutante.
  """
  if request.method == 'POST':
    dataJ = JSONParser().parse(request)  
    dna = dataJ['dna']  
    if isMutant(dna):
      saveDNA(dna, True)
      return JsonResponse({}, status=status.HTTP_200_OK)
    else:
      saveDNA(dna, False)
      return JsonResponse({}, status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def Estadisticas(request):
  """
  consulta las estadisticas de la base de datos de mutantes
  """
  if request.method == 'POST':
    count_mutant_dna = Mutant.objects.filter(is_mutant=True).count()
    count_human_dna = Mutant.objects.filter(is_mutant=False).count()
    ratio = (100 *  count_mutant_dna ) / (count_human_dna + count_mutant_dna)
    return JsonResponse({
        "count_mutant_dna": count_mutant_dna, "count_human_dna": count_human_dna, "ratio": "{:.2f}%".format(ratio)}, 
        status=status.HTTP_200_OK
    )


def saveDNA(dna, state):
  data = {}
  data['dna'] = "{}".format(dna)
  data['is_mutant'] = state
  es_valido = True
  for i in range(len(dna)):
    for j in range(len(dna[i])):
      if dna[i][j] == "A" or dna[i][j] == "T" or dna[i][j] == "C" or dna[i][j] == "G":
        pass
      else:
        es_valido = False
    
  if es_valido:
    serializer = MutantSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
    else:
      print(serializer.errors)
  else:
    print("El dna no es valido")
     

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
