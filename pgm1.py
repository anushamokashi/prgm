import webbrowser
import time

total_breaks = 3
break_count = 0

print("this pgm started on"+time.ctime())
while(break_count < total_breaks):
	webbrowser.open("https://www.youtube.com/watch?v=ubwJMYwc7rs")
	time.sleep(10)
	break_count = break_count + 1	
