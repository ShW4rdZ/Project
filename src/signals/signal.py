class Signal:
    """Signals

    Signals are meant to be used as a way to transfer events between multiple classes, such as item destroys or health gain
    
    """
    def __init__(self):
         self._handlers = []

    def connect(self, handler):
        """Links a handler (function) to the signal
        Functions linked to a signal will be executed when Signal().fire() is called
        """
        self._handlers.append(handler)

    def fire(self, *args):
        """Triggers the signal's associated handlers"""
        for handler in self._handlers:
            handler(*args)
