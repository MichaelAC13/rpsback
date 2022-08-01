from flask import Flask,request,jsonify, send_file
from flask_cors import CORS, cross_origin
from generateRPS import linerotine
from mongo.app import workbase

app = Flask(__name__) 
cors = CORS(app, resources={r"/": {"origins": "*.*"}})
version = '1'
# ROTAS

@app.route("/",  methods=['POST']) 
@cross_origin()
def home():
    return jsonify({
        "api": "API FLASK",
        "version": "1"
    })

@app.route(f"/api/v{version}/download", methods=['POST']) 
@cross_origin()
def downolad():
    req = request.get_json()
    try:
        isert = linerotine().insertdata(req)
        return send_file(isert[0], mimetype='application/zip'),isert[1]
    except Exception as e:
        return jsonify({"error": str(e)}),500
        
# User - Craate User
@app.route(f"/api/v{version}/users", methods=['POST']) 
@cross_origin()
def creatuser(): 
    try:
        obj = request.get_json()
        a = workbase(obj).creatuser()
        return jsonify(a[0]),a[1]
    except:
        return {"message": "internal server erro"}, 500

# Authentication
@app.route(f"/api/v{version}/authenticate", methods=['POST']) 
@cross_origin()
def authenticate(): 
    try:
        obj = request.get_json()
        a = workbase(obj).validateuser()
        return jsonify(a[0]), a[1]
    except:
        return {"message": "internal server erro"}, 500

# User - Fetching data by id
@app.route(f"/api/v{version}/users", methods=['GET']) 
@cross_origin()
def idusers():  
    try:
        obj = request.get_json()
        a = workbase(obj).idselectuser()
        return jsonify(a[0]), a[1]
    except:
        return {"message": "internal server erro"}, 500

# User - Changing and querying
@app.route(f"/api/v{version}/users", methods=['PUT']) 
@cross_origin()
def putuser(): 
    try:
        obj = request.get_json()
        header = request.headers['token']
        obj["currenttoken"] = header
        token = workbase(obj).validatetoken()
        if token['token'] == "valid":
            a = workbase(obj).putuser()
            return jsonify(a[0]),a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500
        
# Service - Create and quering
@app.route(f"/api/v{version}/services", methods=['POST'])
@cross_origin()
def createservice():
    try:
        obj = request.get_json()
        header = request.headers['token']
        obj["currenttoken"] = header
        token = workbase(obj).validatetoken()
        if token['token'] == "valid":
            a = workbase(obj).createservice()
            return jsonify(a[0]),a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500

# Service - Quering
@app.route(f"/api/v{version}/services", methods=['GET']) 
@cross_origin()
def selectservices():
    try:
        obj = {}
        header = request.headers['token']
        obj["currenttoken"] = header
        token = workbase(obj).validatetoken()
        if token['token'] == "valid":
            a = workbase(obj).selectservices()
            return jsonify(a[0]),a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500


# Service - Changing and querying
@app.route(f"/api/v{version}/services", methods=['PUT'])
@cross_origin()
def putservice():
    try:
        obj = request.get_json()
        header = request.headers['token']
        obj["currenttoken"] = header
        token = workbase(obj).validatetoken()
        if token['token'] == "valid":
            a = workbase(obj).putservice()
            return jsonify(a[0]),a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500

# RPS - Create and quering
@app.route(f"/api/v{version}/rps", methods=['POST'])
@cross_origin()
def createrps():
    try:
        obj = request.get_json()
        header = request.headers['token']
        obj["currenttoken"] = header
        token = workbase(obj).validatetoken()
        if token['token'] == "valid":
            a = workbase(obj).createrps()
            return jsonify(a[0]),a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500

# RPS - Quering
@app.route(f"/api/v{version}/rps", methods=['GET']) 
@cross_origin()
def selectrps():
    try:
        obj = {}
        header = request.headers['token']
        obj["currenttoken"] = header
        token = workbase(obj).validatetoken()
        if token['token'] == "valid":
            a = workbase(obj).selectrps()
            return jsonify(a[0]),a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500


# RPS - Changing and querying
@app.route(f"/api/v{version}/rps", methods=['PUT'])
@cross_origin()
def putrps():
    try:
        obj = request.get_json()
        header = request.headers['token']
        obj["currenttoken"] = header
        token = workbase(obj).validatetoken()
        if token['token'] == "valid":
            a = workbase(obj).putrps()
            return jsonify(a[0]),a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500

# Providers - Create and quering
@app.route(f"/api/v{version}/providers", methods=['POST'])
@cross_origin()
def createproviders():
    try:
        obj = request.get_json()
        header = request.headers['token']
        obj["currenttoken"] = header
        token = workbase(obj).validatetoken()
        print(token)
        if token['token'] == "valid":
            a = workbase(obj).createproviders()
            # print(a)
            return jsonify(a[0]),a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except Exception as e:
        return {"message": e}, 500

# Providers - Quering
@app.route(f"/api/v{version}/providers", methods=['GET']) 
@cross_origin()
def selectproviders():
    try:
        obj = {}
        header = request.headers['token']
        obj["currenttoken"] = header
        token = workbase(obj).validatetoken()
        if token['token'] == "valid":
            a = workbase(obj).selectproviders()
            return jsonify(a[0]),a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500


# Providers - Changing and querying
@app.route(f"/api/v{version}/providers", methods=['PUT'])
@cross_origin()
def putproviders():
    try:
        obj = request.get_json()
        header = request.headers['token']
        obj["currenttoken"] = header
        token = workbase(obj).validatetoken()
        if token['token'] == "valid":
            a = workbase(obj).putproviders()
            return jsonify(a[0]),a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500

# Borrowers - Create and quering
@app.route(f"/api/v{version}/borrowers", methods=['POST'])
@cross_origin()
def createborrowers():
    try:
        obj = request.get_json()
        header = request.headers['token']
        obj["currenttoken"] = header
        token = workbase(obj).validatetoken()
        if token['token'] == "valid":
            a = workbase(obj).createborrowers()
            return jsonify(a[0]),a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500

# Borrowers - Quering
@app.route(f"/api/v{version}/borrowers", methods=['GET']) 
@cross_origin()
def selectborrowers():
    try:
        obj = {}
        header = request.headers['token']
        obj["currenttoken"] = header
        token = workbase(obj).validatetoken()
        if token['token'] == "valid":
            a = workbase(obj).selectborrowers()
            return jsonify(a[0]),a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500


# Borrowers - Changing and querying
@app.route(f"/api/v{version}/borrowers", methods=['PUT'])
@cross_origin()
def putborrowers():
    try:
        obj = request.get_json()
        header = request.headers['token']
        obj["currenttoken"] = header
        token = workbase(obj).validatetoken()
        if token['token'] == "valid":
            a = workbase(obj).putborrowers()
            return jsonify(a[0]),a[1]
        else:
            return {"message": "current user has not been validated"}, 401
    except:
        return {"message": "internal server erro"}, 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)