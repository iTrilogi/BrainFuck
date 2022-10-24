from aifc import Error


class BrainfuckMachine(int):
    HeadOverflow = Error
    BracketMismatch = Error

    def run(self):
        self.tape = [0]
        x = 0
        self.head = 0
        index = 0
        loop = []
        while x < len(self.code):
            if self.code[x] == ">":
                index += 1
                self.head += 1
                if index == len(self.tape):
                    self.tape.append(0)
                if index > 64:
                    raise self.HeadOverflow

            if self.code[x] == "<":
                index -= 1
                self.head -= 1
                if index < 0:
                    self.tape.insert(0, 0)
                    index += 1
                    raise self.HeadOverflow

            if self.code[x] == "+":
                self.tape[index] += 1
                if self.tape[index] == 256:
                    self.tape[index] = 0

            if self.code[x] == "-":
                self.tape[index] -= 1
                if self.tape[index] == -1:
                    self.tape[index] = 255

            if self.code[x] == "[":
                loop.append(x)
                if (self.code[x - 1] == "["):
                    raise self.BracketMismatch

            if self.code[x] == "]":
                if self.tape[index] != 0:
                    x = loop[-1]
                else:
                    del loop[-1]

            x += 1
