from groundx import AsyncGroundX, Document
from typing import Optional, Dict, Any

async def upload_remote_file_to_Groundx(
    groundx_api_key: str,
    bucket_id: str,
    file_name: str,
    remote_url: str,
    file_type: str
) -> dict:
    """
    Ingest documents hosted on public URLs into a GroundX bucket.
    
    See: https://docs.eyelevel.ai/reference/api-reference/documents/ingest-documents/ingest-remote

    Args:
        groundx_api_key (str): The API key for GroundX.
        bucket_id (str): The bucketId of the bucket to upload into.
        file_name (str): The name of the file as it will appear in GroundX.
        remote_url (str): URL of the remote file.
        file_type (str): MIME type or supported extension (e.g. 'pdf', 'docx', etc.).
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        response = await client.ingest(
            documents=[
                Document(
                    bucket_id=bucket_id,
                    file_name=file_name,
                    file_path=remote_url,
                    file_type=file_type
                )
            ]
        )
        return response
    except Exception as e:
        return {"error": f"Failed to ingest remote file: {str(e)}"}
