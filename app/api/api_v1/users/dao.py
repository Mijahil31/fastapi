from sqlalchemy.orm import Session, joinedload
from .schema import UserBy, UserCreate
from .models import User
from app.db.database import engine
from datetime import datetime

def get_by_id(id: int):
    with Session(bind=engine) as db:
        return db.query(User).filter(User.id == id).first()
    

def get_all():
    with Session(bind=engine) as db:
        return db.query(User).all()
    

def get_by(user: UserBy):
    try:
        with Session(bind=engine) as db:
            usuario =  db.query(User).filter(User.email == user.email, User.password == user.password).one()
            #wallet = db.query(Wallet).options(joinedload(Wallet.user)).where(Wallet.id_user == usuario.id).one()
            return usuario
    except Exception as err:
        print(err)

def post_create_user(user: UserCreate):
    
    try:
        with Session(bind=engine) as db:
            
            usuario = User(
                name = user.name, 
                email= user.email,
                document = user.document,
                password = user.password,
                is_active = True,
                fecha_creacion = datetime.now()
            )
            db.add(usuario)
            db.commit()
            
            '''
            wallet = Wallet(
                id_user = usuario.id, 
                value = 0.0,
                fecha_creacion = datetime.now(),
                fecha_moficacion = datetime.now()
            )
            
            db.add(wallet)
            db.commit()
            
            return db.query(Wallet).options(joinedload(Wallet.user)).where(Wallet.id_user == usuario.id).one()
            '''
            return db.query(User).filter(User.email == user.email, User.password == user.password).one()
            
    
    except Exception as err:
        print(err)