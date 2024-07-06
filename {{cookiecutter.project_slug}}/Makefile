.PHONY: build up down destroy deps upgrade-deps bash shell makemigrations migrate deploy fly-shell

build:
	docker compose build

up:
	docker compose up

down:
	docker compose down

destroy:
	docker compose down --volumes --remove-orphans --rmi all

deps:
	pip-compile requirements/requirements.in
	pip-compile -o requirements/requirements-dev.txt requirements/requirements.txt requirements/requirements-dev.in

upgrade-deps:
	pip-compile --upgrade requirements/requirements.in
	pip-compile --upgrade -o requirements/requirements-dev.txt requirements/requirements.txt requirements/requirements-dev.in

bash:
	docker compose exec -e COLUMNS="`tput cols`" -e LINES="`tput lines`" web bash

shell:
	docker compose exec web python manage.py shell_plus --quiet-load --ipython

makemigrations:
	docker compose exec web python manage.py makemigrations

migrate:
	docker compose exec web python manage.py migrate

deploy:
	flyctl deploy --local-only --build-target production

fly-shell:
	flyctl ssh console --command 'python /opt/app/manage.py shell'
