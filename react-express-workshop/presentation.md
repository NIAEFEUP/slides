class: center, middle, inverse, small-images

# React and Express
## How you can build the website you've always dreamed of
![](./img/ni_logo.png)

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
1. Help us build our first website! (or something like that)

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

# HTTP

HTTP is a protocol used to communicate between two machines, currently used in web applications.

In a simple form:

1. Client makes a request
1. Server receives and handles the request
1. Server sends a response
1. You get to see cats on your screen

---

# HTTP

![](./img/http.jpg)

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

Check out https://http.cat !

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

# API

API (Application Programming Interface) is the specification of methods through which you can interact with a service. Often web applications use REST APIs.

Some common public APIs:
* Google Maps API https://maps.googleapis.com
* Twitter API https://api.twitter.com
* NIJobs API https://ni.fe.up.pt/nijobs/api

---

class: center, middle, inverse

# Node.js
## Why was the JavaScript developer sad?

---

class: center, middle, inverse

# Node.js
## Why was the JavaScript developer sad?
### Because he didn't .highlight[Node] how to .highlight[Express] himself

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

# npm

## .center[And that's where they come in!]

<div class="flex-columns">
<div>
    <img height=150 src="./img/react.png"/>
    <p> React is a library for building user interfaces (aka Frontend) </p>
</div>

<div>
    <img height=150 src="./img/express.png" style="border-radius: 10%"/>
    <p> Express is a minimal framework used to build web servers (usually Backend)</p>
</div>
</div>

