from groundx import AsyncGroundX

async def delete_group_in_Groundx(groundx_api_key: str, group_id: int) -> dict:
    """
    Delete a group.
    
    See: https://docs.eyelevel.ai/reference/api-reference/groups/delete

    Args:
        groundx_api_key (str): The API key for GroundX.
        group_id (int): The groupId of the group to be deleted.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        response = await client.groups.delete(group_id=group_id)
        return response
    except Exception as e:
        return {"error": f"Failed to delete group: {str(e)}"}