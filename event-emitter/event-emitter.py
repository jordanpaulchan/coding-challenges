class EventEmitter:
    def __init__(self):
        self.events = {}

    def subscribe(self, event, callback):
        if event in self.events:
            self.events[event].append(callback)
        else:
            self.events[event] = [callback]

    def unsubscribe(self, event, callback=None):
        if event not in self.events:
            return

        if not callback:
            self.events.pop(event, None)
        else:
            self.events[event] = list(
                filter(lambda c: c != callback, self.events[event]))

    def emit(self, event, *args):
        if event not in self.events:
            return

        for callback in self.events[event]:
            callback(*args)


def print_callback(*args):
    for arg in args:
        print(arg)


eventEmitter = EventEmitter()
eventEmitter.subscribe("print", print_callback)
eventEmitter.emit("print", "Hello World")
eventEmitter.subscribe("print", print_callback)
eventEmitter.emit("print", "Test")
eventEmitter.unsubscribe("print")
eventEmitter.emit("print", "Don't print")
eventEmitter.subscribe("print", print_callback)
eventEmitter.emit("print", "Print")
eventEmitter.unsubscribe("print", print_callback)
eventEmitter.emit("print", "Don't print")
