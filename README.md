# New ROS Repository

[![pre-commit](https://github.com/Tom-Notch/ROS-Repository-Template/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/Tom-Notch/ROS-Repository-Template/actions/workflows/pre-commit.yml) [![Continuous Integration](https://github.com/Tom-Notch/ROS-Repository-Template/actions/workflows/CI.yml/badge.svg)](https://github.com/Tom-Notch/ROS-Repository-Template/actions/workflows/CI.yml)

This template uses Docker for easy deployment and testing. It also includes GitHub Actions for CI/CD.

## Dependencies

- [Docker](https://docs.docker.com/get-docker/)

## Usage Guidelines

TLDR: Search for `todo` and update all occurrences to your desired name

### Base Repository

1. Change [LICENSE](LICENSE) if necessary

1. Modify [.pre-commit-config.yaml](.pre-commit-config.yaml) according to your need

1. Modify/add GitHub workflow status badges in [README.md](README.md)

### Docker Config

1. Copy [.env.example](.env.example) to `.env`:

   ```shell
   cp .env.example .env
   ```

1. Modify `todo-docker-user`, `todo-base-image`, `todo-image-name`, `todo-image-user` in `.env`

   - `.env` will be loaded when you use docker compose for build/run/push
   - `todo-docker-user` refers to your docker hub account username
   - `todo-base-image` is the image dockerfile is based on, such as `nvidia/cuda:13.0.0-cudnn-devel-ubuntu24.04`
   - `todo-image-user` refers to the default user inside the image, which is used to determine home folder

1. Modify the service name from `todo-service-name` to your service name in [docker-compose.yml](docker-compose.yml), add additional volume mounting options such as dataset directories

1. Update [Dockerfile](docker/latest/Dockerfile) and [.dockerignore](.dockerignore)

   - Existing dockerfile has screen & tmux config, oh-my-zsh, cmake, and other basic goodies
   - Add any additional dependency installations at appropriate locations

1. [build.sh](scripts/build.sh) to build and test the image locally in your machine's architecture

   - The scripts uses buildx to build multi-arch image, you can disable this by removing redundant archs in [docker-compose.yml](docker-compose.yml)
   - Building stage does not have GPU access, if some of your dependencies need GPU, build them inside a running container and commit to the final image

1. [run_container.sh](scripts/run_container.sh) or `docker compose up -d` to run and test a built image

   - The service by default will mount the whole repository onto `CODE_FOLDER` inside the container so any modification inside also takes effect outside, which is useful when you use vscode remote extension to develop inside a running container with remote docker context
   - You should be able to run and see GUI applications inside the container if `DISPLAY` is set correctly when you run the script

1. [push.sh](scripts/push.sh) to push the multi-arch image to docker hub

   - You should have the docker hub repository set up before pushing

### ROS Config

The template ROS package has both C++ and Python entrypoints. You can modify the package to suit your needs.

1. Find all occurrences of **new_package** in code using your IDE's global search feature and replace them with your new ROS package name, must follow *underscore_naming_convention*, these include:

   1. package.xml
   1. CMakeLists.txt
   1. Python sources under scripts and src (both under the package directory)
   1. C++ sources under include and src (both under the package directory)
   1. launch files
   1. shell script [launch.sh](scripts/launch.sh) to launch docker container and the ROS node

1. Find all occurrences of **new_package** or **NewPackage** in the naming of folders and source files and replace them with your package name, must follow *underscore_naming_convention* for python files and *UpperCamelCase* for non-entrypoint C++ files, these include:

   1. package directory
   1. Python library directory
   1. C++ library directory under include

1. Update name of **launch files**

1. (Optional) In ROS 2 Humble, definitions of **msg, action, and srv** file have to be put in a **dedicated standalone package**, otherwise it'll cause conflict with the python portion of new_package, check out [this GitHub issue](https://github.com/ros2/rosidl_python/issues/141) for more info

1. Update the package **dependencies** in **package.xml** and **CMakeLists.txt**

1. Find all occurrences of **new_project** namespace in C++ source files and replace them with your project name

## Developer Quick Start

- Run [scripts/dev_setup.sh](scripts/dev_setup.sh) to setup the development environment

## Note

- This template currently only supports docker image for amd64 and arm64, if you want to support other architectures, please modify the [build.sh](scripts/build.sh) script and [docker-compose.yml](docker-compose.yml) accordingly
