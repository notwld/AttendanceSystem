# FastAPI
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
The key features are:

- Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.
- Fast to code: Increase the speed to develop features by about 200% to 300%. *
- Fewer bugs: Reduce about 40% of human (developer) induced errors. *
- Intuitive: Great editor support. Completion everywhere. Less time debugging.
- Easy: Designed to be easy to use and learn. Less time reading docs.
- Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
- Robust: Get production-ready code. With automatic interactive documentation.
- Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

# Dependencies
Install dependencies using pip.
```bash
pip install -r requirements.txt
```
# Getting Started
Create an .env file and define connection string of your database.
```bash
DATABASE_URL=(your connection string)
```

Run your application using,
```bash
uvicorn main:app --reload
```
`Note: --reload will allow your app to restart automatically on changes to the code`

Now go to `http://127.0.0.1:8000/docs` to see the automatic interactive API documentation (provided by Swagger UI).

![ss](https://github.com/notwld/fast-testing/blob/master/md/ss.png?raw=true)

`Work in progress`

# Important Links
Documentation: https://fastapi.tiangolo.com
