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
  <a href="https://slides.niaefeup.pt/nestjs-workshop/" style="color: white; font-weight:bold; font-size: 1.5rem; text-align:center;">https://slides.niaefeup.pt/nestjs-workshop/</a>
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
- [NIddle Codebase Walkthrough](#niddle-codebase) - Real-world project structure

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

name: project-structure
template: title

# Project Structure

---

# Why structure matters?

When you first create a NestJS project, you get this:

```txt
src/
  app.module.ts          <- root module (the "main" file)
  app.controller.ts      <- handles HTTP requests
  app.service.ts         <- business logic
  app.controller.spec.ts <- tests
  main.ts                <- entry point
```

A real app has users, orders, authentication, and much more. NestJS organizes code by **feature** - each feature is its own module.

---

# main.ts - the entry point

Every NestJS app starts from `main.ts`:

```typescript
import { NestFactory } from "@nestjs/core";
import { AppModule } from "./app.module";

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);
}
bootstrap();
```

- `NestFactory.create(AppModule)` - bootstraps the app using the root module
- `app.listen(3000)` - starts the server on port 3000
- This is also where you register **global** things (pipes, filters)

---

# What is a Module?

A module groups **related code** together - like a department in a company.

- If your app is a restaurant, a module is the "kitchen department"
- Or the "billing department"
- Or the "reservation department"

Every NestJS app starts with one **root module**: `AppModule`, but each feature gets its own module.

```typescript
// users.module.ts
@Module({
  imports: [TypeOrmModule.forFeature([User])],
  controllers: [UsersController],
  providers: [UsersService],
})
export class UsersModule {}
```

---

# Module anatomy

A module can contain four things:

```typescript
@Module({
  imports: [TypeOrmModule.forFeature([User])], // register entities
  controllers: [UsersController], // handles HTTP requests
  providers: [UsersService], // business logic (services)
  exports: [UsersService], // share with other modules
})
export class UsersModule {}
```

- **imports** - Other modules this module depends on
- **controllers** - The "waiters" that handle HTTP
- **providers** - The "kitchen" that does the work (services)
- **exports** - Share your providers with other modules

---

# The four layers

Back to our restaurant analogy:

| Layer          | Role        | Job                                      |
| -------------- | ----------- | ---------------------------------------- |
| **Controller** | Waiter      | Takes orders, brings back food           |
| **Service**    | Kitchen     | Does the actual cooking                  |
| **Entity**     | Recipe card | Defines what data looks like in the DB   |
| **DTO**        | Order slip  | Defines what data goes in/out of the API |

The flow of a request:

```txt
Request -> Controller -> Service -> Database -> Service -> Controller -> Response
```

---

# Controller

The controller is responsible for handling **HTTP requests**.

```typescript
// users.controller.ts
@Controller("users")
export class UsersController {
  @Get()
  findAll() {
    return ["Alice", "Bob"];
  }

  @Get(":id")
  findOne(@Param("id") id: string) {
    return { name: "Alice", age: 20 };
  }
}
```

- `@Controller('users')` - this controller handles `/users`
- `@Get()` - responds to `GET /users`
- `@Get(':id')` - responds to `GET /users/42`

---

# Controller - more methods

```typescript
@Controller("users")
export class UsersController {
  @Post()
  create(@Body() createUserDto: CreateUserDto) {
    return { name: "Charlie", age: 22 };
  }

  @Put(":id")
  update(@Param("id") id: string, @Body() dto: UpdateUserDto) {
    return { name: "Charlie", age: 23 };
  }

  @Delete(":id")
  remove(@Param("id") id: string) {
    return { deleted: true };
  }
}
```

Notice how each decorator maps to an **HTTP method** from the [Web Basics](#web-basics) section.

> Controllers should be **thin** - they just receive the request and pass it to the service.

---

# Service

The service contains the **business logic** - the "kitchen" that does the work.

```typescript
// users.service.ts
@Injectable()
export class UsersService {
  constructor(
    @InjectRepository(User)
    private userRepo: Repository<User>,
  ) {}

  findAll() {
    return this.userRepo.find();
  }

  create(dto: CreateUserDto) {
    const user = this.userRepo.create(dto);
    return this.userRepo.save(user);
  }
}
```

Where does the `userRepo` come from? Check [Dependency Injection](#dependency-injection).

> This is where **CRUD** operations actually happen.

---

# Entity

The entity defines the **shape of your data in the database**.

Think of it as a **blueprint** for a database table.

```typescript
// user.entity.ts
@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  name: string;

  @Column({ unique: true })
  email: string;
}
```

- `@Entity()` - marks this class as a database table
- `@Column()` - each property becomes a column in the table
- `@PrimaryGeneratedColumn()` - the unique identifier (auto-incremented)

---

# What is a Repository?

A Repository is your **interface to the database**. ORMs (**O**bject-**R**elational **M**apping, like TypeORM) gives you one Repository per Entity.

Think of it as a **toolbox** for talking to a specific table:

```txt
userRepo.find()              ->  SELECT * FROM user
userRepo.findOne({ id: 1 })  ->  SELECT * FROM user WHERE id = 1
userRepo.create(dto)         ->  creates a new User in memory
userRepo.save(user)          ->  INSERT or UPDATE in the database
userRepo.delete(id)          ->  DELETE FROM user WHERE id = ?
```

You don't write SQL. You call methods, and the ORM builds the query for you.

---

# DTO

**D**ata **T**ransfer **O**bject - defines what data the client **sends** and **receives**.

Remember JSON from [Web Basics](#web-basics)? DTOs define the shape of that JSON.

```typescript
// create-user.dto.ts
export class CreateUserDto {
  @IsString()
  @IsNotEmpty()
  name: string;

  @IsEmail()
  email: string;
}
```

When a client sends this JSON:

```json
{ "name": "Alice", "email": "alice@example.com" }
```

NestJS maps it to a `CreateUserDto` object that you can use in your service.

> DTOs are the **contract** between your API and the client.

---

# DTO vs Entity

They look similar but serve **different purposes**:

```typescript
// Entity - for the database (what the database stores)
@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number; // DB generates this

  @Column()
  name: string;

  @Column({ unique: true })
  email: string;
}
```

```typescript
// DTO - for the API (what the client sends/receives)
export class CreateUserDto {
  @IsString()
  name: string; // client sends this

  @IsEmail()
  email: string; // client sends this
  // no id! the DB generates it
}
```

---

# The full flow

Let's trace a `GET /users/42` request through all four layers:

```txt
1. HTTP Request arrives:
   GET /users/42

2. Controller receives it:
   @Get(':id')
   findOne(@Param('id') id: string) {
     return this.usersService.findOne(+id);
   }

3. Service asks the Repository:
   findOne(id: number) {
     return this.userRepo.findOneOrFail({ where: { id } });
   }

4. Response goes back (JSON):
   { "name": "Alice", "email": "alice@example.com" }
```

Each layer has a single responsibility.

---

name: dependency-injection
template: title

# Dependency Injection

---

# The problem: tight coupling

Without **DI**, a class has to **create its own dependencies**:

```typescript
export class UsersController {
  private service = new UsersService(new UserRepository(new Database()));
}
```

- The controller is responsible for creating everything it needs
- Want to swap the database? **Change the controller.**
- Want to mock the service for testing? **Can't.**

> Imagine if the waiter had to buy the ingredients, cook the food, _and_ serve it. That's tight coupling.

---

# The solution: Dependency Injection

With **DI**, NestJS **creates and provides** your dependencies automatically:

```typescript
@Controller("users")
export class UsersController {
  constructor(private usersService: UsersService) {}
}
```

The controller doesn't create the service. It just says:

> "I need a `UsersService`" - and NestJS hands it over.

You **declare what you need**, NestJS **provides it**.

---

# How does NestJS know?

Two things make **DI** work:

```typescript
@Injectable() // 1. "This class can be injected"
export class UsersService {
  constructor(
    @InjectRepository(User) // 2. "This repository handles User entities"
    private userRepo: Repository<User>,
  ) {}
}
```

When the app starts:

```txt
1. NestJS scans for @Injectable() classes
2. Creates instances (the "singletons")
3. When a Controller needs a Service, NestJS hands it the existing instance
```

> Think of the IoC container as a restaurant manager. It stocks the kitchen and provides what each waiter needs.

---

# In practice

You've already been using **DI**! Let's highlight the injected parts:

```typescript
@Injectable()
export class UsersService {
  constructor(
    @InjectRepository(User)
    private userRepo: Repository<User>, // <-- injected by NestJS
  ) {}
}
```

```typescript
@Controller("users")
export class UsersController {
  constructor(
    private usersService: UsersService, // <-- injected by NestJS
  ) {}
}
```

Now you know what this is called.

---

# Why should I care?

- **Testing** - swap a real service for a fake one in tests
- **Flexibility** - change the database without touching the controller
- **Clean code** - each class only worries about its own job

> **DI** is what makes NestJS's architecture work. Without it, the Module / Controller / Service structure wouldn't be possible.

---

name: guards
template: title

# Guards

---

# What is a Guard?

A guard is a **gatekeeper** that runs _before_ your route handler.

It answers one question: **should this request proceed?**

- `true` -> request continues
- Throws exception -> request is **rejected**

> Think of it like a bouncer at a club door. Checks your ID before letting you in.

Guards can answer two types of questions:

- **"Who are you?"** -> Authentication (are you logged in?)
- **"Can you do this?"** -> Authorization (are you an admin?)

---

# @UseGuards()

Apply guards to routes with a decorator:

```typescript
@UseGuards(JwtAuthGuard)
@Get("profile")
getProfile() { ... }
```

Stack multiple guards for layered checks:

```typescript
@UseGuards(JwtAuthGuard, AdminOnlyGuard)
@Post()
create() { ... }
```

Guards run **left to right** - the first one to reject stops the chain.

---

# In practice

Here's a real guard from NIddle:

```typescript
@Injectable()
export class AdminOnlyGuard implements CanActivate {
  canActivate(context: ExecutionContext): boolean {
    const user = context.switchToHttp().getRequest().user;
    if (!user || !user.isAdmin) {
      throw new ForbiddenException();
    }
    return true;
  }
}
```

- `JwtAuthGuard` runs first -> loads `user` into the request
- `AdminOnlyGuard` runs second -> checks `user.isAdmin`
- GET endpoints are usually **unprotected** - only CUD operations need guards

---

name: exception-filters
template: title

# Exception Filters

---

# Built-in Exceptions

NestJS gives you ready-made exception classes that return proper HTTP responses:

```typescript
throw new NotFoundException(); // 404
throw new BadRequestException(); // 400
throw new UnauthorizedException(); // 401
throw new ForbiddenException(); // 403
```

Just throw them and NestJS handles the rest - status codes, JSON responses, everything.

---

# Exception Filters

When built-in responses aren't enough, create a **custom filter**:

```typescript
@Catch(EntityNotFoundError)
export class EntityNotFoundFilter implements ExceptionFilter {
  catch(exception, host) {
    const response = host.switchToHttp().getResponse();
    response.status(404).json({
      statusCode: 404,
      message: "Resource not found",
    });
  }
}
```

Register it globally in `main.ts`:

```typescript
app.useGlobalFilters(new EntityNotFoundFilter());
```

---

# In practice

A filter catches TypeORM's `EntityNotFoundError` and returns a clean response:

```txt
// Without filter (raw TypeORM error):
"Could not find any entity of type \"User\" matching: { \"id\": 1 }"

// With filter:
{ "statusCode": 404, "message": "User with id 1 not found" }
```

> Filters turn ugly database errors into friendly API responses.

---

name: live-demo
template: title

# Live Demo

---

# Books + Authors

Let's build a simple API together with two modules.

```typescript
@Entity()
export class Author {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  name: string;

  @Column()
  nationality: string;
}
```

```typescript
@Injectable()
export class AuthorsService {
  constructor(
    @InjectRepository(Author)
    private authorRepo: Repository<Author>,
  ) {}

  // CRUD endpoints
}
```

---

# Books module

```typescript
@Entity()
export class Book {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  title: string;

  @Column()
  year: number;
}
```

```typescript
@Injectable()
export class BooksService {
  constructor(
    @InjectRepository(Book)
    private bookRepo: Repository<Book>,
  ) {}

  // same CRUD pattern as AuthorsService
}
```

---

# Many-to-Many relationship

Now connect them: a book can have **multiple authors**, an author can write **multiple books**.

```typescript
@Entity()
export class Book {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  title: string;

  @Column()
  year: number;

  @ManyToMany(() => Author)
  @JoinTable()
  authors: Author[];
}
```

The `@JoinTable()` tells TypeORM to create an intermediate table.

---

name: niddle-codebase
template: title

# NIddle Codebase Walkthrough

---

# What is NIddle?

**NIddle** is the backend for the **UNI** app.

It provides a REST API that manages:

- **Faculties** - FEUP, FEP, FLUP, etc.
- **Courses** - LEIC, MESW, etc.
- **Associations** - student groups like NIAEFEUP
- **Events** - talks, workshops, parties
- **Services** - cafeterias, stationery shops with schedules
- **Users** - admins and association members

---

# Tech Stack

| Layer      | Technology            |
| ---------- | --------------------- |
| Framework  | NestJS                |
| Database   | PostgreSQL (TypeORM)  |
| Auth       | JWT + Passport        |
| API Docs   | Swagger (`/api/docs`) |
| Validation | class-validator       |
| Testing    | Jest + Supertest      |

All the patterns we covered today are used in production:

> Modules, Controllers, Services, Entities, DTOs, Guards, Exception Filters, Dependency Injection

---

# What you learned today

| Section                  | Topics                                               |
| ------------------------ | ---------------------------------------------------- |
| **Web Basics**           | HTTP, REST, JSON, Status Codes                       |
| **Project Structure**    | Module, Controller, Service, Entity, DTO, Repository |
| **Dependency Injection** | `@Injectable()`, IoC container                       |
| **Guards**               | `@UseGuards()`, Authentication vs Authorization      |
| **Exception Filters**    | Built-in exceptions, custom `@Catch()` filters       |
| **Live Demo**            | Books + Authors with Many-to-Many                    |
| **NIddle Codebase**      | Real-world NestJS + TypeORM + JWT                    |

---

template: title

## Thank you!
