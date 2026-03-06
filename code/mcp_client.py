import asyncio
from fastmcp import Client

client = Client("http://localhost:8003/sse")

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


async def _call_tool(query):
    async with client:
        result = await client.call_tool(
            "search_documents",
            {"query": query}
        )
        return result


def search_docs(query):

    result = loop.run_until_complete(_call_tool(query))

    context = ""

    for doc in result.content[:2]:   # only top 2 docs
        context += doc.text[:500] + "\n"

    return context