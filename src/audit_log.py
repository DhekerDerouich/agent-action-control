"""
Audit Log : enregistre toutes les décisions.
"""

import json


class AuditLog:
    """Gère l'audit log."""

    def __init__(self):
        self.events = []

    def add(self, event):
        """Ajoute un événement."""
        self.events.append(event)

    def export_json(self, filename):
        """Exporte les événements en JSON."""
        with open(filename, 'w') as f:
            json.dump([e.__dict__ for e in self.events], f, indent=2, default=str)