from groundx import AsyncGroundX
from typing import Dict, Any

async def get_document_in_Groundx(
    groundx_api_key: str,
    document_id: str
) -> Dict[str, Any]:
    """
    Look up an existing document by documentId.
    
    See: https://docs.eyelevel.ai/reference/api-reference/documents/get

    Args:
        groundx_api_key (str): The API key for GroundX authentication.
        document_id (str): The documentId of the document for which GroundX information will be provided.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        return await client.documents.get(document_id=document_id)
    except Exception as e:
        return {"error": f"Failed to get document: {str(e)}"}
