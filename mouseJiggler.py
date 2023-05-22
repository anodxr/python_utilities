"""Mouse Jiggler"""
import random
import time
from threading import Thread
import pyautogui as pg
from pynput import keyboard

# Esta variable va a controlar si el programa debe pausarse o no
pause = False
stop = False

def on_press(key):
    """Funcion para revisar la tecla presionada"""
    global pause
    global stop
    # Cuando se presione la tecla 'p', cambia el estado de 'pause'
    if key == keyboard.KeyCode(char='p'):
        pause = not pause
    elif key == keyboard.KeyCode(char='s'):
        stop = True
        

def start_listening():
    """Comienza a escuchar los eventos del teclado"""
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


# Comienza un nuevo hilo que escucha los eventos del teclado
listener_thread = Thread(target=start_listening)
listener_thread.daemon = True
listener_thread.start()

progress = 0

while True:
    if pause:
        print('\rEn pausa: [' + '#' * progress + ' ' * (10 - progress) + ']', end='')
        progress = (progress + 1) % 11
        time.sleep(0.5)
        continue
    elif stop:
        print('\rSaliendo...', end='')
        break
    x = random.randint(900, 1500)
    y = random.randint(400, 800)
    pg.moveTo(x, y, duration=0.5)
    time.sleep(1)

