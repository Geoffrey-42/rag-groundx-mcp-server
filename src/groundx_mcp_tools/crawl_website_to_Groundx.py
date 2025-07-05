from groundx import AsyncGroundX, WebsiteSource
from typing import Optional, Dict, Any

async def crawl_website_to_Groundx(
    groundx_api_key: str,
    bucket_id: int,
    source_url: str,
    cap: Optional[int] = None,
    depth: Optional[int] = None,
    search_data: Optional[Dict[str, Any]] = None
) -> dict:
    """
    Upload the content of a publicly accessible website for ingestion into a GroundX bucket.
    This endpoint crawls a website by following links within the specified URL, recursively,
    up to the specified depth or number of pages.

    Note:
        - This endpoint is not supported for on-prem deployments.
        - The source_url must include the protocol (http:// or https://).
    
    Args:
        groundx_api_key (str): The API key for GroundX authentication.
        bucket_id (int): The bucketId of the bucket which this website will be ingested into.
        source_url (str): The URL from which the crawl is initiated.
        cap (int, optional): The maximum number of pages to crawl. If None, no limit is applied.
        depth (int, optional): The maximum depth of linked pages to follow from the sourceUrl. If None, no limit is applied.
        search_data (dict, optional): Custom metadata which can be used to influence GroundX's search functionality.
                                     This data can be used to further hone GroundX search.
    """
    client = AsyncGroundX(api_key=groundx_api_key)
    try:
        website_params = {
            'bucket_id': bucket_id,
            'source_url': source_url
        }
        
        if cap is not None:
            website_params['cap'] = cap
        if depth is not None:
            website_params['depth'] = depth
        if search_data is not None:
            website_params['search_data'] = search_data
        
        response = await client.documents.crawl_website(
            websites=[
                WebsiteSource(**website_params)
            ]
        )
        return response
    except Exception as e:
        return {"error": f"Failed to crawl website: {str(e)}"}