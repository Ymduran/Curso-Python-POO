Codewars es una plataforma online de práctica de programación donde los usuarios resuelven desafíos (llamados "katas") en varios lenguajes de programación. Sirve para mejorar habilidades de programación, practicar diferentes algoritmos, aprender de otros usuarios y demostrar tus conocimientos a posibles empleadores. 
En detalle:

    Plataforma de práctica:
    Codewars ofrece una amplia variedad de katas, que van desde ejercicios básicos hasta desafíos más complejos. 

Mejora de habilidades:
Al resolver katas, los usuarios practican la resolución de problemas, la aplicación de algoritmos y la optimización del código. 
Aprender de otros:
Codewars permite ver las soluciones de otros usuarios, incluyendo las más populares y "inteligentes", lo que facilita el aprendizaje de diferentes enfoques y técnicas de programación. 
Demostrar conocimientos:
La plataforma permite a los usuarios demostrar sus habilidades a través de su perfil y los logros obtenidos, lo que puede ser útil para buscar trabajo. 
Sistema de rangos y honor:
Codewars utiliza un sistema de rangos y honor que motiva a los usuarios a resolver más katas y mejorar sus habilidades. 
Comunidad:
Codewars cuenta con una comunidad activa de desarrolladores que comparten conocimientos y ofrecen ayuda mutua. 


Notas: 
- Existen formas de reducir las líneas de código, cuando a una sentencia solo correspone una instrucción, entonces se puede escribir en la misma línea.
- Raise – Se usa para crear excepciones, qué hacer cuando ocurre una excepción, igual que ‘except y ‘try’.
- Try – Se usa para crear excepciones, qué hacer cuando ocurre una excepción, igual que ‘raise’ y ‘except.
- Pertenencia e Identidad: in, is

El uso de in nos permite saber si un determinado elemento está en una clase iterable, devolviendo True en el caso de que sea cierto.

lista = ["a", "b", "c"]
print("a" in lista)
- Se puede recorrer una lista comparando elemento por elemento para contar secuencias específicas.
  Notas:

- El método `zfill(n)` convierte una cadena rellenándola con ceros a la izquierda hasta tener longitud `n`.
  Ejemplo: "7".zfill(3) => "007"
- Para combinar texto y valores, se puede usar una f-string: f"Texto {variable}"
- También se puede hacer con formato clásico: "Value is {:05d}".format(valor), aunque en este caso se prefiere claridad.
- zfill solo funciona con strings, por eso primero convertimos el número con str().
- Este tipo de formato es muy usado cuando se manejan códigos, identificadores, tiempos o fechas.

