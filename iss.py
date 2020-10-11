#!/usr/bin/env python

__author__ = 'Erica best purplecoder04 and studyhall'

import requests
import turtle
import time

# payload = {"craft": "ISS", "name": "first Last"}
r = requests.get('http://api.open-notify.org/astros.json')
print(r.text)


def loc():
    r = requests.get('http://api.open-notify.org/iss-now.json').json()
    return r


def partd():
    
    r = requests.get('http://api.open-notify.org/iss-pass.json?lat=39.791000&lon=-86.148003').json()
    indy_time = time.ctime(r["response"][0]["risetime"])
    return indy_time


def map(iss_location, indy_past):
    s = turtle.Screen()
    s.setup(height=360, width=720),
    s.bgpic("map.gif"),
    s.setworldcoordinates(-180, -90, 180, 90)
    s.register_shape("iss.gif")
    #  setting up iss
    iss = turtle.Turtle()
    iss.shape("iss.gif")
    iss.setheading(90)
    lat = float(iss_location["iss_position"]["latitude"])
    lon = float(iss_location["iss_position"]["longitude"])
    iss.penup()
    iss.goto(lon, lat)
    # setting up indy
    indy = turtle.Turtle()
    indy.shape("circle")
    indy.color("purple")
    indy.setheading(90)
    indy.penup()
    indy.goto(-86.148003, 39.791000)
    indy.write(indy_past)
    turtle.done()
    # setiing next time craft will past over indy
    


def main():
    iss_location = loc()
    indy_past = partd()
    map(iss_location,indy_past)

if __name__ == '__main__':
    main()
