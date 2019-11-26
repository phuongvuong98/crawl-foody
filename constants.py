import enum

class Pages(enum.IntEnum):
   NUMBER_PER_PAGE = 10

class Errors(enum.Flag):
   ERROR_NONE = "Error: all fields is not completed"
   ERROR_EXIST = "Error: this fields is exist"