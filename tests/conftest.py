"""Test configuration for AI Security Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "ai-security-agent", "category": "AI Engineering"}
