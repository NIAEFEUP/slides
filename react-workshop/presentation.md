# React

## After you learn it, there is no way back

![](./img/ni_logo.png)

---

# O que é?

- Antigamente utilizava-se javascript normal, mas com o decorrer do tempo começou-se a querer fazer sites mais complicados e começaram a surgir bibliotecas e outras ferramentas para isso ser mais fácil.
- **React** é uma biblioteca com esse objetivo, de permitir que seja mais fácil fazer interfaces mais complicadas e reativas.

---

class: middle

# Exemplo contador

- Como motivação do por quê de React, vamos mostrar um exemplo de um contador simples com um
  indicador do valor do contador e um botão para o incrementar.

---

class: middle

# Javascript - Exemplo contador

```js
<script>
let counter = 0;
</script>

<p id="counter-value">`Valor do contador é: ${counter}`</p>
<button id="add-counter">
    Adicionar
</button>

<script>
    const counterValueHTMLElement = document.getElementById("counter-value");
    document.getElementById("add-counter").addEventListener(() => {
        counterValueHTMLElement.textContent = `${counter + 1}`;
        counter += 1;
    });
</script>
```

---

class: middle

# React - Exemplo contador

```js
// Importamos por que o react uma biblioteca com ferramentas
import { useState } from "react";

function Counter() => {
    const [counter, setCounter] = useState(0);

    return <div>
        <p>Valor do contador é: {counter}</p>
        <button onClick={() => setCounter(counter + 1)}>
            Adicionar
        </button>
    </div>
}
```

- Muito mais fácil de ler!

---

# Uma função a retornar uma espécie de HTML?

- **Sim**, são **componentes**, funções que retornam **JSX**, que é derivado de HTML
  e feito para ser utilizado juntamente com javascript.
- Para renderizar um componente, basta chamar a função da mesma maneira como se estivessemos
  a colocar um elemento HTML.

## Por exemplo

.center[
`App.jsx`

```js
function App() {
  return <Counter />;
}
```

]

---

# JSX - Diferenças com HTML

- `<div class="p-4">` em HTML fica `<div className="p-4">` em JSX.
- Em JSX, os atributos são _camel case_.

### Por exemplo

- `onclick` fica `onClick`
  .flex-columns-center[

```html
<div
  className="hidden"
  onClick={() => {
    console.log("clicked");
  }}
>
  Hidden div
</div>
```

]

---

# Como passar argumentos aos componentes?

- Os componentes de react só recebem um argumento chamado `props` , que é um objeto.
  .flex-columns-center[

```js
function PersonDisplay(props) {
  return (
    <article>
      <h1>{props.name}</h1>
      <p>{props.age} anos</p>
    </article>
  );
}
```

```js
function PersonDisplay({ name, age }) {
  return (
    <article>
      <h1>{name}</h1>
      <p>{age} anos</p>
    </article>
  );
}
```

]

---

# Mais um pormenor sobre props

- Por default, existe um argumento chamado `children` , que é automaticamente preenchido pelo React.
  .flex-columns[

```js
function Box({ children }) {
  return (
    <div style={{ border: "1px solid black", padding: "10px", margin: "10px" }}>
      {children}
    </div>
  );
}
```

```js
function PersonDisplay({ name, age }) {
  return (
    <article>
      <Box>
        <h1>{name}</h1>
        <p>{age} anos</p>
      </Box>
    </article>
  );
}
```

]

---

# Quando é que os componentes são renderizados?

- Quando a página é carregada.
- Quando uma variável de estado (com `useState` ) é atualizada.
- Quando um pai é re-renderizado.

```js
function App() {
  const [someState, setSomeState] = useState(0);

  {
    /*Se <App> re-renderizar, o <Counter> também será re-renderizado*/
  }
  return <Counter />;
}
```

---

# Renderização de componentes - Nota adicional

- Isto **não** funciona! O componente não vai ser re-renderizado e por isso o texto do `<p>` não vai ser alterado. O `useState` contém código que força a re-renderização do componente.
  .flex-columns-center[

```js
function Counter() => {
    const counter = 0;

    return <div>
        <p>Valor do contador é: {counter}</p>
        <button onClick={() => counter + 1}>
            Adicionar
        </button>
    </div>
}
```

]

---

# Nota sobre funcionamento de browsers

.flex-columns-center[

![](./img/browser-workings.png)

]

---

# DOM

- Os browsers constroem uma àrvore chamada **DOM** (Document Object Model) que representa as relações hierárquicas
  dos elementos.
  .flex-columns[

```html
<!DOCTYPE html>
<html>
  <head>
    <meta name="description" content="A simple HTML only web page" />
    <title>Web page</title>
  </head>
  <body>
    <h1>Web page</h1>
    <h2>This is a simple web page</h2>
  </body>
</html>
```

]

---

# Virtual DOM

- Por motivos de eficiência, o React não altera diretamente na DOM as mudanças nos elementos para poder agrupar mudanças, em vez de fazer uma a uma.
- Alterar algo na `virtualDOM` não implica logo re-renderização por parte do browser, só quando é passado para a DOM real.

---

# Keys

- Em vez de re-renderizar a lista toda quando ela muda, com as `keys` , o react permite identificar cada elemento individualmente.
  .flex-columns-center[

```javascript
function App() {
  const requests = fetchRequests();

  return <>
    {requests.map((request, index) => (
      <Request
        key={index}
        request={request}
      />
    )}
  </>
}
```

]

---

# Hooks - O que são?

- **Hooks** são **funções especiais** que são alocadas na memória RAM num local onde quando
  retornam um valor continuam em memória com todas as variáveis dentro dela intactas. **Começam sempre com um **`**use[A-Z]**` .
  .flex-columns[

```js
function counter() {
  const counter = 10;
}
counter();
// A partir daqui a função deixa de estar em memória
```

```js
function useCounter() {
  const counter = 10;
}
useCounter();
// A partir daqui a função continua em memória
```

]

---

# Mas para o que é que isto seria útil?

- Lembram-se do `useState()` ?

```js
import { useState } from "react";
function Counter() {
  const [counter, setCounter] = useState(0);
}
```

- Como fica sempre em memória mesmo depois de ser chamado consegue guardar o estado do componente.
- E **é útil ser em formato de função** por que já imaginaram termos de colocar o código todo que está dentro do `useState` em cada componente que quiséssemos ter estado?

---

# Mais sobre hooks

- É mais fácil quando ouvirem _hooks_ traduzirem simplesmente para _funções especiais que guardam estado_.
- Muitas vezes as pessoas não percebem esta parte dos _hooks_ por ser demasiado abstrato e não tratarem as coisas de forma mais específica.

### Agora vamos falar sobre _hooks_ que a o React disponibiliza já feitos para nós usarmos

---

# useContext - Motivação (1/2)

- Nos exemplos anteriores, a àrvore era simples por que não tinhamos muitos componentes. Mas existem
  circunstâncias onde muitos componentes precisam de aceder a uma mesma variável.
- Se por exemplo se tivessemos um componente `Account` que dentro dele tinha um `Profile` e dentro dele tinha um `UserBasicInfo`
  a renderizar informações sobre o utilizador (nome, email, etc).
- Para `Account` , `Profile` e `UserBasicInfo` terem acesso ao utilizador, neste caso, teríamos de passar o estado da seguinte forma: `Account` -> `Profile` -> `UserBasicInfo` .

---

# useContext - Motivação (2/2)

.flex-columns[

```js
function Account() {
  const { user } = fetchUser();

  return <Profile user={user} />;
}

function Profile({ user }) {
  return <UserBasicInfo user={user} />;
}

function UserBasicInfo({ user }) {
  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}
```

]

---

# useContext - Como receber valores?

```js
function Profile() {
  return <UserBasicInfo />;
}
```

```js
function UserBasicInfo() {
  const { user } = useContext(UserContext);
  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}
```

---

# useContext - Como criar valores?

```js
const UserContext = createContext({
  user: undefined
}});
```

```js
function App() {
  const user = fetchUser();

  return (
    <UserContext.Provider value={user}>
      <Profile />
    </UserContext.Provider>
  );
}
```

---

# useEffect

- Uma função já fornecida pelo React que recebe uma função e um array de dependências, que permite correr código quando certas variáveis mudam ou quando o componente é renderizado.

```js
function Counter() => {
    const [counter, setCounter] = useState(localStorage.getItem("counter") ?? 0);

    useEffect(() => {
        localStorage.setItem("counter", counter);
    }, [counter]);

    return <div>
        <p>Valor do contador é: {counter}</p>
        <button onClick={() => setCounter(counter + 1)}>
            Adicionar
        </button>
    </div>
}
```

---

# Como tornar o código anterior mais modular?

- Se fossemos utilizar um contador com o objetivo de guardar na `localStorage` noutros componentes teríamos de estar
  sempre a copiar o seguinte código.

```js
const [counter, setCounter] = useState(localStorage.getItem("counter") ?? 0);
useEffect(() => {
  localStorage.setItem("counter", counter);
}, [counter]);
```

---

# Criar um hook customizado

```js
function Counter() {
  const [counter, setCounter] = useLocalStorage("counter", 0);

  return ...
}
```

```js
function useLocalStorage(storageItem, defaultValue) {
const [value, setValue] = useState(localStorage.getItem("counter") ?? 0);

useEffect(() => {
  localStorage.setItem("counter", value);
}, [value]);

return [value, setValue];
```

---

## Parte prática

[Exercícios do TTS](https://github.com/NIAEFEUP/tts-fe/wiki/Newcomer-workshop)

---

# É tudo por hoje!

## Obrigado

---
