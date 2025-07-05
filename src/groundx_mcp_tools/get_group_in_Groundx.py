from groundx import AsyncGroundX

async def get_group_in_Groundx(groundx_api_key: str, group_id: int) -> dict:
    """
    Look up a specific group by its groupId.
    
    See: https://docs.eyelevel.ai/reference/api-reference/groups/get

    Args:
        groundx_api_key (str): The API key for GroundX.
        group_id (int): The groupId of the group to look up.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        response = await client.groups.get(group_id=group_id)
        return response
    except Exception as e:
        return {"error": f"Failed to get group: {str(e)}"}
