from flask import Flask, render_template, request
from flaskext.mysql import MySQL
app = Flask(__name__)
app.debug = True
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'scraper'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
TABLE_NAME = 'fxstreet'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

@app.route("/")
def main():
    start_date = request.args.get("start_date",None)
    end_date = request.args.get("end_date",None)
    data = ()
    print (start_date,end_date)
    if start_date and end_date:
        start_date = start_date.replace('-','')
        end_date = end_date.replace('-','')
        cursor.execute("SELECT * from "+TABLE_NAME+" where  nyc_date  > "+start_date+" and nyc_date < "+end_date )
        data = cursor.fetchall()
        
    return render_template('index.html',data=data)


if __name__ == "__main__":
    app.run(port=5000)