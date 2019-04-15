ci:
	python -m unittest
	pytest --pep snnusdk
	pytest test
build-docs:
	cd docs && make html
	@echo "Build successful!"

