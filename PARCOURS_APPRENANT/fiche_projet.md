# Parcours Apprenant

## Contexte métier

SkillPath Academy accompagne des professionnels de la tech dans leur montée en compétences. Les conseillers pédagogiques analysent le profil d'un apprenant, son objectif, ses résultats passés et les formations disponibles afin de construire un parcours adapté.

Un entretien peut demander plusieurs heures de préparation et de discussion. Le projet cherche à assister ce travail tout en laissant la décision au conseiller et à l'apprenant.

## Utilisateurs et enjeux

Les utilisateurs principaux sont les conseillers pédagogiques. Les apprenants sont les bénéficiaires directs des propositions et peuvent les discuter ou les refuser.

Les enjeux sont de préparer des parcours pertinents, compréhensibles et réalistes en termes de prérequis, de durée et de disponibilité. Les risques portent sur les données personnelles, les biais dans les recommandations, une proposition insuffisamment explicable et une décision prise à la place du conseiller.

## Données mises à disposition

Les jeux suivants sont fournis. Ils représentent des sources de travail ; leur sélection et leur rôle dans votre proposition font partie du cadrage.

- `donnees/sources_documentaires/fiche_data_engineering.md`, `fiche_data_scientist.md`, `fiche_mlops.md` et `fiche_llm_engineer.md` : fiches décrivant des métiers cibles.
- `donnees/sources_documentaires/metiers_cibles.md` : vue d'ensemble des métiers et compétences attendues.
- `donnees/donnees_tabulaire/learners.csv` : profils d'apprenants, objectifs et disponibilités.
- `donnees/donnees_tabulaire/assessments.csv` : résultats d'évaluations passées.
- `donnees/donnees_tabulaire/training_catalog.csv` : catalogue de formations et leurs caractéristiques.
- `donnees/donnees_tabulaire/prerequisites.csv` : prérequis entre formations ou compétences.
- `donnees/donnees_tabulaire/certifications.csv` : informations sur les certifications.
- `donnees/jeux_evaluation/eval_recommendations.csv` : cas de référence pour construire et exécuter votre évaluation.

## Contraintes réelles

- Les profils et résultats d'évaluation constituent des données personnelles à protéger.
- Une recommandation doit être explicable et permettre au conseiller de la discuter avec l'apprenant.
- Les prérequis, disponibilités et objectifs peuvent rendre une proposition irréaliste malgré une apparente pertinence.
- La décision finale de parcours appartient au conseiller et à l'apprenant ; aucune inscription ou modification engageante ne doit être automatisée sans validation humaine.

## Workflows métier actuels

### Préparer un entretien d'orientation

**Déclencheur → acteurs → informations consultées → décisions → actions → résultat attendu**  
Demande d'accompagnement → conseiller pédagogique, apprenant → profil, objectif, disponibilité et résultats d'évaluation → identifier les informations manquantes et les objectifs plausibles → préparer les questions de l'entretien → entretien ciblé et dossier complet.

Frottements et risques observables : données incomplètes, objectifs formulés de manière vague, temps de préparation élevé.

### Construire une proposition de parcours

**Déclencheur → acteurs → informations consultées → décisions → actions → résultat attendu**  
Entretien terminé → conseiller pédagogique, apprenant → profil, compétences actuelles, formations, prérequis, métiers et certifications → choisir un objectif, un ordre de progression et une charge réaliste → présenter un ou plusieurs parcours argumentés → proposition compréhensible et adaptée.

Frottements et risques observables : prérequis oubliés, recommandation opaque, biais lié à des profils historiques, charge irréaliste.

### Valider une inscription ou un changement de parcours

**Déclencheur → acteurs → informations consultées → décisions → actions → résultat attendu**  
Proposition discutée → apprenant, conseiller pédagogique, administration si nécessaire → proposition, contraintes de calendrier, capacités des formations et accord de l'apprenant → confirmer ou ajuster le parcours → le conseiller humain valide l'inscription ou la modification → parcours enregistré avec l'accord explicite de l'apprenant.

Frottements et risques observables : indisponibilité d'une formation, consentement mal tracé, recommandation appliquée sans discussion.

## Votre cadrage

À partir de ces éléments, choisissez un objectif prioritaire et formulez un MVP observable. Quel problème précis mérite d'être traité en premier, pour quel utilisateur, et pourquoi ? Définissez une baseline, une métrique de succès et les sources réellement utiles. Précisez le niveau d'automatisation retenu, les risques, les garde-fous et les non-objectifs. Quelle décision doit rester humaine ? Quelle preuve vous ferait conclure que le MVP aide réellement sans accroître le risque ?

Justifiez explicitement pourquoi un **traitement LLM simple (chat)**, un **Workflow**, un **RAG** ou un **Agent** sont retenus ou écartés pour votre périmètre — la solution la plus simple qui fait la preuve de la valeur est un choix légitime. Montrez comment votre proposition reste explicable, protège les données personnelles et conserve la décision humaine.

## Démarrer

La progression, les livrables et les pratiques attendues sont décrits dans le module `Méthodologie Projet AI Eng (FR)` sur la plateforme Learn.

Documentez vos décisions importantes dans des ADR et conservez les preuves demandées à chaque phase : contrat, baseline, tests, résultats d'évaluation, traces et démonstrations de fonctionnement ou d'échec maîtrisé.

Le jeu de 5 à 10 cas demandé dès le cadrage peut partir des cas fournis dans `donnees/jeux_evaluation/` ; complétez-les par vos propres cas ambigus et d'erreur, en documentant ce que vous ajoutez et pourquoi.
