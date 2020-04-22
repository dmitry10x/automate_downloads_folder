from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

from pathlib import Path

class MyHandler(FileSystemEventHandler):
    @staticmethod
    def get_folder_path(filename):
        path_extentions = {'audio':{'extentions':['.mp3','.wma','.aac'],
                                    'folder_path':'C:/Users/Дмитрий/Downloads/audio'},
                           'video':{'extentions':['.webm','mpg','mp2','.mpeg','.ogg','.mp4','.wmv','.avi','.avchd','.flv'],
                                    'folder_path':'C:/Users/Дмитрий/Downloads/video'},
                           'picture':{'extentions':['.psd','.tiff','.bmp','.jpeg','.jpg','.jpeg2000','.gif','.png'],
                                    'folder_path':'C:/Users/Дмитрий/Downloads/picture'},
                           'text':{'extentions':['.txt','.docx'],
                                    'folder_path':'C:/Users/Дмитрий/Downloads/text'},
                           'prezentation':{'extentions':['.pdf','.pptx'],
                                    'folder_path':'C:/Users/Дмитрий/Downloads/prezentation'},
                           'book':{'extentions':['.epub','.fb2'],
                                    'folder_path':'C:/Users/Дмитрий/Downloads/book'},
                           'excel':{'extentions':['.xlsx'],
                                    'folder_path':'C:/Users/Дмитрий/Downloads/excel'}}

        file_extention = (Path(filename).suffix).lower()
        folder_path = 'C:/Users/Дмитрий/Downloads/other'
        for file_type in path_extentions.keys():
            for extention in path_extentions[file_type]['extentions']:
                if file_extention == extention:
                    folder_path = path_extentions[file_type]['folder_path']
                    break
        return folder_path

    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            folders_to_pass = ['audio','excel','picture','other','prezentation','text','video','Telegram Desktop']
            if filename in folders_to_pass:
                pass
            else:
                folder_destination = MyHandler.get_folder_path(filename)
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/" + filename
                try:
                    os.rename(src, new_destination)
                except Exception as e:
                    print(e)


folder_to_track = 'C:/Users/Дмитрий/Downloads'

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
