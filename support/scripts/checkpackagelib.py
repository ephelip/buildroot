# See support/scripts/check-package.txt before editing this file.

from checkpackagebase import _CheckFunction


class ConsecutiveEmptyLines(_CheckFunction):
    def before(self):
        self.lastline = "non empty"

    def check_line(self, lineno, text):
        if text.strip() == "" == self.lastline.strip():
            return ["{}:{}: consecutive empty lines"
                    .format(self.filename, lineno)]
        self.lastline = text


class EmptyLastLine(_CheckFunction):
    def before(self):
        self.lastlineno = 0
        self.lastline = "non empty"

    def check_line(self, lineno, text):
        self.lastlineno = lineno
        self.lastline = text

    def after(self):
        if self.lastline.strip() == "":
            return ["{}:{}: empty line at end of file"
                    .format(self.filename, self.lastlineno)]


class NewlineAtEof(_CheckFunction):
    def before(self):
        self.lastlineno = 0
        self.lastline = "\n"

    def check_line(self, lineno, text):
        self.lastlineno = lineno
        self.lastline = text

    def after(self):
        if self.lastline == self.lastline.rstrip("\r\n"):
            return ["{}:{}: missing newline at end of file"
                    .format(self.filename, self.lastlineno),
                    self.lastline]


class TrailingSpace(_CheckFunction):
    def check_line(self, lineno, text):
        line = text.rstrip("\r\n")
        if line != line.rstrip():
            return ["{}:{}: line contains trailing whitespace"
                    .format(self.filename, lineno),
                    text]
