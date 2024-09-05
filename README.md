# Event Management API

A Django-based REST API for managing events such as conferences and meetups. This project includes user registration, event creation, and event registration, all powered by Django and PostgreSQL, containerized with Docker.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [API Endpoints](#api-endpoints)
  
## Features

- User registration and authentication with JWT
- CRUD operations for managing events
- Event registration for users
- Search and filter events
- Email notifications upon event registration
- API documentation with Swagger and Redoc
- Docker setup for easy deployment

## Technologies Used

- **Django**: Web framework for building the backend
- **Django REST Framework**: Toolkit for building Web APIs
- **PostgreSQL**: Relational database for storing data
- **Docker**: Containerization for easy deployment
- **Swagger and Redoc**: API documentation

## Getting Started

### Prerequisites

- **Docker**: Ensure Docker and Docker Compose are installed on your system.

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/rodionmaulenov/Events.git
    cd Events
    ```

2. **Create a `.env` file**:

   Create a `.env` file in the root directory with the following environment variables:

    ```env
    POSTGRES_DB=event_management
    POSTGRES_USER=user
    POSTGRES_PASSWORD=password
    POSTGRES_HOST=db
    ```
3. **Make the `entrypoint.sh` script executable**:

   The `entrypoint.sh` script needs to be executable to run properly inside the Docker container. You can make it executable by running:

   ```bash
   chmod +x entrypoint.sh

### Environment Variables

- **`POSTGRES_DB`**: The name of the PostgreSQL database.
- **`POSTGRES_USER`**: The username for PostgreSQL.
- **`POSTGRES_PASSWORD`**: The password for the PostgreSQL user.
- **`POSTGRES_HOST`**: The host of the PostgreSQL service (`db`).


### Usage

#### Running the Application

1. **Build and start the Docker containers**:

    ```bash
    docker-compose up --build
    ```

   This command will build the Docker images and start the services defined in `docker-compose.yml`.

2. **Apply Migrations**:

   Migrations are automatically applied during the Docker container startup through the `entrypoint.sh` script.


#### API Endpoints

- **Swagger Documentation**: `http://localhost:8000/swagger/`
- **Redoc Documentation**: `http://localhost:8000/redoc/`

Here are some of the key API endpoints:

- **User Registration**: `POST /api/register/`
- **Token Obtain Pair**: `POST /api/token/`
- **Event List/Create**: `GET /api/events/`, `POST /api/events/`
- **Event Registration**: `POST /api/registrations/`

