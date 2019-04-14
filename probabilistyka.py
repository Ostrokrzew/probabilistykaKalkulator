import statistics

userInput = input("Wpisz liczby po przecinku:\n")
numbs = userInput.split(',')
numbs.sort()
numbList = list()
for n in numbs:
	n = float(n)
	numbList.append(n)
numbList.sort()
print('\n',numbList,'\n',sep='')

def srednia(numbList):
	i = len(numbList)
	m = 0
	for n in numbList:
		m += n
	return m/i

def mediana(numbList):
	return statistics.median(numbList)

def wariancja(numbList):
	return statistics.pvariance(numbList)

def odchylenie(numbList):
	return statistics.pstdev(numbList)

def dominanta(numbList):
	try:
		return statistics.mode(numbList)
	except statistics.StatisticsError:
		return 'nie ma'
		
def sdo3(numbList):
	return statistics.pstdev(numbList) * statistics.pvariance(numbList)

def sdo4(numbList):
	return statistics.pvariance(numbList) * statistics.pvariance(numbList)

def trzeciM(numbList):
	sr = srednia(numbList)
	i = len(numbList)
	m = 0
	for n in numbList:
		m += (n - sr) ** 3
	return m/i

def czwartyM(numbList):
	sr = srednia(numbList)
	i = len(numbList)
	m = 0
	for n in numbList:
		m += (n - sr) ** 4
	return m/i

def asymetria(numbList):
	m3 = trzeciM(numbList)
	s3 = sdo3(numbList)
	return m3/s3

def wspolZmien(numbList):
	s = odchylenie(numbList)
	sr = srednia(numbList)
	return 100 * (s/sr)

def rozstep(numbList):
	xMax = max(numbList)
	xMin = min(numbList)
	return xMax-xMin

def kurtoza(numbList):
	m4 = czwartyM(numbList)
	s4 = sdo4(numbList)
	return (m4/s4)-3

def skosnosc(numbList):
	de = dominanta(numbList)
	sr = srednia(numbList)
	s = odchylenie(numbList)
	if (de != 'nie ma'):
		return (sr-de)/s
	else:
		return 'nie ma'

if __name__ == '__main__':
	print('Średnia: x_średnia',srednia(numbList))
	print('Mediana: me =',mediana(numbList))
	print('Wariancja: s^2 =',wariancja(numbList))
	print('Odchylenie: s =',odchylenie(numbList))
	print('Dominanta: de =',dominanta(numbList))
	print('Współczynnik zmienności: V =',wspolZmien(numbList),'%')
	print('Rozstęp: R =',rozstep(numbList))
	print('s^3:',sdo3(numbList))
	print('s^4',sdo4(numbList))
	print('Trzeci moment: M3 =',trzeciM(numbList))
	print('Czwarty moment: M4 =',czwartyM(numbList))
	print('Współczynnik asymetrii: A =',asymetria(numbList))
	print('Kurtoza: k =',kurtoza(numbList))
	print('Współczynnik skośności: a =',skosnosc(numbList))
