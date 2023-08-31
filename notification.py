from win10toast import ToastNotifier
import datetime

data = datetime.datetime.now()
data = str(data)
toast = ToastNotifier()
toast.show_toast("Date-Time Update", data, duration=5)
