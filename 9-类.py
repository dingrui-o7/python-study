# 类是一种抽象的数据类型，代表某种实体的抽象概念，描述了所有该类的对象共享的属性和行为，对象是类的实例。

class Car:
    def __init__(self, model, energy_capacity=100):
        """初始化类的属性"""
        self.model = model
        self.energy_capacity = energy_capacity

    def show_dashboard(self):
        print(f"Energy remain: {self.energy_capacity}")

    def drive(self, distance_km):
        # 修改类的属性
        self.energy_capacity -= distance_km // 5

    def recharge(self):
        # 修改类的属性
        self.energy_capacity = 100


class ElectricCar(Car):
    def __init__(self, model):
        """初始化子类的属性，子类继承了父类的方法和属性，
        我们可以调用父类的初始化方法来初始化父类的属性"""
        super().__init__(model)
        self.battery_status = 'safe'

    def check_battery_safe(self):
        print(f'Battery is {self.battery_status}!')


mycar = ElectricCar('Tesla-ModelX')
mycar.drive(50),mycar.show_dashboard()
mycar.check_battery_safe()
mycar.recharge(), mycar.show_dashboard()