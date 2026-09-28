"""
Policy Engine : le cerveau qui décide.
"""

from datetime import datetime
from .models import Actor, Action, Decision, RiskLevel, AuditEvent


class PolicyEngine:
    """Prend les décisions d'autorisation."""

    def __init__(self):
        self.audit_log = []

    def evaluate(self, actor: Actor, action: Action) -> AuditEvent:
        """
        Évalue une demande d'action et retourne une décision.
        """
        # 1. Vérifier les permissions
        if action.tool not in actor.permissions:
            return self._log(actor, action, Decision.DENY,
                             "Permission insuffisante", RiskLevel.LOW)

        # 2. Vérifier la ressource
        if action.resource.startswith("confidential"):
            return self._log(actor, action, Decision.DENY,
                             "Ressource interdite", RiskLevel.HIGH)

        # 3. Vérifier le risque
        if action.name in ["export_data", "send_email"]:
            return self._log(actor, action, Decision.REQUIRE_APPROVAL,
                             "Action sensible", RiskLevel.HIGH)

        # 4. Sinon, autoriser
        return self._log(actor, action, Decision.ALLOW,
                         "Action autorisée", RiskLevel.LOW)

    def _log(self, actor, action, decision, reason, risk):
        """Enregistre la décision dans l'audit log."""
        event = AuditEvent(
            timestamp=datetime.now().isoformat(),
            actor_id=actor.id,
            action=action.name,
            resource=action.resource,
            decision=decision,
            reason=reason,
            risk=risk,
            result="executed" if decision == Decision.ALLOW else "blocked"
        )
        self.audit_log.append(event)
        return event