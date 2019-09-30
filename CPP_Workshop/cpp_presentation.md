class: center, middle

# Workshop C++
### NIAEFEUP

---

# Links importantes

- Apresentação: https://niaefeup-workshop-cpp.netlify.com/
- [Exercícios](https://github.com/NIAEFEUP/Workshop_CPP/)
- [OnlineGDB](https://www.onlinegdb.com/online_c++_compiler)

---

# Overview

1. O que é o C++?
2. Hello world!
3. Tipos de dados
4. Variáveis
5. Constantes
6. Operadores
7. Condições
8. Ciclos
9. Vetores
10. Funções
11. Streams

---

# O que é o C++?
- Criado por Bjarne Stroustrup
- Extensão da linguagem C - 99% retrocompatível
- Disponível em praticamente todos os computadores
- Suporta programação orientada a objetos
- Usada para definir precisamente uma sequência de operações que o computador tem 
que executar para realizar uma determinada tarefa
- Extremamente eficiente (quando bem utilizada...)
- Versátil e muito poderosa, mas exige responsabilidade (memory leaks, dangling pointers...)

![Bjarne Stroustrup](img/bjarne.jpg)

---

# Hello world!
```C++
// helloworld.cpp
#include <iostream>

using namespace std;

int main() {
  cout << "Hello world!" << endl;
  return 0;
}
```

---

# Exercícios

**E1.** A função `main` é o ponto de entrada do programa. Comprova a afirmação, copiando o código [neste ficheiro](https://raw.githubusercontent.com/NIAEFEUP/Workshop_CPP/master/introdutory%20exercises/explainMain.cpp) e correndo-o no onlinegdb.

**SC1.** Começa o desenvolvimento do programa MyShoppingCart por adicionar uma mensagem de boas-vindas ao utilizador. Para isso, copia o código [neste ficheiro](https://raw.githubusercontent.com/NIAEFEUP/Workshop_CPP/master/shopping-cart/MyShoppingCart.cpp) e cola-o no onlinegdb. Trabalharás com este ficheiro até ao final do workshop!

Exemplo do programa em execução:
![sc1](https://i.imgur.com/dBVjJKl.png)

---

# Solução


```cpp
int main()
{
    // ...
     
    vector<double> prices;

    cout << "Bem-vindo ao MyShoppingCart!" << endl;
    
    // ...
}
```

---

# Tipos de dados
- char - caracteres alfanuméricos (ex: 'c', '8', '$');
- int - números inteiros (ex: 103, -2)
- float - números com vírgula flutuante de precisão simples (ex: 1.902, -5,926563840)
- double - números com vírgula flutuante de precisão dupla (ex: 1.2, -4.587)  
- bool - verdadeiro ou falso (ex: true, false)
- void - significa "sem qualquer valor". É usado quando uma função não retorna nenhum 
valor

---

# Tipos de dados
## Modificadores de tipos de dados
- signed - para números com sinal
- unsigned - para números sem sinal
- short - valor otimizado para o espaço com comprimento de pelo menos 16 bits
- long - valor otimizado para precisão com comprimento de pelo menos 32 bits
- long long - valor otimizado para precisão com comprimento de pelo menos 64 bits

```C++

int main() {
  unsigned int i = 5;
  int y = 3; // Quando omisso o modificador, é assumido que o valor é signed
  long float z = 9;
  long long double d = 37.2387193;
  char x = 'r';
  int i = 0;
  float y = 1.3;
  double z = 4.586
  bool b = true;

  return 0;
}
```
---
# Variáveis
São contentores capazes de armazenar valores de um determinado tipo

## Como as declarar?
```C++
int myNumber = 15;
bool myBoolean = true;
```
## Tipos de variáveis
- Globais - declarar fora de qualquer função
- Locais - declarar dentro de uma função específica (ex. main)

### NOTAS:
- Podem existir variáveis locais com o mesmo nome e diferentes valores ao mesmo tempo, 
desde que sejam locais e estejam dentro de funções diferentes cada uma 
- Não têm que ser inicializadas ao mesmo tempo que são declaradas

---

# Constantes
Semelhantes a variáveis, mas o seu conteúdo não pode ser alterado após a sua inicialização. 
Podem ser locais ou globais.

```C++
#include <iostream>

using namespace std;

int main() {
  int variable;
  const char constant = 'T';

  variable = 5;
  constant = 3; // IMPOSSÍVEL: seria gerado um erro durante a compilação!
  cout << variable << " " << constant << endl;

  return 0;
}
```

---

# Operadores
## Operadores de igualdade
- **==** verdadeiro se ambos os operandos forem iguais
- **!=** verdadeiro se ambos os operandos forem diferentes
- **>** verdadeiro se operando da esquerda for maior que o da direita
- **<** verdadeiro se operando da esquerda for menor que o da direita
- **>=** verdadeiro se operando da esquerda for maior ou igual que o da direita
- **<=** verdadeiro se operando da esquerda for menor ou igual que o da direita

---
# Operadores
## Operadores Aritméticos
- **+** adição
- **-** subtração
- ***** multiplicação
- **/** divisão
- **%** módulo
- **++** incremento de 1 unidade
- **--** decremento de 1 unidade

## Operadores lógicos
- **&&** E lógico
- **||** OU lógico 
- **!** NÃO lógico (negação)

---

# Operadores
## Alguns operadores de atribuição
- **=** operando da esquerda fica com o valor do da direita
- **+=** operando da esquerda fica com o valor do da direita somado com o seu próprio valor
- **-=** operando da esquerda fica com o valor do da direita subtraído com o seu próprio valor
- ***=** operando da esquerda fica com o valor do da direita multiplicado com o seu próprio valor
- **/=** operando da esquerda fica com o valor do da direita dividido com o seu próprio valor

---


# Operadores
## IO
### Output
De maneira a ser possível enviar informação para o utilizador, é comum imprimir 
mensagens no ecrã do computador. Para isso, e como foi possível ver no slide 
anterior, utiliza-se o objeto **cout** seguido do operador **<<** para 
transmitir informação para o ecrã do utilizador.

```C++
cout << "Bom dia " << nome_do_aluno << "!" << endl;
cout << "Tudo bem contigo?" << endl;
```

--- 

```Bash
// Assuma-se que o conteúdo da variável nome_do_aluno é Inês.
Bom dia Inês!
Tudo bem?
```

NOTA: A partícula **endl** permite mover o cursor para a linha seguinte, entre diferentes 
utilizações do objeto **cout**. Caso não estivesse presente, o resultado seria o 
seguinte:
```Bash
Bom dia Inês!Tudo bem?
```

---
# Operadores
### Input 
De maneira similar, é possível transmitir informações do utilizador para o programa.
Para isso usa-se a stream **cin** e o operador **>>**. Após o operador, coloca-se 
a variável aonde vai ser guardada a informação.

--- 

A stream **cin** permite obter informação de qualquer tipo de dados (exceto tipos 
definidos pelo utilizador, a não ser que o operador >> tenha sido overloaded).

Note-se que também existe a função getline(), que permite obter informação apenas 
sob a forma de strings. A vantagem relativamente ao **cin** é que esta função permite 
receber strings com o caracter espaço ' ' (a string *acaba* apenas quando o caracter '\n' 
é encontrado). Por outro lado, o **cin** utiliza qualquer espaço em branco como 
delimitador (o que inclui espaços, newlines, tabs, etc.).

---
# Operadores
```C++
#include <iostream>
  
using namespace std;
    
// Um mau uso da stream cin

int main() {
    string name;
    cout << "Insert your name here: ";
    cin >> name;
    cout << "Your name is " << name << endl;
    
    return 0;
}     
```

--- 

```Bash
Insert your name here: Rui Alves
Your name is Rui
```

--- 

Repare-se que o nome inserido difere do recebido pelo programa!
Mais à frente veremos o porquê de isto acontecer, e perceberemos melhor o 
funcionamento da stream **cin**.

---

# Exercícios


**E2.** Vamos agora tentar perceber como fazer operações aritméticas. Está atento ao quadro e, se quiseres, reproduz no teu onlinegdb!

**E3.** Vamos experimentar com variáveis. Copia o código [neste ficheiro](https://raw.githubusercontent.com/NIAEFEUP/Workshop_CPP/master/introdutory%20exercises/IOops.cpp) e corre o programa. Completa-o, de forma a também perguntar a idade e imprimi-la de seguida.

**SC2.** Melhora a mensagem de boas vindas de forma a pedir o nome do utilizador e cumprimentá-lo. Atenção aos nomes que contêm espaços. Por exemplo, se o utilizador responder com “Pedro Fernandes”, o programa deve responder “Olá Pedro Fernandes!” e não “Olá Pedro!”.

Exemplo do programa em execução:
![sc2](https://i.imgur.com/GRj1w07.png)

---

# Solução


```cpp
int main()
{
    // ...
    vector<double> prices;
    string name;

    cout << "Bem-vindo ao MyShoppingCart!" << endl;
    cout << "Qual é o teu nome? ";
    getline(cin, name);
    cout << "Olá " << name << "!" << endl;
    
    // ...
}
```

---

# Condições
## Declarações *If*
```C++
if (price < 0)
  return -1;
else if (price == 0)
  return 0;
else
  return 1;
```

```C++
if (cond_variable == true)    // equivalente a if (cond_variable)
  return 0;
```

```C++
if (smart && !lazy)
  return true;
```

---
# Condições
## Declarações *Switch-Case*
Ideail para substituírem declarações *if* muito longas que 
comparam uma variável com vários **valores inteiros** 
```C++
switch (choice) {
  case 1: 
    cout << "First item selected!" << endl;
    break;
  case 2:
    cout << "Second item selected!" << endl;
    break;
  default:
    cout << "Invalid selection :(" << endl;
    break;
}
```
Na ausência do *break*, as outras condições *case* serão executadas 

---

# Exercícios

**E4.** Vamos tentar perceber o funcionamento de programas com `if`. Copia o código [neste ficheiro](https://raw.githubusercontent.com/NIAEFEUP/Workshop_CPP/master/introdutory%20exercises/ControlFlow.cpp) e corre-o no onlinegdb.

**SC3.** Descomenta (removendo as barras) a linha com o conteúdo `printAndChooseOption(option, listItems, prices);`. Se correres o programa, reparas que aparece uma lista das opções disponíveis, e é pedido ao utilizador para escolher uma delas. Melhora o programa de forma a que, quando o utilizador coloca uma opção não existente (ex: -1), seja imprimida uma mensagem a assinalar o erro.

Exemplo do programa em execução:

![sc3](https://i.imgur.com/Yo9oOsI.png)

---

# Solução


```cpp
void printAndChooseOption(int &option, vector<string> &cartItems, vector<double> &prices)
{
    // ...
    
    switch (option)
    {
        // ...
        default:
           cout << "Opção não existente!" << endl;
           break;
    }
    
    // ...
}
```

---

# Ciclos
## While loop 
```C++
while (x < 5)
  cout << x << " is less than 5" << endl;
```

## Do-while loop
```C++
do {
  cout << x << " is less than 5" << endl;
}
while (x < 5);
```
---
# Ciclos
## For loop
```C++
for (unsigned int i = 0; i < 10; i++) {
    int y = i*2;
    cout << y << endl;
}
```

É possível encadear ciclos. Útil para percorrer elementos de matrizes, por exemplo

```C++
#include <iostream>
#include <vector>

using namespace std;

int main() {

  for (unsigned int i = 0; i < 5; i++) {
   for (unsigned int j = 0; j < 5; j++) {
     cout << "Linha " << i << " Coluna " << j << endl;
   }
  }
  
  return 0;
}
```

---

# Exercícios

**E5.** De forma a perceber melhor como ciclos funcionam, copia o código [neste ficheiro](https://raw.githubusercontent.com/NIAEFEUP/Workshop_CPP/master/introdutory%20exercises/Looping.cpp) e coloca-o no onlinegdb.

**SC4.** Melhora o programa de forma a que seja possível continuar a fazer operações enquanto o utilizador assim quiser. Ou seja, como na lista de opções, a opção 0 é a responsável por terminar o programa, este deve continuar enquanto essa opção não for escolhida.
Exemplo do programa em execução:
![sc4](https://i.imgur.com/s7oiTrF.png)

---

# Solução

```cpp
int main()
{
    // ...
    
    cout << "Olá " << name << "!" << endl;

    while (option != 0)
        printAndChooseOption(option, cartItems, prices);

    return 0;
}
```

---

# Vetores
- Estrutura de dados linear com a capacidade de armazenar vários valores de um
determinado tipo. Pode alterar o seu tamanho automaticamente sempre que um elemento 
novo é inserido ou apagado
- São alocados contíguamente na memória, podendo por isso ser acessados através de iteradores
- Os dados são sempre inseridos no final do vetor

## Notas importantes
- Os índices de um vetor iniciam-se sempre no zero. Ou seja, o primeiro elemento de um vetor 
está na posição 0, o segundo elemento na posição 1, etc.
- é possível consultar o conteúdo de um vetor numa determinada posição utilizando parêntesis 
retos [] ou o método .at(); 

---
```C++
#include <iostream>
#include <vector>
    
using namespace std;
    
int main() {
    vector<int> numbers {10, 20, 30}; // inicialização do vetor com 3 elementos
    int size;

    numbers.push_back(40); // adição do valor 40 ao fim do vetor
    numbers.pop_back(); // remove o último valor do vetor (40)

    size = numbers.size();
    
    cout << "Vector size = " << size << endl;
    cout << "Vector elements:";
    for (unsigned int i = 0; i != numbers.size(); i++)
        cout << " " << numbers.at(i); // equivalente a numbers[i]
    cout << endl;
    
    numbers.erase(numbers.begin() + 1); // elimina o segundo elemento do vetor
    
    // EVITAR FAZER O SEGUINTE:
    // Nas próximas linhas de código, estamos a repetir código de maneira a 
    // podermos voltar a imprimir o tamanho e conteúdo do vetor!
    cout << "Vector size = " << size << endl;
    cout << "Vector elements:";
    for (unsigned int i = 0; i != numbers.size(); i++)
        cout << " " << numbers.at(i);
    cout << endl;

    return 0;
}                                                                         
```
---

```Bash
Vector size = 3
Vector elements: 10 20 30
Vector size = 3
Vector elements: 10 30
```

--- 

Atente-se no uso da função erase() para eliminar um elemento de um vetor:
```C++
numbers.erase(numbers.begin() + 1);
```
A função elimina o elemento que se encontrar na posição que estiver a 1 unidade 
do início do vetor (numbers.begin()). Sendo que o primeiro elemento é o número 
10, e que este se encontra na posição 0, a posição a elminar será a que estiver 
à distância 0 + 1 = 1 do início do vetor, ou seja, o elemento 20.

--- 

É também de realçar a repetição do código de impressão do tamanho e conteúdo do vetor!
```C++
cout << "Vector size = " << size << endl;
cout << "Vector elements:";
for (unsigned int i = 0; i != numbers.size(); i++)
    cout << " " << numbers.at(i); // equivalente a numbers[i]
cout << endl;
```

Haverá alguma maneira de evitar esta situação?

---

# Exercícios

**SC5.** Implementa a funcionalidade de adicionar um item, juntamente com o seu preço, ao carrinho. O programa deve pedir ao utilizador o nome do produto, o seu preço, e adicionar cada variável ao seu vetor respetivo. No código, está indicado com “ADICIONAR ITEM” o local onde deves trabalhar neste exercício. Recorda-te que as variáveis devem ser declaradas no início da função.
Exemplo do programa em execução:
![sc5](https://i.imgur.com/3pcErd8.png)

---

# Exercícios

**SC6.** Implementa a funcionalidade de ver os itens no carrinho. Para isso, deves percorrer os vetores de itens e preços (que, recorda-te, têm o mesmo tamanho) e imprimir para o ecrã cada um dos valores. Caso não existam quaisquer produtos, deves imprimir uma mensagem a indicar o mesmo.
Exemplo do programa em execução:
![sc6](https://i.imgur.com/QZuCbUG.png)

**SC7.** Implementa a funcionalidade de remover um item do carrinho. Para isso, deves pedir ao utilizador o ID do produto (que pode ser usado para calcular o índice do mesmo no vetor) e removê-lo do vetor correspondente, juntamente com o preço. No final, para verificar que a função funciona, corre a opção de ver os itens do carrinho e certifica-te que o item escolhido não aparece.
Exemplo do programa em execução:
![sc7](https://i.imgur.com/aB2Ht13.png)

---

# Soluções


```cpp
void printAndChooseOption(int &option, vector<string> &cartItems, vector<double> &prices)
{
    vector<string> options{"Sair do programa", "Ver itens", "Adicionar item", 
    "Atualizar item", "Remover item"};
    string newItem;
    double price;
    
    // ...

    switch (option)
    {
    // ...
    case 2:
        // ADICIONAR ITEM
        cout << "Novo Item: ";
        getline(cin, newItem);
        cout << "Preço (€): ";
        cin >> price;
        cartItems.push_back(newItem);
        prices.push_back(price);
        cout << "Adicionado item: " << newItem << endl;
        break;
        
        // ...
    }
}
```

---

# Soluções


```cpp
void printAndChooseOption(int &option, vector<string> &cartItems, vector<double> &prices)
{
    vector<string> options{"Sair do programa", "Ver itens", "Adicionar item", 
    "Atualizar item", "Remover item"};
    string newItem;
    double price;
    int size = cartItems.size();
    // ...
    switch (option)
    {
    // ...
    case 1:
        // VER ITENS
        cout << "ITENS NO CARRINHO DE COMPRAS" << endl;
        if (size == 0){
            cout << "O carrinho de compras está vazio!" << endl;
        }
        for (int i = 0; i < size; i++){
            cout << i + 1 << " - " << cartItems.at(i) << " - " 
            << prices.at(i) << "€" << endl;
        }
        break;
        // ...
    }
}
```

---

# Soluções 


```cpp
void printAndChooseOption(int &option, vector<string> &cartItems, vector<double> &prices)
{
    // ...
    int size = cartItems.size();
    int id;
    string item;
    // ...
    switch (option)
    {
    // ...
    case 4:
        // REMOVER ITEMS
        cout << "ID do item a remover: ";
        cin >> id;

        item = cartItems.at(id - 1);
        cartItems.erase(cartItems.begin() + id - 1);
        prices.erase(prices.begin() + id - 1);

        cout << "Removido item: " << item << endl;
        break;
    // ...
    }
}
```

---

# Funções
Até agora, todo o código encontrava-se dentro da função main. Para programas mais simples é o suficiente, 
mas à medida que a complexidade (e número de linhas de código) da aplicação aumenta, o uso de funções torna-se extremamente útil.

--- 

## Organização 
Uma função é praticamente um mini-programa que é escrito fora da função main(), sem que se tenha que pensar sobre o resto 
do programa que vamos escrever. Isto permite reduzir um programa complexo noutros mais pequenos e mais fáceis de lidar.

--- 
## Reusabilidade
Após uma função ser escrita, pode ser chamada múltiplas vezes a partir do programa. Isto evita repetição de código e minimiza a 
probabilidade de erros "copy-paste". Estas funções também podem ser partilhadas com outros programas, diminuindo a quantidade que tem 
que ser escrita de raiz de cada vez.

---
# Funções
## Testabilidade
Como as funções reduzem a redundância de código, há menos código para ser testado. Também devido ao facto de que as funções são isoladas, 
depois de as testarmos uma vez, não precisamos de as testar novamente (a não ser que eventualmente a modifiquemos). Isto reduz a quantidade 
de código, o que torna muito mais fácil encontrar bugs (ou evitá-los, preferencialmente).

--- 

## Extensibilidade
Quando precisamos de extender o nosso programa para suportar um caso com o qual este não conseguia lidar anteriormente, 
as funções permitem-nos fazer uma modificação num lugar e ver essas mudanças em ação todas as vezes que a função for chamada.

---

# Funções
## Abstração
De maneira a usar uma função, apenas é necessário saber o seu nome, inputs, outputs e onde ela se localiza. Não é preciso 
saber como funciona, ou se esta é dependente de outras funções. Isto diminui a quantidade de conhecimento requirido para alguém 
poder usar o código de outra pessoa (incluído todo o código presente na standard library (STL)).
 

---

```C++
#include <iostream>

using namespace std;

string getName() {
  string name;
  cout << "Insert your name: ";
  getline(cin, name);
  return name;
}

int getAge() {
  int age;
  cout << "Insert your age: ";
  cin >> age;
  cin.clear();
  cin.ignore(9999, '\n');
}

int main() {
  string name = getName();
  int age;
  cout << "Hello " << name << "! You are " << age << " years old." << endl;
  return 0;
}
```


```C++
Insert your name: Sofia
Insert your age: 18
Hello Sofia! You are 18 years old.
```

---

```C++
#include <iostream>

using namespace std;

void clear_stream() {
    cin.clear();
    cin.ignore(9999, '\n');
}

int multiply(int first_operand, int second_operand) { // dois argumentos!
    return first_operand * second_operand;
}

int get_operand(int order) {
  int operand;
  cout << "Insert operand number " << order << ": ";
  cin >> operand;

  return operand;
}

int main() {
    int n1, n2;

    n1 = get_operand(1);
    clear_stream();

    n2 = get_operand(2);
    clear_stream();

    cout << n1 << "x" << n2 << "=" << multiply(n1, n2) << endl;

    return 0;
}
```

---

```Bash
Insert operand number 1: 4
Insert operand number 2: 7
4x7=28
```
---

# Exercícios

**SC8.** Melhora o programa de forma a que o código que elaboraste para cada um dos últimos 3 exercícios passe para dentro de uma função. Tem atenção aos parâmetros das funções, aonde as deves declarar, e como as deves chamar. Assegura-te que nada no funcionamento do programa se alterou. A partir de agora, sempre que te pedirmos uma nova funcionalidade, deves usar funções para a implementar.

**SC9.** Melhora a função de remover itens para que, caso o utilizador escolha um item não existente, seja imprimida uma mensagem a assinalar o erro, e assegura-te que o código responsável por remover o item não é executado.
Exemplo do programa em execução:
![sc9](https://i.imgur.com/n2rKs5K.png)

---

# Exercícios

**SC10.** Melhora a funcionalidade de mostrar os itens do carrinho de forma a ser possível ver o preço total dos produtos. Para isso, deves escrever uma função que calcule a soma dos preços, chamá-la no local apropriado, e imprimir o valor retornado pela mesma após mostrares os itens presentes no carrinho.
Exemplo do programa em execução:
![sc10](https://i.imgur.com/8LcSoYh.png)

**SC11.** Implementa a funcionalidade de atualizar um item do carrinho. Para isso, deves pedir ao utilizador o ID do produto, pedir o novo nome do produto e preço do produto, e atualizar esses valores nos vetores respetivos. À semelhança do exercício SC9, certifica-te que o utilizador não escolhe um item não existente.
Exemplo do programa em execução:
![sc11](https://i.imgur.com/S20wEuI.png)

---

# Soluções

```cpp
void printItems(vector<string> cartItems, vector<double> prices){
    int size = cartItems.size();

    cout << "ITENS NO CARRINHO DE COMPRAS" << endl;

    if (size == 0) {
        cout << "O carrinho de compras está vazio!" << endl;
    }

    for (int i = 0; i < size; i++) {
        cout << i + 1 << " - " << cartItems.at(i) << " - " << prices.at(i) << "€" << endl;
    }
}

void addItem(vector<string> &cartItems, vector<double> &prices){
    string newItem;
    double price;

    cout << "Novo Item: ";
    getline(cin, newItem);
    cout << "Preço (€): ";
    cin >> price;

    cartItems.push_back(newItem);
    prices.push_back(price);

    cout << "Adicionado item: " << newItem << endl;
}
```

---

# Soluções

```cpp
void removeItem(vector<string> &cartItems, vector<double> &prices)
{
    int id;
    string item;

    cout << "ID do item a remover: ";
    cin >> id;

    item = cartItems.at(id - 1);
    cartItems.erase(cartItems.begin() + id - 1);
    prices.erase(prices.begin() + id - 1);

    cout << "Removido item: " << item << endl;
}
```

---

# Soluções

```cpp
void printAndChooseOption(int &option, vector<string> &cartItems, vector<double> &prices){
    // ...
    switch (option){
    case 0:
        // TERMINAR O PROGRAMA
        cout << "Saindo do programa. Obrigado por escolher a nossa aplicação!" << endl;
        break;
    case 1:
        // VER ITENS
        printItems(cartItems, prices);
        break;
    case 2:
        // ADICIONAR ITEM
        addItem(cartItems, prices);
        break;
    case 3:
        // ATUALIZAR ITEMS
        cout << "Funcionalidade ainda não implementada!" << endl;
        break;
    case 4:
        // REMOVER ITEMS
        removeItem(cartItems, prices);
        break;
    default:
        cout << "Opção não existente!" << endl;
        break;
    }
}
```

---

# Soluções

```cpp
void removeItem(vector<string> &cartItems, vector<double> &prices)
{
    int id;
    string item;

    cout << "ID do item a remover: ";
    cin >> id;

    if (id < 0 || id > cartItems.size())
    {
        cout << "Esse item não existe!" << endl;
        return;
    }

    // ...
}
```

---

# Soluções

```cpp
double sumPrices(vector<double> prices)
{
    double sum = 0;
    int size = prices.size();

    for (int i = 0; i < size; i++)
    {
        sum += prices.at(i);
    }

    return sum;
}

void printItems(vector<string> cartItems, vector<double> prices)
{
    int size = cartItems.size();
    double total = sumPrices(prices);

    // ...

    cout << "Total: " << total << "€" << endl;
}
```

---

# Soluções

```cpp
void updateItem(vector<string> &cartItems, vector<double> &prices){
    int id;
    double newPrice;
    string newItem;
    string oldItem;

    cout << "ID do item a atualizar: ";
    cin >> id;
    cin.ignore(10000, '\n');

    if (id < 0 || id > cartItems.size()){
        cout << "Esse item não existe!" << endl;
        return;
    }

    oldItem = cartItems.at(id - 1);

    cout << "Novo item: ";
    getline(cin, newItem);
    cartItems.at(id - 1) = newItem;

    cout << "Novo preço (€): ";
    cin >> newPrice;
    prices.at(id - 1) = newPrice;

    cout << "Atualizado item " << oldItem << " para " << newItem << endl;
}
```


---


# Streams 
As streams de IO do C++ providenciam uma maneira incrívelmente flexível, mas ao mesmo tempo
simples, de conceber as rotinas de input/output de qualquer aplicação.

A informação pode ser vista como cadeias (streams) de caracteres. Isto faz sentido porque 
qualquer coisa que escrevamos no teclado pode apenas ser um caracter. Suponha-se que o utilizador 
insere o número 7479 - como é possível saber que foi inserido um número? O problema é que na verdade, 
não se sabe ao certo. Tudo o que se tem é o conjunto de caracteres '7', '4', '7' e '9'. Cabe ao 
programador decidir se quer que a string inserida seja um número, uma string, etc. Se os caracteres 
são válidos para o tipo que o programador deseja que sejam? Depende se o tipo de dados consegue interpretar 
os caracteres da input stream como uma descrição de um objeto desse tipo.

Para além de enviar informação para o ecrã (**cout**), as streams podem também direcionar os dados para 
ficheiros, o que permite, por exemplo, gravar o progresso de um jogo.

---

# Streams
```C++
/**
  * INPUT FROM TEXT TO FILE
  * Reads numbers from a file and finds the maximum value
  */
#include <iostream>
#include <string>
#include <fstream> 

using namespace std;

double max_value(ifstream &in)
{
    double highest, next;
    if (in >> next) // if file contains at least 1 element
        highest = next;
    else return 0;
    while (in >> next)
      if (next > highest)
        highest = next;
    return highest
}
```

Note-se a inclusão das bibliotecas string e fstream! 

Uma **ifstream** é um objeto da classe de input stream usado para operar em 
ficheiros. Uma **ofstream** trabalha, analogamente, com output.

---
```C++
int main() {
    string filename;
    cout << "Please enter the data file name: ";
    cin >> filename;

    ifstream infile;
    infile.open(filename);

    if (infile.fail()) { // or if(!infile.is_open()) or if (!infile)
        cerr << "Error opening " << filename << "\n";
        return 1;
    }

    double max = max_value(infile);
    cout << "The maximum value is " << max << "\n";

    infile.close();
    return 0;
}
```
--- 

Conteúdo do ficheiro aux.txt:
```Bash
1 5 4 2 3
```

--- 

```Bash
Please enter the data file name: aux.txt
The maximum value is 5
```

---

```C++
/**
  * OUTPUT TO FILE
  * Writes a simple string into a file
  */
#include <iostream>
using namespace std;

int main() {
    ofstream outfile;
    outfile.open("example.txt");

    outfile << "Writing this very difficult computation into a file  << endl;

    outfile.close()

    return 0;
}
```
--- 

Conteúdo do ficheiro example.txt: 
```Bash
Writing this very difficult computation into a file
```

---

# Exercícios

**SC12.** Neste momento, os itens no carrinho perdem-se quando o programa é terminado. Corrige este problema, começando primeiro por escrever os produtos num ficheiro de texto (.txt), linha a linha, no formato “&lt;NOME&gt; &lt;PREÇO&gt;”:

Exemplo de um ficheiro de texto seguindo este formato:
![sc12](https://i.imgur.com/LtUSpZ6.png)

**SC13.** A funcionalidade anterior é inútil se o programa não fizer uso do ficheiro criado. Complementa-a com a leitura do mesmo ficheiro, inicializando os respetivos vetores no início do programa. Verifica que a função está correta correndo a opção “Ver itens”.

---

# Soluções


```cpp
void writeItems(vector<string> cartItems, vector<double> prices)
{
    ofstream out("shoppingcart.txt");

    for (int i = 0; i < cartItems.size(); i++)
    {
        out << cartItems.at(i) << " " << prices.at(i) << endl;
    }
}

int main()
{
    // ...

    writeItems(cartItems, prices);

    return 0;
}
```

---

# Soluções


```cpp
void readItems(vector<string> &cartItems, vector<double> &prices)
{
    ifstream in("shoppingcart.txt");
    string cartItem;
    double price;

    while (in >> cartItem >> price)
    {
        cartItems.push_back(cartItem);
        prices.push_back(price);
    }
}

int main()
{
    // ...
    
    cout << "Olá " << name << "!" << endl;

    readItems(cartItems, prices);

    while (option != 0)
        printAndChooseOption(option, cartItems, prices);

    // ...
}
```

---

# Recursos Recomendados

## Ferramenta de Desenvolvimento

- Visual Studio Code & Extensão C/C++ & g++ (Linux/Mac)
- Visual Studio (Windows)

## Referência

- [cppreference](https://en.cppreference.com/w/)

## Livros

- The C++ Programming Language, 4ª Edição, de Bjarne Stroustrup
- Effective C++, 3ª Edição, de Scott Meyers
