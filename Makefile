.PHONY: run-dev run-prod build-dev build-prod test

run-dev:
	docker compose -f docker-compose_dev.yml up --build

run-prod:
	docker compose -f docker-compose_prod.yml up --build -d

test:
	python -m pytest -v

style:
	black .
	ruff check . --fix

clear_dev:
	docker compose -f docker-compose_dev.yml down -v
	docker compose -f docker-compose_dev.yml down
	docker compose -f docker-compose_dev.yml build --no-cache
	docker compose -f docker-compose_dev.yml  up