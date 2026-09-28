"""
Action Executor : exécute les actions si ALLOW.
"""

from .models import Decision


class ActionExecutor:
    """Exécute les actions autorisées."""

    def execute(self, event):
        """Exécute l'action si la décision est ALLOW."""
        if event.decision == Decision.ALLOW:
            print(f"✅ Action exécutée : {event.action} sur {event.resource}")
            return True
        elif event.decision == Decision.REQUIRE_APPROVAL:
            print(f"⚠️  Action en attente d'approbation : {event.action}")
            return False
        else:
            print(f"❌ Action bloquée : {event.action}")
            return False