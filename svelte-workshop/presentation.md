name: title
layout: true
class: center, middle, inverse

---

name: normal
layout: true
class: left, middle

---

class: center, middle, inverse, small-images

# Svelte Workshop

<div style="display: flex; justify-content: center; margin-top: 3em; align-items: center; gap: 1em;">
  <img src="./assets/logos/ni.png">
  <div style="font-size: 2.5em; padding-inline: 0.5em;">❤️</div>
  <img src="./assets/logos/svelte.png">
</div>

---

class: center, middle, inverse

# Important links

#### This presentation is available online from the link below:

<div style="display: flex; justify-content: center; align-items: center; margin: 4rem 0rem;">
  <a href="https://slides.niaefeup.pt/slides/svelte-workshop" style="color: white; font-weight:bold; font-size: 1.5rem; text-align:center;">https://slides.niaefeup.pt/svelte-workshop</a>
</div>

#### Svelte's Documentation:

<div style="display: flex; justify-content: center; align-items: center; margin: 4rem 0rem;">
  <a href="https://svelte.dev/docs/svelte" style="color: white; font-weight:bold; font-size: 1.5rem; text-align:center;">https://svelte.dev/docs/svelte</a>
</div>

---

class: center, inverse, middle

## Please don't let this be a monologue

#### Feel free to ask any questions anytime

---

class: middle

# Index

- [Fundamentals](#fundamentals)
- [Components](#components)
- [Reactivity](#reactivity)
- [Control Flow](#control-flow)
- [SvelteKit Basics](#sveltekit-basics)

---

template: title
name: fundamentals

# Fundamentals

---

class: middle

# What is Svelte?

Svelte is a **framework** for building user interfaces.

---

class: middle

## ... But what is a framework?

---

class: middle

## ... But what is a framework?

A **framework** is a set of tools and conventions that helps you build applications more easily.

It provides a robust foundation for your application by offering:

- A defined architecture: Guiding you on how to structure your code effectively
- A component model: Encouraging you to build your UI with modular and reusable pieces
- Built-in solutions: Handling complex tasks like state management and DOM updates automatically

---

# What is Svelte?

Svelte is a **framework** for building user interfaces.

Unlike traditional frameworks, Svelte shifts much of the work to **compile time**, turning declarative components into _plain_ HTML, CSS and JavaScript.

---

class: middle

# Why use Svelte?

- Simple and easy to learn (great developer experience)
- Less boilerplate code (repetitive setup)
- Small bundle sizes (faster websites)

---

class: middle

# Svelte vs. HTML/CSS/JS

- HTML/CSS/JS: You manually update the DOM and manage state 🫩
- Svelte:
  - Lets you write less code to achieve the same results 🤩
  - Handles reactivity and updates for you 🚀
  - Compiles your code to efficient, plain JavaScript 🧠

---

class: middle

# How Svelte works

- Svelte is a **compiler**, not a runtime framework
- It converts your components into optimized JavaScript at build time
- No framework code shipped to the browser
- Output is just HTML, CSS, and JS

---

class: middle

# Hello World

```svelte
<!-- hello.svelte -->
<script>
  let name = 'world';
</script>

<h1>Hello, {name}!</h1>
```

---

class: middle

# .svelte File Structure

A `.svelte` file has **three sections** that you can use (all optional):

```svelte
<script>
  // JavaScript code goes here
  // Variables, functions, logic
</script>

<style>
  /* CSS styles go here */
  /* Scoped to this component only! */
</style>

<!-- HTML goes here -->
<!-- This is what users will see -->
```

All in a single file!

---

class: middle

# SvelteKit Project Structure

```tree
my-svelte-app/
├── src/
│   ├── routes/                     # Your pages (file-based routing)
│   │   ├── +page.svelte            # Home page (/)
│   │   ├── +layout.svelte          # Shared layout for all pages
│   │   └── about/
│   │       └── +page.svelte        # About page (/about)
│   ├── lib/                        # Reusable code
│   │   ├── components/             # Your components
│   │   │   └── Header.svelte
│   │   └── index.ts
│   └── app.html                    # HTML template (rarely changed)
├── static/                         # Static files (served as-is)
│   └── favicon.png
└── package.json                    # Project dependencies
```

---

class: middle

## Understanding the Structure

- **`src/routes/`**: Each folder/file becomes a page (file-based routing)

  - `+page.svelte` creates a page at that route
  - `+layout.svelte` provides shared UI for multiple pages
  - Folders create URL paths (e.g., `about/+page.svelte` → `/about`)

- **`src/lib/`**: Your reusable components and utilities

  - Use the `$lib` alias to import (e.g., `import Header from '$lib/components/Header.svelte'`)

- **`static/`**: Static assets served directly (images, fonts, favicon, etc.)

- **`app.html`**: The base HTML template that wraps your entire app
  - Usually you don’t need to edit this

---

class: middle, center

## Let's Try It Out!

#### Svelte REPL (Read-Eval-Print Loop)

A playground where you can write Svelte code instantly in your browser

#### [svelte.dev/repl](https://svelte.dev/repl)

---

template: title
name: components

# Components

---

class: middle

# What are Components?

Think of components as **custom HTML elements** that you create yourself.

Just like how you use `<div>`, `<button>`, or `<img>` in HTML, you can create your own tags like `<Header>`, `<Card>`, or `<TodoItem>`.

---

class: middle

# Why Use Components?

**Reusability:** Write once, use everywhere

**Organization:** Break complex UIs into smaller, manageable pieces

**Maintainability:** Easier to find and fix bugs

**Teamwork:** Different people can work on different components

---

class: middle

# Your First Component

Let's create a simple greeting component:

```svelte
<!-- Greeting.svelte -->
<script>
  let name = 'Student';
</script>

<div class="greeting">
  <h2>Hello, {name}!</h2>
  <p>Welcome to the Svelte workshop!</p>
</div>
```

---

class: middle

# Using Your Component

Once you've created a component, you can use it in other files:

```svelte
<!-- +page.svelte -->
<script>
  import Greeting from './Greeting.svelte';
</script>

<main>
  <Greeting />
  <p>This is my web page!</p>
</main>
```

---

class: middle

## Component Props (Parameters)

Props let you pass data **into** components, like function parameters:

```svelte
<!-- StudentCard.svelte -->
<script>
  let { name, course, year = 1 } = $props();
</script>

<div class="card">
  <h3>{name}</h3>
  <p>{course} - Year {year}</p>
</div>
```

**`$props()`** gets the data passed from the parent component

---

class: middle

# Passing Props

```svelte
<!-- +page.svelte -->
<script>
  import StudentCard from '$lib/components/StudentCard.svelte';
</script>

<main>
  <h1>Our Students</h1>
  <StudentCard name="Alice" course="Computer Science" year={2} />
  <StudentCard name="Bob" course="Engineering" />
  <StudentCard name="Carol" course="Design" year={3} />
</main>
```

- Strings: `name="Alice"`
- Numbers/Variables: `year={2}` or `year={studentYear}`
- Default values: `year = 1` (when not provided)

---

class: middle

# Component Best Practices

- **File Organization:**

  - Keep components in `src/lib/components/`
  - If the component is scoped to a speficific page, keep it in `src/routes/[page]/_components/`

- **Single Responsibility:**

  - Each component should do one thing well
  - If it's getting too complex, split it up

- **Clear Props:**

  - Use descriptive prop names
  - Provide sensible defaults
  - Consider which props are required vs optional

---

template: title
name: reactivity

# Reactivity

---

class: middle

# What is Reactivity?

**Reactivity** means your UI automatically updates when data changes.

In plain JavaScript, if you change a variable, you need to manually update the DOM.

With Svelte, when reactive data changes, the UI updates **automatically**! ✨

---

class: middle

# What are Runes?

**Runes** are special symbols in Svelte that control reactivity.

- They start with a `$` sign (like `$state`, `$derived`)
- They look like functions but are actually **compiler keywords**
- They tell Svelte: "Hey, track this value and update the UI when it changes!"

---

class: middle

# The Main Runes

We'll cover four essential runes:

1. **`$state`** - Create reactive variables
2. **`$derived`** - Create values that automatically update based on other values
3. **`$effect`** - Run code when reactive values change (side effects)
4. **`$props`** - Receive data from parent components

---

class: middle

## 1. $state - Reactive Variables

`$state` creates a reactive variable. When it changes, the UI updates automatically.

```svelte
<script>
  let count = $state(0);

  function increment() {
    count += 1;
  }
</script>

<button onclick={increment}>
  Clicked {count} {count === 1 ? 'time' : 'times'}
</button>
```

Every time you click, `count` changes and the button text updates!

---

class: middle

## 2. $derived - Computed Values

`$derived` creates values that **automatically update** when their dependencies change.

```svelte
<script>
  let numbers = $state([1, 2, 3, 4]);
  let total = $derived(numbers.reduce((t, n) => t + n, 0));

  function addNumber() {
    numbers.push(numbers.length + 1);
  }
</script>

<p>{numbers.join(' + ')} = {total}</p>

<button onclick={addNumber}>
  Add a number
</button>

```

You never have to manually update `numbers` or `total`, they update automatically!

---

class: middle

## 3. $effect - Side Effects

`$effect` runs code when reactive values change. Use it for **side effects** (actions that affect things outside your component).

Think of it as: _"When this data changes, do something extra"_

```svelte
<script>
  let count = $state(0);

  $effect(() => {
    console.log(`Count is now: ${count}`);
  });
</script>

<button onclick={() => count++}>Count: {count}</button>
```

Every time `count` changes, the effect runs and logs the new value

---

class: middle

## When NOT to Use $effect

❌ **Don't** use `$effect` to create derived state:

```svelte
// BAD - Don't do this!
let count = $state(0);
let doubled = $state(0);

$effect(() => {
  doubled = count * 2; // Wrong approach!
});
```

✅ **Do** use `$derived` instead:

```svelte
// GOOD - Do this!
let count = $state(0);
let doubled = $derived(count * 2); // Correct!
```

**Rule of thumb:** Use `$derived` for values, `$effect` for actions.

---

class: middle

## 4. $props - Component Props

`$props` receives data from parent components.

```svelte
<!-- Child.svelte -->
<script>
  let { name, age = 18 } = $props();
</script>

<p>Hello {name}! You are {age} years old.</p>
```

```svelte
<!-- Parent.svelte -->
<script>
  import Child from './Child.svelte';
</script>

<Child name="Bob" age={25} />
<Child name="Carol" />
```

---

template: title
name: control1-flow

# Control Flow

---

template: title
name: sveltekit-basics

# SvelteKit Basics
