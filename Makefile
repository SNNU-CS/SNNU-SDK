ci:
	python -m unittest
	pytest --pep snnusdk
	pytest test