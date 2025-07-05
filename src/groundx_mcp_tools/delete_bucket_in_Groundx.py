from groundx import AsyncGroundX

async def delete_bucket_in_Groundx(groundx_api_key: str, bucket_id: int) -> dict:
    """
    Delete a bucket.
    
    See: https://docs.eyelevel.ai/reference/api-reference/buckets/delete

    Args:
        groundx_api_key (str): The API key for GroundX.
        bucket_id (int): The bucketId of the bucket being deleted.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        response = await client.buckets.delete(bucket_id=bucket_id)
        return response
    except Exception as e:
        return {"error": f"Failed to delete bucket: {str(e)}"}