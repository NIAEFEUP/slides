name: title
layout: true
class: center, middle, inverse

---

name: normal
layout: true
class: left, middle

---

class: center, middle, inverse, small-images

# Niployments Introduction 

<div style="display: flex; justify-content: center; margin-top: 3em; align-items: center; gap: 1em;">
  <img src="./assets/logos/ni.png">
  <div style="font-size: 2.5em; padding-inline: 0.5em;">❤️</div>
  <img src="./assets/logos/kubernetes.png">
</div>

---

class: center, middle, inverse

# Important links

#### This presentation is available online from the link below:

<div style="display: flex; justify-content: center; align-items: center; margin: 4rem 0rem;">
  <a href="https://slides.niaefeup.pt/slides/niployments-introo" style="color: white; font-weight:bold; font-size: 1.5rem; text-align:center;">https://slides.niaefeup.pt/niployments-intro</a>
</div>

#### Github repository

<div style="display: flex; justify-content: center; align-items: center; margin: 4rem 0rem;">
  <a href="https://github.com/NIAEFEUP/niployments" style="color: white; font-weight:bold; font-size: 1.5rem; text-align:center;">https://github.com/NIAEFEUP/niployments</a>
</div>

---

# Why have a local server cluster?

<img src="./assets/logos/cluster.png" style="width:800px; height:400px; display:block;">

---

# Why kubernetes?

- Automatic replication

- Easy to have multiple computers running the same thing

---

# How to deploy in kubernetes?

<img src="./assets/logos/deployment_example.png" style="width: 450px; height: 425px;"/>

---

# How to put images in niployments?

- Harbor (https://harbor.niaefeup.pt)

- Github Actions to build images 


---

# How to ensure same config in all PCs?

- Ansible

<img src="./assets/logos/ansible_example.png" style="width:550px; height:150px; display:block;">

- `nix` / NixOS (?!?!?!?!?!?!?!?!?!?!?!??!?!?!?!?!?!)

---

# How to redirect `tts.niaefeup.pt` to the container?

---

# Reverse proxies

<img src="./assets/logos/traefik-reverse-proxy.png" style="width: 500px; height: 550px; display: block;" />

---

# How to access `niployments` servers?

- SSH (Secure Shell)

- Needs to be inside VPN (Tailscale)

---

# What is DNS?

- Domain Name System

- Humans understand names better than IP Addresses (e.g. 140.82.121.3)

- `tts.niaefeup.pt` is translated to 193.136.38.172

---

# How we manage records

<img src="./assets/logos/cloudflare-dns-records.png" style="width: 800px; height: 400px;" />

---

# How storage works

---

# Longhorn

- https://longhorn.io/

- Distributed file block storage

- Each deployed app can have a `PersistentVolumeClaim`

- Allows shared storage between all servers

---

# How to load balance and ensure connectivity between pods?

---

# Cilium

- Load balance

- Enables communication between different pods

- Servers as a load balancer for pod services

- It includes `Hubble` to have a certain degree of network observability

---

<img src="./assets/logos/log.png">