import shutil
import os
from fastapi import FastAPI, File, UploadFile

from invoice2data import extract_data
from invoice2data.extract.loader import read_templates
from invoice2data.input import tesseract

invoice_api = FastAPI()
templates = read_templates('./templates/')

@invoice_api.post("/invoice/")
async def upload_invoice(invoice: UploadFile = File(...)):
    with open(f'{invoice.filename}','wb') as buffer:
        shutil.copyfileobj(invoice.file,buffer)

    result = extract_data(f'{invoice.filename}', templates=templates)

    os.remove(f'{invoice.filename}')

    return result
