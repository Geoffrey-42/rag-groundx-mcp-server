from groundx import AsyncGroundX
from typing import Optional

async def create_group_in_Groundx(groundx_api_key: str, name: str, bucket_name: Optional[str] = None) -> dict:
    """
    Create a new group, a group being a collection of buckets which can be searched.
    
    See: https://docs.eyelevel.ai/reference/api-reference/groups/create

    Args:
        groundx_api_key (str): The API key for GroundX.
        name (str): The name of the group being created.
        bucket_name (str, optional): Specify bucketName to automatically create a bucket, by the name specified, and add it to the created group.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        params = {"name": name}
        if bucket_name is not None:
            params["bucket_name"] = bucket_name
        response = await client.groups.create(**params)
        return response
    except Exception as e:
        return {"error": f"Failed to create group: {str(e)}"}