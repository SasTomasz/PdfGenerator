import pandas as pd

from pdf_helper import MyPdf

pdf = MyPdf()

df = pd.read_csv("./topics.csv")
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font('Times', 'B', 22)
    pdf.cell(0, 10, row["Topic"], "B")
    pdf.set_footer(row["Topic"])
    for i in range(row["Pages"] - 1):
        pdf.add_page()
pdf.output('output.pdf')

