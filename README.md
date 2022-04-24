# api-rest-mutantes-django
Detector de mutantes Magneto


- parámetro de entrada, un array de Strings que representan cada fila de una tabla de (NxN) con la secuencia del ADN. 
- Las letras de los Strings solo pueden ser: (A,T,C,G), las cuales representa cada base nitrogenada del ADN.
- Es mutante, si tiene más de una secuencia de cuatro letras iguales, de forma oblicua, horizontal o vertical.
 
POST → /mutant/
{ 
  “dna”:["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"] 
}

La collecion "Mutantes.postman_collection.json" esta configurada para importar desde postman y consumir el serevicio. 
Nota: Cambiar la url de Environment si se encuetra en ambiente local o situado en un servidor.
