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
    const [counter, setCounter] = useState(localStorage.getItem("counter") || 0);

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
const [counter, setCounter] = useState(localStorage.getItem("counter") || 0);
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

# NextJS

Se não sabes React, nem devias estar aqui...

Este é um workshop de Next.js **versão 13** para cima!

---

# O que é o Next.js?

Nextjs é uma **framework**.

É uma tecnologia que fornece uma estrutura para o desenvolvimento de websites com bastantes benificios como **SSR** - Server Side Rendering.

Mas não só, até é possível criar uma simples Rest API sem necessidade de envolver _frontend_.

Next.js é construido em cima de React e utiliza as suas funções para mexer com tudo o que é relacionado com a visualização de conteúdo.

---

<img src="img/n1.png">

---

## SSR - Server Side Rendering / Dynamic Rendering

O conteudo é renderizado no servidor no momento em que o utilizador faz o _request_, isto é, visita a página. O cliente recebe diretamente o html resultante.

### Vantagens

- É muito fácil fornecer **informação personalizada** com base no utilizador, como por exemplo dashboards e perfil.
- Acesso a informações do _request_ como _Cookies_ e _URL Search Params_ no momento.
- Websites mais rápidos pois as páginas podem ser guardadas em _**cache**_ e globalmente distribuidas.
- O **Server Load é reduzido** dado que o conteudo é guardado em cache e não necessita de ser gerado novamente caso as informações não sejam modificadas.
- **SEO** - Os crawlers indexam muito melhor os websites que carregam a informação no momento em que a página acontece. Isto leva a melhores rankings de pesquisa.

---

# Estrutura de Ficheiros

## Routing - App Router

Esta é uma das grandes mudanças na versão 13.

> Tenham sempre cuidado a ver a documentação e se estão a ver a versão correta

<img src="img/n2.png" height="80">

`.ts = .js + TypeScript `

`.tsx = .jsx + TypeScript`

---

<img src="img/n3.png" height="80">

- page.tsx e _nesting_ de folders
- layout.tsx

<img src="img/n4.png" height="100">

> Um dos benefícios de usar layout é que ao mudar de página, os componentes do layout não voltam a ser renderizados.

- loading.jsx
- not-found.jsx
- error.jsx

---

### Dynamic Routing

<img src="img/n5.png" height="100">

```tsx
export default function Page({ params }: { params: { slug: string } }) {
  return <div>My Post: {params.slug}</div>;
}
```

---

### APIs

<img src="img/n6.png" height="100">

```tsx
//`request` e `context` são opcionais
export async function GET(request: Request) {}
export async function HEAD(request: Request, context: { params: Params }) {}
export async function POST(request: Request) {
  return NextResponse.json({ error: "ISE" }, { status: 500 });
}
export async function PUT(request: Request) {}
export async function DELETE(request: Request) {}
export async function PATCH(request: Request) {}
export async function OPTIONS(request: Request) {}
```

> Não pode existir `layout.tsx` nem `page.tsx` ao mesmo nível do route.ts. Tipicamente cria-se uma pasta `api` para servir a API.

---

### Other Project Organization Features

- Pastas privadas, a começar com `_`. Estas pastas não serão consideradas no _routing_ da app.
- Route groups, nome da pasta entre `()`. Desta forma é possível organizar pastas sem interferir no _routing_ da app.

---

## Metadata

```tsx
// Static
export const metadata: Metadata = {
  title: "Título super interessante",
  description: "Os oradores são mesmo nice",
};
```

```tsx
// Dynamic
export async function generateMetadata({
  params,
}: {
  params: { id: string };
}): Promise<Metadata> {
  const id = params.id;
  const product = await fetch(`https://.../${id}`).then((res) => res.json());
  return {
    title: product.title,
    openGraph: {
      images: ["/some-specific-page-image.jpg"],
    },
  };
}
```

---

## Link

```tsx
import Link from "next/link";
```

```tsx
<Link href="/dashboard">Dashboard</Link>
```

> Nunca usem tags `<a>` em Next.js!

---

## Image

```tsx
import Image from "next/image";

<Image
  src="https://s3.amazonaws.com/my-bucket/profile.png"
  alt="Picture of the author"
/>;
```

Uma das razões dos _websites_ de tornarem lentos ao carregar, é exatamente o carregamento das imagens.

Vantagens:

- Prevenir _layout shift_ durante o carregamento de imagens.
- Redimensionamento automático para evitar enviar imagens grandes para dispositivos pequenos.
- _Lazy loading_ por definição. As imagens vão sendo carregadas à medida que vão a aparecer na janela de visualização.
- Formatos modernos, como [﻿WebP](https://developer.mozilla.org/pt-BR/docs/Web/Media/Formats/Image_types#webp) e [﻿AVIF](https://developer.mozilla.org/pt-BR/docs/Web/Media/Formats/Image_types#avif_image), quando o _browser_ é compatível.

---

# "use server" vs "use client"

Por definição, todas as páginas são "use server", exceto escrito o contrário.

O **"use client"** significa que página será renderizada do lado do cliente. Isto significa que um bundle de JavaScript será enviado para o cliente e serão possíveis usar os _hooks_ do React, tal como _useState_ e _useEffect._

Importar referir que o "use client" não precisa de ser especificado para uma página inteira. Podemos ter uma página 80% gerada no servidor onde apenas um componente será renderizado no cliente.

A partir do momento que usamos **"use client"** num componente, não podemos voltar a usar **"use server"** nos seus filhos. Faz sentido, certo?

---

# "use server" vs "use client"

<img src="img/n7.png" height="400">

---

## Server Actions

- Funções assíncronas
- Rodam no servidor
- Podem ser chamadas no lado do cliente.

```tsx
"use server";

export async function updateItem(itemId, formData) {
  // database stuff here
}
```

```tsx
"use client";

import { updateItem } from "./actions";

export default function ClientComponent({ itemId }) {
  return <form action={updateItem}>{/* ... */}</form>;
}
```

Como enviar o `itemId` para o `updateItem`?

---

## Server Actions - [﻿Pending states](https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations#pending-states)

---

# Filosofia da framework!

"We recommend first attempting to **fetch data on the server-side**."

- "However, there are still cases where client-side data fetching makes sense. In these scenarios, you can manually call `fetch` in a `useEffect` (not recommended), or lean on popular React libraries in the community such as [﻿SWR](https://swr.vercel.app/) or [﻿React Query](https://tanstack.com/query/latest) ."

"To reduce the Client JavaScript bundle size, we recommend moving **Client Components down your component tree**."

"Optimizations, whenever is possible"

---

## Coisas interessantes para explorar em casa

- Middleware
- ORM (Prisma or Drizzle)
- Parallel Routes & Tab Groups
- Interception Routes
- Internationalization
- React [﻿useOptimistic](https://react.dev/reference/react/useOptimistic)
- NextAuth

---

# Bora ao trabalho!

> Mini site para inserir links de recursos interessantes da L.EIC.

Requisitos:

- [﻿Node.js](https://nodejs.org/en) acima da versão 18
  Primeiros passos:

- `git clone https://github.com/thePeras/react-next-workshop`
- `cp .env.example .env`
  - Mudar o `<username>`
  - Mudar a `<password>`
- `npm install`
- `npx prisma generate`
- `npm run dev`

---

# Tarefa #1

## Primeiro Componente em React

`components/feed-resource-card.tsx`

Implementa o componente `ResourceCard` .

Tens um html para te ajudar!

---

# Tarefa #2

## Listar os recursos no feed

`app/@feed/page.tsx`

- Se não existirem recursos, mostrar uma mensagem a dizer "No resources found", exemplo:

```
<div className="flex items-center justify-center py-16 text-muted-foreground">
  <span>No resources found.</span>
</div>
```

- Se existirem recursos, mostrar uma lista de ResourceCard.
  > Não te esqueças do `key`

---

# Tarefa #3

## Adptar a página de um recurso

`app/resources/[id]/page.tsx`

Consoante o recurso selecionado através do url, adapta a página para mostrar informações relevantes desse recurso.

- Deves começar por pegar no `id` do recurso do url
- Usar o `id` para ir buscar o recurso à base de dados.
- Se o recurso não existir, podes mostrar uma página de erro 404.
- Se o recurso não tiver `thumbnail`, usa a imagem que existe em `/public/images/placeholder.jpg`.

Bónus:

- Cria uma função para copiar o url da página ao clicar no botão share.

---

# Tarefa #4

## Escreve o Metadata da página do recurso

`app/resources/[id]/page.tsx`

Inspeciona o _website_ e verifica dentro do `<head>` se o título e a descrição estão a ser preenchidos.

> Dica: Consulta os slides à procura do generateMetadata.

---

# Tarefa #5

## Criar uma página 404 para um recurso não encontrado

Qual é o ficheiro que deves criar e onde deves colocar?

---

# Tarefa #6

## Implementa o componente de reações

`app/resources/[id]/counter.tsx`

- O contador deve ser incrementado sempre que o botão for clicado
- Mostra o número de reações
- (Bonus) Guarda o número de reações no localStorage e acessa o valor guardado ao carregar a página

---

# Tarefa #7

## Completa a Server Action para adicionar um recurso novo

`lib/actions/resources.ts`

A função recebe um campo "url" a partir de um FormData.

- Deves ver se o recurso já existe e se sim, retornar um erro
- Obter informação do recurso submetido a partir do URL.

  > Dica: Ver as funções importadas

- Criar o recurso na base de dados.

  > Dica: Ver class `Database`

- Revalidar o cache da página inicial

---

# É tudo por hoje!

## Obrigado

---
