# Simulador Universal de Autômatos Finitos

## Objetivo

Este programa aceita a especificação de um autômato (podendo ser um determinístico ou não determinístico) e a partir daí para uma dada lista de cadeias dizer se o autômato aceita ou não esta cadeia à linguagem reconhecida pelo autômato.

# Método

Para validar se uma cadeia é processável pelo autômato finito de entrada ele é mapeado como uma autômato finito não determinístico (AFN), depois cria-se um autômato finito determinístico (AFD) equivalente e por fim processa a cadeia no AFD equivalente.

# Interações

## Entrada

- Linha (1): número de estados: para o conjunto de estados ![alt text][q_mai], assume-se os nomes dos estados de ![alt text][q_0] a ![alt text][q_n_-_1] , onde n é o número de estados (Obs.: ![alt text][q_0] é o estado inicial, quando houver um único estado inicial (AFD)). Assuma 1 ≤ n ≤ 10;

- Linha (2): o conjunto de sı́mbolos terminais (Σ): entrar com a quantidade de sı́mbolos terminais seguida dos elementos separados por espaço simples. Assume-se tamanho máximo igual a 10;

- Linha (3): o número de estados iniciais (se for AFD, é igual a 1: ![alt text][q_0] ; se for AFN, usa-se ![alt text][q_0] , ![alt text][q_1] , etc. para os estados iniciais). Assume-se tamanho máximo igual a 10;

- Linha (4): o conjunto de estados de aceitação (F): entrar com a quantidade de estados de aceitação seguida dos elementos separados por espaços. Lembre-se de entrar apenas com os números de 0 a 9;

- Linha (5): o número de transições (δ) da máquina (máximo de 50).

- Linha (a partir da 6) : as transições: entra-se com um δ em cada linha, com os elementos separados por espaço: ![alt text][q_min] x ![alt text][q_0] , onde ![alt text][q_min], ![alt text][q_0] ∈ ![alt text][q_mai], x ∈ Σ ∪ {λ}. Represente a cadeia vazia (λ) como “-”. 

- Linha (depois das transições): entrar com o número de cadeias de entrada (máximo de 10).

- Próximas Linhas: cadeias de entrada: entrar com uma em cada linha. Comprimento máximo de cada cadeia = 20 sı́mbolos.

## Saída

A partir da primeira linha a informação sobre a aceitação ou não da respectiva cadeia de entrada, na ordem do arquivo de entrada. Se a cadeia de entrada pertencer à linguagem reconhecida pelo autômato, a cadeia de saı́da será `aceita`. Caso a cadeia de entrada não pertença à linguagem reconhecida pelo autômato, a cadeia de saı́da será `rejeita`.

## Exemplo

**Entrada**

```
3
2 a b
1
1 2
6
0 a 1
0 b 1
1 a 1
1 b 2
2 a 0
2 b 2
10
abbbba
aabbbb
bbabbabbabbb
bbbbbbbbbbb
-
abababababab
bbbbaabbbb
abba
a
aaa
```

**Saída**

```
rejeita
aceita
aceita
aceita
rejeita
rejeita
aceita
rejeita
rejeita
rejeita
```


## Referências:

https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton
https://en.wikipedia.org/wiki/Deterministic_finite_automaton

[q_min]: ./images/q_min.gif "Q"
[q_mai]: ./images/q_mai.gif "q"
[qlinha]: ./images/qlinha.gif "q linha"
[q_0]: ./images/q_0.gif "q de 0"
[q_1]: ./images/q_1.gif "q de 1"
[q_n_-_1]: ./images/q_n_-_1.gif "q de 1"