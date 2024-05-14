from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QListWidget, QTextEdit, QLineEdit
from PyQt5.QtCore import Qt
from text import *

# -----------------создание приложения и работа с окном-----------------------
app = QApplication([]) # выделение места и создание приложения

game = QWidget() # создание окна
game.resize(600, 600)
game.setWindowTitle('The Legend Of Fears')
game.show() # по умолчанию окно скрыто и нужно его показать

# ---------------------------визуальная часть приложения-----------------------

# создание направляющих
v_line = QVBoxLayout()
h_line = QHBoxLayout()
low_line = QHBoxLayout()

inventory = QListWidget() # Ну игровая область там текст инвентарь и сё такое
information = QTextEdit() # хахах влад проости
information.setReadOnly(True)
btn1 = QPushButton('Спрятаться под деревом от страха и рыдать')
btn2 = QPushButton('Убежать из леса и попытаться найти портал')
btn3 = QPushButton('В недоумении искать свою комнату')

h_line.addWidget(inventory) # добалвление всяких панелек
h_line.addWidget(information) #  

v_line.addLayout(h_line)  # закрепление горизонтальной линии на вертикальной направляющей

low_line.addWidget(btn1) # добавление кнопырей
low_line.addWidget(btn2) #  
low_line.addWidget(btn3) #   

v_line.addLayout(low_line) # прикрепление нижней линии к вертикальной

game.setLayout(v_line) # закрепление основного лэйаута для окна

#----------------------------------Классы--------------------------------------------------------

class Character():
    def __init__(self, name, hp, armor, power, inventory=[]):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.power = power
        self.inventory = inventory
    def print_info(self):
        information.setText(f'\n\n\nПоприветствуйте героя -> {self.name}')
        information.setText(f'\n\n\nПоприветствуйте героя -> {self.name}\nУровень здоровья: {self.hp}')
        information.setText(f'\n\n\nПоприветствуйте героя -> {self.name}\nУровень здоровья: {self.hp}\nУровень брони: {self.armor}')
        information.setText(f'{tab}Поприветствуйте героя -> {self.name}\nУровень здоровья: {self.hp}\nУровень брони: {self.armor}\nСила удара: {self.power}')
    def strike(self, enemy):
        enemy.armor -= self.power
        if enemy.armor <= 0:
            enemy.hp += enemy.armor
            enemy.armor = 0

#---------------------------предметы---------------------------------------------

wooden_sw = inventory.findItems("Деревянный меч", Qt.MatchExactly) #             М    но тут не сами предметы по факту а их нахождение 
br_iron_sw = inventory.findItems("Поломанный железный меч", Qt.MatchExactly) #   Е    в инвентаре
slime_sw = inventory.findItems("Поломанный железный меч", Qt.MatchExactly) #     Ч
legendary_sw = inventory.findItems("Легендарный меч", Qt.MatchExactly) #         И
#--------------------------------------------------------------------------------
leg_armor = inventory.findItems("Легендарная броня старого тёмного лорда", Qt.MatchExactly) # броня имбовая
#--------------------------------------------------------------------------------
slime_core = inventory.findItems("Ядро слайма", Qt.MatchExactly) # ядро обычного слайма(нужно 10 штук для крафта)
king_slime_core = inventory.findItems("Ядро короля слаймов", Qt.MatchExactly) # ядро короля слаймов(для крафта слаймового меча)
chest_key = inventory.findItems("Ключ от сундука", Qt.MatchExactly) # ключ от сундука(для брони)
door_key = inventory.findItems("Ключ от сундука", Qt.MatchExactly) # ключ от ворот в деревню гоблинов(для легендарного меча)
camouflage = inventory.findItems("Гоблинский камуфляж", Qt.MatchExactly) # камуфляж гоблина
#============================персы================================================
knight = Character('Вы', 100, 50, 25) # Главный герой
b_slime = Character('Синий слайм', 25, 5, 5) #  Деф слайм
goblin = Character('Гоблин', 100, 50, 25) #  Гоблен(Габен)

#-----------------------------шаблон файта и сам файт со слаймом-------------------------
info_your_strike_txt = f'Ваша информация: {tab} -> {knight.name}\nУровень здоровья: {knight.hp}\nУровень брони: {knight.armor}\nСила удара: {knight.power}'
info_enemy_strike_txt = f'Поприветствуйте героя -> {b_slime.name}\nУровень здоровья: {b_slime.hp}\nУровень брони: {b_slime.armor}\nСила удара: {b_slime.power}'
wow_strike_txt = '->УДАР!'

strike_txt = f'{info_your_strike_txt + tab + info_enemy_strike_txt + tab + wow_strike_txt}'

your_strike_txt = f'\n{knight.name} атакуете {b_slime.name} используя деревянный меч'
second_your_strike_txt = f'\n{b_slime.name} покачнулся, класс брони: {b_slime.armor}, уровень здоровья: {b_slime.hp}'

slime_strike_txt = f'\n{b_slime.name} атакует вас, используя технику истощения с помощью слаймовой магии'
second_slime_strike_txt = f'\n{knight.name} покачнулись, уровень брони: {knight.armor}, уровень здоровья: {knight.hp}'

#-----------------------------первый вин--------------------------------------------------
first_win_txt = f'Поздравляем! Вы с невероятной лёгкостью стёрли {b_slime.name} с лица тёмных земель! В награду за вашу победу вы получите ядро слайма\nЧтобы продолжить нажмите кнопку использовать'

#------------------------------файт с зеленым лошком---------------------------------------
info_your_strike_txt = f'Ваша информация: {tab} -> {knight.name}\nУровень здоровья: {knight.hp}\nУровень брони: {knight.armor}\nСила удара: {knight.power}'
info_goblin_strike_txt = f'Поприветствуйте героя -> {goblin.name}\nУровень здоровья: {goblin.hp}\nУровень брони: {goblin.armor}\nСила удара: {goblin.power}'
goblin_strike_txt = '->УДАР!'

g_strike_txt = f'{info_your_strike_txt + tab + info_goblin_strike_txt + tab + wow_strike_txt}'

g_your_strike_txt = f'\n{knight.name} атакуете {goblin.name} используя почти сломанный железный меч'
g_second_your_strike_txt = f'\n{goblin.name} принял на себя, класс брони: {goblin.armor}, уровень здоровья: {goblin.hp}'

goblin_strike_txt = f'\n{goblin.name} атакует вас, используя копьё с наконечником из куска острого мрамора'
second_goblin_strike_txt = f'\n{knight.name} покачнулись, уровень брони: {knight.armor}, уровень здоровья: {knight.hp}'

#===================================Функции и всё такое===========================================

def new(): #Вступление
    information.setText(new_txt)
    btn1.setText('Спрятаться под деревом от страха и рыдать')
    btn2.setText('Убежать из леса и попытаться найти портал')
    btn3.setText('В недоумении искать свою комнату')
#---------------------------первый выбор вначале игры---------------------------------------------

def order_of_fear():
    information.setText(f'{new_txt}')
    btn1.setText('Спрятаться под деревом от страха и рыдать')
    btn2.setText('Убежать из леса и попытаться найти портал')
    btn3.setText('В недоумении искать свою комнату')

#---------------------------итоги первого выбора---------------------------------------------

cry = 'not started'
def new_cry():
    information.setText(f'{new_txt + tab + new_cry_txt}')
    global cry
    cry = 'ended'
    return cry

room = 'not started'                       
def new_room(): #             
    information.setText(f'{new_txt + tab + new_room_txt}')
    room == 'ended'

#-----------------------------плохой выбор--------------------------------------------------------

before_fight_txt = f'{new_txt + tab + tab + new_portal_txt}'

find_portal = 'not started'
def new_portal():
    information.setText(f'{before_fight_txt}')
    find_portal == 'ended'

first_fight = 'not started'

def print_fight_b_slime(): # сразу и шаблон файта и файт со слаймом
    first_fight = 'started'
    information.setText(f'{before_fight_txt + tab + strike_txt}')
    knight.strike(b_slime)
    information.setText(f'{before_fight_txt + tab + strike_txt + your_strike_txt}')
    information.setText(f'{before_fight_txt + tab + strike_txt + your_strike_txt + tab + second_your_strike_txt}')
    b_slime.strike(knight)
    information.setText(f'{before_fight_txt + tab + strike_txt + your_strike_txt + tab + second_slime_strike_txt + tab + slime_strike_txt}')
    information.setText(f'{before_fight_txt + tab + strike_txt + your_strike_txt + tab + second_your_strike_txt + tab + slime_strike_txt + tab + second_slime_strike_txt}')
    first_fight == 'ended'

after_fight_txt = f'{before_fight_txt + tab + strike_txt + your_strike_txt + tab + second_slime_strike_txt + tab + slime_strike_txt + tab + second_slime_strike_txt}'

first_fight_res = 'not started'

def first_win():
    information.setText(f'{after_fight_txt + tab + first_win_txt}')
    inventory.addItem('Ядро слайма')
    return first_fight_res == 'ended'

#=========================обнаружение дома из дерева и выбор================================

find_sword = 'not started'

def find_iron_sw():
    information.setText(f'{after_fight_txt + tab + first_win_txt + tab + find_iron_sw_txt}')
    global find_sword
    find_sword = 'start'
    return find_sword

def enter_house():
    information.setText(f'{after_fight_txt + tab + first_win_txt + tab + find_iron_sw_txt + tab + enter_house_txt}')

def go_faraway():
    information.setText(f'{after_fight_txt + tab + first_win_txt + tab + find_iron_sw_txt + tab + enter_house_txt + tab + go_faraway_txt}')

def relax():
    information.setText(f'{after_fight_txt + tab + first_win_txt + tab + find_iron_sw_txt + tab + enter_house_txt + tab + go_faraway_txt + tab + relax_txt}')

after_find_home_txt = f'{after_fight_txt + tab + first_win_txt + tab + find_iron_sw_txt + tab + enter_house_txt + tab + go_faraway_txt}'

#-----------------------------выбор внутри дома---------------------------------------------

def check_table(): # осмотр стола
    information.setText(f'{after_find_home_txt + tab + check_table_txt}')

def check_chest(): # осмотр сундука
    information.setText(f'{after_find_home_txt + tab + check_table_txt + tab + check_chest_txt}')
    inventory.addItem('Железный меч')
    inventory.takeItem('Деревянный меч')

def check_bedside_table(): # осмотр тумбочки
    information.setText(f'{after_find_home_txt + tab + check_table_txt + tab + check_chest_txt + tab + check_bedside_table_txt}')

after_find_sw_txt = f'{after_find_home_txt + tab + check_table_txt + tab + check_chest_txt + tab + check_bedside_table_txt}'

#--------------------------поход в пещеру---------------------------------------------------
goblin_fight = 'not started'

def go_to_cave():
    information.setText(f'{after_find_sw_txt + tab + sw_found}')
    if btn3.clicked:
        information.setText(f'{after_find_sw_txt + tab + sw_found}')

def print_fight_goblin():
    information.setText(f'{after_find_sw_txt + tab + sw_found + tab + g_strike_txt}')
    knight.strike(goblin)
    information.setText(f'{after_find_sw_txt + tab + sw_found + tab + g_strike_txt + your_strike_txt}')
    information.setText(f'{after_find_sw_txt + tab + sw_found + tab + g_strike_txt + your_strike_txt + tab + second_your_strike_txt}')
    b_slime.strike(knight)
    information.setText(f'{after_find_sw_txt + tab + sw_found + tab + g_strike_txt + your_strike_txt + tab + second_slime_strike_txt + tab + slime_strike_txt}')
    information.setText(f'{after_find_sw_txt + tab + sw_found + tab + g_strike_txt + g_your_strike_txt + tab + g_second_your_strike_txt + tab + goblin_strike_txt + tab + second_goblin_strike_txt}')
    goblin_fight == 'ended'    

def win_on_goblin():
    information.setText(f'{after_find_sw_txt + tab + sw_found}')

def dungeon_n_dragons():
    information.setText(f'{after_find_sw_txt + tab + sw_found + tab + g_win + tab + g_fight_slimes + tab + find_village + tab + fears + tab + sell}')

#==============================запуск всяких функций и так далее============================

first_stage = 'start'

new()
if wooden_sw: # Проверка на то есть ли деревянный меч чтобы он не дюпался
    inventory.takeItem('Деревянный меч')
else:
    inventory.addItem('Деревянный меч')

order_of_fear()

btn1.clicked.connect(new_cry)

# if btn2.clicked:
#     new_portal()

# if btn3.clicked:
#     new_room()

first_stage = 'end'

if find_portal == 'ended':
    btn2.clicked.disconnect(new_portal)


if cry == 'ended':
    btn1.clicked.disconnect(new_cry)


if room == 'ended':
    btn3.clicked.disconnect(new_room)


second_stage = 'start'

# btn1.setText('Использовать') # кнопки
# btn2.setText('Защита') #
# btn3.setText('Удар') #

btn3.clicked.connect(print_fight_b_slime)
if first_fight == 'ended':
    btn3.clicked.disconnect(print_fight_b_slime)
    btn3.clicked.connect(first_win)

# if first_fight_res == 'ended':
#     btn1.setText(f'Войти в дом')
#     btn2.setText(f'Пойти дальше')
#     btn3.setText(f'Я устал от хождения, лучше посижу')

# btn1.clicked.connect(enter_house)
# btn2.clicked.connect(go_faraway)
# btn3.clicked.connect(relax)

# btn1.disconnect(enter_house)
# btn2.disconnect(go_faraway)
# btn3.disconnect(relax)

# btn1.setText('Осмотреть стол')
# btn2.setText('Осмотреть сундук')
# btn3.setText('Осмотреть тумбочку')

# btn1.clicked.connect(check_table)
# btn2.clicked.connect(check_chest)
# btn3.clicked.connect(check_bedside_table)

# btn1.disconnect(check_table)
# btn2.disconnect(check_chest)
# btn3.disconnect(check_bedside_table)

# btn1.setText('Использовать') # кнопки
# btn2.setText('Защита') #   
# btn3.setText('Удар') #    






app.exec_()