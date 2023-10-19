
import psutil

battery = psutil.sensors_battery()
percent = str(battery.percent)
plugged = battery.power_plugged
plugged = 'Plugged in' if plugged else 'Unpluged'
print(percent + '%' + ' | ' + plugged )

names = ['Alex',
         'Mishel',
         'Anastasia',
         'Adam']



cars  = [
    'Ferrary',
    'Mazda',
    'Toyota',
    'Pegeot',
    'Tesla'

]


streets = ['Begin',
           'Rabin',
           'Weizman'
           ]



companies = ['Apple',
             'Google',
             'X',
             'Matrix',
             '']

#Count length of names
# length = [len(name) for name in names]


#Count length and link
lenghStreet = {name:len(name) for name in streets}






length = {name:len(name) for name in names}

lengthCars = {name:len(name) for name in cars}

#

lengthCompamies ={name:len(name) for name in companies}



print (length)
print (lengthCars)
print(lenghStreet)
print(lengthCompamies)
