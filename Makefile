setup:
	pipenv install --dev --pre 

run:
	pipenv python main.py

shell:
	pipenv shell

ipython:
	pipenv run ipython

docker-run:
	docker-compose up --build

docker-shell:
	docker-compose run web bash

docker-ipython:
	docker-compose run web ipython
