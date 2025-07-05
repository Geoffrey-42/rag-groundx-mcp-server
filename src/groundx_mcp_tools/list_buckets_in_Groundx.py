from groundx import AsyncGroundX
from typing import Optional

async def list_buckets_in_Groundx(
    groundx_api_key: str,
    n: Optional[int] = None,
    next_token: Optional[str] = None
) -> dict:
    """
    List all buckets within your GroundX account.
    
    See: https://docs.eyelevel.ai/reference/api-reference/buckets/list

    Args:
        groundx_api_key (str): The API key for GroundX.
        n (int, optional): The maximum number of returned buckets. Accepts 1-100 with a default of 20.
        next_token (str, optional): A token for pagination. If the number of buckets for a given query is larger than n, the response will include a "nextToken" value. That token can be included in this field to retrieve the next batch of n buckets.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        params = {}
        if n is not None:
            params["n"] = n
        if next_token is not None:
            params["next_token"] = next_token
        response = await client.buckets.list(**params)
        return response
    except Exception as e:
        return {"error": f"Failed to list buckets: {str(e)}"}
