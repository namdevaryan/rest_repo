build-api:
	@echo	"Building	API..."
	cd	code	&&	python	-m	pip	install	-r	requirements.txt

run-test:
	@echo	"Running	tests..."
	cd	code	&&	python	-m	pytest

link-code:
	@echo	"Linting	code..."
	pylint	code/

docker-build:
	@echo	"Building	Docker	image..."
	cd	code	&&	docker	build	-t	my-api-image	.

docker-run:
	@echo	"Running	Docker	container..."
	docker	run	-d	--name	my-api-container	-p	80:8080	my-api-image
