#%%
import re

def is_phone_number(text):
	if len(text) != 12:
		return False
	for i in range(0,3):
		if not text[i].isdecimal():
			return False
	
	if text[3] != '-':
		return False
	
	for i in range(4,7):
		if not text[i].isdecimal():
			return False
	
	if text[7] != '-':
		return False
	
	for i in range(8,12):
		if not text[i].isdecimal():
			return False
	return True

message = '明日415-555-1011に電話してください。オフィスは415-555-9999です。'
for i in range(len(message)):
	chunk = message[i:i+12]
	if is_phone_number(chunk):
		print('電話番号が見つかりました:',chunk)
print('完了')

phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search('私の電話番号は415-555-1151です')
if mo != None:
	print('電話番号：', mo.group())
	print(mo.group(1))
	print(mo.group(2))
	print(mo.group(0))
	print(mo.group())
	print(mo.groups())
	area_code, main_number = mo.groups()
	print(area_code)
	print(main_number)

phone_num_regex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search('私の電話番号(415) 555-4141')
if mo != None:
	print(mo.group(1))
	print(mo.group(2))

hero_regex = re.compile(r'Batman|Tina Fey')
mo1 = hero_regex.search('Batman and Tina Fey.')
print(mo1.group())

mo2 = hero_regex.search('Tina Fey and Batman.')
print(mo2.group())

bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))
print("\r")
bat_regex = re.compile(r'Bat(wo)?man')
mo1 = bat_regex.search('The Adventures of Batman')
print(mo1.group())
mo2 = bat_regex.search('The Adventures of Batwoman')
print(mo2.group())
print("\r")
phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phone_regex.search('私の電話番号は415-444-4242です')
print(mo1.group())
mo2 = phone_regex.search('私の電話番号は555-4141')
print(mo2.group())
print("\r")
bat_regex = re.compile(r'Bat(wo)*man')
mo1 = bat_regex.search('The Adventures of Batman')
print(mo1.group())
mo2 = bat_regex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = bat_regex.search('The Adventures of Batwowowoman')
print(mo3.group())
print("\r")
bat_regex = re.compile(r'Bat(wo)+man')
mo1 = bat_regex.search('The Adventures of Batman')
if mo1 != None:
	print(mo1.group())
mo2 = bat_regex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = bat_regex.search('The Adventures of Batwowowoman')
print(mo3.group())

print("\r")
ha_regex = re.compile(r'(Ha){3,5}')
mo1 = ha_regex.search('HaHaHaHa')
print(mo1.group())

mo2 = ha_regex.search('Ha')
print(mo2 == None)

#%%
