"""
Modèles de données pour le système Agent Action Control.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Decision(Enum):
    """Les décisions possibles du Policy Engine."""
    ALLOW = "ALLOW"
    DENY = "DENY"
    REQUIRE_APPROVAL = "REQUIRE_APPROVAL"


class RiskLevel(Enum):
    """Les niveaux de risque."""
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


@dataclass
class Actor:
    """Représente un acteur (agent IA)."""
    id: str
    role: str
    permissions: list


@dataclass
class Action:
    """Représente une action demandée."""
    name: str
    tool: str
    resource: str
    context: Optional[dict] = None


@dataclass
class AuditEvent:
    """Représente un événement d'audit."""
    timestamp: str
    actor_id: str
    action: str
    resource: str
    decision: Decision
    reason: str
    risk: RiskLevel
    result: str