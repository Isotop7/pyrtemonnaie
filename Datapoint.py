import re
from datetime import date

class Datapoint:
    def __init__(self, recipient="", s_date="01.01.1970", value=0.0, comment=""):
        self.__Recipient = recipient
        self.__Date = s_date
        self.__Value = value
        self.__Comment = comment

    def get_recipient(self):
        return self.__Recipient

    def set_recipient(self, recipient):
        self.__Recipient = recipient
    
    def get_date(self):
        return self.__Date

    def set_date(self, s_date):
        try:
            regex = re.compile(r'\d{1,2}\.\d{1,2}\.\d{4}')
            m = regex.match(s_date)
            if m:
                date_split = s_date.split(".")
                self.__Date = date(date_split[0], date_split[1], date_split[2])
            else:
                raise ValueError
        except ValueError and TypeError:
            now = date.today()
            self.__Date = now.strftime("%d.%m.%Y")

    def get_value(self):
        return self.__Value

    def set_value(self, value):
        if float(value) < 0:
            raise ValueError
        else:
            self.__Value = float(value)

    def get_comment(self):
        return self.__Comment

    def set_comment(self, comment):
        if ";" in comment:
            raise ValueError
        else:
            self.__Comment = comment

    def to_String(self):
        return "{recipient};{date};{value};{comment}".format(recipient=self.__Recipient, date=self.__Date, value=str(self.__Value), comment=self.__Comment)

    def parse(self, line):
        line_split = line.split(";")
        if len(line_split) == 4:
            self.set_recipient(line_split[0])
            self.set_date(line_split[1])
            self.set_value(line_split[2])
            self.set_comment(line_split[3])
        else:
            raise IndexError