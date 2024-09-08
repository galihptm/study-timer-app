import streamlit as st
import time
from playsound import playsound
import threading
from streamlit_javascript import st_javascript

# Fungsi untuk memutar suara alarm
def play_alarm():
    playsound('digitalalarmclocksound.mp3')

# Judul Aplikasi
st.title("Timer dengan Popup Notifikasi dan Suara")

# Input waktu dari pengguna
hours = st.number_input("Masukkan jam", min_value=0, step=1, value=0)
minutes = st.number_input("Masukkan menit", min_value=0, step=1, value=0)
seconds = st.number_input("Masukkan detik", min_value=0, step=1, value=0)

# Tombol untuk memulai timer
if st.button("Mulai Timer"):
    total_seconds = hours * 3600 + minutes * 60 + seconds

    if total_seconds == 0:
        st.warning("Masukkan waktu yang valid!")
    else:
        st.write(f"Timer dimulai untuk {hours} jam, {minutes} menit, dan {seconds} detik...")
        
        # Placeholder untuk sisa waktu
        timer_placeholder = st.empty()

        # Hitung mundur
        while total_seconds > 0:
            hours_left = total_seconds // 3600
            minutes_left = (total_seconds % 3600) // 60
            seconds_left = total_seconds % 60

            timer_placeholder.text(f"Sisa waktu: {hours_left} jam, {minutes_left} menit, {seconds_left} detik")
            time.sleep(1)
            total_seconds -= 1

        # Memutar alarm di thread terpisah
        alarm_thread = threading.Thread(target=play_alarm)
        alarm_thread.start()

        # Menampilkan popup notifikasi waktu habis
        st_javascript('alert("⏰ Waktu habis!");')

        # Tombol untuk menghentikan alarm
        if st.button("Stop Alarm"):
            st.stop()
