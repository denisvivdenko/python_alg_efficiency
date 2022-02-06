import time

class Timer:
    class _Timer:
        def __init__(self) -> None:
            self.start_time = None
            self.is_measuring = False

        def start_measuring(self) -> None:
            if self.is_measuring:
                return

            self.start_time = time.perf_counter()
            self.is_measuring = True

        def stop_measuring(self) -> float:
            if not self.is_measuring:
                raise Exception("Timer: measuring have not been started.")
            
            self.is_measuring = False
            return time.perf_counter() - self.start_time

    instance = None

    def __new__(cls) -> None:
        if not Timer.instance:
            Timer.instance = Timer._Timer()

        return Timer.instance
    
    def __getattr__(self, name) -> None:
        return getattr(Timer.instance, name)

    def __setattr__(self, name) -> None:
        return setattr(Timer.instance, name)


if __name__ == "__main__":
    timer = Timer()
    timer.start_measuring()
    for i in range(10000):
        pass
    print(timer.stop_measuring())
