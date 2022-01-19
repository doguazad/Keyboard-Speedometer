import time
import datetime
print("3 Saniye Sonra Yazmaya Başlayın")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("Başla!")
time.sleep(0.2)
before = datetime.datetime.now()
text=input("Yaz:")
after = datetime.datetime.now()
speed = after - before
seconds = round(speed.total_seconds(),2)
letter_per_second = round(len(text) / seconds,1)
print("{} Saniyede Yazdın".format(seconds))
print("Sniyede {} Harf Yazdın ".format(letter_per_second))