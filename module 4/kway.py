class Relation:
    def __init__(self, pages):
        self.pages = pages
        self.page_index = 0

    def read_next_page(self, M):
        start = self.page_index
        end = min(self.page_index + M, len(self.pages))
        self.page_index = end
        return self.pages[start:end]

    def has_next_page(self):
        return self.page_index < len(self.pages)

    def write_pages(self, pages):
        for page in pages:
            print("Writing page to secondary storage:", " ".join(map(str, page)))

def k_way_pass_zero(relation_R, M):
    while relation_R.has_next_page():
        pages = relation_R.read_next_page(M)
        sorted_pages = sorted([record for page in pages for record in page])
        print("Writing page to secondary storage:", " ".join(map(str, sorted_pages)))

# Sample input
pages = [
    [3, 9, 6],
    [10, 5, 8],
    [4, 7, 2],
    [11, 12, 1]
]

relation_R = Relation(pages)

# Number of frames in the buffer
M = 3

k_way_pass_zero(relation_R, M)
