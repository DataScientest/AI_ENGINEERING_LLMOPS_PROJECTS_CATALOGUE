# Assistant QA

> **Sujet bêta.** Ce sujet est nouveau et peut évoluer. Il suit le même format que les autres sujets du catalogue.

## Contexte métier

TaxiFare prédit le prix d'une course de taxi new-yorkaise avant son départ. La plateforme est réelle et tourne en local : un pipeline d'entraînement qui télécharge de vrais trajets de New York, les valide, entraîne un modèle et ne le promeut dans un registre de modèles que s'il bat le modèle actuel, et une API qui sert le modèle promu. Elle tourne sur environ huit conteneurs (PostgreSQL, MinIO, MLflow, Prefect, l'API).

L'équipe compte six développeurs et une seule personne en QA. Depuis que les développeurs utilisent des assistants IA pour coder, ils livrent environ deux fois plus de changements. La QA, seule à concevoir les tests, est devenue le goulot d'étranglement, et la suite de tests a pris du retard : 4 tests unitaires, 43 % de couverture de branches, aucun test d'intégration, des incidents découverts en production plutôt que par la suite.

Le projet vise à construire un assistant qui aide la QA à tester la plateforme beaucoup mieux et beaucoup plus vite, à tous les niveaux (unitaire, intégration, bout en bout), sans remplacer son jugement sur ce qui est testé et ce qui est fusionné.

## Utilisateurs et enjeux

L'utilisateur principal est la personne chargée de la QA. Les développeurs lisent les tests générés et leurs résultats ; le responsable d'équipe suit la couverture et les incidents.

L'objectif est une suite qui détecte des défauts, pas une suite qui se contente de tourner. Un test qui passe sans vérifier l'exigence donne une fausse confiance. Un test généré qui prend plus de temps à relire qu'à écrire à la main supprime le bénéfice. Un test de bout en bout qui aurait pu être un test unitaire ralentit la suite pour rien.

## Ambition : un minimum, pas de plafond

Le minimum ci-dessous est ce que chaque équipe doit livrer. C'est un plancher, pas une cible : les équipes sont explicitement encouragées à aller plus loin, et l'évaluation valorise ce qui est réalisé au-delà, à condition que ce soit mesuré et maîtrisé.

**Minimum (MVP)**

- Un assistant prend un ticket et la spécification, et propose des cas de test reliés aux critères d'acceptation. Quand un critère n'est pas clair, il pose une question au lieu d'inventer une réponse.
- Les cas validés deviennent des tests unitaires automatisés pour au moins un module, en réutilisant les fixtures existantes.
- Un humain relit tout avant la fusion.
- Vous mesurez, par rapport à une baseline : la couverture gagnée sur ce module, le temps de relecture, et les cas faux ou inventés.

**Pour aller plus loin (exemples, aucun n'est obligatoire)**

- Couvrir tous les tickets et tous les modules.
- Générer des tests d'intégration avec de vraies dépendances (base de données, registre de modèles, stockage d'artefacts) démarrées pour le test.
- Générer des tests de bout en bout sur la plateforme lancée : un entraînement qui promeut un modèle, puis l'API qui le sert.
- Choisir le bon niveau pour chaque cas (unitaire, intégration, bout en bout) et le justifier.
- Mesurer la force de vos propres tests (par exemple avec du mutation testing), pas seulement leur couverture.
- Sélectionner les tests pertinents pour un changement et les lancer en CI, avec un rapport sur la pull request.
- Laisser un agent explorer la plateforme en marche pour proposer des cas que la spécification ne mentionne pas, avec des limites strictes sur ce qu'il peut faire.

## Données mises à disposition

Les sources suivantes sont fournies. Leur sélection et leur rôle dans votre proposition font partie du cadrage.

- **La plateforme** (système testé) : dépôt [`DataScientest/AI_ENGINEERING_QA_ASSISTANT_TAXI_PLATFORM`](https://github.com/DataScientest/AI_ENGINEERING_QA_ASSISTANT_TAXI_PLATFORM), tag `v1.0`. Travaillez sur votre propre fork. Il contient :
  - le code de chaque service et la suite de tests existante (`tests/`) ;
  - `docs/FUNCTIONAL_SPEC.md` : le comportement attendu, en anglais, qui fait référence pour tout résultat attendu.
- `donnees/sources_documentaires/user_stories.md` : le backlog, avec les critères d'acceptation et les liens vers la spécification.
- `donnees/sources_documentaires/contexte_equipe.md` : l'équipe, le cheminement actuel d'un changement et les contraintes.
- `donnees/donnees_tabulaire/tickets.csv` : les mêmes tickets sous forme tabulaire.
- `donnees/donnees_tabulaire/historique_incidents.csv` : les incidents passés, leur cause et le test qui manquait.
- `donnees/donnees_tabulaire/carte_modules_tests.csv` : les modules, les tests existants et leur couverture en `v1.0`.
- `donnees/jeux_evaluation/cas_reference.csv` : des cas de test de référence écrits à la main pour certains tickets, à plusieurs niveaux, pour construire et exécuter votre évaluation.

## Contraintes réelles

- Rien de ce qui est généré n'est fusionné sans relecture humaine, et tout ce qui est généré est identifiable comme tel et rattaché à son ticket.
- Le résultat attendu d'un test vient de la spécification, jamais de l'exécution de la plateforme.
- Les tickets sont écrits par plusieurs personnes et ne sont pas toujours précis.
- Les fixtures existantes sont réutilisées plutôt que dupliquées.
- Les tests de bout en bout sont lents : on les réserve à ce que les niveaux inférieurs ne peuvent pas vérifier.
- Le code généré s'exécute dans un environnement isolé, sans secrets de production.

## Workflows métier actuels

### Concevoir les tests d'un ticket

**Déclencheur → acteurs → informations consultées → décisions → actions → résultat attendu**  
Ticket prêt à tester → QA, développeur → ticket, critères d'acceptation, spécification, tests existants → décider des cas nécessaires (nominal, limite, erreur), de leur niveau et des critères flous → écrire et automatiser les cas, poser des questions sur les critères flous → des tests validés par l'équipe, chacun relié à un critère.

Frottements et risques observables : tickets imprécis, cas limites oubliés, doublons, tests au mauvais niveau, temps passé avant de pouvoir fusionner un changement.

### Combler les trous de couverture

**Déclencheur → acteurs → informations consultées → décisions → actions → résultat attendu**  
Rapport de couverture ou incident → QA → couverture par module, historique d'incidents, spécification → décider quel comportement non testé compte le plus → ajouter les tests manquants → moins d'incidents découverts en production.

Frottements et risques observables : couverture recherchée pour elle-même, tests qui exécutent du code sans rien vérifier.

### Décider quoi lancer après un changement

**Déclencheur → acteurs → informations consultées → décisions → actions → résultat attendu**  
Pull request ouverte → développeur, QA → le changement, la carte des modules, les tests existants → décider quels tests sont pertinents → les lancer et rendre compte → confiance pour fusionner sans tout relancer.

Frottements et risques observables : la suite complète est lente, un test pertinent est oublié, une régression passe.

## Votre cadrage

À partir de ces éléments, choisissez un objectif prioritaire et formulez un MVP observable qui atteint au moins le minimum ci-dessus. Quel problème précis mérite d'être traité en premier, pour quel utilisateur, et pourquoi ? Définissez une baseline, une métrique de succès et les sources réellement utiles. Précisez le niveau d'automatisation retenu, les risques, les garde-fous et les non-objectifs. Quelle décision doit rester humaine ? Quelle preuve vous ferait conclure que l'assistant aide réellement sans accroître le risque ?

Justifiez explicitement pourquoi un **traitement LLM simple (chat)**, un **Workflow**, un **RAG** ou un **Agent** sont retenus ou écartés pour votre périmètre — la solution la plus simple qui fait la preuve de la valeur est un choix légitime. Votre décision doit être proportionnée aux utilisateurs, aux risques et aux preuves que vous pouvez produire.

## Démarrer

Commencez par la [méthodologie unifiée AI Engineering](../../AI_engineering_project_message/README.md). Elle vous guide du cadrage à l'exploitation et rappelle les bonnes pratiques de software engineering attendues.

Documentez vos décisions importantes dans des ADR et conservez les preuves demandées à chaque phase : contrat, baseline, tests, résultats d'évaluation, traces et démonstrations de fonctionnement ou d'échec maîtrisé.

Le jeu de 5 à 10 cas demandé dès le cadrage peut partir des cas fournis dans `donnees/jeux_evaluation/` ; complétez-les par vos propres cas ambigus et d'erreur, en documentant ce que vous ajoutez et pourquoi.
