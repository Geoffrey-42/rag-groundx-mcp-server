from groundx import AsyncGroundX
from typing import Dict, Any, Optional

async def get_processing_status_by_id_in_Groundx(groundx_api_key: str, process_id: str) -> Dict[str, Any]:
    """
    Gets the processing status of a specific ingestion process by ID using the EyeLevel API.

    See: https://docs.eyelevel.ai/reference/api-reference/documents/get-processing-status-by-id

    Args:
        groundx_api_key (str): The API key for GroundX authentication.
        process_id (str): The unique identifier of the ingestion process to check.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        return await client.documents.get_processing_status_by_id(
            process_id=process_id
        )
    except Exception as e:
        return {"error": f"Failed to get processing status: {str(e)}"}


