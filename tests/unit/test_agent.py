"""AI Security Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_red_team_model():
    """Test Run adversarial attacks against an AI model to find vulnerabilities."""
    tools = AgentTools()
    result = await tools.red_team_model(target_endpoint="test", attack_types="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_assess_model_security():
    """Test Assess model security posture against OWASP LLM Top 10."""
    tools = AgentTools()
    result = await tools.assess_model_security(model_config="test", deployment_config="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_detect_data_poisoning():
    """Test Detect potential data poisoning in training or fine-tuning data."""
    tools = AgentTools()
    result = await tools.detect_data_poisoning(dataset_path="test", detection_method="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_test_extraction_resistance():
    """Test Test model resistance to model extraction attacks."""
    tools = AgentTools()
    result = await tools.test_extraction_resistance(target_endpoint="test", query_budget=1)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.ai_security_agent_agent import AiSecurityAgentAgent
    agent = AiSecurityAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
