import pyautogui

# Pobieranie aktualnej pozycji kursora
x, y = pyautogui.position()

# Wyświetlanie pozycji kursora
print("Pozycja kursora:")
print("X:", x)
print("Y:", y)
