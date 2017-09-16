from shopybot.settings import HUEY

@HUEY.task()
def test():
    print('test huey')