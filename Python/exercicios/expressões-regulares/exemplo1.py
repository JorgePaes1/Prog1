

import re  # usar esta importação para  expressoes regulares

# findall => encontra todas ocorrencias do padrão pesquisado no texto
# search => retorna o indice da primeira ocorrência encontrada no texto
# sub => substitui um valor dentro do texto
# compile => compila expressões regulares

string = "Este é um teste de expressões regulares é um teste de paciencia, mas este teste pode ser util."

# usa re.funcao(r"valor procurado", variavel)
print(re.search(r"teste", string))
# retorna uma expressão Match informando onde a palavra inicia e onde termina dentro da string

# usar re.funcao(r"valor procurado", variavel)
print(re.findall(r"teste", string))
# pesquisa a palavra teste na string e retorna uma lista com o resultado da expressão

# usar re.funcao(r"valor procurado", variavel)
print(re.sub(r"teste", "ABCD", string, count=2))
# cont substitui duas ocorrencias da palavra teste por ABCD na string informada na expressão


# Para evitar que o código seja compilado em todas as chamadas de expressão regular
# podemos criar uma unica expressão e usar o codigo compilado nas expressões seguintes

print("\nUsando Compile para otimizar o uso de expresssões")
regexp = re.compile(r"teste")
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub("DFG", string))
print(regexp.sub('DFG', string, count=2))
