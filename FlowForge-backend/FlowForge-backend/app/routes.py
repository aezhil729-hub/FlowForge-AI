from fastapi import APIRouter
from app.models import PromptRequest
from app.gemini_service import generate_workflow
from app.simulator import simulate_workflow

router = APIRouter()

@router.post("/generate-workflow")
async def create_workflow(data: PromptRequest):

    workflow = generate_workflow(data.prompt)

    return {
        "success": True,
        "workflow": workflow
    }


@router.post("/simulate-workflow")
async def simulate(data: PromptRequest):

    workflow = generate_workflow(data.prompt)

    logs = simulate_workflow(workflow)

    return {
        "success": True,
        "workflow": workflow,
        "logs": logs
    }