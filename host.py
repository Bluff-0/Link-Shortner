from flask import Flask
import pymongo

app = Flask(__name__)

@app.route("/")
def hello():
    return "404 Page Not Found"


@app.route("/<sht>", methods=["GET"])
def retr(sht):
    client = pymongo.MongoClient("mongodb+srv://test:test@cluster0-fvejx.gcp.mongodb.net/test?retryWrites=true&w=majority")
    collection = client.get_database('Shortner')
    db= collection.URL
    for i in db.find({"Short":"http://127.0.0.1:60000/"+str(sht)}):
    	return "<script type=\"text/javascript\">window.open(\'"+i['URL']+"\',\'_self\');</script>"

if __name__ == '__main__':
    app.run(port= 60000, debug=True)