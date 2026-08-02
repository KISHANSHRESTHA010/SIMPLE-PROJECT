class car:
    def __init__(self,brand):
        self.brand=brand
        self.is_running=False

    def start(self):
        if not self.is_running:
            self.is_running=True
            print(f"{self.brand} has started")
        
        else:
            print(f"{self.brand} is already running")

    def stop(self):
        if self.is_running:
            self.is_runnin=False
            print(f"{self.brand} has stopped")
        else:
            print(f"{self.brand} is stopped already")

car1=car("Lamborgini aventador")
car1.start()
car1.stop()

