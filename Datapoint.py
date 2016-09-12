#!/usr/bin/env python3

import re
from datetime import date
from datetime import datetime

class Datapoint:
    def __init__(self, recipient="", s_date=datetime.today(), value=0.0, comment=""):
        self.__Recipient = recipient
        self.__Date = datetime.date(s_date)
        self.__Value = value
        self.__Comment = comment

    def get_recipient(self):
        return self.__Recipient

    def set_recipient(self, recipient):
        self.__Recipient = recipient
    
    def get_date(self):
        return self.__Date.strftime("%d.%m.%Y")

    def set_date(self, s_date):
        try:
            regex = re.compile(r'\d{2}\.\d{2}\.(\d{4}|\d{2})')
            m = regex.match(s_date)
            if m:
                self.__Date = datetime.strptime(s_date, "%d.%m.%Y").date()
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
            self.__Comment = comment.rstrip()

    Recipient = property(get_recipient, set_recipient)
    Date = property(get_date, set_date)
    Value = property(get_value, set_value)
    Comment = property(get_comment, set_comment)

    def __str__(self):
        return "{recipient};{date};{value};{comment}".format(recipient=self.__Recipient, date=self.__Date.strftime("%d.%m.%Y"), value=str(self.__Value), comment=self.__Comment)

    def parse(self, line):
        line_split = line.split(";")
        if len(line_split) == 4:
            self.set_recipient(line_split[0])
            self.set_date(line_split[1])
            self.set_value(line_split[2])
            self.set_comment(line_split[3])
        else:
            raise IndexError