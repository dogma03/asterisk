from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QListWidget, QTextEdit, QLineEdit
from PyQt5.QtCore import Qt

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
information = QTextEdit()
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

#=======================текста и всё связанное с ними============================

tab = '\n\n------------------------------\n\n'

history_txt = 'Привет герой, кажись это твой первый раз нахождения в этом мире\nНо ничего страшного, это не помешает геймплею или истории\nПо сюжету ты обычный торговец, но гуляя как-то раз по лесу, ты находишь меч, и решаешь встать на путь путешественника'

order_of_fear_txt = '''После того как вы взяли свой меч вы решили вернуться в город из леса в котором вы нашли свой меч, затем когда вы вернулись в город вы увидели такую картину
"Весь город в огне, множество людей орут и бегают по всему городу от страха, верно, на ваш город напали тёмные силы, по словам очевидца в центре города открылся портал и оттуда выбрались эти демоны и нечисть
,они устроили полную разруху, поджигают и взрывают дома, убивают и едят людей, повсюду эти тёмные порталы", увидев это вы в панике зашли в свой дом чтобы собрать вещи и слинять, но под вами открывается портал,
 и по итогу вы падаете из своего дома в потусторонний мир, вы приземлились посреди леса, что будете делать дальше?\nКнопка использовать отвечает за выбор "Спрятаться под деревом от страха и рыдать"\nВ то же время защита отвечает за выбор "Убежать из леса и попытаться найти портал"'''

new_txt = f'{history_txt + tab + order_of_fear_txt}'

new_cry_txt = 'Вас нашёл маленький радиоактивный тёмный паук, вы его не заметили, он вас укусил и вы превратились в полчище таких же пауков, игра окончена.'
new_room_txt = 'Судя по всему вы не заметили того как попали в этот мир и начали искать лестницу чтобы взять важные вещи из спальни на втором этаже.\nИтог: на вас напали тёмные лозы и задушили вас, игра окончена'
new_portal_txt = 'В процессе поиска портала домой вы заметили синего слайма, он выглядел безобидным так как не заметил ВАС, но вы знаете что в этом мире кто угодно готов убить вас, вы решили напасть на него со спины'

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
#-------------------------------нахождение дома и меча железного--------------------------
find_iron_sw_txt = 'После того как вы уничтожили слайма, вы решили пройтись по тёмному лесу... Спустя час блуждания по тёмным землям вы нашли некое поломанное старое дряхлое здание из тёмного дерева.Зайти внутрь?'
enter_house_txt = 'По итогу вы решили зайти в дом, внутри дома находится дряхлая кровать, поломанный стол, тумбочка, приоткрытый сундук из которого торчит кончик меча\nЧто осмотрите первым делом?'
go_faraway_txt = 'Вы решили пойти дальше и не заходить в дом, пройдя дальше вы ничего не заметили кроме странной пещеры, вы решили вернуться в дом и посмотреть что там'
relax_txt = 'После того как вы отдохнули вы решили зайти в этот дом и посмотреть что там(открою секрет, выбора в этих кнопках нет, это иллюзия выбора, психологический трюк, рофел)'

check_table_txt = 'Получается вы решили первым делом осмотреть стол, вы всего лишь нашли там всякие таблички, бумажки и так далее, на них написано что-то на неизвестном для вас языке. На бумаге написано: ぁ゜゜゜゜👺ぁぁ🥷げごさ しぜぢ\nА на табличках написано: げごぢ👺ぁ゜ぁご'
check_chest_txt = 'Вы решили посмотреть сундук так как вас заинтересовал меч который торчит оттуда, вы открыли его, и увидели железный меч, вашей радости не было предела, но затем вы заметили что на нём было множество сколов, трещин и так далее, но это всё равно лучше вашей деревянной палки(меча)\nВы решили забрать меч себе и выкинуть старый'
check_bedside_table_txt = 'Вы решили осмотреть тумбочку у дряхлой кровати, открыв её вы обнаружили там ручку из которой потекла паста, опять непонятные бумаги, ну и всё впринципе'
#-------------------------------поход в пещеру---------------------------------------------
sw_found = 'После того как вы забрали себе меч, вы решили выйти из дома и поискать что либо ещё, вы наткнулись на гоблина, ваши действия?'
#------------------------------файт с зеленым лошком---------------------------------------
info_your_strike_txt = f'Ваша информация: {tab} -> {knight.name}\nУровень здоровья: {knight.hp}\nУровень брони: {knight.armor}\nСила удара: {knight.power}'
info_goblin_strike_txt = f'Поприветствуйте героя -> {goblin.name}\nУровень здоровья: {goblin.hp}\nУровень брони: {goblin.armor}\nСила удара: {goblin.power}'
goblin_strike_txt = '->УДАР!'

g_strike_txt = f'{info_your_strike_txt + tab + info_goblin_strike_txt + tab + wow_strike_txt}'

g_your_strike_txt = f'\n{knight.name} атакуете {goblin.name} используя почти сломанный железный меч'
g_second_your_strike_txt = f'\n{goblin.name} принял на себя, класс брони: {goblin.armor}, уровень здоровья: {goblin.hp}'

goblin_strike_txt = f'\n{goblin.name} атакует вас, используя копьё с наконечником из куска острого мрамора'
second_goblin_strike_txt = f'\n{knight.name} покачнулись, уровень брони: {knight.armor}, уровень здоровья: {knight.hp}'
#--------------------------------------после победы погнал в пещеру и начал самого себя закапывать в горечи и сострадании------------------------
g_win = '''Поздравляем! Вы жестко и беспощадно убили гоблина который встал на вашем пути, но что же делать дальше? Вы решили отправиться поискать чего-то интересного и 
наткулись на пещеру, ах да, мы забыли упомянуть что после победы над гоблином из него выпал ключ который вы подобрали и положили к себе в инвентарь, так вот, зайдя в пещеру вы обнаружили там 5 слаймов которые охраняли некий сундук'''
g_fight_slimes = '''После победы над безобидными слаймами которые вам даже ничего не сделали а просто охраняли сундук, вы заметили что для него нужен ключ, и к счастью ключ который 
вы получили от гоблина подошел, открыв большой сундук вы нашли там некую тяжеленную броню, а рядом была записка, на ВАШЕМ языке, предназнчаенная для кого-то из ВАШЕГО мира, так вот 
текст в записке гласил "Давным-давно, когда этот мир только появился тут ничего не было, только монстры и монстры, но затем появилась земля, а вместе с ней и земля в вашем мире, но 
у монстров не было правителя, они вели себя слишком хаотично, и затем, Аргалл, стал править, у него была своя личная броня выкованная из крыльев величественных пустых драконов(пустые не в том смысле что внутри, а в том что это типо такой вид), и броня это была 
очень тяжёлой, тёмной, спустя время Аргалла свергли, а его броня до сих пор блуждает в этом мире переходя от владельца к владельцу", и так, сопоставив дважды два вы поняли что вам капец как повезло и присвоили броню себе, у вас 
появилась теория что МОЖЕТ быть, чтобы вернуться домой надо одолеть НЫНЕШНЕГО лорда ордена страха(а.к.а. место в которым вы находитесь), но ввам нужна не только броня, но ещё и меч, вы решили на всякий случай найти гоблина, опять же беспощадно 
убить его разрушив всю его жизнь, вы обрекли его семью на вечную горечь от потери своего родственника, но вам плевать, ведь вы человек и вам нужно домой, вы использовали тело гоблина как камуфляж чтобы 
надеть его тело на себя и быть так сказать "своим" чтобы вас не трогали'''
find_village = '''Спустя время блужданий по этим тёмным землям вы обнаружили деревню гоблинов, изучая её вы смогли найти некую "торговую точку", а нашли вы её благодаря тому что следовали за вором который воровал дорогие украшения 
у мам отвлекая их не ребенка, затем он направился в эту так называемую торговую точку, а вы собственно за ним, исследую её вы смогли найти обмен на некий меч у какой-то гадалки, ну или же старухи 
осмотрев меч вы решили что он достаточно силён, и вам такой нужен, но чтобы его получить она сказала что вам нужно принести некий ключ который есть у другого гоблина, по её словам в одной пещере есть сундук на замке, а 
там вещи которые оставила её тетя ей, но ключ украл какой-то гоблин, сразу поняв что она блефует и говорит о сундуке в котором вы нашли броню, вы приняли заказ и сделали вид что отправились за ним, но так как 
уже наступил вечер вы отправились в гостиницу чтобы переночевать, но вы не могли заснуть.'''
fears = '''Почему я не могу заснуть? Никто не знает, но та ночь была самой ужасной в вашей жизни, почему же? Сейчас и разберем, вы пришли в гостиницу, сняли номер и легли спать, но вы не 
можете заснуть, вас одолевают ужасные мысли о содеянном, о всех тех кого вы убили и кому испортили жизнь напрочь, гоблины, которые молили о пощаде, а что если вы разрушили их семью? 
Подвергли родственников гоблинов вечной горечи? Вдруг кто-то подумает что это виноват ОН так как допустим он отправил гоблина прогуляться, а того убил некий маньяк, то есть вы, верно 
вы начали проявлять сострадание к монстрам, вы всё время вспоминаете как убивали их, гоблины, слаймы, сколько жизней вы погубили? Сколько семей разрушили? Сколько судеб вы испортили? Верно, никто не знает, 
но почему только сейчас это начало происходить? Почему вы начали об это думать? Правильно, это место давит на вас, вы здесь чужой, вы не должны быть здесь столько, сколько уже находитесь тут. 
Но вы уже уничтожаете это место изнутри, также как и себя, всё время вспоминая о зверских убийствах невиннный и ни в чём не повинных гоблинов, слаймов и так далее. Затем вы засыпаете, но это не идёт вам на пользу, 
в процессе сна вы вспоминаете это, как долго вы об этом думаете? Минута? Час? День? Для вас этот сон, уже превратился в кошмар, вы сами себя "объедаете" изнутри этими мыслями 
во время сна вы незаметно для себя становитесь на роль монстров которых вы убили, вы чувствуете это на себе, уничтожающая боль, пронизывает всё ваше тело, для вас вы находитесь в этом кошмаре уже месяц, и тут, в очередной раз думая об этом 
вы просыпаетесь.'''
sell = '''У вас смешанные мысли, вы ничего не понимаете, но прекрасно помните опыт который получили во время вашего кошмара, вы собрались и отправились в торговую точку. Но кошмары не уходят бесследно, вы дрожжите, еле как отдаётё ключ и получаете меч, и вот, вы уже на "последней точке" врзвращаться назад 
нельзя, вы уже почти в самом конце, вы идёте к тёмному лорду, начинается поединок, вы отрубаете ему ногу, у вас идёт ожесточённая битва, и вот, вы уже на финишной черте, но как вдруг, ваш разум снова посещают эти мысли, и вот, не заметив 
того как лорд кому-то свистнул, вашу голову отрубает его подчиненный со спины, вы мертвы. Игра окончена.'''


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
    cry == 'ended'

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
    return find_sword == 'start'

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

btn1.setText('Спрятаться под деревом от страха и рыдать')
btn2.setText('Убежать из леса и попытаться найти портал')
btn3.setText('В недоумении искать свою комнату')

order_of_fear()

if btn1.clicked:
    new_cry()

if btn2.clicked:
    new_portal()

if btn3.clicked:
    new_room()

first_stage = 'end'

if find_portal == 'ended':
    btn2.clicked.disconnect(new_portal)


if cry == 'ended':
    btn1.clicked.disconnect(new_cry)


if room == 'ended':
    btn3.clicked.disconnect(new_room)


second_stage = 'start'

btn1.setText('Использовать') # кнопки
btn2.setText('Защита') #
btn3.setText('Удар') #

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