from groundx import AsyncGroundX

async def update_bucket_in_Groundx(groundx_api_key: str, bucket_id: int, new_name: str) -> dict:
    """
    Rename a bucket.
    
    See: https://docs.eyelevel.ai/reference/api-reference/buckets/update

    Args:
        groundx_api_key (str): The API key for GroundX.
        bucket_id (int): The bucketId of the bucket being updated.
        new_name (str): The new name of the bucket being renamed.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        response = await client.buckets.update(bucket_id=bucket_id, new_name=new_name)
        return response
    except Exception as e:
        return {"error": f"Failed to update bucket: {str(e)}"}
