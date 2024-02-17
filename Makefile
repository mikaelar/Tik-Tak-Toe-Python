setup:
	@pip install -r requirements.txt && echo "Completed installing requirements."

fmt: setup
	@black .
	@echo "Formated using black!"

test: setup
	@echo "Running unittests and Generating coverage."
	@coverage run -m unittest discover
	@coverage report
	@coverage html
	@echo "\nOpen htmlcov/index.html in browser for more details...\nYou can do that by executing:\n'''\nopen -a \"Google Chrome\" ./htmlcov/index.html\n'''\nin the shell directly.\n"
	@echo "Completed."