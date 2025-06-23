# 🛡️ RPi PIR-Camera Surveillance System with Buzzer & Web Interface

A motion-triggered Raspberry Pi surveillance system using:
- **Raspberry Pi 4**
- **Pi Camera v2**
- **HC‑SR501 PIR motion sensor**
- **Passive buzzer**
- Python-powered backend + Flask webserver
- Auto photo capture + email alerts + in-browser live photo tab

---

## 📦 Hardware

- Raspberry Pi 4
- Pi Camera v2 (CSI connector)
- HC‑SR501 PIR sensor (VCC, GND, OUT)
- Passive buzzer
- Jumper wires, breadboard & 1 kΩ resistor

---

## 🛠️ Software Dependencies

```bash
sudo apt update
sudo apt install python3-gpiozero python3-picamera python3-flask
pip3 install flask-mail
'''
---

## How the Project works

the project focuses on making a web server inside the RPi, by a PIR sensor python file so that if the detected movement is more than 4 seconds, a **photo will be taken by the RPi** and **will be sent to the email of the car/home owner and the buzzer will alarm the user.** Also, inside **the web server**, there will be a **tab** for the user that he can check. This **tab will be updated automatically and will show the last photo taken.**

---

## ⚙️ Operation Flow

1. Motion in >4s: PIR sensor triggers.

2. Script waits for 4+ secs of continuous motion.

3. Capture image via PiCamera.

4. Activate buzzer alarm (2–5 secs).

5. Send email with the captured image via SMTP to the user's gmail.

6. Add image to web server.

7. Web interface: Displays latest image, auto-refreshing periodically.

---

![Web server giving the User the last pic taken](https://github.com/user-attachments/assets/f5e61017-6ead-419c-bbce-8672b1b20227)
