class Sudoku(object):

    def __init__(self, q):
        if len(q) != 81:
            raise IndexError('question with wrong length.')
        self.question = []
        for i in range(len(q)):
            self.question.append(int(q[i]))
        self.answer = self.get_answer()

    def __str__(self):
        return 'Sudoku()'

    def print(self):
        for i in range(3):
            for ii in range(3):
                x = i * 3 + ii
                tt = ''
                for j in range(3):
                    for jj in range(3):
                        y = j * 3 + jj
                        tt = tt + ' ' + str(self.question[x * 9 + y])
                    tt += ' '
                print(tt)
            print('')

    def print_answer(self):
        for i in range(3):
            for ii in range(3):
                x = i * 3 + ii
                tt = ''
                for j in range(3):
                    for jj in range(3):
                        y = j * 3 + jj
                        tt = tt + ' ' + str(self.answer[x * 9 + y])
                    tt += ' '
                print(tt)
            print('')

    def get_answer(self):

        def solve(question):

            def is_legal(question):

                def is_legal_block(block):
                    if len(block) != 9:
                        raise IndexError('block with wrong length.')
                    s = set(block)
                    s.discard(0)
                    return block.count(0) + len(s) == 9

                if len(question) != 81:
                    raise IndexError('question with wrong length.')
                for i in range(0, 9):
                    block = question[i * 9 : i * 9 + 9]
                    if not is_legal_block(block):
                        return False
                    block = question[i : i + 73 : 9]
                    if not is_legal_block(block):
                        return False
                for i in range(0, 55, 27):
                    for j in range(0, 7, 3):
                        block = []
                        for ii in range(0, 19, 9):
                            for jj in range(3):
                                block.append(question[i+j+ii+jj])
                        if not is_legal_block(block):
                            return False
                return True

            def is_completed(question):
                return 0 not in question

            def find_blank(question):
                if not is_completed(question):
                    return question.index(0)

            if not is_legal(question):
                return False
            elif is_completed(question):
                return question
            blank = find_blank(question)
            q = question.copy()
            for i in range(1, 10):
                q[blank] = i
                result = solve(q)
                if result:
                    return result
            return False

        return solve(self.question)
