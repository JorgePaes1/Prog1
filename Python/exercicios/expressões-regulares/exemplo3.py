# Meta caracteres: ^  $  ()
# *  0 ou n - existe 0 ou n vezes
# +  1 ou n - existe 1 ou n vezes
# ?  0 ou 1 - existe 0 ou 1 vezez
# {n}  - uma quantidade em especifido
# {5, 10,} permite entre 5 e 10 o
# {10,} permite 10 ou mais caracteres
# {, 10} - até 10 caracteres
# {10} apenas 10, valores a mais ou menos serão descartados
# {min, max} - um valor minimo e um maximo
# ()+  [a-\-zA-Z0-9]+  - literal é aplicado a todo conjunto entre parenteses ou colchetes

import re

texto = """
João trouxe flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo 5aria, a boa mineira que é, nunca esquece seu famoso
1aria de pão de queijo. 7aria.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeeeeeeeeem, veeeeeeeeemm, veeeeeeeeeeeeeemmm"!
"""

# [] (conjunto de caracteres) e flag=re.I (I = Ignorecase)
# seleciona intervalo de a ate z minusculo e A ate Z maiusculo
# procura a palavra  joão no texto, o primeiro caracter o possui um ou muitos (+)
print(re.findall(r"jo+ão", texto, flags=re.IGNORECASE))

# [] (conjunto de caracteres) e flag=re.I (I = Ignorecase)
# procura a palavra joão no texto, o primeiro 1º e o 2º caracter "o" possuem literal um ou muitos (+)
print(re.findall(r"jo+ão+", texto, flags=re.IGNORECASE))
