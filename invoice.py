import pdfplumber
import pandas as pd

data = []

with pdfplumber.open("invoice.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        for line in text.split("\n"):
            data.append([line])

df = pd.DataFrame(data, columns=["Text"])
print(df)



