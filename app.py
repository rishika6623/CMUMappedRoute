from flask import Flask, render_template, request, flash, redirect, url_for, session
import sqlite3

app = Flask(__name__)

@app.route('/')
def index_page():  # put home applications's code here
    return render_template('index.html')