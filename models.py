class Sudoku(object):

    def __init__(self, q):
        if len(q) != 81:
            raise IndexError('question with wrong length.')
        self.question = list(map(lambda x: int(x), q))
        self.answer = self.get_answer()

    def __str__(self):
        self.print()

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

                def rows(q):
                    def row(q, r):
                        start = r * 9
                        return [q[start + i] for i in range(9)]
                    return [row(q, r) for r in range(9)]

                def columns(q):
                    def column(q, c):
                        start = c
                        return [q[start + i * 9] for i in range(9)]
                    return [column(q, c) for c in range(9)]

                def frames(q):
                    def frame(q, f):
                        start = f // 3 * 27 + f % 3 * 3
                        return [q[start + i // 3 * 9 + i % 3] for i in range(9)]
                    return [frame(q, f) for f in range(9)]

                def is_legal_block(b):
                    if len(b) != 9:
                        raise IndexError('block with wrong length.')
                    s = set(b)
                    s.discard(0)
                    return b.count(0) + len(s) == 9

                if len(question) != 81:
                    raise IndexError('question with wrong length.')
                blocks = rows(question) + columns(question) + frames(question)
                for block in blocks:
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
