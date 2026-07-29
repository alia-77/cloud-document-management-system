from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.core.auth import get_current_user
from app.db.database import get_db
from app.models.document import Document
from app.models.user import User
from app.schemas.document import DocumentResponse
from app.services.s3 import upload_file_to_s3, download_file_from_s3, delete_file_from_s3


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post("/upload")
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    
    stored_filename = upload_file_to_s3(file)

    document = Document(
        original_filename=file.filename,
        stored_filename=stored_filename,
        file_path=stored_filename,
        file_size=file.size,
        content_type=file.content_type,
        owner_id=current_user.id
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return {
        "message": "File uploaded successfully",
        "document_id": document.id,
        "filename": document.original_filename
    }


@router.get(
    "",
    response_model=list[DocumentResponse]
)
def get_my_documents(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    documents = (
        db.query(Document)
        .filter(Document.owner_id == current_user.id)
        .all()
    )

    return documents


@router.get("/{document_id}")
def download_document(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    document = (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    if document.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    temp_path = download_file_from_s3(
        document.stored_filename
    )

    return FileResponse(
        path=temp_path,
        filename=document.original_filename,
        media_type=document.content_type
    )


@router.delete("/{document_id}")
def delete_document(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    document = (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    if document.owner_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    delete_file_from_s3(
        document.stored_filename
    )

    db.delete(document)
    db.commit()

    return {
        "message": "Document deleted successfully"
    }