# class TubIterator:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.current <= self.end:
#             if self.tub_sonlar(self.current):
#                 tublar = self.current
#                 self.current += 1
#                 return tublar
#             self.current += 1
#         raise StopIteration
#
#     def tub_sonlar(self, number):
#         if number <= 1:
#             return False
#         for i in range(2, int(number ** 0.5) + 1):
#             if number % i == 0:
#                 return False
#         return True
#
#
# tub_iter = TubIterator(1, 77)
# with open("tub_numbers_iterators.txt", "w") as file:
#     for number in tub_iter:
#         file.write(f"{number}\n")
#         print(number)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Ikkinchi versiya<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# class TubIterator:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.current <= self.end:
#             if self.tub_son(self.current):
#                 tub = self.current
#                 self.current += 1
#                 return tub
#             self.current += 1
#         raise StopIteration
#
#     def tub_son(self, son):
#         if son <= 1:
#             return False
#         if son <= 3:
#             return True
#         if son % 2 == 0 or son % 3 == 0:
#             return False
#         i = 5
#         while i * i <= son:
#             if son % i == 0 or son % (i + 2) == 0:
#                 return False
#             i += 6
#         return True


# prime_iter = TubIterator(1, 85)
# with open("tub_numbers_iterator.txt", "w") as file:
#     for number in prime_iter:
#         file.write(f"{number}\n")
#         print(number)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Uchinchi versiya<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# class TubIterator:
#     def __init__(self, end):
#         self.end = end
#         self.sive = [True] * (end + 1)
#         self.sive[0] = self.sive[1] = False
#         for start in range(2, int(end**0.5) + 1):
#             if self.sive[start]:
#                 for multpil in range(start*start, end + 1, start):
#                     self.sive[multpil] = False
#         self.current = 2
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.current <= self.end:
#             if self.sive[self.current]:
#                 tub = self.current
#                 self.current += 1
#                 return tub
#             self.current += 1
#         raise StopIteration
#
#
# tub_iter = TubIterator(47)
# with open("tub_numbers__iterator.txt", "w") as file:
#     for number in tub_iter:
#         file.write(f"{number}\n")
#         print(number)
