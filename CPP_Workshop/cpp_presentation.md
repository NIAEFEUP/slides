class: center, middle

# Workshop C++
### NIAEFEUP

---

# Links importantes

- Apresentação: https://niaefeup-workshop-cpp.netlify.com/
- [Exercícios](https://github.com/NIAEFEUP/Workshop_CPP/)
- [OnlineGDB](https://www.onlinegdb.com/online_c++_compiler), [Visual Studio](https://visualstudio.microsoft.com), [CLion](https://www.jetbrains.com/clion/) (escolher um)

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
9. Funções
10. Apontadores
11. Vetores
12. Classes

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
int main() {
    // ...
     
    vector<double> prices;

    cout << "Bem-vindo ao MyShoppingCart!" << endl;
    
    // ...
}
```

---

# Tipos de dados primitivos
- **char:** caracteres alfanuméricos (ex: 'c', '8', '$');
- **int:** números inteiros (ex: 10**3, -2)
- **float:** números com vírgula flutuante de precisão simples (ex: 1.902, -5,926563840)
- **double:** números com vírgula flutuante de precisão dupla (ex: 1.2, -4.587)  
- **bool:** verdadeiro ou falso (ex: true, false)
- **void:** significa "sem qualquer valor". É usado quando uma função não retorna nenhum 
valor

---

# Tipos de dados
## Modificadores de tipos de dados
- **signed/unsigned:** para números com/sem sinal
- **short:** valor otimizado para o espaço com comprimento de pelo menos 16 bits
- **long/long long:** valor otimizado para precisão com comprimento de pelo menos 32/64 bits

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
São contentores capazes de armazenar, em memória, valores de um determinado tipo, para serem reutilizados mais tarde.

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
desde que sejam locais e estejam em diferentes blocos de código (entre {})
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
# Input/Output
## Requisitos
Para utilizar os operadores I/O de C++, é necessário incluir as seguintes linhas no topo do ficheiro de código:

```C++
#include <iostream>
using namespace std;
```

`iostream` é a biblioteca *standard* que fornece operadores e funções de I/O.

Se o *namespace* `std` não for declarado, é necessário pré-anexar `std::` aos métodos *standard* (e.g. `std::cout`).

---


# Input/Output
## Escrever Informação
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
// Assuma-se que o conteudo da variável nome_do_aluno é Inês.
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
# Input/Output
### Ler Informação
De forma semelhante, é possível ler informações do utilizador, usando o objeto **cin** e o operador **>>** seguido da variável onde vai ser guardada a informação.

--- 

O objeto **cin** permite obter informação de qualquer tipo de dados (exceto tipos 
definidos pelo utilizador, a não ser que o operador >> tenha sido *overloaded*).

Para ler *strings*, **cin** utiliza qualquer espaço em branco como delimitador (o que inclui espaços, newlines, tabs, etc.). Para ler strings com o caracter espaço ' ', pode user usada a função *getline()* (a string *acaba* apenas quando o caracter '\n' é encontrado).

---
# Input/Output
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
Insert your name here: André Moreira
Your name is André
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
int main() {
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
Ideal para substituir declarações *if* muito longas que 
comparam uma variável com vários **valores inteiros** (incluíndo *char*)
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
Na ausência do *break*, as condições *case* seguintes seriam executadas 

---

# Exercícios

**E4.** Vamos tentar perceber o funcionamento de programas com `if`. Copia o código [neste ficheiro](https://raw.githubusercontent.com/NIAEFEUP/Workshop_CPP/master/introdutory%20exercises/ControlFlow.cpp) e corre-o no onlinegdb.

**SC3.** Descomenta (removendo as barras) a linha com o conteúdo `printAndChooseOption(option, listItems, prices);`. Se correres o programa, reparas que aparece uma lista das opções disponíveis, e é pedido ao utilizador para escolher uma delas. Melhora o programa de forma a que, quando o utilizador coloca uma opção não existente (ex: -1), seja imprimida uma mensagem a assinalar o erro.

Exemplo do programa em execução:

![sc3](https://i.imgur.com/Yo9oOsI.png)

---

# Solução


```cpp
void printAndChooseOption(int &option, vector<string> &cartItems, vector<double> &prices) {
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
for (int i = 0; i < 10; i++) {
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
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
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

Primeiro Input             |  Segundo Input
:-------------------------:|:-------------------------:
![](https://i.imgur.com/tsuIpln.png)  |  ![](https://i.imgur.com/jNhPLPR.png)

---

# Solução

```cpp
int main() {
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
- São alocados contiguamente na memória, podendo por isso ser vistos como uma extensão de *arrays* de C
- Os dados são geralmente inseridos no final do vetor (por razões de eficiência)

## Notas importantes
- Os índices de um vetor iniciam-se sempre no zero. Ou seja, o primeiro elemento de um vetor 
está na posição 0, o segundo elemento na posição 1, etc.
- é possível consultar o conteúdo de um vetor numa determinada posição utilizando parêntesis 
retos [] ou o método .at();

---

# Vetores
## Métodos Fundamentais

- **[*idx*]/at(*idx*)**: Retorna um elemento no índice dado
- **push_back(*elem*):** Adiciona um elemento ao vetor
- **pop_back()**: Remove o último elemento do vetor
- **size()**: Tamanho do vetor
- **begin()**: Referência para o início do vetor (a ser usado noutros métodos)
- **insert(*pos*, *elem*)**: Inserte um elemento ao vetor na posição dada
- **erase(*pos*):** Remove um elemento do vetor na posição dada


Para mais informação, consultar [***Cpp Reference***](https://www.cplusplus.com/reference/vector/vector/).

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

    numbers.erase(numbers.begin() + 1); // elimina o segundo elemento do vetor (20)
    numbers.insert(numbers.begin(), 0); // adição do valor 0 ao início do vetor

    size = numbers.size();
    cout << "Vector size = " << size << endl;

    cout << "Vector elements:";
    for (int i = 0; i < numbers.size(); i++)
        cout << " " << numbers.at(i); // equivalente a numbers[i]
    cout << endl;
    
    return 0;
}                                                                         
```
---

```Bash
Vector size = 3
Vector elements: 0 10 30
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

A função *insert()* funciona de uma forma semelhante:
```C++
numbers.insert(numbers.begin(), 0);
```
Aqui, insere-se o elemento 0 no início do vetor.

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
void printAndChooseOption(int &option, vector<string> &cartItems, vector<double> &prices) {
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
void printAndChooseOption(int &option, vector<string> &cartItems, vector<double> &prices) {
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
void printAndChooseOption(int &option, vector<string> &cartItems, vector<double> &prices) {
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
mas à medida que a complexidade (e número de linhas de código) da aplicação aumenta, o uso de funções torna-se indispensável.

- **Organização**: Reduzem um programa complexo em módulos mais pequenos e fáceis de lidar.
- **Reusabilidade**: A função pode ser chamada múltiplas vezes, evitando repetição de código e minimizando a probabilidade de erros.
- **Testabilidade**: Como as funções são isoladas, isto torna mais fácil testar as várias partes do programa e reduz o número de testes necessários. Reduz também a quantidade código, facilitando a correção e prevenção de bugs.
- **Extensibilidade**: Permitem-nos fazer uma modificação num lugar e vê-la ao longo de todo o programa.
- **Abstração**: Não é necessário saber sobre o funcionamento da função, apenas como chamá-la.

---

# Funções
## Como Declarar e Invocar uma Função

![](https://cdn.programiz.com/sites/tutorial2program/files/cpp-function-return-statement.png)

(Imagem retirada de [*Programiz*](https://www.programiz.com/cpp-programming/function))

---

# Funções
## Argumentos
Os argumentos nas funções podem ser passados de diferentes formas.
- **Cópia**: O objeto e a sua memória associada são copiados para um novo objeto. Quaisquer alterações à variável passada no argumento não terão efeito no objeto original.
- **Referência**: O objeto passado por argumento poderá ser manipulado e terá efeito no objeto original (tipo do argumento marcado com **&**).
- **Apontador**: Funciona de forma semelhante a ser passado por referência. No entanto, tem uma utilização diferente (tipo do argumento marcado com **\***). Representa o endereço do objeto em memória.


---

```C++
#include <iostream>
using namespace std;

int getAge() {
    int age;
    cout << "Insert your age (years): ";
    cin >> age;

    cin.clear(); // Caso o utilizador insira dados inválidos
    cin.ignore(9999, '\n'); // Ignora tudo até fim de linha

    return age;
}

/*
    Não funciona corretamente
    Com funções, podemos corrigi-la e aplicar a mudança a todo o código
*/
void convertToMonths(int& age) {
    age = age * 12;
}

int main() {
    int age = getAge();
    convertToMonths(age);
    cout << "Hello! You are " << age << " months old." << endl;
    return 0;
}
```


```Bash
Insert your age (years): 18
Hello! You are 216 months old.
```

---
```C++
#include <iostream>
using namespace std;

void clearInput() {
    cin.clear();
    cin.ignore(9999, '\n');
}

int multiply(int first, int second) {
    return first * second;
}

int getOperand(int* order) {
    int operand;
    cout << "Insert operand no. " << *order << ": ";
    cin >> operand;

    *order += 1; // É necessário desreferenciar o apontador
    return operand;
}

int main() {
    int n1, n2;
    int order = 1;

    n1 = getOperand(&order); // passar apontador para order
    clearInput();
    n2 = getOperand(&order);
    clearInput();
    
    cout << n1 << "x" << n2 << "=" << multiply(n1, n2) << endl;
    return 0;
}
```
---

# Funções
Execução do programa:
```Bash
Insert operand no. 1: 4
Insert operand no. 2: 7
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
void printItems(vector<string> cartItems, vector<double> prices) {
    int size = cartItems.size();
    cout << "ITENS NO CARRINHO DE COMPRAS" << endl;

    if (size == 0) {
        cout << "O carrinho de compras está vazio!" << endl;
    }

    for (int i = 0; i < size; i++) {
        cout << i + 1 << " - " << cartItems.at(i) << " - " << prices.at(i) << "€" << endl;
    }
}

void addItem(vector<string> &cartItems, vector<double> &prices) {
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
void removeItem(vector<string> &cartItems, vector<double> &prices) {
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
void printAndChooseOption(int &option, vector<string> &cartItems, vector<double> &prices) {
    // ...
    switch (option){
    case 0: // TERMINAR O PROGRAMA
        cout << "Saindo do programa. Obrigado por escolher a nossa aplicação!" << endl;
        break;
    case 1: // VER ITENS
        printItems(cartItems, prices);
        break;
    case 2: // ADICIONAR ITEM
        addItem(cartItems, prices);
        break;
    case 3: // ATUALIZAR ITEMS
        cout << "Funcionalidade ainda não implementada!" << endl;
        break;
    case 4: // REMOVER ITEMS
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
void removeItem(vector<string> &cartItems, vector<double> &prices) {
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
double sumPrices(vector<double> prices) {
    double sum = 0;
    int size = prices.size();

    for (int i = 0; i < size; i++)
    {
        sum += prices.at(i);
    }

    return sum;
}

void printItems(vector<string> cartItems, vector<double> prices) {
    int size = cartItems.size();
    double total = sumPrices(prices);

    // ...

    cout << "Total: " << total << "€" << endl;
}
```

---

# Soluções

```cpp
void updateItem(vector<string> &cartItems, vector<double> &prices) {
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

# Exercícios

**SC12.** Neste momento, os itens no carrinho perdem-se quando o programa é terminado. Corrige este problema, começando primeiro por escrever os produtos num ficheiro de texto (.txt), linha a linha, no formato “&lt;NOME&gt; &lt;PREÇO&gt;”:

Exemplo de um ficheiro de texto seguindo este formato:
![sc12](https://i.imgur.com/LtUSpZ6.png)

**SC13.** A funcionalidade anterior é inútil se o programa não fizer uso do ficheiro criado. Complementa-a com a leitura do mesmo ficheiro, inicializando os respetivos vetores no início do programa. Verifica que a função está correta correndo a opção “Ver itens”.

---

# Soluções


```cpp
void writeItems(vector<string> cartItems, vector<double> prices) {
    ofstream out("shoppingcart.txt");

    for (int i = 0; i < cartItems.size(); i++)
    {
        out << cartItems.at(i) << " " << prices.at(i) << endl;
    }
}

int main() {
    // ...

    writeItems(cartItems, prices);

    return 0;
}
```

---

# Soluções


```cpp
void readItems(vector<string> &cartItems, vector<double> &prices) {
    ifstream in("shoppingcart.txt");
    string cartItem;
    double price;

    while (in >> cartItem >> price)
    {
        cartItems.push_back(cartItem);
        prices.push_back(price);
    }
}

int main() {
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

- [Visual Studio Code](https://code.visualstudio.com/) & Extensão C/C++ & g++ (Linux/Mac)
- [Visual Studio](https://visualstudio.microsoft.com/) (Windows)
- [CLion](https://www.jetbrains.com/clion/) (Windows/Linux/Mac)

## Referência

- [cppreference](https://en.cppreference.com/w/)

## Livros

- The C++ Programming Language, 4ª Edição, de Bjarne Stroustrup
- Effective C++, 3ª Edição, de Scott Meyers
class: center, middle
