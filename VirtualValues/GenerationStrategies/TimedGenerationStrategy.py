import threading
from VirtualValues.GenerationStrategy import GenerationStrategy
from Utilities import every


class TimedGenerationStrategy(GenerationStrategy):
    cycle_in_seconds = 5
    wait_thread = None
    has_cycle_completed = False

    def __init__(self, cycle_in_seconds):
        self.cycle_in_seconds = cycle_in_seconds
        self.wait_thread = threading.Thread(target=lambda: every(self.cycle_in_seconds, self.on_wake_up))

    def start(self):
        self.wait_thread.start()

    def on_wake_up(self):
        self.has_cycle_completed = True

    def should_generate(self):
        if self.has_cycle_completed:
            self.has_cycle_completed = False
            return True
        return False
