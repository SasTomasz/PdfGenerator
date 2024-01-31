import pandas as pd
from fpdf import FPDF


def add_footer(name):
    pdf.set_y(-25)
    pdf.set_font('Arial', 'I', 8)
    pdf.cell(0, 5, name, 1, 0, align="R")


pdf = FPDF()
pdf.set_margins(0, 0, 0)

df = pd.read_csv("./topics.csv")
for index, item in df[['Topic', 'Pages']].iterrows():
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, item.iloc[0], "B")
    add_footer(item.iloc[0])
    for i in range(item.iloc[1] - 1):
        pdf.add_page()
pdf.output('output.pdf')
