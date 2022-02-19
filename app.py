from flask import Flask , request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource # new
from flask_marshmallow import Marshmallow # new
from dateutil.parser import parse


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app) 





class Transactions(db.Model):
    ID  = db.Column("ID",db.Integer , primary_key = True)
    ACC_NUM = db.Column("Account No",db.Integer)
    DATE_ = db.Column("Date",db.String(50))
    TRANS_DETAILS = db.Column("Transaction Details",db.String(255))
    VALUE_DATE = db.Column("Value Date",db.String(50))
    WITHDRAWAL_AMT = db.Column("Withdrawal AMT",db.String(50))
    DEPOSIT_AMT = db.Column("Deposit AMT",db.String(50))
    BALANCE_AMT = db.Column( "Balance AMT",db.String(50))

    def __repr__(self):
        return '<Transaction %s>' % self.ACC_NUM


class PostSchema(ma.Schema):
    class Meta:
        fields = (
            "ID","ACC_NUM",
        "DATE_",
        "TRANS_DETAILS",
        "VALUE_DATE",
        "WITHDRAWAL_AMT",
        "DEPOSIT_AMT",
        "BALANCE_AMT"
        )
        model = Transactions

post_schema = PostSchema()
posts_schema = PostSchema(many=True)
    
# 29-06-17
class TransactionsByDate(Resource):
    def get(self,date):
        month_num = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
        date = date.split("-")
        # print(date)
        if len(date) == 3:
            date[1] = month_num[int(date[1])]
            
            date = " ".join(date)
            
            accounts = Transactions.query.filter_by(DATE_= date).all()
            return posts_schema.dump(accounts)
        else:
            return None
        
        # return {"date": date}
        
    
        
        
        

class TransactionsList(Resource):
    def get(self):
        transactions = Transactions.query.all()
        print(transactions)
        trans = posts_schema.dump(transactions)
        for i in range(len(trans)):
             
            trans[i]["Account No"] = trans[i].pop("ACC_NUM")
            trans[i]["Date"]= trans[i].pop("DATE_")
            trans[i]["Transaction Details"]= trans[i].pop("TRANS_DETAILS")
            trans[i]["Value Date"]= trans[i].pop( "VALUE_DATE")
            trans[i]["Withdrawal AMT"]= trans[i].pop( "WITHDRAWAL_AMT")
            trans[i]["Deposit AMT"]= trans[i].pop( "DEPOSIT_AMT")
            trans[i]["Balance AMT"]= trans[i].pop("BALANCE_AMT")
        return trans
            


class BalanceOnDate(Resource):
    def get(self,date):
        month_num = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
        date = date.split("-")
        # print(date)
        if len(date) == 3:
            date[1] = month_num[int(date[1])]
            
            date = " ".join(date)
            transactions = Transactions.query.filter_by(DATE_= date).all()
            trans = posts_schema.dump(transactions)[-1].get("BALANCE_AMT")
            for i in range(len(trans)):
                 
                trans[i]["Account No"] = trans[i].pop("ACC_NUM")
                trans[i]["Date"]= trans[i].pop("DATE_")
                trans[i]["Transaction Details"]= trans[i].pop("TRANS_DETAILS")
                trans[i]["Value Date"]= trans[i].pop( "VALUE_DATE")
                trans[i]["Withdrawal AMT"]= trans[i].pop( "WITHDRAWAL_AMT")
                trans[i]["Deposit AMT"]= trans[i].pop( "DEPOSIT_AMT")
                trans[i]["Balance AMT"]= trans[i].pop("BALANCE_AMT")
            return trans
class Details(Resource):
    def get(self,id):
        transactions = Transactions.query.filter_by(ID = id).all()
        
        trans = posts_schema.dump(transactions)
        # print("trans" , trans)
        if len(trans) > 0:
            for i in range(len(trans)):
                print(trans[i])
                trans[i]["Account No"] = trans[i].pop("ACC_NUM") 
                trans[i]["Date"]= trans[i].pop("DATE_")
                trans[i]["Transaction Details"]= trans[i].pop("TRANS_DETAILS")
                trans[i]["Value Date"]= trans[i].pop( "VALUE_DATE")
                trans[i]["Withdrawal AMT"]= trans[i].pop( "WITHDRAWAL_AMT")
                trans[i]["Deposit AMT"]= trans[i].pop( "DEPOSIT_AMT")
                trans[i]["Balance AMT"]= trans[i].pop("BALANCE_AMT")
            return trans
        return trans
            

class PostTransaction(Resource):
    def post(self):
        post_data =request.json
        req_fields = [
        "Account No",
        "Date",
        "Transaction Details",
        "Value Date",
        "Withdrawal AMT",
        "Deposit AMT",
        "Balance AMT"]
        
        for field in req_fields:
            if field not in post_data:
                return "Data Incomplete"
            
        if type(post_data['Account No']) != int :
            return "Error"
        
        try :
            parse(post_data["Date"])
            parse(post_data["Value Date"])
            parse(post_data["Value Date"])
        except:
            return "Invalid Date format"
        
        for label in ["Withdrawal AMT",
        "Deposit AMT",
        "Balance AMT"]:
            money = post_data[label]
            print(money)
            if money.strip(" ") != "":
                money = money.replace(",","")
                try:
                    print(float(money))
                except:
                    return "Invalid "+ label
            else:
                if money.strip(" "):
                    return "Invalid " + label
        
        accounts = Transactions.query.all()
        new_acc = Transactions(
            ID = len(accounts)+1,
            ACC_NUM  = post_data["Account No"],
    DATE_ = post_data["Date"],
    TRANS_DETAILS = post_data["Transaction Details"],
    VALUE_DATE = post_data["Value Date"],
    WITHDRAWAL_AMT = post_data["Withdrawal AMT"],
    DEPOSIT_AMT = post_data["Deposit AMT"],
    BALANCE_AMT = post_data["Balance AMT"])
        
        db.session.add(new_acc)
        db.session.commit()
        return post_schema.dump(new_acc)
        
            
            
        
                
        
        
            
        

api.add_resource(TransactionsList, '/transactions')
api.add_resource(TransactionsByDate, '/transactions/<string:date>')
api.add_resource(BalanceOnDate , '/balance/<string:date>')
api.add_resource(Details , '/details/<int:id>' )
api.add_resource(PostTransaction ,'/add' )




if __name__ == '__main__':
    app.run(debug=True)