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

template: title
name: reactivity

# Reactivity

---

template: title
name: control1-flow

# Control Flow

---

template: title
name: sveltekit-basics

# SvelteKit Basics
