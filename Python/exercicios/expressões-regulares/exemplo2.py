# Meta caractere: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com excensão de quebra linha)
# [] conjunto de carcteres

import re

texto = """
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo 5aria, a boa mineira que é, nunca esquece seu famoso
1aria de pão de queijo. 7aria.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
"""

# | (OU)
# seleciona João ou Maria na string texto, Expressão case sensitive
print(re.findall(r"João|Maria", texto))

# . (qualquer coisa) (comm exceção de quebra linha)
# seleciona palavras iniciadas em p e terminadas em o
print(re.findall(r"p.o", texto))

# [] (comjuntos de caracteres)
print(re.findall(r"[Jj]oão", texto))  # seleciona as palavras João e joão

# [] (conjunto de caracteres)
# seleciona intervalo de a ate z minusculo e A ate Z maiusculo
print(re.findall(r"[a-zA-Z]aria", texto))

# [] (conjunto de caracteres) e flag=re.I (I = Ignorecase)
# seleciona intervalo de a ate z minusculo e A ate Z maiusculo
print(re.findall(r"maria", texto, flags=re.IGNORECASE))
