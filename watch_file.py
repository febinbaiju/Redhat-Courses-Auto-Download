from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from config import DOWNLOADS_PATH
import os


class Handler(FileSystemEventHandler):
    def __init__(self, observer, filename):
        self.observer = observer
        self.filename = filename

    def on_created(self, event):
        filepath = str(event.src_path)
        thepath, ext = os.path.splitext(filepath)
        if ext != ".crdownload":
            print("Found the target")
            newpath = filepath.replace(os.path.basename(filepath), "")+"/"+self.filename+".mp4"
            os.rename(filepath, newpath)
            self.observer.stop()


def watch_completion(_filename):
    observe = Observer()
    handler = Handler(observe, _filename)
    observe.schedule(handler, DOWNLOADS_PATH, False)
    observe.start()
    observe.run()
    observe.join()
