class NotInBoundsError(Exception):
    def __str__(self):
        return "There is an error!"


def check_integer(num):
    if 45>num >67:
        return num
    else:
        raise NotInBoundsError

def error_handling(num):
    try:
        check_integer(num)
    except NotInBoundsError as err:
        print (err)


error_handling(5)


# Second, create a new function error_handling(num).
# It should call the check_integer(num) function and use the try-except block to catch
# the NotInBoundsError.
# If there is an error, print its error message.
# If there are no errors, print the result of the check_integer(num) function.
