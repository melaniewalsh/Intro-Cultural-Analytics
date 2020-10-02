# Scrape PDFs with PDFtoText

Scraping a PDF of an AP English exam from the web

!pip install pdftotext

import pdftotext

https://pypi.org/project/pdftotext/

## Scrape PDF From File

This is a random PDF of genres from Goodreads

with open("Genre-List-For-Advertisers.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

print("\n\n".join(pdf))

## Scrape PDF From The Web

import requests
import io

Here's where my PDF is

https://apcentral.collegeboard.org/pdf/ap18-frq-english-literature.pdf?course=ap-english-literature-and-composition

response = requests.get("https://apcentral.collegeboard.org/pdf/ap18-frq-english-literature.pdf?course=ap-english-literature-and-composition")

with io.BytesIO(response.content) as f:
    pdf = pdftotext.PDF(f)

print("\n\n".join(pdf))