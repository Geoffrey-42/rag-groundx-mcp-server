from groundx import AsyncGroundX
from typing import Optional, Dict, Any

async def list_documents_in_Groundx(
    groundx_api_key: str,
    n: Optional[int] = None,
    filter: Optional[str] = None,
    sort: Optional[str] = None,
    sort_order: Optional[str] = None,
    status: Optional[str] = None,
    next_token: Optional[str] = None
) -> Dict[str, Any]:
    """
    Lookup all documents across all resources which are currently on GroundX.
    
    See: https://docs.eyelevel.ai/reference/api-reference/documents/list

    Args:
        groundx_api_key (str): The API key for GroundX authentication.
        n (int, optional): The maximum number of returned documents. Accepts 1-100 with a default of 20.
        filter (str, optional): Only documents with names that contain the filter string will be returned in the results.
        sort (str, optional): The document attribute that will be used to sort the results. Allowed values: 'name', 'created'.
        sort_order (str, optional): The order in which to sort the results. A value for sort must also be set. Allowed values: 'asc', 'desc'.
        status (str, optional): A status filter on the get documents query. If this value is set, then only documents with this status will be returned in the results.
        next_token (str, optional): A token for pagination. If the number of documents for a given query is larger than n, the response will include a "nextToken" value. That token can be included in this field to retrieve the next batch of n documents.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        params = {}
        if n is not None:
            params['n'] = n
        if filter is not None:
            params['filter'] = filter
        if sort is not None:
            params['sort'] = sort
        if sort_order is not None:
            params['sortOrder'] = sort_order
        if status is not None:
            params['status'] = status
        if next_token is not None:
            params['nextToken'] = next_token
        return await client.documents.list(**params)
    except Exception as e:
        return {"error": f"Failed to list documents: {str(e)}"}
