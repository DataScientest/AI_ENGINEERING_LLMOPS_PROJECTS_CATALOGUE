# Catalogue de projets LLMOps

Ce répertoire est le paquet apprenant du catalogue : il propose quatre contextes métier, plus un sujet bêta, pour construire un projet d'AI Engineering. Il fournit le point de départ : une fiche projet et des données. La manière de concevoir la solution appartient à chaque équipe.

La progression, les livrables et les pratiques attendues sont décrits dans le module Module: `Méthodologie Projet AI Eng (FR)` sur la plateforme Learn.

## Choisir un sujet

- [Support Produit](SUPPORT_PRODUIT/fiche_projet.md) — assister une équipe support dans la résolution de tickets sur un produit SaaS.
- [Conformité Réglementaire](CONFORMITE_REGLEMENTAIRE/fiche_projet.md) — aider des auditeurs à analyser une situation au regard d'un cadre réglementaire.
- [Parcours Apprenant](PARCOURS_APPRENANT/fiche_projet.md) — aider à construire des parcours de formation cohérents avec un profil et un objectif.
- [LocalMind](LOCAL_MIND/fiche_projet.md) — produire des synthèses de documents sensibles dans un environnement local.
- [Assistant QA (bêta)](ASSISTANT_QA/fiche_projet.md) — construire un assistant qui augmente la couverture de tests et la détection de défauts d'une vraie plateforme ML d'entraînement et de service.

Pour votre sujet, commencez par lire la fiche, explorer les données et cartographier les workflows métier présentés. Ils décrivent le travail actuel et ses contraintes ; ils ne prescrivent pas une solution à construire.

## Ressources destinées aux apprenants

Chaque dossier de projet contient une `fiche_projet.md` et un dossier `donnees/`. Les données sont classées par nature :

- `sources_documentaires/` : documents, procédures, notes ou références métier ;
- `donnees_tabulaire/` : registres, catalogues, historiques et autres données structurées ;
- `jeux_evaluation/` : cas et références utilisables pour préparer un protocole d'évaluation ;
- `exemples_prompts/` : exemples de formulations, présents uniquement pour LocalMind.

L'Assistant QA s'appuie aussi sur un dépôt séparé, la plateforme testée, référencé dans sa fiche.

Le choix des moyens de stockage, des accès, des transformations et de la démarche d'évaluation relève de l'équipe. Il doit être cohérent avec le cas d'usage retenu, les données, les risques et les contraintes métier.

Les ressources d’évaluation sont distribuées séparément à l’équipe pédagogique ; elles ne font pas partie de ce paquet apprenant.

## Responsabilités de l'équipe

En suivant la méthodologie, chaque équipe doit notamment :

- cadrer un problème et un MVP vérifiable à partir du flux métier ;
- établir une baseline et décider où une assistance ou une automatisation apporte réellement de la valeur ;
- documenter les décisions structurantes dans des ADR ;
- produire, à chaque phase du projet, les preuves attendues de qualité, de test, de traçabilité, de sécurité, d'évaluation et d'exploitation.

Les choix doivent être justifiés. L'objectif est de démontrer une solution utile, maîtrisée et maintenable, plutôt que d'adopter une technologie particulière.

## Contraintes communes

Les réalisations reposent sur des composants open source. Lorsqu'un sujet l'exige, l'équipe doit pouvoir reproduire l'exécution dans un environnement local. La solution doit aussi assurer une traçabilité suffisante des décisions et des exécutions, et reposer sur une démarche d'évaluation explicite.
