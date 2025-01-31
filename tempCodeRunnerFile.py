async def main():
    await download(file_path, "laptops.csv")
    file_name = "laptops.csv"
    df = pd.read_csv(file_name, header=None)
    print(df.head(10))

import asyncio
asyncio.run(main())
