from groundx import AsyncGroundX
from typing import Dict, Any, List

async def delete_documents_in_Groundx(
    groundx_api_key: str,
    document_ids: List[str]
) -> Dict[str, Any]:
    """
    Delete multiple documents hosted on GroundX.
    
    See: https://docs.eyelevel.ai/reference/api-reference/documents/delete

    Args:
        groundx_api_key (str): The API key for GroundX authentication.
        document_ids (List[str]): A list of documentIds which correspond to documents ingested by GroundX.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        response = await client.documents.delete(
            document_ids=document_ids
        )
        return response
    except Exception as e:
        return {"error": f"Failed to delete documents: {str(e)}"}