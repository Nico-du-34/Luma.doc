---
description: Point de départ pour comprendre le serveur et savoir quoi lire.
---

# 👋 Bienvenue sur LUMA Roleplay

Bienvenue sur LUMA Roleplay.

Cette documentation fixe le cadre du serveur. Elle est organisée en **deux univers** dans le sommaire :

1. **Règlement — …** — règles pour jouer (serveur, illégal, entreprises, police, médical, vie civile…).
2. **Lois — …** / **Lois & justice** — ce qui s’applique _dans_ le RP (textes fondamentaux, codes, amendes, justice).

Commence par ces pages :

1. Comment lire la documentation
2. Différence entre RP et HRP
3. Résumé rapide
4. Ordre conseillé de lecture

Lis ensuite selon ton rôle :

* Police - SASP → sommaire **Règlement — Police SASP**
* Médical - SAMS → **Règlement — Médical SAMS**
* Entreprises RP → **Règlement — Entreprises RP**
* Illégal RP → **Règlement — Illégal RP**

Pour les peines, amendes et codes : sections **Lois —** et page [Lois & justice](lois-and-justice.md).

En cas de doute, applique la règle la plus claire. Si besoin, fais un report.

## Publication GitHub Pages

Ce dépôt est publié sur GitHub Pages via mdBook et GitHub Actions.

1. Dans **GitHub → Settings → Pages** du dépôt `PN-ProjectNexus/Luma.doc`, choisis **Source : GitHub Actions** (pas la branche `gh-pages`).
2. Dans **Custom domain**, indique `luma.anzoris.fr` (mdBook génère le fichier `CNAME` à la racine du site lors du build).
3. Pousse sur la branche `main` pour déclencher le workflow de déploiement.
4. Le site est disponible à l’adresse : `https://luma.anzoris.fr/`

Pour tester en local :

```bash
python scripts/prepare-mdbook.py
mdbook build
mdbook serve
```
