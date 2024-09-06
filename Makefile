.phony init:
init:
	pipenv shell
.phony run:
run:
	black EC1.py
	python3 EC1.py
