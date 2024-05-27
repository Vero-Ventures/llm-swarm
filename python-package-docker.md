# Running the docker for python-package

docker build -t my-python-app -f python-package/Dockerfile .

docker run -it --rm my-python-app -i /path/to/input -o /path/to/output -v
