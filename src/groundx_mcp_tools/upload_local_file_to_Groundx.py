from groundx import AsyncGroundX, Document
from typing import Optional, Dict, Any

async def upload_local_file_to_Groundx(
    groundx_api_key: str,
    bucket_id: str,
    file_name: str,
    file_path: str,
    file_type: str
) -> dict:
    """
    Upload documents hosted on a local file system into a GroundX bucket.
    
    See: https://docs.eyelevel.ai/reference/api-reference/documents/ingest-documents/ingest-local

    Args:
        groundx_api_key (str): The API key for GroundX.
        bucket_id (str): The bucketId of the bucket to upload into.
        file_name (str): The name of the file as it will appear in GroundX. (e.g. 'document.pdf').
        file_path (str): Absolute or relative path to the local file to ingest. (e.g. '/path/to/document.pdf').
        file_type (str): MIME type or supported extension (e.g. 'pdf', 'docx', etc.).
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        response = await client.ingest(
            documents=[
                Document(
                    bucket_id=bucket_id,
                    file_name=file_name,
                    file_path=file_path,
                    file_type=file_type
                )
            ]
        )
        return response
    except Exception as e:
        return {"error": f"Failed to ingest local file: {str(e)}"}
