import pandas as pd
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello World!')
pdf.output('output.pdf')

df = pd.read_csv("./topics.csv")
for i in df[['Topic', 'Pages']].iterrows():
    print(i)

