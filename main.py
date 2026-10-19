from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

def main():
    print("Hello from sethera-world!")

if __name__ == "__main__":
    main()
