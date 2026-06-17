import time
import docker
import docker.errors

from executors.base import Executor, ExecutionResult, ResourceLimits


class DockerExecutor(Executor):
    def __init__(self):
        self._client = docker.from_env()
        self._image = "python:3.11-alpine"

        