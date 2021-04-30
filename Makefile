setup:
	pipenv install --dev --pre 

run:
	pipenv run python main.py

shell:
	pipenv shell

ipython:
	pipenv run ipython

docker-build:
	docker-compose build

docker-stop:
	docker-compose stop 

docker-destroy:
	docker-compose down 

docker-run:
	docker-compose up --build

docker-shell:
	docker-compose run web bash

docker-ipython:
	docker-compose run web ipython

expose:
	./ngrok http http://localhost:8000

