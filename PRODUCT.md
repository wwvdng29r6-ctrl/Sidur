# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

- **Primary (admin version, `index.html`):** the person responsible for the duty schedule of several shift commanders. Builds next year's schedule, checks it is fair between the shifts, approves it, and publishes it to the commanders. Works mostly on a phone, mostly in daytime.
- **Secondary (commanders' version, `mefakdim/`):** the shift commanders. They view the approved schedule, shared trainings, and keep their own notes. They join with a code from the admin.

## Product Purpose

Run a rotating duty schedule of three shifts (א׳ · ב׳ · ג׳), where exactly one shift is on duty every day. Answer "who is on today/tomorrow" instantly, show the monthly and yearly boards, and let the admin build next year's draft so that days and holidays are divided fairly. Success: an approved yearly schedule everyone trusts as fair, and a one-glance answer to "what is my shift".

## Positioning

A fairness engine specific to this rotation: it tries hundreds of rotation-swap scenarios so each holiday goes to the shift that has gone longest without it over the last three years, while keeping total days within one day between shifts (using balance days when needed). Corrections can be made by chat ("change the 12th to ב").

## Operating Context

- Yearly cycle: draft the coming year, run the engine, correct, approve, publish to commanders.
- Daily: check current shift, next holidays, trainings.
- Data lives in the browser and syncs between the admin's devices via Firebase (sync code). Commanders receive only what the admin published; their notes are encrypted.
- Hebrew holidays and weekends (Friday–Saturday) are central to fairness.

## Capabilities and Constraints

- Static site on GitHub Pages; no build tooling beyond `src/build.py`, which produces `index.html` (admin) and `mefakdim/index.html` (commanders) from `src/sidur.src.html` using `@admin` / `@member` markers. Both versions share one stylesheet.
- Hebrew, right-to-left throughout.
- Views: overview, monthly board, yearly board, next-year workspace (admin), trainings, notes (commanders), corrections chat (admin), settings/backup.
- Terminology: משמרת, טיוטה, מנוע הוגנות, יום איזון, אישור והחלה, קוד הצטרפות.

## Product Principles

1. The answer to "what is my shift" is never more than a glance away.
2. Fairness is shown, not asserted: every number the engine optimizes is visible and explainable.
3. Nothing changes the schedule without a way back.
4. The phone is the primary device; desktop is for the yearly build.

## Accessibility & Inclusion

Full keyboard and screen-reader support for schedule editing; text legible on a phone in daylight; meaning never carried by color alone.
