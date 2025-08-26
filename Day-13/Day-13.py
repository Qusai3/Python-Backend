import asyncio
import time

async def download_file(name, seconds):
    print(f"Start downloading {name} (will take {seconds}s)")
    await asyncio.sleep(seconds) 
    print(f"Finished {name}")
    return name

async def main():
    files = [
        ("file1.zip", 3),
        ("file2.mp4", 5),
        ("file3.pdf", 2),
        ("file4.jpg", 4),
    ]

    tasks = [asyncio.create_task(download_file(n, s)) for n, s in files]
    results = await asyncio.gather(*tasks)
    print("All done:", results)

if __name__ == "__main__": 
    start = time.perf_counter()
    asyncio.run(main())
    total = time.perf_counter() - start
    print(f"Took {total:.2f} seconds total")