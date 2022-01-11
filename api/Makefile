docker-build-amd64:
	cp -r ../services/protos/ ./protos/
	docker buildx build --platform linux/amd64 .
	rm -rf ./protos
