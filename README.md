---
description: Point de départ pour comprendre le serveur et savoir quoi lire.
icon: person-waving
---

# Bienvenue sur LUMA Roleplay

Bienvenue sur LUMA Roleplay.

Cette documentation fixe le cadre du serveur. Elle aide aussi à jouer des scènes claires et cohérentes.

Commence par ces pages :

1. [Comment lire la documentation](accueil/comment-lire-la-documentation.md)
2. [Différence entre RP et HRP](accueil/difference-entre-rp-et-hrp.md)
3. [Résumé rapide](reglement-serveur-hrp/resume-rapide.md)
4. [Ordre conseillé de lecture](references-utiles/ordre-conseille-de-lecture.md)

Lis ensuite les règles liées à ton rôle :

* [Police - SASP](police-sasp/mission-de-la-sasp.md)
* [Médical - SAMS](medical-sams/mission-du-sams.md)
* [Entreprises RP](entreprises-rp/reglement-entreprises-rp.md)
* [Illégal RP](illegal-rp/reglement-illegal-rp.md)

En cas de doute, applique la règle la plus claire. Si besoin, fais un report.

## Publication GitHub Pages

Ce dépôt peut être publié sur GitHub Pages via mdBook et GitHub Actions.

1. Dans **GitHub → Settings → Pages** du dépôt `PN-ProjectNexus/Luma.doc`, choisis **Source : GitHub Actions** (pas la branche `gh-pages`).
2. Pousse sur la branche `main` pour déclencher le workflow de déploiement.
3. Le site sera disponible à l’adresse : `https://pn-projectnexus.github.io/Luma.doc/`

Pour tester en local :

```bash
python scripts/prepare-mdbook.py
mdbook build
mdbook serve
```
