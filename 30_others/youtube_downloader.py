from pytube import YouTube
from pytube.cli import on_progress

link = input("Линк : ")

yt = YouTube(link, on_progress_callback = on_progress)

print("Заглавие = ", yt.title)
print("Тегли се...")

ys = yt.streams.get_highest_resolution()

ys.download('E:\Programing\SoftUni\Python Web Framework - юли 2021')

