from fpdf import FPDF


class MyPdf(FPDF):
    def __init__(self):
        super().__init__()
        self.page_name = ""

    def footer(self):
        self.set_y(-15)
        self.set_font('Times', 'I', 8)
        self.cell(0, 10, self.page_name, 0, 0, "R")

    def set_footer(self, page_name):
        self.page_name = page_name
