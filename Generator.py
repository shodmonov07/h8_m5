# def tub_generator(start, end):
#     current = start
#     while current <= end:
#         if tub_son(current):
#             yield current
#         current += 1
#
#
# def tub_son(son):
#     if son <= 1:
#         return False
#     for i in range(2, int(son**0.5) + 1):
#         if son % i == 0:
#             return False
#     return True
#
#
# gen = tub_generator(1, 56)
# with open("tub_numbers_generator.txt", "w") as file:
#     for number in gen:
#         file.write(f"{number}\n")
#         print(number)


# # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Ikkinchi versiya>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# def tub_generator_2(start, end):
#     current = start
#     while current <= end:
#         if tub_sonlar_2(current):
#             yield current
#         current += 1
#
#
# def tub_sonlar_2(num):
#     if num <= 1:
#         return False
#     if num <= 3:
#         return True
#     if num % 2 == 0 or num % 3 == 0:
#         return False
#     i = 5
#     while i * i <= num:
#         if num % i == 0 or num % (i + 2) == 0:
#             return False
#         i += 6
#     return True
#
#
# gen = tub_generator_2(1, 33)
# with open("tub_numbers__generator.txt", "w") as file:
#     for number in gen:
#         file.write(f"{number}\n")
#         print(number)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Uchinchi versiya<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# def tub_generator_3(end):
#     sive = [True] * (end + 1)
#     sive[0] = sive[1] = False
#     for start in range(2, int(end**0.5) + 1):
#         if sive[start]:
#             for multiple in range(start*start, end + 1, start):
#                 sive[multiple] = False
#     for son in range(2, end + 1):
#         if sive[son]:
#             yield son
#
#
# gen = tub_generator_3(75)
# with open("tub_numbers_generator_3.txt", "w") as file:
#     for numbers in gen:
#         file.write(f"{numbers}\n")
#         print(numbers)
