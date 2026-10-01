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

# Auth Reuse

Keep what works:

- SIGARRA OIDC — same flow, new implementation
- Students keep university accounts
- Manual OIDC flow (~50 lines) or `openid-client`
- Admin role via database flag

No new passwords. No new accounts.

---

# Email Service

Migration from Mailjet to Resend:

- Same domain (`tts.niaefeup.pt`)
- Simpler API, better TypeScript support
- Uses standard `fetch` — perfect for Bun
- Free tier: 100 emails/day

```typescript
await resend.emails.send({
  from: 'TTS <noreply@tts.niaefeup.pt>',
  to: `up${nmec}@up.pt`,
  subject: 'Confirmação de troca',
  html: confirmationTemplate(link),
})
```

---

# What We Reuse

From the old backend:

- SIGARRA OIDC auth flow
- Email templates (HTML)
- Exchange validation logic (overlap detection)
- Docker Compose + nginx deployment
- Database data (migration script)

We only rewrite the parts that cause pain.

---

# What Is Excluded (For Now)

Not building yet:

- Redis — add if we need distributed caching
- Message queue — fire-and-forget emails are fine
- tRPC — REST is simpler, can migrate later
- Feature flags — fresh launch does not need them

This keeps scope realistic for 4 months.

---

# Timeline

September → January:

- **Setup + onboarding:** 2 weeks
- **Domain layer:** 2 weeks
- **Core exchange:** 4-5 weeks
- **SIGARRA integration:** 2-3 weeks
- **Admin + periods:** 2 weeks
- **Testing + polish:** 2-3 weeks
- **Buffer:** 2-3 weeks

Total: ~17 weeks. Tight but doable.

---

# Team & Onboarding

For first-year recruits:

- **Day 1:** walk through the exchange module end to end
- **Day 2:** make a small change (add a field)
- **Day 3:** add a new endpoint
- **Week 1:** first feature

The structure tells you where everything goes.
ESLint rules enforce boundaries automatically.

---

# Risks & Mitigation

- **Clean Architecture learning curve** — pragmatic shortcuts for simple features
- **Uni exams overlap** — 3-week buffer built in
- **First-year skill gap** — pair programming, golden example module
- **SIGARRA API changes** — isolated in `infrastructure/external/`
- **Scope creep** — cut real-time features and feature flags

---

template: title

# Next Steps

1. Approve this proposal
2. Create repository and CI pipeline
3. Set up Prisma schema
4. Scaffold the exchange module
5. Assign first issues to new recruits

## Questions?
