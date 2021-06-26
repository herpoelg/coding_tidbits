from functools import wraps


#decorator with: wrapper function which takes an argument
def pimp_vehicle_with_something(pimping):
    def pimp_vehicle(func):
        @wraps(func)
        def wrapper(car):
            return func(car) + '\n' + pimping
        return wrapper
    return pimp_vehicle

@pimp_vehicle_with_something('golden ashtray') #syntactic sugar for decorators
@pimp_vehicle_with_something('dark spoiler')
@pimp_vehicle_with_something('chrome blue')
def get_car(title):
    """
    A function that takes and returns a string
    """
    return title

print(get_car('Bmw X1'))
print('\n @wraps hepls to keep the functions metadata:')
print(get_car.__name__)
print(get_car.__doc__)
