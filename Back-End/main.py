import datetime
from fastapi import FastAPI , Depends, File , HTTPException, UploadFile , status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import engine , get_db
import models , schemas , utils
import os
from uuid import uuid4

# running the db migrations
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# OAuth2 for token base auth
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# upload folder setup
UPLOAD_FOLDER = "../uploads/"
os.makedirs(UPLOAD_FOLDER,exist_ok=True)

# register route
@app.post("/register" , response_model=schemas.User , status_code=status.HTTP_201_CREATED)
def register_user(user: schemas.UserCreate , db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.user_name == user.user_name).first()
    if db_user :
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail="User already exist")

    hashed_pass = utils.hash_password(user.password)
    new_user = models.User(user_name = user.user_name , email = user.email , hashed_password = hashed_pass)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {user : new_user}


# login route
@app.post("/login", response_model=schemas.Token)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.user_name == form_data.username).first()
    if not user or not utils.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password, please try again!",
            headers={"WWW-Authenticate": "Bearer"}
        )

    access_token = utils.create_access_token(data={"sub": user.user_name})
    return {"access_token": access_token, "token_type": "bearer"}





# upload resume
@app.post("/upload_resume/")
async def upload_resume(user_name:str , file: UploadFile = File(...) , response_model=schemas.Resume, db: Session = Depends(get_db)):
    try:
        if not file.filename.lower().endswith(('.pdf' , '.doc' , '.docx')):
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail="FILE TYPES CAN BE PDF OR DOC")

        u_name = ".".join(file.filename.split('.')[:-1]) + "_" + str(uuid4()) + "." + file.filename.split(".")[-1]
        file_location = os.path.join(UPLOAD_FOLDER , u_name )
        with open(file_location,'wb') as f :
            f.write(await file.read())

        resume = models.Resume(
            user_name = user_name,
            file_path = file_location,
            uploaded_at=datetime.utcnow(),
            format=file.filename.split(".")[-1],
            original_name=file.filename
        )
        db.add(resume)
        db.commit()
        db.refresh(resume)

        return {"message": "Upload successful", "resume": resume.file_path}
    except:
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail="UPLOAD FAILED")


# analyze resume




# show recommandation




# update alignment





# return all sessions




# delete a session



# update user information

# delete user
