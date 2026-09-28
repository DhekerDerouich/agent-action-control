# Réponses aux 10 questions — Agent Action Control

## 1. Pourquoi un agent IA ne devrait-il pas être considéré comme une autorité de sécurité ?

Un agent IA peut être manipulé (injection de prompt, document malveillant, contexte trompeur). Il ne faut pas lui faire confiance pour décider ce qui est autorisé. Dans mon prototype, l'agent ne décide pas : il **demande**. C'est le **Policy Engine** qui décide. C'est la séparation fondamentale entre "celui qui agit" et "celui qui contrôle".

## 2. Quelle différence fais-tu entre identité, authentification et autorisation ?

- **Identité** : Qui est l'agent ? (son ID unique, ex : `sales_agent_001`)
- **Authentification** : Comment on vérifie que c'est bien lui ? (token, certificat, mot de passe)
- **Autorisation** : Qu'est-ce qu'il a le droit de faire ? (permissions, ex : `read_customer`)

Dans mon prototype, je gère seulement l'**identité** (via l'ID) et l'**autorisation** (via les permissions). L'authentification n'est pas implémentée (limite).

## 3. Pourquoi une permission technique ne suffit-elle pas à déterminer si une action est légitime ?

Parce qu'une permission technique dit "tu PEUX", mais pas "tu DOIS". Le contexte compte :
- Est-ce que l'action est cohérente avec le rôle de l'agent ?
- Est-ce que c'est le bon moment ?
- Est-ce que la ressource est appropriée ?

Exemple : un commercial a la permission de `send_email`, mais envoyer un email à 3h du matin avec des données confidentielles n'est pas légitime.

## 4. Quelles informations sont nécessaires pour prendre une décision d'autorisation ?

- **Qui** : identité de l'agent (`actor_id`)
- **Quoi** : action demandée (`action.name`)
- **Sur quoi** : ressource ciblée (`action.resource`)
- **Quand** : contexte temporel (`action.context`)
- **Pourquoi** : raison de la demande (`action.context`)
- **Quelles permissions** : droits de l'agent (`actor.permissions`)
- **Quel risque** : niveau de danger (`RiskLevel`)

## 5. Où doit se situer la frontière de sécurité principale ?

**Entre l'agent et les outils.** C'est là qu'on intercepte l'action avant qu'elle ne soit exécutée. L'agent ne doit **jamais** avoir accès direct aux outils. Toutes les demandes passent par le Policy Engine.

Dans mon architecture :

Le Policy Engine est le **point de contrôle unique**.

## 6. Comment empêcher un agent compromis de contourner le mécanisme d'autorisation ?

- L'agent n'a **pas accès direct** aux outils
- Toutes les demandes passent par le **Policy Engine**
- Le Policy Engine est **séparé** de l'agent
- On **log** tout (audit log)
- On peut **révoquer** les permissions à tout moment
- Le **contexte** (prompt) ne doit **pas** influencer la décision

Dans mon scénario 6, l'agent essaie de contourner avec un prompt malveillant. Le système ignore le prompt et se base uniquement sur les **règles**.

## 7. Que se passe-t-il lorsqu'une politique change alors qu'un agent est déjà en fonctionnement ?

Le Policy Engine doit **recharger** les règles. Les nouvelles demandes sont évaluées avec les **nouvelles règles**. Les actions déjà en cours peuvent être **réévaluées**.

Dans mon prototype, les règles sont **codées en dur** (limite). Pour une vraie production, il faudrait un Policy Engine externe (OPA) qui recharge les règles dynamiquement.

## 8. Quelles informations doivent être conservées dans les logs ?

Dans mon `AuditEvent`, je conserve :
- **Qui** : `actor_id`
- **Quoi** : `action`
- **Sur quoi** : `resource`
- **Quand** : `timestamp`
- **Décision** : `decision` (ALLOW/DENY/REQUIRE_APPROVAL)
- **Pourquoi** : `reason`
- **Risque** : `risk` (LOW/MEDIUM/HIGH)
- **Résultat** : `result` (executed/blocked)

Pour une vraie production, il faudrait ajouter :
- L'IP de l'agent
- Le contexte complet (prompt)
- La version des règles
- Un hash pour garantir l'intégrité

## 9. Quels sont les principaux risques ou limites de ton prototype ?

- **Pas de vraie authentification** : juste un ID, pas de token/certificat
- **Pas de base de données** : les logs sont en mémoire (perdus au redémarrage)
- **Pas de gestion multi-agents** : un seul agent à la fois
- **Pas de chiffrement** : les logs sont en clair
- **Règles codées en dur** : pas de rechargement dynamique
- **Pas de monitoring** : pas d'alerte en temps réel

## 10. Si tu devais faire évoluer ce prototype vers un système utilisé en production, quelles seraient tes trois premières améliorations ?

1. **Authentification réelle** (mTLS, JWT) : pour vérifier l'identité de l'agent
2. **Base de données immuable** pour les logs (append-only) : pour la traçabilité
3. **Policy Engine externe** (OPA) : pour des règles complexes et dynamiques

Ensuite :
4. Dashboard de monitoring
5. Intégration avec un vrai agent IA (LangChain, Llama)
6. Alertes en temps réel