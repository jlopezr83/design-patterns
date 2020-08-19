DOCKER_IMAGE = design-patterns

build:
	docker build -t ${DOCKER_IMAGE} .

test:
	docker run ${DOCKER_IMAGE} bash -c 'PYTHONPATH=./src pytest tests'

deploy: build test


.PHONY: build deploy test
