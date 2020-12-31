import pyautogui

pyautogui.DELAY = 0.5

pyautogui

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
digit_positions = []
clear_key = None
print('Locating buttons')
for d in digits:
    while True:
        pos = pyautogui.locateCenterOnScreen(f'calc{d}key.png')
        if pos is None:
            pyautogui.alert(f'Couldn\'t locate the {d} key.\nBring calculator into view, then click OK')
        else:
            print(f'found {d} key')
            break
    digit_positions.append(pos)

while True:
    pos = pyautogui.locateCenterOnScreen(f'clearkey.png')
    if pos is None:
        pyautogui.alert(f'Couldn\'t locate the C key.\nBring calculator into view, then click OK')
    else:
        print(f'found C key')
        break
clear_key = pos

number = pyautogui.prompt("Enter number")
try:
    int(number)
except ValueError:
    pyautogui.alert("Nope")
    raise ValueError
pyautogui.click(clear_key.x, clear_key.y)
print('C', end='', flush=True)
for d in number:
    print(d, end='', flush=True)
    pyautogui.click(digit_positions[int(d)].x, digit_positions[int(d)].y)
