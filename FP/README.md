# Teoria - FP Exame

## LINKS 
>####Sala 3 : [Zoom](https://videoconf-colibri.zoom.us/j/81089901408?pwd=eGd6Zy80MjZuZkhXT0NhWUwyVGhJdz09)
>>####Bloco 1 : [Enunciado](https://www.hlt.inesc-id.pt/~alberto/fp/e1/parte1/ist198968.pdf)
>>####Bloco 2 : [Enunciado](https://www.hlt.inesc-id.pt/~alberto/fp/e1/parte2/ist198968.pdf)
>>####Bloco 3 : [Enunciado](https://www.hlt.inesc-id.pt/~alberto/fp/e1/parte3/ist198968.pdf)
### BNF
>1. *Simbolos nao terminais* : entre < >
>2. *Simbolos terminais*
>3. *Simbolo inicial*
>
>Regras de produção:
> - ' ::= ' -> define simb. ñ term.
> - ' | ' -> possiveis alternativas
> - ' + ' -> 1 ou mais repetições
> - ' *  ' -> 0 ou mais repetições
> - '{ }' -> simbolos opcionais

>*Mais info* : [Gramática de Pyhton 3](https://docs.python.org/3/reference/grammar.html)

### Algoritmia

#### *Algoritmo* : Um algoritmo é uma sequência finita de instruções bem definidas e não ambíguas cada uma das quais pode ser executada mecanicamente num período de tempo finito e com uma quantidade de esforço finito.
>1. Características de um algoritmo : rigoroso, eficaz e finito
>2. Relação algoritmo/ programa : um programa é um algoritmo escrito numa linguagem de programação 
>3. Relação processo/ programa : Um processo corresponde ao conjunto de ações tomadas por um computador durante a execução de um programa.

#### *Programa* : Algoritmo escrito numa linguagem de programação.
>Fases de Desenvolvimento de um Programa:
>>1. Análise do problema
>>2. Desenvolvimento da solução
>>3. Programação da solução
>>4. Testes
>>5. Manutenção

#### *Tipo de dados* : Um conjunto de elementos (as constantes do tipo), juntamente com um conjunto de
operações que se aplicam a esses elementos.

#### *Processo Computacional* : ente imaterial que existe no interior de um computador durante a execução de um programa, cuja evolução é ditada pelo proprio - define a execução do programa.

### F Strings
>#### Método str.format(), sintaxe:
>
	f'Hello, my name is {name} and I'm {years} old. 
>
>>##### Em que {name} e {years} sao variaveis 
>>##### *Mais info* : [F-strings](https://realpython.com/python-f-strings/)

### Maths 

#### *a % b* : resto da divisão de a por b
>##### EX : 35 % 10 = 5
#### *a // b* : divisão inteira de a por b
>##### EX : 35 // 10 = 3
#### *Obter divisores*
>i é divisor se a condição é verificada:
	num % i == 0 for i in range(1, num + 1)

### Elementos básicos de programação

>#### Dicionários:
>>*Não permitem* repetição de keys

>#### *Strings / Slicing* 
>>Inverter string:
>
	string[::-1]
>
>#### *Utilização de ciclos* :
> - For : Quando é conhecido o número de iterações 
>
> - While : Quando o número de iterações necessárias é desconhecido

### Iteração

#### *Processo iterativo* : caracterizado por x variáveis (variáveis de estado) juntamente com uma regra especifica de atualização das mesmas. As variáveis fornecem o estado da computação a cada momento.

### Recursão 

#### *Recursão linear* : chamada repetida da pópria função (expansão de memória) que cria operações adiadas até atingir o caso terminal.
#### *Recursão de cauda* : O cálculo é realizado antes da chamada recursiva, passando os resultados da etapa atual para a seguinte. A chamada recursiva é a última operação realizada pela função, não existindo operações adiadas.

### Funcionais sobre listas
>Modo de apresentação:
>
	reduce(function, lista>
	filter(predicado, lista)
	map(function, lista)

### Abstração

>#### *Abstração* : Consiste em ignorar certos aspectos de uma entidade, considerando apenas os aspectos relevantes.
>#### *Abstração Procedimental* : Consiste em considerar o que um programa *faz* e ignorar o modo *como o faz*.
>#### *Abstração de Dados* : Consiste em considerar as propriedades de um tipo de dados, ignorando o modo como este é representado.
>#### *Barreiras de Abstração* : Impedem qualquer acesso aos elementos do tipo que não seja feito através de operações básicas.

### Operações Básicas
>1. Construtores : cosntroem novos elementos do tipo
>>#####  *Nota* : À partida, são os únicos que verificam os argumentos 
>2. Seletores : permitem aceder aos constituintes dos elementos do tipo 
>3. Reconhecedores : identificam elementos do tipo
>4. Testes : efetuam comparações entre os elementos do tipo

### Métodos:
>*Objeto* : Uma entidade com estado interno (um conjunto de nomes), o qual só pode ser acedido
por um conjunto de operações definidas dentro do objeto (os métodos). 

>count() : atua sobre listas
>
>random() : gera um n entre 0 <= n < 1
>
>*Mais info* : [Functions](https://docs.python.org/pt-br/3/library/functions.html)

### Classes
>Metodo que visa obter 1 única representação do objeto:
>
	def __ repr__(self) 
 