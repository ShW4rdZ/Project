class Signal:
    """Signals

    Signals are meant to be used as a way to transfer events between multiple classes, such as item destroys or health gain
    
    """
    def __init__(self):
         self._handlers = []

    def connect(self, handler):
         self._handlers.append(handler)

    def fire(self, *args):
         for handler in self._handlers:
             handler(*args)
