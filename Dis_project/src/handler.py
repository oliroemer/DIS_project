from flask import Flask, redirect, url_for , render_template, request, flash 
from datetime import timedelta
import pandas as pd 
from psycopg2 import sql, connect
from commons import *

#FLASK CONFIG##########################################
app = Flask(__name__)
app.secret_key = CONFIG["SECRET_KEYS"]["APP_SECRET_KEY"]


#DATABASE CONFIG#######################################
conn = connect(dbname=CONFIG["DATABASE"]["dbname"],
        user=CONFIG["DATABASE"]["user"],
        host=CONFIG["DATABASE"]["host"],
        password=CONFIG["DATABASE"]["password"])
cur = conn.cursor()


init_succes, cols = init_database(cur)
assert init_succes, "Something went wrong when creating the database!"


#Front page / home page 
@app.route("/", methods=('GET','POST'))
@app.route("/data",methods=('GET','POST'))
def home():
    if request.method == 'POST':
        requirements_lst = []
        requirements_lst.append(request.form["Formål"])
        requirements_lst.append(request.form["Priser"]) 
        requirements_lst.append(request.form["OS"]) 
        requirements_lst.append(request.form["Gaming"])

        if requirements_lst==['0', '0', '0', '0']: 
            return render_template("front_page.html")




        filtered_data = get_filted_data(requirements_lst,cur)
   

        if filtered_data: 
            return render_template("data.html" ,table_headings = cols, table_data = filtered_data)
        
        else: 
            flash("No results for your search! ")
            return render_template("front_page.html")
    else:
        return render_template("front_page.html")



#Discount page
@app.route("/discount")
def discount():
    discount_data = get_discount(cur)
    return render_template("data.html", table_headings = cols, table_data = discount_data )

