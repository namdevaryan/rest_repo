build-api:
	@echo "Building API..."
	cd code && python3 -m pip install -r requirements.txt

run-tests:
	@echo "Running tests..."
	cd code && PYTHONPATH=$(PWD) python3 -m pytest

lint-code:
	@echo "Linting code..."
	cd code && find . -name "*.py" | xargs pylint || true

docker-login:
	@echo "Logging into Docker registry..."
	docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}

docker-build:
	@echo "Building Docker image..."
	docker build . -t aryan2001/my-api-image

docker-push:
	@echo "Pushing Docker image..."
	docker push aryan2001/my-api-image
