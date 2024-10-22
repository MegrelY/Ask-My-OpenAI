from fastapi import APIRouter
from .models import QueryRequest, QueryResponse
from .openai_client import generate_response

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
async def query_openai(request: QueryRequest):
    answer = generate_response(request.question)
    # Assuming references are not used for now
    return QueryResponse(answer=answer, references=[])
