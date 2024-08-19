import yfinance as yf; import time; from gtts import gTTS; from playsound import playsound; from datetime import datetime; import pytz;  # Import pytz for timezone handling
from flask import Flask, request, jsonify; import threading; import pyautogui
app = Flask(__name__)
def play_audio(message): filename = "alert.mp3"; tts = gTTS(text=message, lang='en'); tts.save(filename); playsound(filename) # Function to play audio for the specified message
@app.route('/alert', methods=['POST'])  # Route to handle POST requests from TradingView
def handle_alert():
    data = request.json
    if 'message' in data:
        message = data['message']; play_audio(message); time.sleep(2); ping_filename = "ping.mp3"; 
        '''
#!-----------------------------------------------------------------------------------------------------------------------------   
        ping_message = "Mouse Moving!"; tts = gTTS(text=ping_message, lang='en'); tts.save(ping_filename); playsound(ping_filename)
        wake_x = 100; wake_y = 100; wake_x2 = 2000; wake_y2 = 1000
        pyautogui.moveTo(wake_x, wake_y, duration=1); pyautogui.moveTo(wake_x2, wake_y2, duration=1); pyautogui.moveTo(wake_x, wake_y, duration=1); time.sleep(7)  
#!-----------------------------------------------------------------------------------------------------------------------------   
        start_x = 1272  
        start_y = 1141  
        end_x =   1272 
        end_y =   800  
#!-----------------------------------------------------------------------------------------------------------------------------
        pyautogui.moveTo(start_x, start_y, duration=1); pyautogui.mouseDown(); pyautogui.moveTo(end_x, end_y, duration=1); pyautogui.mouseUp() 
#!-----------------------------------------------------------------------------------------------------------------------------   
        '''
        return jsonify({"status": "success", "message": "Alert received and processed."})
    else:
        return jsonify({"status": "error", "message": "Invalid data received."})
def play_audio_one_minute():
    filename = "one_minute.mp3"; message = "1"; tts = gTTS(text=message, lang='en'); tts.save(filename);playsound(filename)
def announce_five_minutes():
    filename = "five_minutes.mp3"; message = "5 minutes!"; tts = gTTS(text=message, lang='en'); tts.save(filename); playsound(filename)
def announce_time_in_mst():  # Function to announce the current time in MST
    mst_tz = pytz.timezone('America/Denver'); current_time_mst = datetime.now(mst_tz).strftime("%I:%M")  # Format the time in 12-hour format without AM/PM
    message = f"{current_time_mst}."; filename = "time_announcement.mp3"; tts = gTTS(text=message, lang='en'); tts.save(filename); playsound(filename)
def monitor_time():
    while True:
        now = datetime.now(); current_minute = now.minute; current_second = now.second
        if current_second == 0:  # Check if it's the top of the minute
            if current_minute % 5 == 0:  # Every 5 minutes, check if it's time to announce the current time
                announce_five_minutes(); announce_time_in_mst()
            else:
                play_audio_one_minute()  # Play audio for "1 minute" if not at the top of the 5-minute mark
        time.sleep(1)  # Sleep for 1 second to avoid tight loop
if __name__ == "__main__":  # Run the Flask app in a separate thread to allow monitoring to run concurrently
    threading.Thread(target=lambda: app.run(port=5000, debug=True, use_reloader=False)).start() # Start the Flask app in a separate thread
    monitor_time() # Start monitoring time

    