from fastapi import FastAPI, Form, File, UploadFile


app = FastAPI()

@app.post("/form")
def form_handler(username: str = Form(...), password: str = Form(default=..., min_length=8)):
    print(username, password)
    return {"username": username}

#@app.post("/fileform")
#def file_as_bytes_form_handler(file: bytes = File(...)):
#    with open ("file", "wb") as f:
#        print(file)
#        f.write(file)
#        f.close()
#    
#    return {"message": "file uploaded"}

@app.post("/fileform")
async def file_as_file_form_handler(file: UploadFile = File(...), description: str = Form(...)):
    contents = await file.read()
    print(len(contents))
    
    return { "filename": file.filename }