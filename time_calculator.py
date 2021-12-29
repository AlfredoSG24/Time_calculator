def add_time(start, duration, startDay = None):
  
 #Lista de dias validos
  validDays = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
  if startDay:
    startDayIndex = validDays.index(startDay.lower())

  # tiempo AM o PM
  curTimePM = (start.split(' ')[-1] == 'PM')

  # obtener tiempo y minutos
  curHours, curMinutes = start.split(':')
  curMinutes = curMinutes.split(' ')[0]

  # Integracion de tiempo  minutos y hora
  curHours = int(curHours)
  curMinutes = int(curMinutes)
  if curTimePM:
    curHours += 12

  # parseo de minutos a hora 
  addHours, addMinutes = duration.split(':')
  addHours = int(addHours)
  addMinutes = int(addMinutes)

  # añadir horas
  newHours = curHours
  newMinutes = curMinutes + addMinutes
  newHours += (newMinutes // 60)
  newMinutes %= 60

  # agregar 
  newHours += addHours
  daydifference = newHours // 24
  newHours %= 24

  # calcular si es durante dia o tarde
  newAMPM = 'AM'
  if newHours // 12 == 1:
    newAMPM = 'PM'

  # cambiar 12 horas de regreso
  newHours %= 12
  if newHours == 0:
    newHours = 12
  
  # figure out how many days have passed since our initial time
  daydiffstring = ""
  if daydifference == 1:
    daydiffstring = " (next day)"
  if daydifference > 1:
    daydiffstring = " (%d days later)" % daydifference

  # calcula dia de inicio y restante
  newDay = ""
  if startDay:
    newDayIndex = (startDayIndex + daydifference) % 7
    newDay = ", " + validDays[newDayIndex].capitalize()

  # calculo de tiempo final
  new_time = "%d:%02d %s%s%s" % (newHours, newMinutes, newAMPM, newDay, daydiffstring)

  return new_time