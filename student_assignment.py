# pip install -qU langchain_community pypdf

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    pdf = PyPDFLoader(q1_pdf).load()
    pages = CharacterTextSplitter(separator='\f', chunk_overlap=0).split_documents(pdf)
    return pages[-1]

def hw02_2(q2_pdf):
    pdf = PyPDFLoader(q2_pdf).load()
    content = ''.join([page.page_content for page in pdf])
    chunks = RecursiveCharacterTextSplitter(
        chunk_size=1,
        chunk_overlap=0,
        is_separator_regex = True,
        keep_separator=True,
        separators=[r'第 .+ 條', r'第 .+ 章']
    ).split_text(content)
    return len(chunks)

print(hw02_1(q1_pdf))
print(hw02_2(q2_pdf))