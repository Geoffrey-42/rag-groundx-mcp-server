from groundx import AsyncGroundX
from typing import Optional

async def get_processes_in_Groundx(
    groundx_api_key: str,
    n: Optional[int] = None,
    status: Optional[str] = None
) -> dict:
    """
    Get a list of ingest process requests, sorted from most recent to least.
    
    See: https://docs.eyelevel.ai/reference/api-reference/documents/get-processes

    Args:
        groundx_api_key (str): The API key for GroundX.
        n (int, optional): The maximum number of returned processes. Accepts 1-100 with a default of 20.
        status (str, optional): A status filter on the processing status. If this value is set, then only processes with this status will be returned in the results.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        params = {}
        if n is not None:
            params['n'] = n
        if status is not None:
            params['status'] = status
        response = await client.documents.get_processes(**params)
        return response
    except Exception as e:
        return {"error": f"Failed to get processes: {str(e)}"}