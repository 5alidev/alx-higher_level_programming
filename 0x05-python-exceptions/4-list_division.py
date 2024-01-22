#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """divides element by element 2 lists."""
    i = 0
    div = []
    result = 0
    for i in range(0, list_length):
        try:
            n1 = my_list_1[i]
            n2 = my_list_2[i]
            result = n1 / n2
        except TypeError:
            print("wrong type")
            reslut = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        except Exception:
            result = 0
        finally:
            div.append(result)
    return div
