from groundx import AsyncGroundX

async def create_bucket_in_Groundx(groundx_api_key: str, name: str) -> dict:
    """
    Create a new bucket.
    
    See: https://docs.eyelevel.ai/reference/api-reference/buckets/create

    Args:
        groundx_api_key (str): The API key for GroundX.
        name (str): The name of the new bucket.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        response = await client.buckets.create(name=name)
        return response
    except Exception as e:
        return {"error": f"Failed to create bucket: {str(e)}"}