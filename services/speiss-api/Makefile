docker-build-m1:
	cp -r ../protos/ ./protos/
	docker buildx build --platform linux/amd64 .
	rm -rf ./protos

docker-build-ci:
	cp -r ../protos/ ./protos/
	docker build . -t $(tag)
	rm -rf ./protos
