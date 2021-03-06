# Instructions to build and run the docker image

## build the image

assuming docker is installed and running in the machine and the `Dockerfile` is in the working directory.

use the command `sudo docker build -t <image name:version> .` to build the image.

## run the docker image

*The previously image created uses as base image the "official" fastapi image hence it is possible to override sensible configuration variables (e.g. Gunicorn configuration variables) in the `docker run` command. For more information refer to this [link](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker)*.

to run the image use the command `sudo docker run -d  --name <container name> -p <host port>:<container port>  <image name:version>`.

Notice that by default the container is listening on port 80 to override this value use `-e PORT=<container port>`.