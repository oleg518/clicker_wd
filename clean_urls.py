import os.path
import sys
import time
from datetime import datetime

start_time = time.time()
now = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")

for i in range(5):
	print()

orig_file='urls.txt'
cleaned='urls_cleaned.txt'

print('Доброго времени суток!')
print('Сейчас',now)
print("Эта программа переносит строки из файла ",orig_file,' в файл ',cleaned,' без повторов.')
print('by Oleg Petrov')
print()
print("===	Начало исполнения	===")

if not os.path.exists(orig_file):	# Проверка существования файла
	print('Файл ',orig_file,' не найден. ')
	print('Он должен быть в той же папке, что и программный файл.')
	input('Press ENTER to exit   ')
	sys.exit()

rfile=open(orig_file,'r')  # исходный файл

lines1=rfile.readlines()
text1=rfile.read()


open(cleaned, 'w').close()	# создание/очистка выходного файла

print(" --- читаем исходный файл по строкам (начало) ---")

n_obrab=0
n_repeats=0

i=0
for line_i in lines1:
	i+=1
	print('№ ',i,':  ',line_i)
	repeat=0
	for line_j in lines1:
		if line_i==line_j:
			repeat+=1
	if repeat==1:
		print('... повторов нет, записываем в выходной файл.')
		with open(cleaned,'a') as wfile:
			wfile.write(line_i)
	if repeat>1:
		print('... эта строка имеет повторы, проверим, записывали ли ее в выходной файл ранее..')
		with open(cleaned,'r') as rfile_i:
			print('    ... окрываем выходной файл на чтение ...')
			text_i=rfile_i.read()
			if text_i.count(line_i)==0:
				with open(cleaned,'a') as wfile:
					print('    ... в выходном файле такого нет, на первый раз запишем.')
					wfile.write(line_i)
			else:
				print('    ... такое уже в выходном файле, не будем записывать.')
				n_repeats+=1
if i==0:
	print('Файл пуст!')
print(" --- читаем файл по строкам (конец) ---")
print()
print('Готово! Выполнено за ',round((time.time() - start_time),3),' секунд.')

n_obrab=i

rfile.close()
#wfile.close()


for i in range(3):
	print()

if n_obrab==0:
	n_obrab=1


proc_repeats=100*(n_repeats/n_obrab)
if proc_repeats<3:
	proc_repeats=round(proc_repeats,1)
else:
	n_round=0
	proc_repeats=round(proc_repeats)

print('  ===  Статистика  ===  ')
print()
print('  Обработано строк: ',n_obrab)
print('   Из них повторов: ',n_repeats)
print('        % повторов: ',proc_repeats,'%')
print('Оригинальных строк: ',n_obrab-n_repeats)
print()
input('Press ENTER to exit...   ')


#==================================
sys.exit()	# Ниже - неактуальное
