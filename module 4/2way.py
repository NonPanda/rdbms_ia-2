from typing import List

class Relation:
    def __init__(self, pages: List[List[int]]):
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

def two_way_pass_zero(relation_R):
    while relation_R.has_next_page():
        page = relation_R.read_next_page()
        sorted_page = sorted(page)
        relation_R.write_page(sorted_page)

pages = [
    [9, 6, 3],
    [7, 4, 1],
    [5, 2, 0]
]

relation_R = Relation(pages)

two_way_pass_zero(relation_R)
