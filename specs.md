It's a bookstore.

- On github.
- Tasks/management on github

* API (python)
* UI (react)
* infra

# Overview

What does it do?
Every user has its own dashboard.

The user can see the books that they have rented.

- previous rentals
- current rentals
- search

The user can view the books available.
These are searchable.

For each book:

- title/desc/author etc
- copies available
- hardcopies

## Admin

- can add new books
- can edit

- can manage users (to some extent).

# Models

## User

- id: uuid
- username: string
- password: string
- fullName: string
- avatar?: URL
- bio?: string
- <other>

## Books

- id: uuid
- isbn: ISBN
- title: string
- description: string
- coverImage: URL
- availableQuantity: int
- totalQuantity: int
- tags: []string
- category?: string

## Rentals

- id: uuid
- userId: uuid (ref to user)
- bookId: uuid, ref to user
- rentedAt: Date (TZ)

## Filters

- userId: uuid (ref to uer)
- filter: JSON

# API

## Auth

## Users

## Books

## Rentals

## Stats/reports

# Front-end specs

## User dashboard

### Main page

- List of avaibale books
- Available filters (for example by category, latest, most rented etc)
- Search

### User dashboard

- Preview current rented books
- Previous rentals

## Admin dashboard

### Main board

- stats - total books, total rented (in time intrval), new users, rentals per user etc
- alerts: late rentals

### Management pages

- User management
  - Update user password, invite user, disable account
- Books management
  - Add book
  - Remove books
  - update
  - view stats
- Rentals
- currently rented
- late rentals
- previous rentals
