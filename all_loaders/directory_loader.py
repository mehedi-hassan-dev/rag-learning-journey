from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='data/pdf',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load() # ak bare ak ta kore document load kore. oneak document thakle lazy_load use kora best

for document in docs:
    
    print(document.metadata)
    print(document.page_content)
   