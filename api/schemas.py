from pydantic import BaseModel
from datetime import datetime
from api.models import JobStatus

class JobCreate(BaseModel):
    code: str


class JobResponse(BaseModel):
    id: str
    status: JobStatus
    code: str
    stdout: str | None
    stderr: str | None
    exit_code: int | None
    duration_ms: float | None
    created_at: datetime
    completed_at: datetime | None

    model_config = {"from_attributes": True}