# LocalMind

## Contexte métier

LocalMind est une plateforme interne de traitement documentaire pour des équipes qui manipulent des rapports, comptes rendus et politiques internes sensibles. Les documents ne doivent pas sortir du système d'information. Les collaborateurs passent beaucoup de temps à lire des contenus longs pour en extraire l'essentiel.

Le projet porte sur une assistance de synthèse fiable, mesurable et compatible avec ces contraintes de confidentialité.

## Utilisateurs et enjeux

Les utilisateurs principaux sont les collaborateurs qui déposent ou consultent des documents. Les responsables des équipes sont attentifs à la confidentialité, à la disponibilité du service et à la qualité des synthèses.

Les enjeux sont de réduire le temps de lecture et de rendre l'information plus accessible sans dénaturer le document. Les risques sont une fuite de contenu sensible, une synthèse trompeuse, des traitements longs qui bloquent l'utilisateur et l'indisponibilité sur des machines aux ressources limitées.

## Données mises à disposition

Les jeux suivants sont fournis. Ils représentent des sources de travail ; leur sélection et leur rôle dans votre proposition font partie du cadrage.

- `donnees/sources_documentaires/politique_teletravail.md` : politique interne relative au télétravail.
- `donnees/sources_documentaires/compte_rendu_reunion_produit.txt` : compte rendu de réunion produit.
- `donnees/sources_documentaires/rapport_activite_2025_fondation_lumen.md` : rapport d'activité d'une fondation.
- `donnees/exemples_prompts/prompt_v1.txt` et `prompt_v2.txt` : exemples de consignes de synthèse à comparer et faire évoluer.
- `donnees/jeux_evaluation/eval.csv` : documents et synthèses de référence pour construire et exécuter votre évaluation.

## Contraintes réelles

- Les contenus restent dans le système d'information et ne doivent pas être transmis à un service externe.
- Les documents peuvent être longs et nécessiter un traitement dont la durée varie.
- L'utilisateur doit comprendre l'état d'un traitement et pouvoir récupérer son résultat sans attente opaque.
- Des machines modestes peuvent être utilisées ; prévoyez des comportements acceptables lorsque les ressources sont limitées ou le service indisponible.

## Workflows métier actuels

### Demander la synthèse d'un document

**Déclencheur → acteurs → informations consultées → décisions → actions → résultat attendu**  
Document à lire → collaborateur → document, objectif de lecture, niveau de confidentialité → décider du type de synthèse utile et des informations à préserver → soumettre la demande → synthèse adaptée au besoin de lecture.

Frottements et risques observables : consigne ambiguë, document trop long, information importante omise, contenu sensible exposé.

### Suivre un traitement long

**Déclencheur → acteurs → informations consultées → décisions → actions → résultat attendu**  
Demande en cours → collaborateur, service interne → état du traitement, disponibilité des ressources, document concerné → décider d'attendre, de relancer ou de réduire le périmètre de la demande → consulter l'avancement et récupérer le résultat lorsqu'il est disponible → utilisateur informé sans blocage opaque.

Frottements et risques observables : durée imprévisible, échec non signalé, indisponibilité locale, perte de résultat.

### Diffuser une synthèse sensible

**Déclencheur → acteurs → informations consultées → décisions → actions → résultat attendu**  
Synthèse préparée pour un partage → collaborateur, responsable d'équipe → document d'origine, synthèse, destinataires et règles de confidentialité → vérifier l'exactitude et le niveau de diffusion autorisé → un responsable humain valide le partage lorsque l'impact est sensible → synthèse diffusée aux personnes autorisées avec les réserves nécessaires.

Frottements et risques observables : synthèse inexacte, omission de nuance, diffusion à un mauvais destinataire, absence de validation.

## Votre cadrage

À partir de ces éléments, choisissez un objectif prioritaire et formulez un MVP observable. Quel problème précis mérite d'être traité en premier, pour quel utilisateur, et pourquoi ? Définissez une baseline, une métrique de succès et les sources réellement utiles. Précisez le niveau d'automatisation retenu, les risques, les garde-fous et les non-objectifs. Quelle décision doit rester humaine ? Quelle preuve vous ferait conclure que le MVP aide réellement sans accroître le risque ?

Justifiez explicitement pourquoi un **traitement LLM simple (chat)**, un **Workflow**, un **RAG** ou un **Agent** sont retenus ou écartés pour votre périmètre — la solution la plus simple qui fait la preuve de la valeur est un choix légitime. Expliquez comment vous préservez la confidentialité, évaluez la qualité et gérez les traitements longs ou indisponibles.

## Démarrer

La progression, les livrables et les pratiques attendues sont décrits dans le module `Méthodologie Projet AI Eng (FR)` sur la plateforme Learn.

Documentez vos décisions importantes dans des ADR et conservez les preuves demandées à chaque phase : contrat, baseline, tests, résultats d'évaluation, traces et démonstrations de fonctionnement ou d'échec maîtrisé.

Le jeu de 5 à 10 cas demandé dès le cadrage peut partir des cas fournis dans `donnees/jeux_evaluation/` ; complétez-les par vos propres cas ambigus et d'erreur, en documentant ce que vous ajoutez et pourquoi.
