name: title
layout: true
class: center, middle, inverse

---

name: normal
layout: true
class: left, middle

---

class: center, middle, inverse, small-images

# NestJS Workshop

<div style="display: flex; justify-content: center; margin-top: 3em; align-items: center; gap: 1em;">
  <img src="./assets/logos/ni.png">
  <div style="font-size: 2.5em; padding-inline: 0.5em;">❤️</div>
  <img src="./assets/logos/nestjs.png">
</div>

---

class: center, middle, inverse

# Important links

#### This presentation is available online from the link below

<div style="display: flex; justify-content: center; align-items: center; margin: 4rem 0rem;">
  <a href="https://slides.niaefeup.pt/slides/nestjs-workshop/" style="color: white; font-weight:bold; font-size: 1.5rem; text-align:center;">https://slides.niaefeup.pt/nestjs-workshop/</a>
</div>

#### NestJS's Documentation

<div style="display: flex; justify-content: center; align-items: center; margin: 4rem 0rem;">
  <a href="https://docs.nestjs.com/" style="color: white; font-weight:bold; font-size: 1.5rem; text-align:center;">https://docs.nestjs.com/</a>
</div>

---

class: center, inverse, middle

## Please don't let this be a monologue

#### Feel free to ask any questions anytime

---

class: middle

# Index

- [Web Basics](#web-basics) - HTTP, REST
- [Project Structure](#project-structure) - Entity, DTO, Service, Controller, Module
- [Dependency Injection](#dependency-injection) - Decorators, providers
- [Guards](#guards) - Authentication & authorization
- [Exception Filters](#exception-filters) - Custom error handling
- [Live Demo](#live-demo) - Building a simple API from scratch
- [Niddle Codebase Walkthrough](#niddle-codebase) - Real-world project structure

---

name: web-basics
template: title

# Web Basics

---

# How do websites work?

Every app you use (UNI, SIGARRA, Instagram) needs to:

- **Store data** - users, posts, grades
- **Send that data to your screen** - so you can see it and interact with it

Think of it like a _restaurant_:

- You (the **frontend**) look at a menu and place an order
- The kitchen (the **backend**) prepares your food
- A waiter (**HTTP**) delivers it back to you

---

# Frontend vs Backend

.horizontal[

- What you **see** and **interact with**
- Buttons, pages, forms, animations
- Runs inside your **browser**
- Built with HTML, CSS, JavaScript


- The **brain** behind the scenes
- Stores data, enforces rules, does the heavy lifting
- Runs on a **server** (a computer somewhere on the internet)
- Usually built with frameworks like **NestJS**
]

The frontend **asks** the backend for data. The backend **replies** with it.

---

# What is an API?

Now that we know the frontend needs data from the backend, _how_ do they talk?

**A**pplication **P**rogramming **I**nterface

An API is a **contract** between the frontend and the backend:

> "If you send me **this**, I'll respond with **that**"

Think of it like a **menu at a restaurant**:

- You don't need to know _how_ the kitchen cooks your food
- You just need to know _what you can order_ and _what you'll get_
- The menu is the **API**

In web apps, an API is a set of **URLs** (called **endpoints**) that you can talk to.

---

# How do they talk? - HTTP

**H**yper**T**ext **T**ransfer **P**rotocol

If the API is the **menu** (what you can order), HTTP is the **language** you use to place the order.

- Every conversation has two parts:
  - A **request** - what the client (your browser) asks for
  - A **response** - what the server sends back
- It's **stateless**: every request is independent

> The server does not keep any state between requests!

---

# HTTP Requests

Every request has three key parts:

- **Method** - _What_ you want to do
- **URL / Endpoint** - _Which_ resource you're asking about
- **Body** (optional) - _Extra data_ you're sending

```txt
GET /users/42
```

> "Give me user number 42"

```txt
POST /users
Body: { "name": "Alice", "age": 20 }
```

> "Create a new user called Alice, age 20"

---

# Responses & Status Codes

Every response comes with a **status code** - tells you what happened.

- **`2xx` Success** - everything went fine
  - `200 OK` - here's your data
  - `201 Created` - your resource was created

- **`4xx` Client error** - _you_ messed up
  - `404 Not Found` - that resource doesn't exist
  - `401 Unauthorized` - you're not logged in

- **`5xx` Server error** - _the server_ messed up
  - `500 Internal Server Error` - something broke on our side

---

# Methods - CRUD

CRUD is a concept - the four basic operations on any data. HTTP methods are how we **implement** CRUD in our API:

- **GET** - **R**ead -> fetch data
- **POST** - **C**reate -> send new data
- **PUT** - **U**pdate -> replace existing data
- **DELETE** - **D**elete -> remove data

---

# What is REST?

**RE**presentational **S**tate **T**ransfer

REST is a convention for designing your API so that it uses **HTTP methods** to perform **CRUD operations** on **resources** identified by **URLs**:

- Resources are identified by **URLs**
  - `/users` - all users
  - `/posts/5` - post number 5
- Use **HTTP methods** to act on those resources
  - `GET /users` -> list all users
  - `DELETE /posts/5` -> delete post #5
- Data is exchanged as **JSON**

> REST is the "style guide" of web APIs.

---

# What is JSON?

**J**ava**S**cript **O**bject **N**otation

A lightweight, human-readable text format for exchanging data:

```json
{
  "name": "Alice",
  "age": 20,
  "courses": ["LTW", "AC"]
}
```

- It's just **key-value pairs** (like a dictionary in Python)
- Almost every web API in the world sends and receives JSON
- JavaScript can parse it natively - `JSON.parse()` and `JSON.stringify()`

---

# Putting it all together

Here's what happens when you open a webpage and it loads your profile:

```txt
1. Browser sends an HTTP request (API endpoint):
   GET /users/42

2. Backend receives the request:
   Queries the database for user #42

3. Backend sends an HTTP response (JSON data):
   Status: 200 OK
   Body: { "name": "Alice", "age": 20 }

4. Browser receives the JSON response:
   Renders your profile on screen
```

That's it! (Almost) Every interaction on the web follows this same pattern.

---

template: title

## Thank you!
