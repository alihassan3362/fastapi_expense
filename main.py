from fastapi import FastAPI, Depends, HTTPException, status
from apis import models, schemas
from apis.database import Sessionlocal, engine
from sqlalchemy.orm import Session

app = FastAPI()


models.Base.metadata.create_all(engine)

def get_db():
    db=Sessionlocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/categories/", tags=["Categories"])
def List(db:Session  = Depends(get_db)):
    cate=db.query(models.category).all()
    return cate



@app.post("/categories/", tags=["Categories"])
def create_category(request:schemas.Category, db:Session = Depends(get_db)):
    new_cate=models.category(name=request.Name)
    db.add(new_cate)
    db.commit()
    db.refresh(new_cate)
    return new_cate


@app.put("/categories/", tags=["Categories"])
def update_category(id:int,request:schemas.Category, db:Session = Depends(get_db)):
    cate=db.query(models.category).filter(models.category.id==id)
    if not cate.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"category of id {id} is not found")
    cate.update(request.dict())
    db.commit()
    return 'updated'

@app.delete("/categories/", tags=["Categories"])
def destroy(id:int,db:Session = Depends(get_db)):
    cate=db.query(models.category).filter(models.category.id==id)
    if not cate.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"category of id {id} is not found")
    cate.delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.get("/category/", tags=["Categories"])
def category_by_id(id:int,db:Session = Depends(get_db)):
    cate=db.query(models.category).filter(models.category.id==id).first()
    if not cate:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f"Category with id {id} is not avaliable")
    return cate 


######################################################




@app.get("/user/", tags=["User"])
def list(db:Session  = Depends(get_db)):
    users=db.query(models.user).all()
    return users

@app.post("/user/", tags=["User"])
def create_user(request:schemas.user, db:Session = Depends(get_db)):
    new_user=models.user(name=request.Name,email=request.email,create_at=request.create_at)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.put("/user/", tags=["User"])
def update_user(id:int,request:schemas.user, db:Session = Depends(get_db)):
    users=db.query(models.user).filter(models.user.id==id)
    if not users.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"id of user {id} is not found")
    users.update(request.dict())
    db.commit()
    return 'updated'

@app.delete("/user/", tags=["User"])
def destroy(id:int,db:Session = Depends(get_db)):
    users=db.query(models.user).filter(models.user.id==id)
    if not users.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"id of user {id} is not found")
    users.delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.get("/user/{id}/", tags=["User"])
def user_by_id(id:int,db:Session = Depends(get_db)):
    users=db.query(models.user).filter(models.user.id==id).first()
    if not users:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f"user with this id {id} is not avaliable")
    return users 

##########################################

@app.get("/ledger/", tags=["ledger"])
def list(db:Session  = Depends(get_db)):
    ledger=db.query(models.ledger).all()
    return ledger

@app.post("/ledger/", tags=["ledger"])
def create_ledger(request:schemas.ledger, db:Session = Depends(get_db)):
    new_ledger=models.ledger(user_id=request.user_id,amount=request.amount,account_id=request.account_id,category_id=request.category_id,create_at=request.create_at,transaction=request.transaction,transfer_to=request.transfer_to)
    db.add(new_ledger)
    db.commit()
    db.refresh(new_ledger)
    return new_ledger


@app.put("/ledger/", tags=["ledger"])
def update_ledger(id:int,request:schemas.ledger, db:Session = Depends(get_db)):
    ledger=db.query(models.ledger).filter(models.ledger.id==id)
    if not ledger.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"id of user {id} is not found")
    ledger.update(request.dict())
    db.commit()
    return 'updated'

@app.delete("/ledger/", tags=["ledger"])
def destroy(id:int,db:Session = Depends(get_db)):
    ledger=db.query(models.ledger).filter(models.ledger.id==id)
    if not ledger.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"id of user {id} is not found")
    ledger.delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.get("/ledger/{id}/", tags=["ledger"])
def ledger_by_user(id:int,db:Session = Depends(get_db)):
    ledger=db.query(models.ledger).filter(models.ledger.id==id).first()
    if not ledger:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f"user with this id {id} is not avaliable")
    return ledger

########################


@app.get("/ledger/", tags=["Ledger"])
def list(db:Session  = Depends(get_db)):
    ledger=db.query(models.ledger).all()
    return ledger

@app.post("/ledger/", tags=["Ledger"])
def create_ledger(request:schemas.ledger, db:Session = Depends(get_db)):
    new_ledger=models.ledger(name=request.Name,email=request.email,user_id=request.user_id,create_at=request.create_at,intial_balance=request.Intial_balance,ledger_type=request.ledger_type)
    db.add(new_ledger)
    db.commit()
    db.refresh(new_ledger)
    return new_ledger

##
@app.put("/ledger/", tags=["Ledger"])
def update_ledger(id:int,request:schemas.ledger, db:Session = Depends(get_db)):
    ledger=db.query(models.ledger).filter(models.ledger.id==id)
    if not ledger.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"id of user {id} is not found")
    ledger.update(request.dict())
    db.commit()
    return 'updated'

@app.delete("/ledger/", tags=["Ledger"])
def destroy(id:int,db:Session = Depends(get_db)):
    ledger=db.query(models.ledger).filter(models.ledger.id==id)
    if not ledger.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"id of user {id} is not found")
    ledger.delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.get("/ledger/{id}/", tags=["Ledger"])
def ledger_by_user(id:int,db:Session = Depends(get_db)):
    ledger=db.query(models.ledger).filter(models.ledger.id==id).first()
    if not ledger:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f"user with this id {id} is not avaliable")
    return ledger
