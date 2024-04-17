class: center, middle, inverse, small-images

# Kubernetes Workshop

### A gentle introduction to application deployment and orchestration 

<div style="display: flex; justify-content: center; margin-top: 3em; align-items: center; gap: 1em;">
<img src="./assets/ni_logo.png">
<div style="font-size: 2.5em; padding-inline: 0.5em;">❤️</div>
<img src="./assets/kubernetes-logo.png">
<img src="./assets/kubernetes-name_white.png">
</div>

---

class: inverse

# Important links

This presentation is available online from the link below:

<div style="display: flex; justify-content: center; align-items: center; margin: 10rem 0rem;">
<a href="https://niaefeup.github.io/slides/kubernetes-workshop" style="color: white; font-weight:bold; font-size: 2rem; text-align:center;">https://niaefeup.github.io/slides/kubernetes-workshop</a>
</div>

---

class: center, middle, inverse

### Your host

<img src="./assets/sirze.jpg" style="width: 20%; border-radius: 5em;">

**José Costa**

M.EIC Finalist

<div style="display: flex; justify-content: center; align-items: center;">
<a href="https://github.com/Sirze01">
<img src="./assets/gh.png" style="width:50px;">
</a>
</div>

---

class: inverse

### Agenda

- Introduction to application deployment
  - A brief history lesson
  - The advent of containers
  - The need for orchestration
  - How does application deployment relate to CI/CD and DevOps?
- Kubernetes basic concepts
  - Architecture and main components
  - Pods, Workloads, Services and Ingresses, etc.
  - Networking overview
  - Kubernetes in the cloud vs bare-metal
- Hands-on: Deploying a bank's services

---
class: inverse

# Hands-on prequisites
If you want to prepare things beforehand, you will need:

- A container engine such as [docker](https://www.docker.com/)
- [Kind](https://kind.sigs.k8s.io/docs/user/quick-start/), a Kubernetes-in-Docker tool
- A clone of the [Bank of athos repository](https://github.com/GoogleCloudPlatform/bank-of-anthos/tree/main)
- [`kubectl`](https://kubernetes.io/docs/tasks/tools/#kubectl), a command to interact with your Kubernetes cluster 

Don't worry if you can't prepare these things beforehand, we will guide you through the process during the hands-on portion.

---
class: center, middle, inverse

## Please don't let this be a monologue

#### Ask questions whenever you want

---

class: center, middle, inverse
# Introduction to application deployment

---

class: center, middle, inverse
## A brief history lesson

---

### A brief history lesson
#### In the beginning
- Applications were deployed on physical servers
- Each application was installed on top of the OS
- Dependencies were hard to manage and conflicts were common
- Little to no isolation between applications
- Scalability was hard to achieve and tighly coupled to the hardware

This represents the **bare metal** era.

---

### A brief history lesson
#### Leveraging virtualization
- The physical hardware runs a hypervisor, capable of creating virtual machines, providing OS-level isolation
- High availability can be achieved by clustering multiple physical servers
- Each VM runs its own OS and applications, with its own set of dependencies
- Scalability is easier to achieve, as VMs can be easily cloned and moved around
- However, VMs are still heavy and slow to boot, resulting in wasted resources

AWS EC2 instances are an example of a service providing this type of hosting.
More info: https://www.ibm.com/topics/iaas

---

### A brief history lesson
#### Preparing environments and launching applications
What deployments looked like:
- Ad-hoc bash scripts to install dependencies and start the application

<img style="width:100%;" src="./assets/old-niployments.png">
A excerpt from the old service deployment system at NIAEFEUP, [niployments](https://github.com/NIAEFEUP/niployments)


---

class: center, middle, inverse
# The advent of containers

---

### The advent of containers
#### What are containers?
- Containers are a way to package applications and their dependencies in a single unit. 
- Behave as a lightweight and portable environment for the applications they package.
- Containers are isolated from each other and from the host system. Through the container runtime (e.g. Docker, containerd, cri-o), they can be run on any machine that has the runtime installed. The runtime deals with all the calls to the host OS, abstracting the underlying system.
<div style="display:flex; justify-content:center;">
<img style="height:250px;" src="./assets/containers-architecture.png">
</div>

---

### The advent of containers
#### What are containers?

<div style="display:flex; justify-content:center;">
<img style="height:250px;" src="./assets/containers-vs-vms.svg">
</div>

Containers allowed for better application packaging by providing a simple way of ensuring all dependencies are installed and configured correctly, making it easier to move applications between environments and ensring they run the same way everywhere.

More info:
- In the Docker workshop (2022): https://niaefeup.github.io/slides/docker-workshop/Docker%20workshop_juliane_marubayashi.pdf
- Kubernetes docs: https://kubernetes.io/docs/concepts/overview/

---

### The advent of containers
#### What are image registries?

Containers are built from images. These images are built using a Dockerfile, which contains the instructions to build the image. Images can be stored in a registry, which can be public or private.

Registries enable easy sharing of images between developers and teams, and can be used to store images for CI/CD pipelines. Not only that but your computer also has a local registry to keep track of the images you have downloaded and to make it easier to build containers from them.

Some examples of registries are Docker Hub, Google Container Registry, and GitHub Container Registry.

---

class: center, middle, inverse
## The need for orchestration

---

### The need for orchestration
#### The common modern application

<img src="./assets/bank-of-anthos-architecture.png" style="height: 400px;">


---

### The need for orchestration
#### Modern application requirements

- Multiple services, each with its own dependencies (Microservices, providing responsability isolation and team autonomy)

- Multiple programming languages and frameworks with different requirements

- Pre-packaged software (e.g. databases, caches, etc.) that needs to be deployed alongside the application

- Configuration for each service, such as environment variables, secrets, etc.

- Inter-service communication, load balancing, and service discovery

- Scalability, high availability and performance requirements

- Monitoring, logging, and alerting

More info on modern app architectures: https://github.com/nginxinc/kic-reference-architectures (Also a good way for getting a cluster up and running with some common cool services)

---

### The need for orchestration
#### Achieving the impossible

**Orchestration** is the process of coordinating the automated configuration, management, and deployment of systems and software. 

In the context of microservices, orchestration is the process of managing the lifecycle of containers, ensuring they are running, healthy, and available.

Seems a simple concept, but when you have hundreds of services to manage it easily becomes a burden.

Seems like a lot of work, right? That's where **Kubernetes** comes in.

---

class: center, middle, inverse
## How does application deployment relate to CI/CD and DevOps?

---

### How does application deployment relate to DevOps and CI/CD?
#### CI/CD
From the definitions [(taken from the GitHub Actions workshop)](https://niaefeup.github.io/slides/gh-actions-workshop/#6):
- Continuous integration automates the process of trying to integrate new code into a main branch of a repository early and automatically to detect possible errors before actually merging the new code into production;

- Continuous delivery automates the release process once new changes are merged into the main branch by building the final binary of an application or even by moving to continuous deployment that also automates de deployment process (eg.: releasing a new version to Google Play).

We can see that Kubernetes can be used to automate the deployment process, making it easier to deploy new versions of the application and to scale it as needed, which is a key part of the CI/CD pipeline and ensuring applications fullfil their requirements.

Not only that but Kubernetes can also be used to automate the testing process, by providing a flexible environment to run tests in parallel and to ensure the application is working as expected.

---

### How does application deployment relate to DevOps and CI/CD?
#### DevOps
According to the definition provided by (Len Bass, Ingo Weber, and Liming Zhu), according to [Wikipedia](https://en.wikipedia.org/wiki/DevOps):
- DevOps is a set of practices that combines software development (Dev) and IT operations (Ops). It aims to shorten the systems development life cycle and provide continuous delivery with high software quality.

Apart from the CI/CD practices alredy mentioned, the configuration repeatability and centralized control provided by Kubernetes can help ensure that the development and operations teams are aligned and that the applications are deployed in a consistent way, reducing the risk of errors and ensuring that the applications are running as expected.

Not only that but the observability and monitoring tools that can be used with Kubernetes can help the teams to understand how the applications are behaving and to identify possible issues before they become a problem.

---

class: center, middle, inverse
# Kubernetes basic concepts
## (Finally, right?)

---

class: center, middle, inverse
## Architecture and main components

---

### Architecture and main components
#### Architecture overview

<div style="display:flex; justify-content:center;">
<img style="height:400px;" src="./assets/kubernetes-architecture.svg">
</div>

---

### Architecture and main components
#### The control plane
The control plane is where services responsible by managing the Kubernetes system are deployed. Machines running these services are called **master nodes**. By having multiple master nodes, the system can be made more resilient to failures, with the control plane services being distributed among the nodes.

The main components of the control plane are:

- **API Server**: The entry point for all the REST commands used to interact with the cluster.
- **Scheduler**: Responsible for distributing workloads across the nodes.
- **Controller Manager**: Responsible for monitoring the state of the cluster and making changes to ensure the desired state is achieved.
- **etcd**: A distributed key-value store used to store the cluster state.

---

### Architecture and main components
#### The workers
The worker nodes are the machines where the containers are run. They are managed by the control plane and are responsible for running the containers, monitoring their health, and reporting back to the control plane.

The main components of the worker nodes:
- **Kubelet**: The agent that runs on each node and is responsible for ensuring that the containers are running in a pod.
- **Kube-proxy**: A network proxy that runs on each node and is responsible for forwarding traffic to the correct container.
- **Container runtime**: The software that is responsible for running the containers. Docker is the most common runtime, but others like containerd and cri-o are also supported.

---

class: center, middle, inverse
## Pods, Workloads, Services and Ingresses, etc.

---

### Pods, Workloads, Services and Ingresses, etc.
#### Pods
A pod is the smallest deployable unit in Kubernetes. It represents a single instance of a running process in the cluster. Pods can contain one or more containers, which are run together in the same node and network namespace. They can share storage.

#### Workloads
Workloads are higher-level abstractions that represent a set of pods. They can be used to manage the lifecycle of the pods, such as scaling them up or down, rolling out new versions, etc. Some examples of workloads are Deployments, StatefulSets, and DaemonSets.

---

### Pods, Workloads, Services and Ingresses, etc.
#### Services
Services are used to expose pods to the network. They provide a stable internal IP address and DNS name for the pods, and can be used to load balance traffic between them. There are different types of services, such as ClusterIP, NodePort, and LoadBalancer.

#### Ingresses
Ingresses are used to expose services to the outside world. They provide a way to route external traffic to the services inside the cluster. Ingresses can be configured with rules to route traffic based on the host, path, etc.

---

### Pods, Workloads, Services and Ingresses, etc.
#### Etc.

- **ConfigMaps and Secrets**: Used to store configuration data and sensitive information, such as passwords and API keys. They can be mounted as volumes in the pods or used as environment variables. **Note**: Secrets are stored in etcd, but are not encrypted by default.

- **Volumes**: Used to provide persistent storage to the pods. There are different types of volumes, such as emptyDir, hostPath, and persistentVolumeClaim.

Many other Kubernetes (k8s) resources can be used to manage the cluster and the applications running in it. The [official documentation](https://kubernetes.io/docs/concepts/) is a good place to start learning about them.

We migh be using some later :)

---

class: center, middle, inverse
## Networking overview

---

### Networking overview
<div style="display:flex; justify-content:center;">
<img style="width:1000px;" src="./assets/networking.svg">
</div>

In a cloud managed Kubernetes cluster, the networking is usually handled by the cloud provider. In a managed cluster, the provider handles the networking for you by setting upa cloud load balancer which routes traffic to the correct service from an external endpoint.

In a bare-metal cluster, you will need to configure the networking yourself to achieve the same behaviour.

---


class: center, middle, inverse
## Kubernetes in the cloud vs bare-metal

---

### Kubernetes in the cloud vs bare-metal
When using a managed Kubernetes instance, provided by a 3<sup>rd</sup> party, like Google Cloud, AWS, or Azure, the provider takes care of the infrastructure, such as the control plane, worker nodes, and networking. This makes it easier to get started with Kubernetes, as you don't need to worry about setting up the cluster yourself.

Using bare metal deployments can have some performance advantages over some managed clusters.

This happens because some cloud providers use virtual machines to run the worker nodes, which can introduce some overhead.

---
## Other resources
- [Mara from NGINX](https://github.com/nginxinc/kic-reference-architectures) and the blogpost ["Mara now running on a workstation near you"](https://www.nginx.com/blog/mara-now-running-on-workstation-near-you/)
- My Networks and systems management course project - [Kubernetes pod autoscaling according to the number HTTP per service](https://github.com/Sirze01/feup-grs-autoscale)
- [K9s](https://k9scli.io/), a terminal UI for interacting with your Kubernetes clusters