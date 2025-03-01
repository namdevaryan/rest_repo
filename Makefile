build-api:
[TAB]@echo "Building API..."
[TAB]cd code && python -m pip install -r requirements.txt

run-tests:
[TAB]@echo "Running tests..."
[TAB]cd code && python -m pytest

lint-code:
[TAB]@echo "Linting code..."
[TAB]pylint code/

docker-build:
[TAB]@echo "Building Docker image..."
[TAB]cd code && docker build -t my-api-image .

docker-run:
[TAB]@echo "Running Docker container..."
[TAB]docker run -d --name my-api-container -p 80:8080 my-api-image
