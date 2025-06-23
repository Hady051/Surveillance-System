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
