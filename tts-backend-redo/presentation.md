name: title
layout: true
class: center, middle, inverse

---

name: normal
layout: true
class: left, top

---

template: title
class: small-images

# TTS Backend Redo
## Proposal

<div style="display: flex; justify-content: center; margin-top: 2em;">
  <img src="../logo.png" alt="NIAEFEUP" style="width: 200px;">
</div>

NIAEFEUP — September 2026

---

# Why Are We Doing This?

Current backend problems:

- **4 fragmented exchange systems** (direct, marketplace, urgent, enrollment)
- Business logic mixed with HTTP handlers
- No audit trail or event log
- No automated tests
- SIGARRA calls scattered everywhere
- Hard to onboard new members

> Fixing a bug in one exchange type does not fix the other three.

---

# Goals

What success looks like by end of January:

- One unified exchange model
- Clear separation of concerns
- First-year students can contribute in week 1
- Critical paths are tested
- Clean deployment with Docker Compose + nginx

---

# Tech Stack

.horizontal[

- **Runtime:** Bun
- **Framework:** Elysia
- **ORM:** Prisma
- **Database:** PostgreSQL


- **Validation:** Zod
- **Email:** Resend
- **Auth:** SIGARRA OIDC (reused)
- **Testing:** Bun test
- **Deployment:** Docker Compose + nginx

]

---

# Why Elysia + Bun?

- Built for each other — native Bun integration
- Frontend team already knows TypeScript
- Built-in validation and plugins
- Fast hot reload and testing
- Type-safe end-to-end with Eden Treaty

> We keep deployment the same. Only the app inside the container changes.

---

# Architecture

Clean Architecture layers — dependencies point inward:

<div style="margin-top: 1em; text-align: center; font-family: 'Ubuntu Mono', monospace;">
  <div style="background: #13212e; color: white; padding: 0.8em; margin: 0.3em 0;">
    <strong>domain/</strong> — pure business rules
  </div>
  <div style="background: #1e3a52; color: white; padding: 0.8em; margin: 0.3em 0;">
    <strong>application/</strong> — use cases
  </div>
  <div style="background: #2a5270; color: white; padding: 0.8em; margin: 0.3em 0;">
    <strong>infrastructure/</strong> — Prisma, SIGARRA, email
  </div>
  <div style="background: #366a8e; color: white; padding: 0.8em; margin: 0.3em 0;">
    <strong>interface/</strong> — routes, middleware
  </div>
</div>

---

# Folder Structure

```text
src/
├── domain/           # entities, value-objects, ports
├── application/      # use-cases, services
├── infrastructure/   # database, external APIs
├── interface/        # routes, middleware, validators
├── core/             # errors, utils
└── main.ts
```

Each layer has one job. Boundaries are enforced by ESLint.

---

# Database Design

One table for all exchanges:

```text
exchange_request            (kind, status)
exchange_participant        (one row per student)
exchange_item               (one row per student per UC)
exchange_confirmation_token (UUID email links)
exchange_event              (audit log)
exchange_period             (when exchanges are open)
```

**Before:** 4 fragmented table pairs

**After:** 3 normalized tables + audit + tokens

---

template: title

# Next Steps

## Questions?
