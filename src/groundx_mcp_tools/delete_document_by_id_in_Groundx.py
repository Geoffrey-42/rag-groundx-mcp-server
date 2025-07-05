from groundx import AsyncGroundX
from typing import Dict, Any

async def delete_document_by_id_in_Groundx(
    groundx_api_key: str, 
    document_id: str
) -> Dict[str, Any]:
    """
    Delete a single document hosted on GroundX.
    
    See: https://docs.eyelevel.ai/reference/api-reference/documents/delete-by-id

    Args:
        groundx_api_key (str): The API key for GroundX authentication.
        document_id (str): A documentId which correspond to a document ingested by GroundX.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        response = await client.documents.delete_by_id(
            document_id=document_id
        )
        return response
    except Exception as e:
        return {"error": f"Failed to delete document: {str(e)}"}
