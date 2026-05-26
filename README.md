<h1 align="center">ROS Repository Template</h1>

<p align="center">
  <em>A GitHub repository template for ROS 2 projects with Docker, pre-commit hooks, and CI/CD</em>
</p>

<p align="center">
  <a href="https://github.com/Tom-Notch/ROS-Repository-Template/actions/workflows/pre-commit.yml"><img src="https://github.com/Tom-Notch/ROS-Repository-Template/actions/workflows/pre-commit.yml/badge.svg" alt="pre-commit"></a>
  <a href="https://github.com/Tom-Notch/ROS-Repository-Template/actions/workflows/CI.yml"><img src="https://github.com/Tom-Notch/ROS-Repository-Template/actions/workflows/CI.yml/badge.svg" alt="CI"></a>
  <img src="https://img.shields.io/badge/ROS_2-Humble-22314e?logo=ros&logoColor=white" alt="ROS 2 Humble">
  <img src="https://img.shields.io/badge/Docker-Required-2496ed?logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
</p>

A GitHub repository template for ROS 2 (Humble) projects. Uses Docker for easy deployment and testing, with pre-commit hooks and GitHub Actions CI/CD included. The template package has both C++ and Python entrypoints.

> **TLDR:** Search for `todo` and update all occurrences to your desired name.

## Dependencies

- [Docker](https://docs.docker.com/get-docker/)

## Usage

### Base Repository

1. Change [LICENSE](LICENSE) if necessary
1. Modify [.pre-commit-config.yaml](.pre-commit-config.yaml) according to your needs
1. Modify/add GitHub workflow status badges in [README.md](README.md)

### Docker Config

1. Fill in all `todo-*` placeholders directly in [.env.example](.env.example) and commit — these are project-level constants, not secrets

   | Placeholder | Description |
   |-------------|-------------|
   | `todo-docker-user` | Your Docker Hub account username |
   | `todo-base-image` | Base image the Dockerfile builds from (e.g. `nvidia/cuda:13.0.0-cudnn-devel-ubuntu24.04`) |
   | `todo-image-name` | Name of the image you are building |
   | `todo-image-user` | Default user inside the image, used to determine the home folder |

1. Copy [.env.example](.env.example) to `.env` and add any user-specific secrets or local overrides:

   ```shell
   cp .env.example .env
   ```

   > `.env` is gitignored and will NOT be committed — it is the right place for secrets and per-user values. It is loaded automatically by docker compose.

1. Modify the service name from `todo-service-name` to your service name in [docker-compose.yml](docker-compose.yml), add additional volume mounting options such as dataset directories

1. Update [Dockerfile](docker/latest/Dockerfile) and [.dockerignore](.dockerignore) — the existing Dockerfile includes screen & tmux config, oh-my-zsh, cmake, and other basic tools

1. Run scripts to build, test, and push:

   | Script | Action |
   |--------|--------|
   | [build.sh](scripts/build.sh) | Build and test the image locally (uses `buildx` for multi-arch) |
   | [run_container.sh](scripts/run_container.sh) | Run and test a built image (`docker compose up -d` also works) |
   | [push.sh](scripts/push.sh) | Push the multi-arch image to Docker Hub |

   > The service mounts the entire repository onto `CODE_FOLDER` inside the container — modifications inside are reflected outside, useful for VS Code remote development.

### ROS Config

The template ROS package has both C++ and Python entrypoints.

1. Find all occurrences of **new_package** in code using your IDE's global search and replace with your ROS package name (`underscore_naming_convention`):

   <details>
   <summary>Files to update</summary>

   - `package.xml`
   - `CMakeLists.txt`
   - Python sources under `scripts/` and `src/` (both under the package directory)
   - C++ sources under `include/` and `src/` (both under the package directory)
   - Launch files
   - [launch.sh](scripts/launch.sh) — entry point to launch the ROS node from outside the container

   </details>

1. Rename folders and source files containing **new_package** or **NewPackage**:

   <details>
   <summary>Items to rename</summary>

   - Package directory → `underscore_naming_convention`
   - Python library directory → `underscore_naming_convention`
   - C++ library directory under `include/` → `UpperCamelCase`

   </details>

1. Update names of **launch files**

1. **(Optional)** In ROS 2 Humble, definitions of **msg, action, and srv** files must be in a **dedicated standalone package** to avoid conflicts with the Python portion of new_package — see [this GitHub issue](https://github.com/ros2/rosidl_python/issues/141) for details

1. Update package **dependencies** in **package.xml** and **CMakeLists.txt**

1. Find all occurrences of **new_project** namespace in C++ source files and replace with your project name

## Developer Quick Start

```shell
bash scripts/dev_setup.sh
```

## Notes

- Supports `amd64` and `arm64` Docker images. To add other architectures, modify [build.sh](scripts/build.sh) and [docker-compose.yml](docker-compose.yml).
