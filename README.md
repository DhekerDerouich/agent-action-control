# 🛡️ Agent Action Control

> Un prototype de contrôle d'actions pour agents IA autonomes.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Tests](https://img.shields.io/badge/Tests-6%2F6%20passing-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📋 Table des matières
- [Problème](#problème)
- [Solution](#solution)
- [Architecture](#architecture)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Scénarios de test](#scénarios-de-test)
- [Choix techniques](#choix-techniques)
- [Limites](#limites)
- [Améliorations futures](#améliorations-futures)
- [Auteur](#auteur)

## 🎯 Problème

Les agents IA modernes ne se contentent plus de répondre. Ils **agissent** :
- Accèdent à des données
- Appellent des APIs
- Envoient des emails
- Modifient des CRM

**Question centrale :** Comment contrôler une action demandée par un agent IA **avant** qu'elle ne soit exécutée ?

## 💡 Solution

Ce prototype implémente un **Policy Engine** qui :
1. Reçoit une demande d'action
2. Vérifie l'identité, les permissions, le contexte, le risque
3. Retourne une décision : `ALLOW`, `DENY`, ou `REQUIRE_APPROVAL`
4. Enregistre la décision dans un **audit log**

## 🏗️ Architecture

(Insérer ton diagramme ici)

## 🚀 Installation

```bash
git clone https://github.com/ton-username/agent-action-control.git
cd agent-action-control
pip install -r requirements.txt
