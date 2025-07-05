from groundx import AsyncGroundX

async def update_group_in_Groundx(groundx_api_key: str, group_id: int, new_name: str) -> dict:
    """
    Rename a group.
    
    See: https://docs.eyelevel.ai/reference/api-reference/groups/update

    Args:
        groundx_api_key (str): The API key for GroundX.
        group_id (int): The groupId of the group to update.
        new_name (str): The new name of the group being renamed.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        response = await client.groups.update(group_id=group_id, new_name=new_name)
        return response
    except Exception as e:
        return {"error": f"Failed to update group: {str(e)}"}
