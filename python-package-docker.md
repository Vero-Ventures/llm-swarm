# Running the docker for python-package

docker build -t my-python-app -f python-package/Dockerfile .
docker run -p 8000:8000 my-python-app
