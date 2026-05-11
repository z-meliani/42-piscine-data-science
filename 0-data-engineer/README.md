# Piscine Data Science - Data Engineer

The `Data Engineer` project is a light entry project to database creation and manipulation where you setup a PostgresSQL database within a container and creates tables from CSV files.

## 🏗️ Project Architecture

```bash
.
├── data/
├── secrets/
│   └── postgres_password.txt
├── src/
│   ├── ex00
│   ...
│   └── ex04
├── .env
├── docker-compose.yml
└── Makefile
```

## ⚙️ Setup

### 1. Environment variables

Create a `.env` file at the root of the project and define the following variables:

```bash
POSTGRES_USER=          # Database user name
POSTGRES_DB=            # Database name
```

### 2. Secrets

Create the required secrets file inside the `secrets/` directory and fill them:

- `postgres_password.txt`


## ▶️ How to run
```bash
# Start services
make
# or
make up

# Display logs
make logs

# Check container status
make check

# Stop containers
make stop

# Start stopped containers
make start

# Stop and remove containers
make down

# Remove containers, images, and anonymous volumes
make clean

# Equivalent to make clean + remove named volumes
make fclean

# Rebuild and start
make re

# Full clean + rebuild
make ref
```