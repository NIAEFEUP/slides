class: center, middle, inverse, small-images

# Git - Workshop Interno

---

class: inverse

# Num projeto...

Vocês escrevem código e querem partilhar esse código com os restantes membros do vosso grupo em que estão. Ou então querem escrever código mas manter um registo de todas as alterações que foram fazendo ao longo do tempo.

Podem _zippar_ o vosso código e mandar para os vossos colegas, ou então criam várias pastas no vosso computador, cada uma delas com uma versão diferente do vosso código.

![Meme funny 1](assets/versoes_trabalho_funny.png)
---

class: center, middle, inverse

# O problema

---

class: inverse

# O problema é...

Que isto é demasido trabalho para um projeto em que o foco é escrever código, e não é prático andar a trocar ficheiros _zip_ com código dos vossos colegas ou guardar todas as alterações que fazem em separado (rapidamente ficavam sem espaço no disco). A quantidade de ficheiros que iam trocar vai aumentar exponencialmente com o número de pessoas no vosso projeto.

A solução é...

---

class: center, middle, inverse

# _Version Control_

---

class: inverse

# O que é _Version Control_?

Um _Version Control System_ é um sistema que dá track a mudanças no código ou em ficheiros de maneira organizada e o mais automatizada possível. Normalmente existe um servidor centralizado que contêm todas as mudanças no código mas não é necessário.
Existem vários programas que tentam resolver este problema: 
- Git (o que vamos usar)
- Subversion
- Mercurial
---

class: inverse

# O que é Git?

Git é um _Version Control System_, feito pelo Linus Torvalds originalmente para auxiliar no desenvolvimento do kernel do Linux, e foi lançado no dia 7 de abril de 2005. É o sistema de _version control_ mais usado no mundo, e é o que vamos usar neste workshop.
---

class: inverse

# Como instalar Git?

Se estiverem a usar Linux, muito provavelmente vai estar diretamente no vosso package manager: 
```bash
   sudo apt install git
   sudo pacman -S git
   sudo dnf install git
```
Se estiverem no Windows (😢), podem fazer download de um instalador em [https://git-scm.com/download/win](https://git-scm.com/download/win)

---

class: inverse, center, middle

# Como é que o Git funciona? 

---

class: inverse

### Repositórios

A base de trabalho do Git é o **repositório**. Um repositório é uma pasta que contêm todos os ficheiros do vosso projeto, e o histórico de todas as alterações que foram feitas a esses ficheiros desde que o repositório foi iniciado.

Para o fazer, devem executar o comando
```bash
   git init
```
Este comando cria uma pasta `.git` dentro da pasta onde o comando foi executado. Esta pasta contêm todos os ficheiros necessários para o Git funcionar.

Se quiserem criar uma pasta em particular para o vosso repositorio, podem executar o comando
```bash
   git init <nome da pasta>
```
e o resultado vai ser semelhante.

---
class: inverse

### *Stages*

No Git existe uma noção de **stages**. Um stage é uma "área" em que as alterações que fazem ficam para serem utilizadas depois.

<img height="440" width="750" src="assets/git_00_intro_01_sections.webp">

???

Começar com a **working directory**, depois passar para o **staging** area, e depois para o **repository**.

Por fim mencionar a **stash**.

---

class: inverse

### *Stages* - Hands-on

Depois de termos o repositório criado com `git init`, criamos um ficheiro `hello_world.txt`.
Ao fazer-mos `git status` devemos obter o seguinte resultado:

```bash
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hello_world.txt

nothing added to commit but untracked files present (use "git add" to track)
```

---

class: inverse

### *Stages* - Hands-on

Se quisermos adicionar o ficheiro à `staging area` podemos fazer:
```bash
    git add hello_world.txt
```

Se quisermos adicionar todos os ficheiros modificados ou untracked na pasta atual e nos seus filhos podemos fazer:
```bash
    git add .
```

Se quisermos adicionar todos os ficheiros modificados ou untracked no repositorio podemos fazer:
```bash
    git add -A
```
Ao fazer `git status` obtemos:
```bash
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   hello_world.txt
```
Ou seja podemos concluir que o `hello_world.txt` está na `staging area`.