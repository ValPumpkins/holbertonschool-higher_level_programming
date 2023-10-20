#!/usr/bin/python3

class MyInt(int):
    def __eq__(self, number):
        return super().__ne__(number)

    def __ne__(self, number):
        return super().__eq__(number)
