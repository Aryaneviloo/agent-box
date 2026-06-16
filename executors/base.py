from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class ResourceLimits:
    memory_mb: int = 128
    cpu_quota: float = 0.5
    timeout_seconds: int = 10
    max_processes: int = 32



@dataclass
class ExecutionResult:
    stdout: str
    stderr: str
    exit_code: int
    duration_ms: float
    timed_out: bool = False


class Executor(ABC):
    @abstractmethod
    def run(
        self,
        code: str,
        limits: ResourceLimits = ResourceLimits()
    ) -> ExecutionResult:
        pass
    