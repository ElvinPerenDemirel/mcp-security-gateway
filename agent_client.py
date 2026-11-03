import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_agent():
    # Server parameters to run server.py as a background subprocess
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )
    
    # Initialize secure stdio connection with the server
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection and handshake with the server
            await session.initialize()
            
            # 1. List available tools from the server
            tools = await session.list_tools()
            print("--- Tools Received from Server ---")
            print(tools)
            
            # 2. Test the calculate_sum tool
            sum_result = await session.call_tool("calculate_sum", {"a": 150, "b": 50})
            print("\n--- calculate_sum Result ---")
            print(sum_result.content[0].text)

            # 3. Test the read_secret_file tool (Attack simulation)
            file_result = await session.call_tool("read_secret_file", {"file_path": "passwords.txt"})
            print("\n--- read_secret_file Result ---")
            print(file_result.content[0].text)

if __name__ == "__main__":
    asyncio.run(run_agent())