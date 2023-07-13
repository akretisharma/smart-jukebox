#!/usr/bin/env python
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

DEVICE_ID="DeviceID"
CLIENT_ID="ClientID"
CLIENT_SECRET="ClientSecret"

while True:
    try:
        reader=SimpleMFRC522()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))
        
        # create an infinite while loop that will always be waiting for a new scan
        while True:
            print("Waiting for record scan...")
            id= reader.read()[0]
            print("Card Value is:",id)
            sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
            
            # DONT include the quotation marks around the card's ID value, just paste the number
            if (id==124817002481):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:1uyf3l2d4XYwiEqAb7t7fX')
                sleep(2)
                
            elif (id==399694909361):
                
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:7tBzJeTvJSZ254cu879LpK')
                sleep(2)
                
            elif (id==674572816241):
                
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:4YOJFyjqh8eAcbKFfv88mV'])
                sleep(2)
                
            elif (id==949450723121):
                
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:4kzvAGJirpZ9ethvKZdJtg'])
                sleep(2)
                
            elif (id==674421821304):
                
                # playing a song
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:47BBI51FKFwOMlIiX6m8ya'])
                sleep(2)
                
            # continue adding as many "elifs" for songs/albums that you want to play

    # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...")
        GPIO.cleanup()
