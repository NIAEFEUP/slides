class: center, middle, inverse, small-images

# React
## After you learn it, there is no way back
![](./img/ni_logo.png)

---

# O que é?



---




























class: inverse, middle

# Will this be a boring workshop?

### No.

.highlight[Please feel free to interrupt and ask questions, make this more of a conversation and less of a lecture.]

What we have on menu today:
1. What is React exactly
1. React Theory
1. Common libraries that go well together with React
1. React in practice

---
class: inverse, middle

# Your Host

<div class="left" style="display: flex; align-items: center; gap: 1em">
<div><img width=150 src="./img/angelo.jpg" style="display: inline-block; border-radius: 50%"/></div>
<div>
    <p class="highlight">Angelo Teixeira</p>
    <p>MIEIC Finalist</p>
    <p>2+ Years experience with React - Including internships and NIJobs development</p>
</div>
</div>

<!-- Use this if you have more presenters -->
<!-- <div class="right" style="display: flex; align-items: center; gap: 1em;justify-content: flex-end">
<div>
    <p class="highlight">Second Host</p>
</div>
<div><img width=150 src="./img/img-name" style="display: inline-block; border-radius: 50%"/></div> -->

</div>

Follow along if you want to check the slides: 

https://ws-react-niaefeup.netlify.app/

---
class: inverse, middle

# Disclaimer

### You will not learn React (or any Language / Lib / Framework, really) in a day.
.justify[
I purposefully left some (somewhat relevant) parts out because I'm about to give a lot of information at once, which can be counter-productive.

<!-- It was only recently that I started to feel confident about my React skills (about 2 years in).  -->

<!-- It is normal if you feel lost in the beginning. If you like this are of development, don't give up and eventually it will start to make sense.  -->

It is normal if you feel lost in the beginning, don't give up and eventually all will start to make sense.
]
<br>
<br>

.right[Never stop learning.]

---
class: center, middle, inverse

# React
## What is it, really?

---
class: middle
# React

.highlight[React] is a .highlight[JavaScript] library that automatically renders and handles component updates on a `<div>` of your website. 

.center[
```javascript
ReactDOM.render(
    <App />,
    document.getElementById("root")
);
```
]

---
class: middle

# React

This allows it to run .highlight[__wherever__] inside an existing website. You can even migrate progressively from old UIs to React-powered UI components. 

React is just glorified JavaScript. .highlight[__Always keep this in mind!__] Most of the problems you'll face are just JavaScript problems.

To use React, you just need to load it in a `script` tag in your HTML.
<!-- , then you can use all of its functionalities. -->

---

# React in an HTML page

.center[
```html
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>NIJobs</title>
        <link href="https://ni.fe.up.pt/st4g1ng/nijobs/static/css/main.4f9a2d8f.chunk.css" rel="stylesheet">
    </head>
    <body>
        <noscript>You need to enable JavaScript to run this app.</noscript>
        <div id="root"></div>

        <!-- React source code -->
        <script src="https://ni.fe.up.pt/st4g1ng/nijobs/static/js/2.8ac0d13b.chunk.js"></script>
        <!-- Application source code, using React -->
        <script src="https://ni.fe.up.pt/st4g1ng/nijobs/static/js/main.df8d00d7.chunk.js"></script>
    </body>
</html>
```
]

<!-- ---

# React vs JavaScript

React .highlight[**is**] JavaScript. Most of the problems you'll face are just JavaScript problems.

In fact, React was really good in the sense that it made me learn a lot of JavaScript theory. -->

---

# React is only the View

<!-- In a typical web application, you have 3 layers: -->

* .highlight[**Data Layer**] - Stores the data of the application (Users, posts, comments, etc...).
* .highlight[**Logical Layer**] - Manages the interactions between the View Layer and the Data Layer (An HTTP API for example).
* .highlight[**View Layer**] - The page that is visible to users and with which they can interact.

###### React is designed to only be used in the .highlight[**View Layer**].

.height-limit-250[![MVC Pattern](./img/web-mvc.png)]

---
class: middle

# Declarative vs Imperative Paradigms


In .highlight[**Imperative**] programming, you define exactly what will be done and .highlight[**how**].

In .highlight[**Declarative**] programming, you define what happens depending on some .highlight[**state**].

---
class: middle
# Imperative Programming

.center[
```javascript
function markSelected(id) {
    const item = document.getElementById(id);
    item.classList.add("selected");
}

Array.from(document.getElementsByClassName("todo-item"))
    .forEach(elem => elem.addEventListener("click", markSelected(elem.id)))

```
]

---

# Declarative Programming (in React)

.center[
```javascript

const [items, setItems] = useState([{isSelected: false, text: "TODO1"}])

const toggleItemSelection = (i) => {
    setItems((items) => {
        const updatedItems = cloneDeep(items);
        updatedItems[i].isSelected = !items[i].isSelected
        return updatedItems
    });
}

items.map((item, i) => (
    <p 
        className={item.isSelected && "selected"}
        onClick={toggleItemSelection(i)}
    >
        {item.text}
    </p>
))
```
]

---
class: middle

# Comparison

### Example: Add .highlight['how many are selected'] counter
.highlight[**Imperative**] - add a new listener or change the current one.

.highlight[**Declarative**] - add new component that counts each item with `isSelected: true`, since that is already done in the onClick definition of the item.

---
class: middle
# Comparison
.highlight[**Declarative**] has a big advantage since it releases you from needing to think how things interact with each other every time.

## .centered[.highlight[Think about the state and how it changes]]
The components will change according to the current state automatically.

<!-- ##### * Of course you still need to link the state to the component in some way for it to know about it, like we do by using the `isSelected` variable -->

---
class: middle
# Context Sum up

* React is .highlight[**NOT**] a website maker.
* There are no "React websites". There are websites that .highlight[**USE**] React.
* This is why React is a library and not a framework.
* React uses .highlight[**declarative programming**] to design the interface components, making them rely on a .highlight[**state**], instead of requiring you to specify exactly how they should modify themselves. React handles the DOM changes for you :)

---

class: center, middle, inverse

# React Theory

## Now it will start to make sense, I hope

---

# JSX

React uses an .highlight[**HTML-in-JS language (JSX)**] that lets you specify the components similarly to how you would do it in regular HTML.

.center[
```html
<div className="meteorolgy-widget">
<p>{"This is Javascript. " + "Today it's " + getMeteoPrediction()}</p>
{
    weeklyPredictions.map(prediction => (
        <p>{prediction.day + " - " + prediction.state}</p>
    ))
}
</div>
```
]

There are some differences like using `className` instead of `class`, and allowing you to have JavaScript sections to generate some parts of it.

---

# Components

React is based on a .highlight[**tree of components**], recursively rendered: a component can render none or multiple children, which will be other components, which will be rendered themselves, and so on.

.center[
```javascript
const NewsWebpage = ({news, ads}) => (
    <> // Special "dummy" component - React.Fragment
        <NewsArea news={news}/>
        <AdsColumn ads={ads}>
    </>
)
```
]

### .center[.highlight[Good Practice:] Create .highlight[small] and .highlight[simple] components, responsible for the minimum possible logic]

---
class: middle
# Components - Props

Components can receive a `props` object to use when creating the rendering logic, in order to change dynamically.

Components always have a `children` prop representing their children components.

---
# Components - Props


.center.dense-wide[
```html
const WrapperThatAddsAnHelloV1 = (props) => (
    <>
        <p>Hello,</p>
        <p>{props.name}</p>
    </>
)

const WrapperThatAddsAnHelloV2 = (props) => (
    <>
        <p>Hello,</p>
        {props.children}
    </>
)

const MyPage = () => (
    <>
        <WrapperThatAddsAnHelloV1 name="World"/>
        <WrapperThatAddsAnHelloV2>
            <p>World</p>
        </WrapperThatAddsAnHelloV2>
    </>
)
```
]

---

# DOM and VDOM

.highlight[**DOM (Document Object Model)**] is the browser's representation of a web page.
.center[
```html
<html>
    <head>
      <title>DOM</title>
    </head> 
    <body>
        <p>Hello World</p>
    </body>
</html>
```
]

React has the concept of the .highlight[**Virtual DOM**], which it stores internally to manage the components' state.

---
class: middle

# VDOM

Virtual DOM  as it only updates the relevant components instead of the whole page when rendering components in the browser.

<br>

### .highlight[**Reconciliation Phase**]

When the VDOM changes, those are mapped to instructions to update the real DOM (.highlight[**append**], .highlight[**delete**] and .highlight[**update**] operations). These instructions are generated by comparing the new version of the VDOM with the older one, and generating the minimum set of operations required to change it on the DOM*.

<br>

###### * This is a known problem for which state-of-the-art algorithms have a complexity in the order of O(n^3), n being the number of tree elements.

---
class: middle
# Reconciliation Optimizations

If we used this in React, displaying .highlight[**1000 elements**] would require in the order of .highlight[**one billion comparisons**]. This is far too expensive. Instead, React implements a heuristic O(n) algorithm based on two assumptions:

* Two elements of different types will produce different trees.
* The developer can hint at which child elements may be stable across different renders with a key prop.

---

# Reconciliating Lists

By default, when recursing on the children of a DOM node, React just iterates over both lists of children at the same time and generates a mutation whenever there’s a difference.

For example, when adding an element at the end of the children, converting between these two trees works well:

.center[.dense[
```html
<ul> <!-- before -->
  <li>first</li>
  <li>second</li>
</ul>
<ul> <!-- after -->
  <li>first</li>
  <li>second</li>
  <li>third</li>
</ul>
```
]]
React will match the two `<li>first</li>` trees, match the two `<li>second</li>` trees, and then insert the `<li>third</li>` tree.

---

# Reconciliating Lists

If you implement it naively, inserting an element at the beginning has worse performance. For example, converting between these two trees works poorly:

.center[.dense[
```html
<ul> <!-- before -->
  <li>Duke</li>
  <li>Villanova</li>
</ul>
<ul><!-- after -->
  <li>Connecticut</li>
  <li>Duke</li>
  <li>Villanova</li>
</ul>
```
]]

React will mutate every child instead of realizing it can keep the `<li>Duke</li>` and `<li>Villanova</li>` subtrees intact. This inefficiency can be a problem.

---

# Keys

In order to solve this issue, React supports a .highlight[**key**] attribute. When children have keys, React uses the key to match children in the original tree with children in the subsequent tree. For example, adding a key to our inefficient example above can make the tree conversion efficient:

.center[.dense[
```html
<ul>
  <li key="2015">Duke</li>
  <li key="2016">Villanova</li>
</ul>
<ul>
  <li key="2014">Connecticut</li>
  <li key="2015">Duke</li>
  <li key="2016">Villanova</li>
</ul>
```
]]

Now React knows that the element with key '2014' is the new one, and the elements with the keys '2015' and '2016' have just moved.

---
class: middle

# Keys

Usually, React will let you know when you have some list of mutating children and you should be using keys. 

But there are some things to consider before choosing your keys:

* They must be .highlight[**unique**] among the elements of the same list.
* They must be .highlight[**constant**] during the life of the element on the list.

---
class: middle
# Keys

A first instinct is to use .highlight[**array indexes as keys**], since they are obviously unique among elements.

However, they .highlight[**DON'T**] respect the .highlight[**second rule**] if the list changes with some reorder, for example.

<br>
<br>

Let's check an example...

https://jsbin.com/gotihihihi/edit?js,output

---
class:middle                                                                                                        
# Component Lifecycle

In order to interact with the Virtual DOM, React lets you use .highlight[**React Components**], which can be .highlight[**classes**] or .highlight[**functions**] (we’ll use functions) that represent a part of the website and can contain more components inside them.

These React Components are .highlight[**bound**] by a .highlight[**Lifecycle**] that manages their existence and interactions, which reflect on the actual DOM after the .highlight[**Reconciliation Phase**].

---

# Component Lifecycle

There are 4 steps:  

* .highlight[**Mounting**] **(When the component is first added to the DOM)**: 
    * The methods and events that take place here happen as the component is mounted in the DOM.
* .highlight[**Updating**] **(When the state or one of the props change, or if parent re-renders*)**: 
    * Here the methods and events take place after the React component has entered the DOM.
* .highlight[**Un-mounting**]: 
    * Here the methods and events take place as they React component leaves the DOM or is unmounted from the DOM.
* .highlight[**Error Boundaries**]: 
    * This is a special category that deals with handling or gracefully catching errors in order not to totally break your React application render.


###### * Might not happen if the child component is memoized with React.memo(), for example.

---

# React Hooks

React .highlight[**Hooks**] are JavaScript .highlight[**functions**] that can interact with the component, by executing specific actions during the component lifecycle.

React exposes some default hooks, but you can create custom hooks which call React's ones for more complex scenarios.

There are two rules when using React Hooks:

* ### .highlight[Only Call Hooks at the Top Level] 
    * Don’t call Hooks inside loops, conditions, or nested functions. Instead, always use Hooks at the top level of your React function.
* ### .highlight[Only Call Hooks from React Functions]
Don’t call Hooks from regular JavaScript functions. Instead, you can:
    * Call Hooks from React function components.
    * Call Hooks from custom Hooks

---

# Common React Hooks

### .highlight[useState(initialState)]
Let's you store some state in-between re-renders. If you pass a function as the initial value, it will only run it on the first render.

Returns an array where the first value is the state value and the second is a setter function for that value.

It's recommended you have a separate state for every variable you want to store, instead of a giant object with a field for each.

.center[.dense[
```javascript
const [count, setCount] = useState(0);

const incrementCounter = () => {
    setCount(count + 1)
}

const decrementCounter = () => {
    setCount(currentCount => currentCount - 1)
}
```
]]

---
class: middle
# Common React Hooks

### .highlight[useState(initialState):] `setState(val)` vs `setState(fn)`

Using the .highlight[**function version**] is .highlight[**better**] due to async updates. If you call `incrementCounter` in rapid succession, React will batch the updates and race conditions may prevent the counter from updating multiple times, i.e. the `count` variable will not update in between calls.

Using an updater function, the "current state" variable is always correct.

---
class: middle
# Common React Hooks

### .highlight[useEffect(fn, [...dependencies])]

Lets you execute code at different stages of the lifecycle. It is .highlight[**called at every render**], but it might do nothing, depending on the dependencies.

.center[
```javascript
useEffect(() => {
    // This will run on every render
})
```
]

Notice the .highlight[**undefined**] dependency array. This is the same as not calling `useEffect`, and writing the code directly on the component.

---
class: middle
# Common React Hooks

### .highlight[useEffect(fn, [...dependencies])]

.center[
```javascript
useEffect(() => {
    // This will run on mount only
}, [])
```
]

Notice the .highlight[**empty**] dependency array, indicating that the code will run .highlight[**at mount only**].

---

# Common React Hooks

### .highlight[useEffect(fn, [...dependencies])]

.center[
```javascript
useEffect(() => {
    // This will run every time the dependencies change
    console.log(foo, bar)
}, [foo, bar])

```
]
`foo` and `bar` might be some component props or variables created inside the component that depend on props. If the props change, making `foo` or `bar` change, the `useEffect` function will be executed.

Does .highlight[**NOT**] execute if the .highlight[**references**] to the dependencies don’t change.

---

# Common React Hooks

### .highlight[useRef(initialValue)]

`useRef` is similar to `useState`, however it does .highlight[**NOT trigger**] anything .highlight[**on change**]. It's just a mutable JavaScript object with a current field which stores whatever.

It's also used to store references to DOM elements, so that you can program something .highlight[**imperatively**], if needed.

.center[.dense[
```javascript
function TextInputWithFocusButton() {
    const inputEl = useRef(null);
    const onButtonClick = () => {
        inputEl.current.focus();  // `current` points to the mounted text input
    };
    return (
        <>
            <input ref={inputEl} type="text" />
            <button onClick={onButtonClick}>Focus the input</button>
        </>
    );
}
```
]]

---

# Custom React Hooks

We can create a function that calls any React Hook and call it as if it were a React Hook, for more complex scenarios.

.center[
```javascript
function useForm(fieldOptions) {
    const initialState = Object.entries(fieldOptions).map(...)
    const [fields, setFields] = useState(initialState)

    const setField = (fieldName) = (val) => {
        setFields(fields => ({
            ...fields,
            [fieldName]: val
        }))
    }

    return [fields, setField];
}
```
]

---
class: center, middle, inverse

# Common Patterns
## Don't re-invent the wheel

---

# Controller Component

A component that handles all the state and only renders stateless components to handle the visual part.

.center[.dense[
```html
const FormHandler = () => {
    const [name, setName] = useState("")
    const [age, setAge] = useState(0)

    const handleSubmit = () => //call something using `name` and `age`
    return (
        <form onSubmit={handleSubmit}>
            <input 
                value={name} 
                onChange={(e) => setName(e.target.value)}
            />
            <input 
                type="number"
                value={age} 
                onChange={(e) => setAge(e.target.value)}
            />
            <button type="submit">
                </form>
    )
}
```
]]

---

# Higher-order Component (HoC)

A function that wraps components to inject some props.

.center[.dense[
```html
// Utils file
const withMath = (WrappedComponent) => {
    const sum = (a,b) => a+b

    return (
        <WrappedComponent sum={sum} />
    )
}

// Component file
const MyCalculator = ({sum, a, b}) => (
    <div>
        <input value={a}/>
        <input value={b}/>
        <button onClick={() => { console.log(sum(a,b)) }>Sum</button>
    </div>
)

export default withMath(MyCalculator);
// No need to specify the sum `prop` when using this component.
// It will already be populated by the `withMath()`.

```

]]

---
class: center, middle, inverse

# Common libraries/API that you must know

---

# PropTypes

Since React is programmed in JavaScript, props .highlight[**DON'T**] have types by default. This can lead to some errors if you're not careful.

.highlight[**PropTypes**] lets you define the types for you component props, and even if they are required or not.

.center[
```javascript
const SomeComponent = ({prop1, prop2, prop3}) => ()

SomeComponent.propTypes = {
    prop1: PropTypes.string.isRequired,
    prop2: PropTypes.func,
    prop3: PropTypes.oneOf(["first", "second", "third"]).isRequired,
}
```
]

---

# Calling APIs - Fetch

In order to make requests to an HTTP API, you can use the built-in JS library .highlight[**fetch**], or some external package such as .highlight[**Axios**].

.center[
```javascript
try {
        const response = await fetch(`${API_HOSTNAME}/offers`, {
            method: "GET",
        });
        
        if (!response.ok) {
            // Any HTTP status non 2xx will make ok = false
        }
        
        // If the response is JSON, call .json() which returns a Promise
        const json = await res.json();

    } catch (error) {
        // Handle Network Error
}
```
]

---

# React Router

React Router allows you to .highlight[**simulate**] different pages in your application.

.center[
```html
<BrowserRouter>
    <Switch>
        <Route
            exact
            path="/"
        >
            <HomePage/>
        </Route>
        <Route
            path="/apply/company"
        >
            <CompanyApplicationPage/>
        </Route>
    </Switch>
</BrowserRouter>
```
]

---
class: middle
# React Router

When you .highlight[**define different Routes**], technically, it will .highlight[**NOT create different pages**]. The user will still access "/", which will then load the application code and then the rest of the path will be parsed and a different component will be rendered, depending on the route.

This is why when you have an .highlight[**"only React with React Router"**] web application, you need to re-route all pages to "/", so that they are resolved by React, instead of the web server itself.

---
class: middle
# Redux

.highlight[**Redux**] allows you to .highlight[**centralize your application's state and logic**] enables powerful capabilities like .highlight[**undo/redo**] and .highlight[**state persistence**].

Redux is made for JavaScript in general, but it has specific bindings for React, which are really useful.

---

# Redux -- The Problem

Imagine you want to store cart information (for example in an e-commerce app). However, you want it in the navbar, and you need to edit it in some other places of the page.

.height-limit-250[![Prop Drilling](./img/cart-prop-drilling.png)]


You would need to store it in a common ancestor for all, and pass it down via props (called .highlight[**prop-drilling**]).

---

# Redux -- (One of) The solution(s)

Redux lets you create a `store` which will hold .highlight[**common state**]. Then, you make components .highlight[**subscribe**] to it (via HoC pattern or Hooks), which will then react to changes in the store and have access to ways of changing it.

.center[
```javascript
import { combineReducers } from "redux";
import notificationReducer from "./notificationReducer";
import searchOffersReducer from "./searchOffersReducer";
import companyApplicationReducer from "./companyApplicationReducer";
import navbarActionsReducer from "./navbarActionsReducer";

// Multiple reducers can exist for different parts of the app
export default combineReducers({
    messages: notificationReducer,
    offerSearch: searchOffersReducer,
    companyApplication: companyApplicationReducer,
    navbar: navbarActionsReducer,
});
```
]

---

# Redux --- (One of) The solution(s)

.center[
```javascript
const mapStateToProps = ({ offerSearch }) => ({
    searchValue: offerSearch.searchValue,
    jobType: offerSearch.jobType,
    minJobDuration: offerSearch.jobDuration[0],
    maxJobDuration: offerSearch.jobDuration[1],
    fields: offerSearch.fields,
    techs: offerSearch.techs,
    showJobDurationSlider: offerSearch.filterJobDuration,
});

const mapDispatchToProps = (dispatch) => ({
    // This will come in later :P
});

export default connect(mapStateToProps, mapDispatchToProps)(SearchArea);
```
]

This will make sure that `SearchArea` receives those props from the Redux Store automatically, and re-renders if they change!

---
class: middle 
# Redux --- How does state change

### .highlight[Actions]

State is read-only, it should only change by emitting an action. Actions are the representation of what will change in the store.

### .highlight[Reducers]

Reducers will receive actions and generate the change in the state.

Reducers must be .highlight[**pure**]. This means they just receive the current state, and return a new version. They DO NOT change the state directly.

---

# Reducers --- Example

.center[
```javascript
const initialState = {
    offers: [],
    loading: false,
    error: null,
    // ......
};

export default (state = initialState, action) => {

    switch (action.type) {
        case OfferSearchTypes.SET_OFFERS_SEARCH_RESULT:
            return {
                ...state,
                offers: action.offers,
            };
        // ........
    }
};
```
]

---
class: middle
# Actions --- Example

.center[
```javascript
export const setSearchOffers = (offers) => ({
    type: OfferSearchTypes.SET_OFFERS_SEARCH_RESULT,
    offers,
});
```
]

---
class: middle
# Redux --- Back to the example

.center[
```javascript
export default connect(mapStateToProps, mapDispatchToProps)(SearchArea);
```
]

.center[
```javascript
const mapDispatchToProps = (dispatch) => ({
    setSearchOffers: (value) => dispatch(setSearchOffers(value)),
    // ....
});
```
]

This makes the function available to the component, which can call an API, and when it returns, call the `setSearchOffers` with the offers value.

---

class: center, middle, inverse

# MaterialUI

## Wrapping up in style.

---

# Material UI

https://material-ui.com/

.height-limit-400[![MVC Pattern](./img/mui-docs-demo.gif)]

---
class: middle
# Material UI --- Theme

You can specify the .highlight[**application theme**] with some UI defaults such as colors palette, the font type, spacing settings, etc...

This way, every time you are creating a UI, you don't have to worry about making everything consistent.

Usually, it's placed at the .highlight[**top of the Component Tree**].

---

# Material UI --- Theme

.center.dense[
```javascript
const theme = responsiveFontSizes(createMuiTheme({
    palette: {
        primary: {
            main: "#DC4F47",
        },
        secondary: {
            main: "#4F1315",
        },
    },
    typography: {
        fontFamily: [
            "Poppins",
            "Roboto",
            "sans-serif",
        ].join(","),
    },
}));

<ThemeProvider theme={AppTheme}>
    <App/>
</ThemeProvider>
```
]

---

class: center, middle, inverse

# React in Practice

---

# ~~Github~~ Nithub

Nithub is a simple app that lets you see issues for any public Github repository.

For this, it will use the Github API.

* https://api.github.com/repos/{user}/{repo}/issues
* https://docs.github.com/en/rest/reference/issues#list-repository-issues

Clone the repository, install the dependencies, and let's begin!

.center[
```bash
git clone https://github.com/imnotteixeira/react-workshop-exercise.git
cd react-workshop-exercise
npm install
npm start
```
]
