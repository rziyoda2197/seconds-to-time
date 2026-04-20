def sekundni_saatga(qaysi_sekund):
    soat = qaysi_sekund // 3600
    daqiqa = (qaysi_sekund % 3600) // 60
    sekund = qaysi_sekund % 60
    return soat, daqiqa, sekund

sekund = int(input("Sekundni kiriting: "))
soat, daqiqa, sekund = sekundni_saatga(sekund)
print(f"{soat}:{daqiqa}:{sekund}")
