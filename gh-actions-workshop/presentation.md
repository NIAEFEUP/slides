class: center, middle, inverse, small-images

# CI/CD Workshop
### Using GitHub Actions

![NIAEFEUP's logo](assets/logo_2018.png)

---

class: inverse

# Important links

You can follow this presentation on your computer from the link below:

<div style="display: flex; justify-content: center; align-items: center; margin: 10rem 0rem;">
<a href="https://niaefeup.github.io/slides/" style="color: white; font-weight:bold; font-size: 2rem;">https://niaefeup.github.io/slides/</a>
</div>


---
class: inverse, center

# Your Host

<img src="./assets/profile.png" height=200 width=200 style="border-radius: 50%; object-fit: cover">

**Luís Duarte**

L.EIC Finalist

---

class: center, inverse, middle

## Please don't let this be a monologue

#### Feel free to ask any questions anytime

---

### What is CI/CD - an introduction

To put it simply, CI/CD falls under the umbrella of _DevOps_ and combines the practices of 
**continuous integration** and **continuous delivery**. It tries to **automate** much 
of the process of getting new code into production: by **testing**, **building**, **deploying**, and sometimes, provisioning the infrastructure needed.

By automating this boring process that happens every development cycle developers can be more **productive** and also reduce possible **downtime**.

<div style="display: flex; justify-content:center;">
<img src="./assets/ci-cd.webp" width=500>
</div>

---

### Difference between CI and CD

- **Continuous integration** automates the process of trying to integrate new code into a main branch of a repository early and automatically to detect possible errors before actually merging the new code into production;

- **Continuous delivery** automates the release process once new changes are merged into the main branch by building the final binary of an application or even by moving to **continuous deployment** that also automates de deployment process (eg.: releasing a new version to Google Play).

**NOTE:** you don't need to do both processes, it depends on the requirements of your project.

<div style="display: flex; justify-content:center;">
<img src="./assets/pipeline.png" width=500>
</div>

---

### Why should you include a CI/CD system in your project?

- **Improved productivity**: With proper testing, the review time of each change is significantly reduced and also frees up your time from testing your project manually;
- **Fix bugs faster**: When using _CD_ there are smaller software updates so when bugs appear, it's easier to rollback or to pin them down;
- **Reduced Risk**: By having a proper testing suite and by using CI, you can be confident that your changes will work when your code is deployed;
- And many other advantages that are not relevant in this context :) 

Implementing a CI/CD pipeline takes some time, but sometimes you have to lose time now to **gain** time in the future.

---

### "Requirements" when using CI/CD

Having a proper _Git_ process that allows for parallel work and has small meaningful commits is very important for a CI/CD pipeline to be effective, for example:
 - [Gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
 - [Trunk based development](https://trunkbaseddevelopment.com/)

It is also essential to have a way to properly **test** your project, by having:
  - Static testing (_linting_, _formatting_, _code analysis_)
  - Unit testing
  - Integration testing

---

### CI/CD pipeline tools

Now that you roughly know what CI/CD is, you can try to implement it. However, trying to do it from scratch is not practical so there are many tools available on the market that try to streamline this process:

- **GitHub Actions** (free for open repositories, "paid" for closed repos when you surpass the limit);
- **GitLab Pipelines** (400 compute minutes for free, paid if you wish to use their runners);
- **Jenkins** (open source, need to bring your infrastructure, harder to learn);
- **CircleCI** (6000 minutes for free, need to upgrade for more)

---

class: inverse, center, middle


## GitHub Actions
### Now we're getting to the fun part ;)