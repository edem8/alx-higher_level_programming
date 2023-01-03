#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("Wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("dividion by 0")
            result.append(0)
        except IndexError:
            print("divison by 0")
            result.append(0)
        finally:
            pass
    return result
