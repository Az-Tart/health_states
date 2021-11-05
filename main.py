#ПО мониторинга состояния здоровья
import os
import sqlite3
from   datetime import datetime

#Создание переменных даты и времени формата DDMMYYYYHHmm
current_year     = str(datetime.now().year)
current_month    = str(datetime.now().month)
current_day      = str(datetime.now().day)
current_hour     = str(datetime.now().hour)
current_minute   = str(datetime.now().minute)
if int(current_day)    <= 9:
	current_day    = str(0) + current_day 
if int(current_hour)   <= 9:
	current_hour   = str(0) + str(current_hour)
if int(current_minute) <= 9:
	current_minute = str(0) + str(current_minute)

#Создание переменных
ans_dict     = {}
result_percs = {}

current_date = str(current_day+current_month+current_year) 
current_time = str(current_hour + current_minute)

#Создание базы данных
hs_db  = sqlite3.connect('shdb.db')
cursor = hs_db.cursor()
cursor.execute(f'''CREATE TABLE IF NOT EXISTS health_states (
	date TEXT, 
	value TEXT,
	result TEXT 
)''')

os.system("cls")

q_list = [
	"0. Самочувствие хорошее 3-4|плохое 1-2"     , 
	"1. Чувствую себя сильным 3-4 |слабым 1-2"   , 
	"2. Пассивный 1-2|активный 3-4"              , 
	"3. Малоподвижный 1-2|подвижный 3-4"         , 
	"4. Весёлый 3-4|грустный 1-2"                , 
	"5. Настроение хорошее 3-4|плохое 1-2"       , 
	"6. Работоспособный 3-4|разбитый 1-2"        , 
	"7. Полный сил 3-4|обезсиленный 1-2"         ,
	"8. Медлительный 1-2|быстрый 3-4"            , 
	"9. Бездеятельный 1-2|деятельный 3-4"        , 
	"10. Счастливый 3-4|несчастный 1-2"          , 
	"11. Жизнерадостный 3-4|мрачный 1-2"         , 
	"12. Напряжённый 1-2|расслабленный 3-4"      , 
	"13. Здоровый 3-4|больной 1-2"               , 
	"14. Безучастный 1-2|увлечённый 3-4"         , 
	"15. Равнодушный 1-2|заинтересованный 3-4"   ,
	"16. Восторженный 3-4|унылый 1-2"            , 
	"17. Радостный 3-4|печальный 1-2"            , 
	"18. Отдохнувший 3-4|усталый 1-2"            , 
	"19. Свежий 3-4|изнуренный 1-2"              , 
	"20. Сонливый 1-2|возбуждённый 3-4"          , 
	"21. Желание отдохнуть 1-2|работать 3-4"     , 
	"22. Спокойный 3-4|взволнованный 1-2"        , 
	"23. Оптимистичный 3-4|пессимистичный 1-2"   , 
	"24. Выносливый 3-4|утомляемый 1-2"          ,
	"25. Бодрый 3-4|вялый 1-2"                   , 
	"26. Соображать трудно 1-2|легко 3-4"        , 
	"27. Рассеяный 1-2|внимательный 3-4"         , 
	"28. Полный надежд 3-4|разочарованный 1-2"   , 
	"29. Довольный 3-4|недовольный 1-2"          ,
	"30. Идейный 3-4|безыдейный 1-2"             ,
	"31. Добрый 3-4|злой 1-2"                    ,
	"32. Аппетит хороший 3-4|нет аппетита 1-2"
]


def qestions(ans_dict):
	'''
	Список вопросов
	'''
	od = 0
	ans_dict = ans_dict 
	for i in q_list: 
		os.system("cls")
		print("Состояние здоровья на "+current_date +"-"+ current_time)
		print("Ответьте на вопросы цифрой от 1 до 4")
		print("Предыдущие ответы: "+str(ans_dict))
		user_input = input(i+": ")
		ans_dict.update({od:user_input})
		od+=1

qestions(ans_dict)

def print_results(result_percs):
	'''
	Вывод результатов
	'''
	result_percs = result_percs
	os.system("cls")
	t = 0
	print("Полученные ответы")
	for a in q_list:
		i = ans_dict[t]
		print(f'''\t{a}: {i}''')
		t+=1

	feeling = int(ans_dict[0]) + int(ans_dict[1]) + int(ans_dict[6]) + int(ans_dict[7]) + int(ans_dict[12]) + int(ans_dict[13]) + int(ans_dict[18]) + int(ans_dict[19]) + int(ans_dict[24]) + int(ans_dict[25]) + int(ans_dict[32]) 
	activity = int(ans_dict[2]) + int(ans_dict[3]) + int(ans_dict[8]) + int(ans_dict[9]) + int(ans_dict[14]) + int(ans_dict[15]) + int(ans_dict[20]) + int(ans_dict[21]) + int(ans_dict[26]) + int(ans_dict[27]) + int(ans_dict[30])  
	mood = int(ans_dict[4]) + int(ans_dict[5]) + int(ans_dict[10]) + int(ans_dict[11]) + int(ans_dict[16]) + int(ans_dict[17]) + int(ans_dict[22]) + int(ans_dict[23]) + int(ans_dict[28]) + int(ans_dict[29]) + int(ans_dict[31])

	percent_feeling  = feeling/(44/100)
	percent_activity = activity/(44/100)
	percent_mood     = mood/(44/100)

	result_percs     = {'feeling':feeling, 'activity':activity, 'mood':mood}

	print("\nОбщий итог состояния"+"\n\tОбщее самочувствие: "+f"\t{str(feeling)}/44 - {int(percent_feeling)}%" + "\n\tАктивность: " + f"\t\t{str(activity)}/44 - {int(percent_activity)}%" + "\n\tНастроение: " + f"\t\t{str(mood)}/44 - {int(mood)}%")


print_results(result_percs)


def write_to_db():
	'''
	Запись результата в базу данных 
	'''
	user_input_0 = input("\nСохранить результаты (y/n)?: ")
	if user_input_0 == "y":
		sql = '''INSERT INTO health_states (date, value, result) VALUES (?, ?, ?)'''
		val = (str(current_date+current_time), str(otv_dict), str(result_percs))
		cursor.execute(sql, val)
		hs_db.commit()
		os.system("cls")
		print(f"Результаты на {str(current_date) + str(current_time)} сохранены.")
		user_input_1 = input("Пройти проверку заново (y/n)?: ")
		if user_input_1 == "y":
			qestions(ans_dict)
			print_results(result_percs)
			write_to_db()
	else:
		os.system("cls")
		print("Сохранение результатов отменено.")
		user_input_2 = input("Пройти проверку заново (y/n)?: ")
		if user_input_2 == "y":
			qestions(ans_dict)
			print_results(result_percs)
			write_to_db()

write_to_db()			
