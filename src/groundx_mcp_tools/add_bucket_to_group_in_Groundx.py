from groundx import AsyncGroundX

async def add_bucket_to_group_in_Groundx(groundx_api_key: str, group_id: int, bucket_id: int) -> dict:
    """
    Add an existing bucket to an existing group. Buckets and groups can be associated many to many.
    
    See: https://docs.eyelevel.ai/reference/api-reference/groups/add-bucket

    Args:
        groundx_api_key (str): The API key for GroundX.
        group_id (int): The groupId of the group which the bucket will be added to.
        bucket_id (int): The bucketId of the bucket being added to the group.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        response = await client.groups.add_bucket(group_id=group_id, bucket_id=bucket_id)
        return response
    except Exception as e:
        return {"error": f"Failed to add bucket to group: {str(e)}"}
