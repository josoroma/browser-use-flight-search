# Set up the project by installing dependencies and activating the virtual environment
setup:
	@echo "Setting up the project..."
	poetry env use `which python3.11`
	poetry install
	poetry shell

# Add new dependencies to the project (example)
add:
	poetry add browser-use langchain-openai python-dotenv pydantic logging black pytest pytest-cov

# Run the Kayak flight search agent
run:
	poetry run python -m src.main "flights from San Francisco to Tokyo on April 5th returning April 12th"

# Run linting and formatting checks on the project
lint:
	poetry run black --check.

# Format the codebase with Black
format:
	poetry run black.

# Run all unit tests using pytest
test:
	poetry run pytest tests

# Generate and view a coverage report
coverage:
	poetry run pytest --cov=. --cov-report=html
	open htmlcov/index.html

# Clean up the project
clean:
	rm -rf `poetry env info -p`
	rm -rf poetry.lock
	rm -rf htmlcov
	rm -rf.pytest_cache
	rm -rf.mypy_cache