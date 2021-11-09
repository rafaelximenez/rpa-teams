import pyautogui
import time

def select_component(file_path, sleep_seconds):
    try:
        element = pyautogui.locateOnScreen(file_path)
        element_x, element_y = pyautogui.center(element)
        pyautogui.click(element_x, element_y)
        time.sleep(sleep_seconds)

        return element
    except:
        print(f'Falha ao encontrar o elemento {file_path}')
    

button_teams = select_component('images/teamsCloseIco.PNG', 5)
button_teams = select_component('images/teamsOpenIco.PNG', 1)


search_bar = select_component('images/searchBar.png', 1)

text_search = 'Erick Castorino e Vinicius'
pyautogui.write(text_search)

time.sleep(1)

selected_chat = select_component('images/selectedChat.png', 1)
message_bar = select_component('images/messageBar.png', 1)

message = '.'
pyautogui.write(message)
#pyautogui.press('enter')
