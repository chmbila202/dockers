# save this as app.py
from flask import Flask
from flask_mysqldb import MySQL
from flask import jsonify

app = Flask(__name__)

app.config['MYSQL_HOST'] = '172.17.0.2'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'abc123'
app.config['MYSQL_DB'] = 'docker'

mysql = MySQL(app)
print(mysql)
@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/customers")
def customers():
    cursor = mysql.connection.cursor()
    cursor.execute(''' SELECT cid,cname FROM customer''')
    data = cursor.fetchall()
    return jsonify(data)


@app.route('/customers/<int:cid>')
def customerid(cid):
    # Logic goes here
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM customer where cid=%s" % str(cid))
    data = cursor.fetchall()
    return jsonify(data)

@app.route('/customers/<int:cid>/orders')
def customerorders(cid):
    # Logic goes here
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM orders where cid=%s" % str(cid))
    data = cursor.fetchall()
    return jsonify(data)

@app.route('/customers/<int:cid>/orders/<int:oid>')
def customerordersunique(cid,oid):
    # Logic goes here
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM orders where oid=%s" % str(oid))
    data = cursor.fetchall()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5001)