#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    l = []
    for w in range(list_length):
        try:
            result = my_list_1[w] / my_list_2[w]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            l.append(result)

    return (l)
