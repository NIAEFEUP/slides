class: center, middle, inverse, small-images

# React and Express
## How you can build the website you've always dreamed of
![](./img/ni_logo.png)

# 

# 

##### 14 November 2022

---
class: inverse

# Will this be a boring workshop?

We really hope not!

.highlight[Please feel free to interrupt and ask questions, make this more of a conversation and less of a lecture.]

<div class="flex-columns">
<div>
What we have on menu today:
.sparse[
1. Brief introduction to HTTP and Node.js
1. What is React and how to use it
1. What is Express and how to use it
1. Help us build our first website! (not exactly)
]
</div>

<div>
What we .highlight[don't] have on menu today:
.sparse[
1. Javascript
1. Deep understanding of the Web and Node.js
1. Databases
]
</div>
</div>

Please keep learning after this workshop! There are many people available to help you.

---
class: inverse

# Your Hosts

<div class="left" style="display: flex; align-items: center; gap: 1em">
<div><img width=150 src="./img/bruno.jpg" style="display: inline-block; border-radius: 30%"/></div>
<div>
    <p class="highlight">Bruno Rosendo</p>
    <p>MEIC 1st Year</p>
    <p>(Almost) Senior Backend Engineer</p>
</div>
</div>

<div class="right" style="display: flex; align-items: center; gap: 1em;justify-content: flex-end">
<div>
    <p class="highlight">João Mesquita</p>
    <p>MEIC 1st Year</p>
    <p>(Almost) Senior Frontend Engineer</p>
</div>
<div><img width=150 src="./img/joao.jpg" style="display: inline-block; border-radius: 30%"/></div>

</div>



---
class: center, middle, inverse

# HTTP
## Holy-sh*t, This Title Pops

--

### No, but really
### .highlight[Hypertext Transfer Protocol]

---

# Programming 101

Apart from variables and flow control and a few other basic concepts in programming, functions are pretty much **required** if you want to keep your code organized and readable.

It allows for code splitting in a semantically organized way.

.center[
```javascript
function main() {
    const firstName = "Nucleo";
    const lastName = "Informatica";

    console.log(
        getFullName(firstName, lastName)
    );
}

function getFullName(firstName, lastName) {
    return firstName + " " + lastName;
}
```
]

---

# Basic function structure

Usually, a function has the following sections:

.center[
```javascript
function myFunction(arg) {

    /** Validate Arguments                  **/
    /** ----------------------------------- **/
    /** Internal logic, which               **/
    /** may include calling other functions **/
    /** ----------------------------------- **/
    /** Return something                    **/

}
```
]

---

# Who you're gonna call?

Functions can also be called from outside the local process! That's usually called RPC (Remote Procedure Invocation)

.height-limit-400[![RPC Diagram](./img/rpc-diagram.png)]

---

# ~~Ghostbusters~~ RPC

With RPC, clients have access to a stub they call as if it were a local function.

However, that call is sent to another process (Can be remote or not) to be executed, and after that remote invocation responds, the stub returns the response, as if it were a local function. For the client, it's completely transparent.

This implies that the client always has access to:
* Response types 
* Possible errors/exceptions
* Available methods to call

---

# ~~Ghostbusters~~ RPC

.center[
```java
public interface BeverageServiceStub {
    public List<Double> getPrices();

    public Integer getStock(BeverageType beverage) 
        throws InvalidBeverageException;
    
    public Integer buy(BeverageType beverage, PaymentMethod payment) 
        throws InvalidBeverageException, 
        InvalidPaymentMethodException, 
        InsufficientCreditException;

    (...)
}
```
]

* Each language must have its own stub implementation to be able to call the remote service.

---
# HTTP

HTTP is a protocol used to communicate between two machines, currently used in web applications.

In a simple form:

1. Client makes a request
1. Server receives and handles the request
1. Server sends a response
1. You get to see cats on your screen

---

# REST to the RESCue

REST (Representational State Transfer) uses HTTP Status and URI rules to give meaning to calls and represent resources and operations.

Instead of .dense[`GET /getStock?beverageType=water`]

we have .dense[`GET /beverages/water/stock`]

<hr>

<div class="flex-columns">
<div>
Instead of 
.sparse[
```bash
POST /buy
{
    beverageType: water,
    quantity: 2,
    paymentMethod: {
        type: "credit-card",
        id: "1111-1111-1111-1111"
        ...
    }
}
```
]
</div>

<div>
we have
.sparse[
```bash
POST /water/buy
{
    quantity: 2,
    paymentMethod: {
        type: "credit-card",
        id: "1111-1111-1111-1111"
        ...
    }
}
```
]
</div>
</div>

---

# REST

REST focuses on **Resources** and **Operations**, instead of behaviors, like RPC. You don't call functions. You don't even know which functions exist. Only need to know about resources, and what you can do with those.

Often, the same URL is used but, by changing the HTTP Method, it gives a completely different meaning:

.dense[
```bash
POST /posts/new # Creates a new post
```
]

.dense[
```bash
GET /posts/new # Fetches the latest posts
```
]

---

# API

API (Application Programming Interface) is the specification of methods through which you can interact with a service. Often web applications use REST APIs.

Some common public APIs:
* Google Maps API https://maps.googleapis.com
* Twitter API https://api.twitter.com/

---

# HTTP Methods

HTTP has many methods, so we'll only show the most common:

* `GET` Usually used to .highlight[read] or fetch resources. Should not have secondary effects on the server.
* `POST` Usually used to interact with a resource, often causing a change in state or .highlight[side-effects].
* `PUT` Usually used to .highlight[create/replace] entities. Should be idempotent - No matter how many times you call it, the result is the same.
* `PATCH` Usually used to apply partial .highlight[updates] to a resource.
* `DELETE` Usually used to .highlight[delete] a resource.


---

# HTTP Status

Each HTTP Response has an associated Status code.

* .dense[`1XX`] Information
* .dense[`2XX`] Success
* .dense[`3XX`] Redirects
* .dense[`4XX`] Client error
* .dense[`5XX`] Server error

Check out https://http.cat!

---

# HTTP Status

Some examples:

* .dense[`201 Created`] After a successful creation of a resource
* .dense[`301 Moved Permanently`] Useful for crawlers to know when a webpage has been moved to another location
* .dense[`401 Unauthorized`] Requires authentication to access the resource
* .dense[`404 Not Found`] The requested resource does not exist
* .dense[`418 I'm a teapot`] An HTTP easter-egg
* .dense[`503 Service Unavailable`] The server is not ready to handle the request. Maybe it's under heavy load, or undergoing maintenance

---

class: center, middle, inverse,

# CORS
## Currently Out of Rad Subtitles

--

### No, but really
### .highlight[Cross-Origin Resource Sharing]

---

# CORS

CORS (Cross-Origin Resource Sharing) is a mechanism that uses additional HTTP headers to tell a browser to let a web application running at one origin (domain) have permission to access selected resources from a server at a different origin.

Due to this, you **cannot** make requests to services in different locations by default. This is the most common error for beginner web developers.

![](./img/cors-error.png)
![](./img/cors-req-headers.png)
![](./img/cors-res-headers.png)

---

# From browser to server and back

What happens when you type https://ni.fe.up.pt into the url bar on your browser?

1. It will try to find the corresponding IP (check cache).
1. If no mapping found, query DNS servers
1. Initiate a TCP connection with the server
1. Send an .dense[`HTTPS GET /`] request (sending additional informational headers along)
1. The server will receive the request and handle it (in this case generate an HTML page --- Server Side Rendering)
1. The Server sends the HTTP response with headers and HTML
1. Your browser renders NI's website

---

# HTTP web server applications

> The server will receive the request and handle it

Web applications are simply programs that listen for requests and send responses, using the HTTP protocol.

Almost any language has its version of an http server module.

The most common are Java, Python, C# and Node.js.

Today, we'll look specifically into .highlight[Node.js]

---

class: center, middle, inverse

# Node.js
### Almost Heaven

---

class: center, middle, inverse

# Node.js
## Almost Heaven
### West Virginia

---

class: center, middle, inverse

# Node.js
## Almost Heaven
### ~~West Virginia~~
### JavaScript on the server!

# 

# 

I am running out of good subtitles, really

---

# Node.js

.highlight[Node.js] is a server-side language that uses V8 JavaScript engine, which means you can use (almost) the same language you have to use on the browser, but now on the server as well!

.center[
```javascript
const http = require('http');

const server = http.createServer(function (req, res) {
    res.write('Hello World!'); // write a response to the client
    res.end(); // end the response
});

server.listen(80); //the server listens on port 80 (HTTP default)
```
]

---

# Node.js

.center[
```javascript
const server = http.createServer(function (req, res) {
    const endpoint = request.url;

    if(endpoint === "/") processHomepage(req, res);
    if(endpoint === "/about") processAboutPage(req, res);
    if(endpoint === "/store") processStorePage(req, res);
    (...)
});
```
]

---

# Node.js + Express.js = 🤍

Express.js is a web framework that abstracts some of the work involved in creating a web server in Node.js.

.center[
```javascript
const express = require('express')
const app = express()
const port = 80

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
```
]

---
class: center, middle, inverse

# Wait, did you say JS?
## JS means .highlight[JavaScript] and although it has "Java" in the name, it has NOTHING to do with it, apart from also being a programming language

---
class: center, middle, inverse

# JavaScript Theory
## Because you can't hate what you don't know

---

# Variables

.center[
```javascript
let foo; // declared but not initialized - its value is undefined
let bar = 5 // declared and initialized
const baz = "buzz" // also declared and initialized, but constant
```
]

---

# const vs let

Both `const` and `let` serve to declare variables but there are some differences:

* `let` allows the variable to be re-declared, that is, its reference or value can change
* `const` prevents this re-declaration, but it .highlight[does not] prevent mutation of non-primitive types such as Array or Object

.center[
```javascript
const a = [1]
console.log(a) // [1]
a.push(2)
console.log(a) // [1, 2]

a = [1,2,3] // Error!
```
]

To prevent mutation, use `Object.freeze()`


---

# Functions

<div class="flex-columns-center">
<div>
.center[Normal Syntax]
.sparse[
```javascript
function foo(bar) {
    return bar === "baz";
}
```
]
</div>
<div>
.center[Arrow Function Syntax]
.sparse[
```javascript
const foo = (bar) => bar === "baz";
```
]
.sparse[
```javascript
const foo = (bar) => {
    // Don't do this, it's just to show 
    // a multiline version
    const ret = bar === "baz";
    return ret;
}
```
]
</div>
</div>

Functions can be variables too! They are .highlight[first-class citizens]. 

They can be passed as parameters, can be returned from other functions, and can be tested for equality.

---

# Scopes

.center[
```javascript
const a = "global"

function func() {
    console.log(a) // global
    
    const a = "function";
    console.log(a) // function
    
    if(a) {
        const a = "block";
        console.log(a) // block
    }
    
    console.log(a) // function
}

console.log(a) // global
```
]

---

# Hey! But I've seen some vars around!

In fact, before ES6, variable declaration used to be done with the `var` keyword. That is no longer the standard way and is discouraged, since it had some memory leak problems.

Also, `var` is .highlight[function scoped], which means that the declaration would attach to the nearest function scope, unlike `let` or `const`, which belong to their blocks (ifs, loops, etc)

---

# Objects

In JavaScript, everything that is not a primitive type (string, number, boolean, etc) is an .highlight[object]. Even arrays and functions are objects.

Objects are a map-like structure that stores keys and values. The keys can be strings or numbers, but values can be whatever type you want.

.center[
```javascript
const obj = {
    myKey1: 1
    key2: {
        innerKey: true
    }
}

obj.key2.innerKey = false;
obj["myKey1"]++
```
]

---

# Arrays

Arrays are a special kind of objects, which contain a list of elements of any type. You can mix types in a single array, although you probably shouldn't.

.dense[
```javascript
const arr = [1,2,3,4];
const evenNumbers = arr.filter(num => num % 2 === 0); 
// [2,4]
```
]

.dense[
```javascript
const numberLabels = arr.map(num => `${num}-${getNumberLabel(num)}`); 
// ["1-One", "2-Two", "3-Three", "4-Four"] (assuming we have a function getNumberLabel that returns a label for a given number)
```
]

.dense[
```javascript
const sum = arr.reduce((total, current) => total + current, 0); 
// 10
```
]

---

# Array methods

These functions always return a .highlight[new] array (or value, in case of `.reduce`). They never mutate the original object, unless you specifically do it in the body of these functions (which you shouldn't)

You can combine these utilities and create a pipeline of changes for more complex stuff.

There are more functions to use such as `.find()`, `.every()` or `.join()`, the MDN docs are a good start to understand them.

---

# Iterating Arrays

Apart from the classic `for(let i = 0; i < arr.length; i++)`, you have the `for..in` and `for..of` loops.
<div class="flex-columns-center">
<div>
.dense[
```javascript
const arr = ["foo", "bar", "baz"];
for(const key in arr) {
    console.log(key)
}
// 0
// 1
// 2
```
]
</div>

<div>
.dense[
```javascript
const arr = ["foo", "bar", "baz"];
for(const key of arr) {
    console.log(key)
}
// "foo"
// "bar"
// "baz"
```
]
</div>
</div>

---

# Iterating Objects

<div class="flex-columns-center">
<div>
.dense[
```javascript
const obj = {foo: true, bar: false};
for(const key in obj) {
    console.log(key)
}
// "foo"
// "bar"
```
]
</div>

<div>
.dense[
```javascript
const obj = {foo: true, bar: false};
for(const key of obj) {
    console.log(key)
}
// true
// false
```
]
</div>
</div>

---

# What sorcery is *this* ?

The `this` keyword generally refers to the current context of execution. It is implicitly passed when calling functions.

* Inside a function, it refers to the context of where the function was called from, unless otherwise specified.

* Under normal circumstances, `this` will refer to the global object in Node.js (equivalent to the `window` object in the browser)
* If a function is an object property, `this` will refer to the object itself. This is useful to have fields that derive from others.

.center.dense[
```javascript
const person = {
    name: "John",
    surname: "Smith",
    getFullName: function() { return this.name + " " + this.surname; }
}
```
]

---

# What sorcery is *this* ?

Similarly to the objects' behavior, inside a class, `this` corresponds to the class instance. After all, Classes are glorified objects.

.center[
```javascript
class Person {
    constructor(name, surname) {
        this.name = name;
        this.surname = surname;
    }
    
    getFullName() {
        return this.name + " " + this.surname;
    }
}
```
]

---

# What's this, Mr. Arrow?

The biggest difference between normal functions and arrow functions is that arrow functions do not bind their own `this`.

Instead, they inherit the one from the parent scope, which is called "lexical scoping". This makes arrow functions to be a great choice in some scenarios but a very bad one in others.

This is why you cannot use arrow functions in class methods, for example.

---

# Super Example

.center[
```javascript
class Hero {
  constructor() {
    this.powerName = "Super Punch"
    this.buildSuperPower()
  }

  printPowerName() {
    console.log("this", this)
    console.info(this.powerName + " is ready!")
  }

  buildSuperPower() {
    console.info("Initiated Timer");
    setTimeout(this.printPowerName, 500)
    //setTimeout(() => this.printPowerName(), 500)
  }
}

const hero = new Hero()
```
]

---

# Super Example
The code as is (with L14 being executed) will print "undefined is ready!" since the this that is passed to the printPowerName is the context of the setTimeout upon invocation.

If an arrow function is used instead, the this corresponds to the context of where the function is defined, which is the context of buildSuperPower, which in turn will be the Hero instance. In this case, the print is correct: "Super Punch is ready!"

---

class: center, middle, inverse, small-images

# This time the title is in the subtitle
## I Promise

---

# Promises

Imagine MIEIC's professors were JavaScript entities. Imagine you called the method `getGrades()`. It would obviously take too long, right?

If only there was a way for you to do something else while they don't answer back... They could **promise** they would answer some time in the future, and you would go on your way, only to face another teacher that didn't have the grades ready...

---

# Promises

Well, Promises are exactly that: Structures that eventually turn into data or error out. They have 3 possible states:

* Pending: While not fulfilled or rejected
* Fulfilled: When the work has finished, represents the result
* Rejected: When some error occurred, represents the error

.center[
```javascript
const sleep = (time) => new Promise((resolve) => {
    setTimeout(()=>{resolve()}, time)
})

sleep(1000).then(() => {console.log("Time's up!")})

console.log("I can't wait!"); // This will execute first
```
]

---

# Promises, but better

## Async/Await Syntax

```javascript
const longFunction = () => new Promise((resolve, reject) => {
    try {
        const {result, error} = doSomeLongComputation();
        if(error) return reject(error)

        return resolve(result);

    } catch (err) {
        reject(err)
    }
})

longFunction()
    .then((value) => { console.log(value) })
    .catch((err) => { console.error(err) })
```

---

# Promises, but better

## Async/Await Syntax

```javascript
const longFunction = async () => {
   
    const {result, error} = doSomeLongComputation();
    if (error) throw error

    return result;
    
})

const someOtherFunction = async () => {
    try {
        const result = await longFunction();
    } catch (err) {
        console.error(err)
    }
} 
```

---

class: center, middle, inverse

# Node.js specifics
## This introduces the next module

# 

# 

--

#### You'll understand this subtitle in a few slides...

---

# npm

.highlight[npm] is the package manager for Node.js. The basic commands you need to know are:

.dense[
```bash
# Bootstraps the project, creating the package.json
npm init
```
]

.dense[
```bash
# Adds a dependency to package.json and installs it locally 
npm install <package>
```
]

.dense[
```bash
# Runs a command as defined in the `scripts` section on package.json
npm run <cmd>
```
]

---

# User defined modules

Usually in Node.js applications, you will split the code in multiple files and folders, creating .highlight[modules].

Each module exports whatever it needs, including variables (will be constant) or functions, which can be imported by any other module (as long as there is no circular dependency 👀)

.dense[
```javascript
const myVar = "CONSTANT_STUFF"

module.exports = myVar;

// Import with
const importedVar = require("./path-to-other-module") // "CONSTANT_STUFF"

```
]

To export multiple values, export an object with a property for each thing you want to share.

---

# Built-in Modules

Node.js includes some modules such as .highlight[fs] and .highlight[path] to help you interact more easily with the file system.

.center[
```javascript
const fs = require("fs");
const path = require("path");

const filePath = path.join(__dirname, <file path relative to file>);

fs.readFile(filePath, "utf8", (err, data) => {
    // Handle Data
});

```
]

Let's see an example...

---

class: center, middle, inverse

# Node.js in practice
## < enter subtitle here >

---

# Express.js

Express.js is a web framework that helps you define the routes of you API. It has a nice feature which are .highlight[middleware] functions.

Middleware runs between the request arrival and the route handler body, so it's useful for validation logic, for example, or some logic you want to run every time you receive a request such as logging.

.dense.center[
```javascript

const mustBeAValidName = (req,res,next) => {
    if(req.query.name !== "Alice" && req.query.name !== "Bob") {
        return next("I only greet Alice and Bob!");
    } 
    else next()
}

app.get("/hello", 
    mustBeAValidName, 
    (req,res,next) => {
        res.status(200).send(`Hello, ${req.query.name}`);
    }
)
```
]

---

# Express.js

## The Request Handler

.dense.center[
```javascript

// Also receives query parameters in req.query
// and body in req.body
app.get("/hello/:name", 
    (req,res,next) => {
        res.status(200).send(`Hello, ${req.param.name}`);
    }
)
```
]

---

# Databases

In practice, applications use a .highlight[database] to store data permanently. As it is not in the scope of this workshop, let's just say that databases allow CRUD operations (Create, Read, Update, and Delete).

Usually, interacting with them directly is quite verbose so there are frameworks that abstract some of this for the developers.

---

# MongoDB --- Mongoose

One of the used databases is MongoDB. 

MongoDB stores information in "documents", which are similar to JS Objects.

Mongoose lets you define a Model, which defines a structure (Schema) for those entities, and provides utilities to execute the CRUD operations.

---
# MongoDB --- Mongoose

.dense.center[
```javascript

const AccountSchema = new Schema({
    email: {
        type: String,
        trim: true,
        lowercase: true,
        unique: true,
        required: true,
    },
    password: { type: String, required: true },
});

const Account = mongoose.model("Account", AccountSchema);

await Account.find();
await Account.create({email, password});
```
]

---

class: center, middle, inverse

# NIJobs
## A Node.js based API for with job advertisements for students

# 

# 

#### Made by NIAEFEUP

---

# NIJobs

NIJobs uses the concepts introduced so far to expose an API that allows for Companies to have accounts and create offers, which are searchable. Additionally, we have Admins we can oversee operations and take action if needed.

We split the application in two parts: Backend and Frontend

---

# NIJobs --- Backend

The Backend has the following structure:

* src/
    * api/
        * routes/ - Methods that register endpoints for the app
        * middleware/ - Application middleware. For example validators go here
    * lib/ - Supporting code
    * loaders/ - Modules responsible for the startup process
    * models/ - Database entity models (Mongoose models)
    * services/ - Business logic for the controllers
    * config/ - Application config (settings, authentication, etc.)
        * env.js - Environment variables and related configurations
    * index.js - App entry point

---

# NIJobs --- Frontend

The Frontend is a separate application that is a React app. It is merely a client that makes requests to the API (Backend), and allows us to separate the view logic from the "business" logic.

To learn more about how we do it, check next week's workshop on React ;)

---

class: center, middle, inverse

# Putting the hands in the pasta
## Direct translations from Portuguese never work...

---

# Hand me That Tasty Peverage

.dense[`git clone https://github.com/NIAEFEUP/workshop-node-2021/`]

A Drinks Vending machine powered by HTTP.

This application is used to buy drinks on a vending machine, but it lacks implementation, because it was an LGP project and they lost too much time on "Ideation phase" 👀.

You can use .highlight[hoppscotch.io] to test your API in the browser (beware of CORS), or .highlight[Postman] or .highlight[httpie] if you and something running locally.

---

# Hand me That Tasty Peverage

// TODO: Return drinks and their information (price, description, etc.)

// TODO: Get a specific drink's information

// TODO: Purchase units of a drink and reduce stock. Only one drink type at a time.

// TODO: Add stock back to the vending machine! Also only one drink type at a time for now!

// TODO: Edit a drink's description and information (price, etc.)

// TODO: Add a drink to the system

// TODO: Remove a drink from the system