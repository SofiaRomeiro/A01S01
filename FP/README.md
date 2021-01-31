# Teoria - FP Exame

### BNF
>1. *Simbolos nao terminais* : entre < >
>2. *Simbolos terminais*
>3. *Simbolo inicial*
>Regras de produção:
>>1. ::= -> define simb. ñ term.
>>2. | -> possiveis alternativas
>>3. + -> 1 ou mais repetições
>>4. * -> 0 ou mais repetições
>>5. {} -> simbolos opcionais
>[Gramática de Pyhton 3](https://docs.python.org/3/reference/grammar.html)

### Algoritmia

##### *Algoritmo*: Um algoritmo é uma sequência finita de instruções bem definidas e não ambíguas cada uma das quais pode ser executada mecanicamente num período de tempo finito e com uma quantidade de esforço finito.
>1. Características de um algoritmo : rigoroso, eficaz e finito
>2. Relação algoritmo - programa : um programa é um algoritmo escrito numa linguagem de programação 
>3. Relação processo - programa : Um processo corresponde ao conjunto de ações tomadas por um computador durante a execução de um programa.

##### *Programa*: Algoritmo escrito numa linguagem de programação.
>Fases de Desenvolvimento de um Programa:
>>1. Análise do problema
>>2. Desenvolvimento da solução
>>3. Programação da solução
>>4. Testes
>>5. Manutenção

##### *Processo Computacional*: ente imaterial que existe no interior de um computador durante a execução de um programa, cuja evolução é ditada pelo proprio - define a execução do programa.

### Abstração

>##### *Abstração* : Consiste em ignorar certos aspectos de uma entidade, considerando apenas os aspectos relevantes.
>##### *Abstração Procedimental* : Consiste em considerar o que um programa faz e ignorar o modo como o faz.
>##### *Abstração de Dados* : Consiste em considerar as propriedades de um tipo de dados, ignorando o modo como este é representado.
>##### *Barreiras de Abstração* : Impedem qualquer acesso aos elementos do tipo que não seja feito através de operações básicas.

### Maths 

##### *a % b* : resto da divisão de a por b
>EX : 35 % 10 = 5
##### *a // b* : divisão inteira de a por b
>EX : 35 // 10 = 3
##### *Obter divisores*
	num % i == 0 for i in range(1, num + 1)
>i é divisor se a condição é verificada

### Iteração

##### *Processo iterativo* : caracterizado por x variáveis (variáveis de estado) juntamente com uma regra especifica de atualização das mesmas. As variáveis fornecem o estado da computação a cada momento.

### Recursão 

##### *Recursão linear* : chamada repetida da pópria função (expansão de memória) que cria operações adiadas até atingir o caso terminal.
##### *Recursão de cauda* : O cálculo é realizado antes da chamada recursiva, passando os resultados da etapa atual para a seguinte. A chamada recursiva é a última operação realizada pela função, __não existindo operações adiadas__ .

### Operações Básicas
>1. Construtores : cosntroem novos elementos do tipo
>>*Nota* : À partida, são os únicos que verificam os argumentos 
>2. Seletores : permitem aceder aos constituintes dos elementos do tipo 
>3. Reconhecedores : identificam elementos do tipo
>4. Testes : efetuam comparações entre os elementos do tipo



### Funções Embutidas e Métodos:
>count() : atua sobre listas
>random() : gera um n entre 0 <= n < 1
>*Mais info* : [Functions](https://docs.python.org/pt-br/3/library/functions.html)


### Elementos básicos de programação

>##### *Strings / Slicing* 
>>Inverter string : [::-1]

>##### *Utilização de ciclos* :
>>For : Quando é conhecido o número de iterações 

>>While : Quando o número de iterações necessárias é desconhecido

### Classes
>__repr__ : metodo que visa obter 1 única representação do objeto
 