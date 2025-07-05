from groundx import AsyncGroundX

async def remove_bucket_from_group_in_Groundx(groundx_api_key: str, group_id: int, bucket_id: int) -> dict:
    """
    Remove a bucket from a group. Buckets and groups can be associated many to many, this removes one bucket to group association without disturbing others.
    
    See: https://docs.eyelevel.ai/reference/api-reference/groups/remove-bucket

    Args:
        groundx_api_key (str): The API key for GroundX.
        group_id (int): The groupId of the group which the bucket will be removed from.
        bucket_id (int): The bucketId of the bucket which will be removed from the group.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        response = await client.groups.remove_bucket(group_id=group_id, bucket_id=bucket_id)
        return response
    except Exception as e:
        return {"error": f"Failed to remove bucket from group: {str(e)}"}
