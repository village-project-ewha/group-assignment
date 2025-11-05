import pyrebase
import json

class DBhabdler:
    def __init__(self):     #인증
        with open('./authentication/firebase_auth.json') as f:
            config = json.load(f)
        
        firebase = pyrebase.initialize_app(config)  #config를 기반으로 인증을 하게 됨
        self.db = firebase.database()   #db 생성 구문

    
    def insert_item(self, name, data, img_path):
        item_info ={    #jason 형식의 value
            "seller": data['seller'],
            "addr": data['addr'],
            "email": data['email'],
            "category": data['category'],
            "card": data['card'],
            "status": data['status'],
            "phone": data['phone'],
            "img_path": img_path
        }
 
        self.db.child("item").child(name).set(item_info)
        print(data,img_path)
        return True