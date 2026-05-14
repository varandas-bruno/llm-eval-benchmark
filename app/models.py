from pydantic import BaseModel
from typing import Optional

class EvaluationRequest(BaseModel):
    prompt: str
    provider: str = "ollama"
    rag: bool = False
    llm_response: str
    retrieved_chunks: Optional[list[str]]
    ground_truth: Optional[str]
    
class MetricResult(BaseModel):
    score: Optional[float] = None
    reasoning: str
    
    
class MetricBreakdown(BaseModel):
    factual_accuracy: MetricResult
    grounding: MetricResult
    completeness: MetricResult
    relevance: MetricResult
    clarity: MetricResult
    actionability: MetricResult
    # Only for RAG evaluations
    retrieval_relevance: Optional[MetricResult]
    context_usage: Optional[MetricResult]
    source_attribution: Optional[MetricResult]
    

class EvaluationResponse(BaseModel):
    prompt: str
    provider: str
    rag: bool
    metrics: MetricBreakdown
    overall_score: str
    overall_score_reasoning: str
    