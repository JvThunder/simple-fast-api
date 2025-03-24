1. Make a python venv and activate it:
```
python -m venv venv

# For Windows:
venv\Scripts\activate

# For Unix or MacOS:
source venv/bin/activate
```

2. Run the following command to install the dependencies:
```
python -m pip install fastapi uvicorn[standard] pydantic
```

3. Make a new file called main.py and add the following code:
```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"message": "Hello World"}
```

4. Run the following command to start the server:
```
venv\Scripts\activate
uvicorn main:app --reload
```

5. Open the following URL to see the API documentation:
```
http://127.0.0.1:8000/docs
```

