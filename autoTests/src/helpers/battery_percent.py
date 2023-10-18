import psutil

battery = psutil.sensors_battery()
percent = int(battery.percent)
print(f'percentege of battery is:{percent}%')

cpu = psutil.cpu_freq()
frequency_of_cpu = int(cpu.max)
print(f'freq of cpu is: {frequency_of_cpu}')