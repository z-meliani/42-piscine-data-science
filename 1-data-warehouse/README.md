# Piscine Data Science - Data Warehouse

The `Data Warehouse` project serves as a foundational introduction to the ETL (Extract, Transform, Load) pipeline. It demonstrates the process of taking raw, fragmented data and turning it into a structured, queryable database.

- Extract: Raw data ingestion from CSV files into SQL tables.
- Transform: Data cleaning (removing duplicates) and relational modeling (joining tables).
- Load: Finalizing the data warehouse for efficient storage and retrieval.


## 🏗️ Project Architecture

```bash
.
├── data/
├── secrets/
│   └── postgres_password.txt
├── src/
│   ├── ex00
│   ...
│   └── ex03
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