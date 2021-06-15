import asyncio

async def async_func():
  await asyncio.sleep(1) # <- replace this with your async code

loop = asyncio.get_event_loop()
coroutine = async_func()
loop.run_until_complete(coroutine)