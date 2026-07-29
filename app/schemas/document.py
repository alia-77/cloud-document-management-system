from pydantic import BaseModel
from datetime import datetime


class DocumentResponse(BaseModel):
    id: int
    original_filename: str
    file_size: int
    content_type: str
    uploaded_at: datetime

    class Config:
        from_attributes = True