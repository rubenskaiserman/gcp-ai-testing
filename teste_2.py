from typing import Optional

from google.api_core.client_options import ClientOptions
from google.cloud import documentai 

def process_document_sample(
    project_id: str,
    location: str,
    processor_id: str,
    file_path: str,
    mime_type: str,
    field_mask: Optional[str] = None,
    processor_version_id: Optional[str] = None,
) -> None:
    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")

    client = documentai.DocumentProcessorServiceClient(client_options=opts)

    if processor_version_id:
        name = client.processor_version_path(
            project_id, location, processor_id, processor_version_id
        )
    else:
        name = client.processor_path(project_id, location, processor_id)

    with open(file_path, "rb") as image:
        image_content = image.read()

    raw_document = documentai.RawDocument(content=image_content, mime_type=mime_type)

    request = documentai.ProcessRequest(
        name=name, raw_document=raw_document, field_mask=field_mask
    )

    result = client.process_document(request=request)

    document = result.document

    print("The document contains the following text:")
    print(document.text)
        


# process_document_sample(
#     mime_type="application/pdf",
#     project_id="286362658457",
#     location="us",
#     processor_id="be352832bca42589",
#     file_path="small.pdf"
# )

process_document_sample(
    mime_type="application/pdf",
    project_id="286362658457",
    location="us",
    processor_id="ac68117c57f23e39",
    file_path="small.pdf"
)