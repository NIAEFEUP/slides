class: center, middle, inverse, small-images

# **JavaScript Workshop**



<div style="display: flex; justify-content: center; margin-top: 3em; align-items: center; gap: 2em;">
<img src="./assets/logos/niaefeup.png">
<img src="./assets/logos/js.png">

<div class="footer">April 2025</div>

---

class: inverse, center, middle, small-images

### You can follow the presentation here

<a href="https://slides.niaefeup.pt/js-workshop" class="line">https://slides.niaefeup.pt/js-workshop</a>

<img src="./assets/logos/niaefeup.png"><br></br>

---

class: inverse, center, middle

# Your Host

<img src="./assets/profile.jpg" height=210 width=210 style="border-radius: 50%; object-fit: cover">

### **Pedro Nunes**

#### M.EIC Finalist and NIAEFEUP Member

---

class: inverse, middle, center

# **Introduction**

---

class: inverse, middle

## **What is JavaScript?**

- JavaScript is a dynamic, imperative and functional language
- Along with HTML and CSS, JavaScript is one of the three main technologies used in the Web
- It has many uses, but it's most commonly used as a client-side scripting language (in browsers)

---

class: inverse, middle

## **Without JavaScript in the Web**

- Websites would just be styled, static documents (HTML + CSS) 
- Very underwhelming **user experience** for our standards
- Much different from the modern websites we use today 

---

class: inverse, middle

## **(from most websites)**

<div class="large-images center">
<img src="./assets/sigarra.png">

---

class: inverse, middle, center

# **Syntax**

---

class: inverse, middle

## **Automatic Semicolons**

Statements are separated by semicolons:

```javascript
console.log(123); console.log('abc');
``` 

But these can be omitted where there is a line break:

```javascript
console.log(123)
console.log('abc')
``` 

---

class: inverse, middle

## **Variables**

JavaScript is a **loosely/weakly** and **dynamically** typed language:

- values have types, variables do not
- types are checked at runtime

There are 3 ways to initialize a variable:

- **let**: Initialize a variable that can change its value
- **const**: Initialize a constant variable (will never change its value)
- **var**: Don't use it (don't ask me why)

---

class: inverse, middle

## **Primitive Data Types**

- **Number** (double-precision 64-bit which represents integers and floating point values, e.g. 3.14, 10)
- **String** (textual data, e.g. 'hello', "grill")
- **Boolean** (true or false)
- **BigInt** (numbers of arbitrary length not representable by Number, e.g. 123456789n)
- **Null** (absence of any object value, case sensitive - null)
- **Undefined** (absence of any object value, case sensitive - undefined)

---

class: inverse, middle

## **Type Conversion**

Most of the time, operators and functions automatically convert a value to the right type (type conversion)

```javascript
console.log("Hello" + "World"); // 'Hello world'
console.log(13.5 + 29); // 42.5
console.log("13.5" + 29); //'13.529'
```

You can use the String, Number and Boolean functions to manually convert a value

```javascript
const a = 0;
const b = Boolean(a); // false
const c = String(a); // '0'
const d = String(b); // 'false'
```

To convert from a string to a number, we can use the parseInt and parseFloat functions

```javascript
console.log(parseFloat("123.4")); // 123.4
console.log(parseInt("123", 10)); // 123
console.log(parseInt("123", 8)); // 83
console.log(parseInt("0123")); // 123 or 83 in some browsers
```

---

class: inverse, middle

## **Comparison**

When comparing values belonging to different types, they are converted to numbers

```javascript
1 == "1"; // 1 == 1 -> true
0 == false; // 0 == 0 -> true
"0" == true; // 0 == 1 -> false
"" == false; // 0 == 0 -> true
Boolean("0") == false; // 1 == 0 -> false
Boolean("0") == true; // 1 == 1 -> true
```

## **Strict Equality**

In strict equality neither of the values is converted, if the values are from different type they are unequal

```javascript
0 === 0; // true
0 === "0"; // false
0 === false; // false
```

---

class: inverse, middle

## **Type Of**

We can use the typeof function to check the type of a variable

```javascript
console.log(typeof undefined)         // "undefined"
console.log(typeof 0)                 // "number"
console.log(typeof 10n)               // "bigint"
console.log(typeof true)              // "boolean"
console.log(typeof 'foo')             // "string"
console.log(typeof new Boolean(true)) // "object"
console.log(typeof Boolean(true))     // "boolean"
console.log(typeof null)              // "object"
console.log(typeof console.log)       // "function"
```

---

class: inverse, middle

## **Loop through Objects/Arrays**

The **for ... in** statement iterates over all properties of an object

```javascript
const person = { name: 'António Santos', age: 40 }

for (let key in person)
  console.log(`${key} = ${person[key]}`)

// name = António Santos
// age = 40
```

You can use a **for ... of** loop to iterate over array elements

```javascript
const years = [2002, 2003, 2004, 2005]

for (const year of years)
  console.log(year)
```


---

class: inverse, middle

## **Functions**


```javascript
function add(num1, num2) {
  return num1 + num2;
}

let result = add(1, 2);
console.log(result); // 3
```

- **Primitive** parameters are passed to functions by **value**
- **Non-primitive** parameters (objects) are passed by **reference**

Functions can also **return** any value (if no return is used it'll return undefined)

---

class: inverse, middle

## **Alternative Function Declarations**

```javascript
const add = function (num1, num2) {
  return num1 + num2;
}

let result = add(1, 2);
console.log(result); // 3
```

```javascript
const add = (num1, num2) => num1 + num2;

let result = add(1, 2);
console.log(result); // 3
```

---

class: inverse, middle

## **Functions as Parameters**

```javascript
function foo(i) {
  console.log('bar = ' + i)
}

function executeNTimes(f, n) { // Executes function f, n times
  for (let i = 0; i < n; i++)
    f(i)
}

executeNTimes(foo, 3)   // bar = 0 bar = 1 bar = 2
```

---

class: inverse, middle

## **Error Handling**

- The **try** block contains statements to try

- The **catch** block contains code to deal with any exception thrown inside the try block

- The **finally** block executes regardless of whether an exception is thrown. Useful for cleanup operations (e.g., closing a connection)


```javascript
try {
  veryRealFunctionThatExists(); // it doesn't
  console.log("I will not print");
} catch (e) {
  console.log(e); // prints the error
  throw new Error("💥"); // uncaught exception
} finally {
  console.log("I always print");
}
console.log("Will I print?");
```

---

class: inverse, middle

## **Error Handling**

We can deal with different types of errors

```javascript
catch (e) {
  if (e instanceof DatabaseError) {
    // statements to handle DatabaseError exceptions
  }
  if (e instanceof SomethingElseError) {
    // statements to handle SomethingElseError exceptions
  }
}
```

---

class: inverse, middle

## **Async**

JavaScript is a **single-threaded** language! Code is executed sequencialy

If a function takes some time to execute our website will freze until the function has finished its execution

```javascript
const takes_one_minute = () => sleep(60);
const takes_two_minutes = () => sleep(120);

takes_one_minute(); // takes one minute to finish its execution
takes_two_minutes(); // takes two minutes to finish its execution
rest_of_the_code(); // this will only run after 3 minutes
```

We can circumvent this by scheduling **asynchronous** actions in JavaScript Runtime Environments

---

class: inverse, middle

## **Async**

We get asynchronous code by adding the keyword **async** to function declarations

```javascript
const takes_one_minute = async () => sleep(60);
const takes_two_minutes = async () => sleep(120);

takes_one_minute(); // takes one minute to finish its execution
takes_two_minutes(); // takes two minutes to finish its execution
rest_of_the_code(); // this will start running at the same time of the other two
```

---

class: inverse, middle

## **Await**

The **await** keyword instructs JavaScript to pause the execution of an async function until the awaited *Promise* (more on that soon) is returned 

- **await** only works inside async functions
- **await** suspends the current function without blocking the main thread

```javascript
async function fileLength(filename) {
  const contents = await readFile(filename)
  return contents.length
}
```

---

class: inverse, middle

## **Promises**

A promise represents the eventual result of an asynchronous operation (async functions always return a promise)

- A promise may be in one of 3 possible states: **fulfilled**, **rejected**, or **pending**

```javascript
const promise = new Promise((resolve, reject) => {
  readFile('file.txt', (err, data) => {
    if (err) reject(err)
    else resolve(data)
  })
})
```

When the promise resolves or is rejected, we can use **.then** and **.catch** to consume it (register a function to be called when the promise is resolved or rejected, respectively)

```javascript
promise
  .then((content) => console.log(content))
  .catch((error) => console.log(error));
```

---

class: inverse, middle, center

# **DOM**

---

class: inverse, middle, medium-images

## **What is the DOM**

- The **Document Object Model** (DOM) is a representation of a web page as a tree of nodes
- It allow us to programmaticaly access the tree and change the document **structure**, **style** and **content**
- It can be manipulated from the browser using **⋆JavaScript⋆**

<div style="display: flex; justify-content: center; align-items: center;">
<img src="./assets/dom.png">

---

class: inverse, middle

## **Selecting Elements**

- **getElementById(id)** returns an Element <br>
  <small>returns the element with the specified id </small>
- **getElementsByClassName(class)** returns a NodeList <br>
  <small> returns all elements with the specified class </small>
- **getElementsByTagName(name)** returns a NodeList <br>
  <small> returns all elements with the specified tag name </small>
- **querySelector(selector)** returns an Element <br>
  <small> returns _the first element_ selected by the specified CSS selector </small>
- **querySelectorAll(selector)** returns a NodeList <br>
  <small> returns _all elements_ selected by the specified CSS selector </small>

```javascript
const menu = document.getElementById("menu");
const paragraphs = document.getElementsByTagName("p");
const intros = document.querySelectorAll("article p:first-child");
const links = menu.querySelectorAll("a");
```

---

class: inverse, middle

## **Traversing**

You can also get access to other elements related to the selected one by traversing the tree

```html
<div id="container">
  <p>First paragraph</p>
  <p>Second paragraph</p>
</div>
```

```javascript
const container = document.getElementById("container");

container.firstChild.textContent; /* #text (whitespace before <p>) */
container.firstElementChild.textContent; /* First Paragraph */
container.firstElementChild.nextElementSibling.textContent; /* Second Paragraph */
container.lastElementChild.textContent; /* Second Paragraph */
```

---

class: inverse, middle

## **Altering Elements**

After selecting an Element, you can access and alter its:

- Attributes
- Class List
- Style
- HTML Code

```javascript
const elem = document.getElementById('myDiv');
elem.setAttribute('title', 'Hello!');
elem.classList.replace('old-class', 'new-class');
elem.style.backgroundColor = 'lightblue';
elem.innerHTML = 'New content here!';
```

And even apply some methods to it:

- **focus()** – Sets keyboard focus on the element
- **click()** – Simulates a mouse click on the element
- ...

---

class: inverse, middle

## **Altering Elements**

You can also **create**, **insert** or **remove** elements

```javascript
const link = document.querySelector("a");
const label = document.createElement("span");
label.textContent = "[Link] "; /* sets the span's text */
link.parentNode.insertBefore(
  label,
  link
); /* inserts the label before the link */

link.remove();
```

---

class: inverse, middle

## **Events**

**Events** are occurrences that happen in the system

Specific events in specific objects can have event handlers attached to them

When the event happens, the attached handler is called

Some possible events:

- **Mouse** - click, dblclick, mouseup, mousenter, mouseleave, mouseover
- **Forms** - input, focus, submit
- **Keyboard** - keydown, keyup, keypress

---

class: inverse, middle

## **Event Handlers**

On modern browsers, the **addEventListener** function is the most common way to attach event handlers

```javascript
function handleEvent() {
  console.log("User clicked button");
}

const button = document.querySelector("button");
button.addEventListener("click", handleEvent);
```

---

class: inverse, middle

## **Event Handlers**

A function that handles an event can receive a parameter representing the event

- Events can have different properties and methods
- We can use the **preventDefault** method to ensure that the default behavior is suppressed (e.g. a link isn't followed or a form isn't submitted)

```javascript
function handleEvent(event) {
  event.preventDefault()
}

const button = document.querySelector("button")
button.addEventListener('click', handleEvent)
```

---

class: inverse, middle, center

# **AJAX**


---

class: inverse, middle

## **AJAX**

AJAX (Asynchronous Javascript And XML) is a technique for building web applications, consisting of asynchronous communication between the client (browser) and the server, **without requiring a full page reload**

Although originally associated with XML, in modern usage **JSON** is far more common as the data format

---

class: inverse, middle

## **Sending Requests**

```javascript
async function getData() {
  const response = await fetch('https://example.com/', {
    method: 'GET'
  })
  return await response.json()
}

const result = await getData()
```

```javascript
async function postData(data) {
  const response = await fetch('https://example.com/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  if (!response.ok) {
      const errorText = await response.text() 
      throw new Error(`HTTP status: ${response.status}, body: ${errorText}`)
  }
  return await response.json()
}

const result = await postData({ id: 1, name: 'Toni' })
```

---

class: inverse, middle

## **Sending Requests**

If you’re sending data to a server expecting traditional form submissions:

- *Might happen in your LTW project*
- Need to encode your data for **application/x-www-form-urlencoded** instead of JSON

---

class: inverse, middle, center

# **Start Scripting**

---

class: inverse, middle

## **Start Scripting**

JavaScript code can be written in a **&lt;script&gt;** tag in the HTML document

As with CSS, the most common way is to write your script in a separate file, and then link it in the HTML document

```html
<html>
  <head>
    <script src="...location of your script..."></script>
    <script>
      ...javascript code goes here...
    </script>
  </head>
</html>
```

- Conventionally, this goes in the end of the **&lt;head&gt;** tag but you can add the script anywhere in the HTML document (just keep in mind how the browser processes it)

---

class: inverse, middle, center

# **It Gets Better**

---

class: inverse, middle, smaller-images

## **JS Libraries/Frameworks**

For anything beyond a simple website, working with plain JavaScript will be a pretty tedious process, with repetitive work and a lot of opportunities to make mistakes and spend time debugging them

Thankfully, other developers have created (a lot of) **libraries** and **frameworks** that can help us easily and quickly build more solid web applications 

<div style="display: flex; justify-content: center; margin-top: 1em; align-items: center; gap: 1em;">
<img src="./assets/logos/react.png">
<img src="./assets/logos/svelte.png">
<img src="./assets/logos/vue.png">
<img src="./assets/logos/angular.png">
</div>

> TLDR: It's good to learn how the web works but don't reinvent the wheel every time

---

class: inverse, middle, center, small-images

# **TypeScript**

<div style="display: flex; justify-content: center; margin-top: 3em; align-items: center; gap: 2em;">
<img src="./assets/logos/js.png">
<div style="font-size: 1em">➕</div>
**<p style="font-size: 1.8em">Types</p>**
<div style="font-size: 1em">🟰</div>
<img src="./assets/logos/ts.png">

---

class: inverse, middle

## **TypeScript**

Working with JavaScript often comes with finding runtime errors since you can't verify variable types

So Microsoft made a **strongly typed** version of it  

<br>

> Definitely use this once you're done with LTW

---

class: inverse, middle

## **TypeScript**

```typescript
type User = {
  id: number
  name: string
  email: string
}

async function fetchUsers(): Promise<User[]> {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/users')

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    const users: User[] = await response.json()
    return users
  } catch (error) {
    console.error('Failed to fetch users:', error)
    return []
  }
}
```

---

class: inverse, middle, center

# **Practical Exercise**

---

class: inverse, middle, center, smaller-images

### Find the code for the practical exercise here:

<a href="https://github.com/pedronunes19/ni-workshop-js-25" class="line">https://github.com/pedronunes19/ni-workshop-js-25</a>

<img src="./assets/logos/gh.png">

