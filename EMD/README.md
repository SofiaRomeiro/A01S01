# EMD

### Múltiplos e Divisores
>##### Multiplo: a é multiplo de b:
>
	a = k . b (k é inteiro)
>

### Equações Diofantinas
>##### Uma equação diofantina:
>> 1. tem os coeficientes e os termos independentes pertencentes a Z
>> 2. tem como solução para as variáveis x e y valores em Z
>> 3. é do tipo ax + by = c em que os coeficientes (a e b) e o termo independente (c) pertencem a Z



### Grafos
>##### Constituidos por nº finito de *vértices* e *arestas*
>##### Um grafo G é um par G = (V,A) onde
>>- V - conjunto finito de vértices/ nós
>>- A - conjunto finito de arestas
>##### em que cada aresta une dois nós e 
>>- nenhuma aresta o une um nó a si próprio
>>- há no máximo 1 aresta a unir dois nós
>
>#### Teoremas
>##### *Definição*: O grau de um vértice é o nº de arestas nele incidentes
>##### *1º Teorema*: A soma dos graus dos nós de um grafo é o dobro do número de arestas => número par
>>##### *Justificação*: cada aresta é contada 2 vezes  

### Algoritmo de Dijkstra
>##### Riscar da tabela apenas os vértices 'percorridos'
>##### Escrever pela ordem que vão aparecendo na 'progressao' do exercicio
>##### Indicar a ordem pela qual as arestas foram riscadas 
>##### Custo da trajetória: custo acumulado do percurso até à aresta final
>##### Indicação da trajetória: < V,V,V,V > 
>##### Como responder:
>> 1. Assinalar a traço mais grosso / cor diferentes as arestas selecionadas pelo algoritmo
>> 2. Indicar os custos de Dijkstra nos vértices
>> 3. Assinalar na tabela auxiliar a ordem pela qual as arestas vão sendo eliminadas
>> 4. Parar assim que o vertice final é atingido

### Algoritmo de Ford-Fulkerson
>##### Uma rede s-t capacitada é uma rede orientada conexa, com setas associadas a nº naturais (*capacidade da seta*)
>>##### s : vértice *source* que não é destino de nenhuma seta
>>##### t : vertice *target* que não é origem de nenhuma seta 
>##### *Fluxo de rede*: associa a cada seta um valor de fluxo menor ou igual à capacidade máxima dessa seta
>##### *Valor do fluxo da rede capacitada*: soma dos fluxos das setas com origem em *s*
>##### *Fluxo máximo numa rede capacitada*: é um fluxo f cujo valor é maior ou igual que o valor de qualquer outro fluxo nessa rede (setas que apontam para t)
>##### Como responder:
>> 1. Todas as setas começam com fluxo 0
>> 2. O fluxo pode aumentar até ao máximo dessa seta 
>> 3. O fluxo pode diminuir até 0
>> 4. Capacidade residual:
