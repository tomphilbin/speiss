docker-build-m1:
	(cd ../../; sh ./scripts/protoc.sh)
	docker buildx build --platform linux/amd64 .

docker-build-ci:
	(cd ../../; sh ./scripts/protoc.sh)
	docker build . -t $(tag)
