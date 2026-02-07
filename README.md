# fullstack_developer_capstone

````md
# Best Cars Dealership Review Platform

![Django](https://img.shields.io/badge/Django-4.2-orange)
![React](https://img.shields.io/badge/React-18-blue)
![MongoDB](https://img.shields.io/badge/MongoDB-7.0-green)
![Node.js](https://img.shields.io/badge/Node.js-20-purple)
![Docker](https://img.shields.io/badge/Docker-Containers-lightblue)
![IBM Cloud](https://img.shields.io/badge/IBM%20Cloud-Code%20Engine-purple)

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Microservices Implementation](#microservices-implementation)
- [Django Models & Views](#django-models--views)
- [Car Inventory Management](#car-inventory-management)
- [Django Proxy Services Implementation](#django-proxy-services-implementation)
- [Setup Instructions](#setup-instructions)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Why I Built This](#why-i-built-this)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Overview

**Best Cars Dealership Review Platform** is a full-stack web application built for a national car dealership network to enhance customer transparency and trust. The platform allows customers to browse dealerships across the United States, read authentic customer reviews, and submit their own experiences.

Built as a capstone project demonstrating enterprise-level development practices, this application showcases a modern **microservices architecture** using **Django, React, MongoDB**, and **cloud-native deployment**.

The solution addresses key business requirements identified through market research by providing a centralized review system that helps customers make informed decisions while giving dealerships valuable feedback for continuous improvement.

---

## Architecture

### System Architecture Diagram

```text
┌─────────────────────────────────────────────────────────────────────────┐
│                          User Browser                                   │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    Django Application (Port: 8000)                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐                 │
│  │   Static    │  │     Auth    │  │   Django        │                 │
│  │   Pages     │  │   System    │  │   Models        │                 │
│  └─────────────┘  └─────────────┘  └─────────────────┘                 │
│         │                │                    │                         │
│         └────────────────┼────────────────────┘                         │
│                          │                                              │
│                  ┌───────▼───────┐                                     │
│                  │   Django      │                                     │
│                  │  Proxy Views  │                                     │
│                  └───────┬───────┘                                     │
│                          │                                              │
└──────────────────────────┼──────────────────────────────────────────────┘
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
         ▼                 ▼                 ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│  Node.js/Mongo  │ │   Sentiment     │ │    Django       │
│    Service      │ │    Analyzer     │ │     Admin       │
│   (Port: 5000)  │ │   (Port: 5050)  │ │    (Port: 8000) │
└─────────────────┘ └─────────────────┘ └─────────────────┘
         │                    │                    │
         ▼                    ▼                    ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│    MongoDB      │ │   NLTK/VADER    │ │    SQLite       │
│   Database      │ │     Library     │ │    Database     │
└─────────────────┘ └─────────────────┘ └─────────────────┘
````

---

### Component Architecture

| Component          | Technology                  | Purpose                                      |
| ------------------ | --------------------------- | -------------------------------------------- |
| Frontend UI        | React.js + Bootstrap        | Responsive dealership browsing and review UI |
| Web Framework      | Django 4.2                  | Main application server, routing, templates  |
| Authentication     | Django Auth                 | User registration, login, session management |
| Dealership Service | Node.js + Express + MongoDB | Dealership and review microservice           |
| Django Models      | SQLite + Django ORM         | Car makes, models, and inventory             |
| Sentiment Analysis | Flask + NLTK/VADER          | AI-powered review sentiment scoring          |
| Database           | SQLite + MongoDB            | Dual-database architecture                   |
| Proxy Services     | Django REST Helpers         | Microservice communication layer             |
| Containerization   | Docker                      | Container-based deployment                   |

---

## Features

### 🏢 Anonymous Users

* Browse dealership listings across all U.S. states
* Filter dealerships by state
* View dealership details
* Read customer reviews
* Access **About Us** and **Contact Us** pages
* Fully responsive design

---

### 🔐 Registered Users

Includes all anonymous features plus:

* User registration and authentication
* Submit reviews for dealerships
* Review form with:

  * Star ratings
  * Purchase verification
  * Vehicle details (make, model, year)
  * Purchase date
  * Text review with sentiment analysis
* Personal dashboard for submitted reviews

---

### ⚙️ Admin Users

* Django Admin interface
* CRUD operations for car makes and models
* User management and moderation
* Review validation and approval
* Analytics dashboard
* Sentiment analysis reports

---

### 📊 Advanced Features

* **Sentiment Analysis** (Positive / Neutral / Negative)
* **Real-time updates** for newly submitted reviews
* **Persistent data storage**
* **Search and filter** by state
* **Security features**:

  * CSRF protection
  * Secure authentication
  * Input validation
* **Microservices integration**

---

## Tech Stack

### Frontend

* React 18
* Bootstrap 5
* CSS3
* JavaScript (ES6+)

---

### Backend

* Django 4.2
* Django REST Framework
* SQLite
* Node.js + Express
* MongoDB
* Mongoose ODM
* Flask
* NLTK / VADER

---

### DevOps & Deployment

* Docker
* GitHub Actions (CI/CD)

---

### AI / ML Integration

* Natural Language Processing
* VADER Sentiment Analysis
* NLTK Library

---

## Microservices Implementation

### Node.js + MongoDB Dockerized Server

The Django application communicates with MongoDB through a **containerized Node.js microservice**, enabling scalability and separation of concerns.

---

### Implemented API Endpoints

| Endpoint                   | Method | Description                | Response                |
| -------------------------- | ------ | -------------------------- | ----------------------- |
| `/fetchDealers`            | GET    | Fetch all dealerships      | Array of dealers        |
| `/fetchDealer/:id`         | GET    | Fetch dealership by ID     | Dealer object           |
| `/fetchDealers/:state`     | GET    | Fetch dealerships by state | Array of dealers        |
| `/fetchReviews`            | GET    | Fetch all reviews          | Array of reviews        |
| `/fetchReviews/dealer/:id` | GET    | Fetch reviews for a dealer | Array of reviews        |
| `/insertReview`            | POST   | Insert a new review        | Success / error message |

```
```
