SHELL := /usr/bin/env bash

# include ./srcs/.env

# Path of compose file
COMPOSE_FILE = docker-compose.yml

# File to avoid relink
COMPOSE_TMP = .compose.tmp

# Docker compose command with flags
DOCKER_COMPOSE = docker compose -f $(COMPOSE_FILE)

RM = rm -rf

all : up

up: $(COMPOSE_TMP)

$(COMPOSE_TMP) : $(COMPOSE_FILE)
	$(DOCKER_COMPOSE) up -d --build
	@ touch $(COMPOSE_TMP)

# Start containers
start:
	$(DOCKER_COMPOSE) start

# Stop containers
stop:
	$(DOCKER_COMPOSE) stop

# Stop and remove containers
down:
	$(DOCKER_COMPOSE) down
	@ $(RM) $(COMPOSE_TMP)

# Display logs
logs:
	$(DOCKER_COMPOSE) logs -f

# Check container status
check:
	@ $(DOCKER_COMPOSE) ps -q \
	| xargs docker inspect --format '{{printf "{\"%s\": %s}\n" (title .Name) (json .State)}}' \
	| jq -s 'add'

# Removes containers, images and anonymous volumes
clean: down
	$(DOCKER_COMPOSE) down --rmi all
	docker image prune -f
	docker volume prune -f
	@ $(RM) $(COMPOSE_TMP)

# Remove containers, images and volumes
fclean: clean
	$(DOCKER_COMPOSE) down -v

# clean, build and start
re: clean up

# full clean, build and start
ref: fclean up


.PHONY : all up start stop down logs check clean fclean re ref
