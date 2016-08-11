from datetime import datetime

hey = "HelloWorld!"

print hey

tmef = datetime.now()

print '%s/%s/%s %s:%s' % (tmef.month, tmef.day, tmef.year, tmef.hour, tmef.minute)
