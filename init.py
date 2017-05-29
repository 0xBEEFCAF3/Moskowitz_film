# -*- coding: utf-8 -*-
"""
Created on Mon May 15 19:52:10 2017

@author: Armin
"""
import csv
import urllib2
from bs4 import BeautifulSoup 
from flask import Flask, request, render_template, session, redirect,g
from flask_pymongo import PyMongo

app =  Flask(__name__)

@app.route('/')


def index():
	makeEmbed()
	return render_template('index.html',var = '<h1> HI </h1>')

def makeEmbed():
	#read the csv with the embeded code 
	a = []
	with open('embeds.csv') as embed:
		reader = csv.reader(embed)
	    	for row in reader:
	    		a.append(row)
	print(a)
	#create html file
	with open('templates/embed.html','w') as htmlFile:
		for i in a:
			print("this is once")
			htmlFile.write("<!-- Start Person Block --> <div class='person'>")
			htmlFile.write(str(i))
			htmlFile.write("</div><!-- Clear--><div class='clear'></div><!-- End Person Block -->")
			htmlFile.write("\n")

if __name__ == "__main__":
    app.run(debug = True)