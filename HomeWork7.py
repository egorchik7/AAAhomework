import sys
import datetime


def my_write(string_text):
    original_write('[{}]:'.format(datetime.datetime.now()) + string_text)


def timed_output(function):
    def wrapper(*args, **kwargs):
        original_write = sys.stdout.write

        def my_write(string_text):
            original_write('[{}]:'.format(datetime.datetime.now()) + string_text)
        sys.stdout.write = my_write
        function(*args, **kwargs)
        sys.stdout.write = original_write
    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


if __name__ == "__main__":
    original_write = sys.stdout.write
    sys.stdout.write = my_write
    print('1, 2, 3')
    sys.stdout.write = original_write
    print('1,2,3')

    print_greeting("Egor")
