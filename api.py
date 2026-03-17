import httpx


class RejectionAPI:
    URL = "https://naas.isalman.dev/no"

    @classmethod
    async def get_rejection(cls) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.get(cls.URL)
            response.raise_for_status()
            data = response.json()
            return data.get("reason", "No reason provided.")
