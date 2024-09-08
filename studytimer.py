import streamlit as st
import time
from playsound import playsound
import threading
from streamlit_javascript import st_javascript

# Fungsi untuk memutar suara alarm
def play_alarm():
    playsound('digitalalarmclocksound.mp3')

# Judul Aplikasi
st.title("Simple Study Timer App")

# Input waktu dari pengguna
hours = st.number_input("Input hour", min_value=0, step=1, value=0)
minutes = st.number_input("Input minute", min_value=0, step=1, value=0)
seconds = st.number_input("Input second", min_value=0, step=1, value=0)

# Tombol untuk memulai timer
if st.button("Start Study!"):
    total_seconds = hours * 3600 + minutes * 60 + seconds

    if total_seconds == 0:
        st.warning("Input valid time!")
    else:
        st.write(f"Study timer is set for {hours} hour(s), {minutes} minute(s), dan {seconds} second(s)...")
        
        # Placeholder untuk sisa waktu
        timer_placeholder = st.empty()

        # Hitung mundur
        while total_seconds > 0:
            hours_left = total_seconds // 3600
            minutes_left = (total_seconds % 3600) // 60
            seconds_left = total_seconds % 60

            timer_placeholder.text(f"Time Remaining: {hours_left} hour(s), {minutes_left} minute(s), {seconds_left} second(s)")
            time.sleep(1)
            total_seconds -= 1

        # Memutar alarm di thread terpisah
        alarm_thread = threading.Thread(target=play_alarm)
        alarm_thread.start()

        # Menampilkan popup notifikasi waktu habis
        st_javascript('alert("⏰ Time Overr!");')

        # Tombol untuk menghentikan alarm
        if st.button("Reset Alarm"):
            st.stop()
