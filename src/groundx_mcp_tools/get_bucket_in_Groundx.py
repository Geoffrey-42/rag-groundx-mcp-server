from groundx import AsyncGroundX

async def get_bucket_in_Groundx(groundx_api_key: str, bucket_id: int) -> dict:
    """
    Look up a specific bucket by its bucketId.
    
    See: https://docs.eyelevel.ai/reference/api-reference/buckets/get

    Args:
        groundx_api_key (str): The API key for GroundX.
        bucket_id (int): The bucketId of the bucket to look up.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        response = await client.buckets.get(bucket_id=bucket_id)
        return response
    except Exception as e:
        return {"error": f"Failed to get bucket: {str(e)}"}
