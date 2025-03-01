build-api:
		@echo	"Building	API..."
		cd	code	&&	python	-m	pip	install	-r	requirements.txt

run-tests:
		@echo	"Running	tests..."
		cd	code	&&	python	-m	pytest

lint-code:
		@echo	"Linting	code..."
		pylint	code/

docker-build:
		@echo	"Building	Docker	image..."
		cd	code	&&	docker	build	-t	my-api-image	.

docker-run:
		@echo	"Running	Docker	Container..."
		docker	run	-d	--name	my-api-container	-p	80:8080	my-api-image
