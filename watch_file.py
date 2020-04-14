from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from config import DOWNLOADS_PATH


class Handler(FileSystemEventHandler):
    def __init__(self, observer):
        self.observer = observer

    def on_moved(self, event):
        print(event.src_path)
        self.observer.stop()

    def on_created(self, event):
        print(event.src_path)
        self.observer.stop()


observe = Observer()
handler = Handler(observe)
observe.schedule(handler, DOWNLOADS_PATH, False)
observe.start()
observe.run()
observe.join()
