from queue import PriorityQueue
import time

class Relation:
    def __init__(self, pages):
        self.pages = pages
        self.page_index = 0

    def read_next_page(self):
        if self.page_index < len(self.pages):
            page = self.pages[self.page_index]
            self.page_index += 1
            return page
        return None

    def has_next_page(self):
        return self.page_index < len(self.pages)

    def write_page(self, page):
        print("Writing page to secondary storage:", page)

def replacement_selection_pass_zero(relation_R, M):
    input_frame = []
    output_frame = []
    Q1 = PriorityQueue()
    Q2 = PriorityQueue()

    input_frame.append(relation_R.read_next_page())
    for _ in range(M - 2):
        page = relation_R.read_next_page()
        if page:
            input_frame.append(page)

    for frame in input_frame[1:]:
        for record in frame:
            Q1.put(record)

    while input_frame or not Q1.empty() or not Q2.empty():
        if Q1.empty():
            while not Q2.empty():
                Q1.put(Q2.get())
            if output_frame:
                relation_R.write_page(output_frame)
                output_frame = []

        if input_frame:  
            r1 = Q1.get()
            output_frame.append(r1)

            if not input_frame and relation_R.has_next_page():
                input_frame.append(relation_R.read_next_page())

            if input_frame and input_frame[0]: 
                r2 = input_frame[0].pop(0)
                if r2 < r1:
                    Q1.put(r2)
                else:
                    Q2.put(r2)

            if len(output_frame) == M:
                relation_R.write_page(output_frame)
                output_frame = []

# Sample input
pages = [
    [5, 8, 10],
    [3, 6, 9],
    [2, 4, 7]
]

relation_R = Relation(pages)
M = 4
start_time = time.time()
replacement_selection_pass_zero(relation_R, M)
end_time = time.time()

execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")