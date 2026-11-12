# Support Produit

## Contexte métier

Nexus Platform est une solution SaaS B2B de gestion de projets techniques. L'équipe support traite environ 200 tickets par mois. Une part importante du temps des agents est consacrée à retrouver la bonne information, à déterminer si un incident est déjà connu et à tenir compte du contexte du client.

Le projet vise à améliorer ce travail, sans remplacer la responsabilité de l'agent dans sa relation avec le client.

## Utilisateurs et enjeux

Les utilisateurs principaux sont les agents support. Les responsables support suivent aussi le respect des engagements de service et la cohérence des réponses.

Les enjeux sont de réduire le temps de recherche, d'aider à formuler des réponses fiables et de mieux traiter les incidents déjà identifiés. Une réponse erronée, périmée ou envoyée trop vite peut dégrader la confiance du client ou entraîner le non-respect des engagements de niveau de service (SLA).

## Données mises à disposition

Les jeux suivants sont fournis. Ils représentent des sources de travail ; leur sélection et leur rôle dans votre proposition font partie du cadrage.

- `donnees/sources_documentaires/guide_installation_v2.md` et `guide_installation_v3.md` : guides d'installation de deux versions du produit.
- `donnees/sources_documentaires/release_notes_v3.md` : évolutions et corrections de la version 3.
- `donnees/sources_documentaires/faq_erreurs_frequentes.md` : réponses aux problèmes fréquents.
- `donnees/sources_documentaires/api_reference.md` : référence fonctionnelle de l'API.
- `donnees/donnees_tabulaire/tickets.csv` : historique anonymisé de tickets et de leurs résolutions.
- `donnees/donnees_tabulaire/clients.csv` : profil et contexte des clients.
- `donnees/donnees_tabulaire/product_versions.csv` : versions du produit et leur état.
- `donnees/donnees_tabulaire/sla_matrix.csv` : engagements de réponse et de résolution.
- `donnees/donnees_tabulaire/known_issues.csv` : incidents connus, symptômes et contournements.
- `donnees/jeux_evaluation/eval_tickets.csv` : cas de référence pour construire et exécuter votre évaluation.

## Contraintes réelles

- Les informations doivent rester cohérentes avec la version du produit et le contexte du client.
- Les engagements de service demandent de distinguer urgence, gravité et délai restant.
- Toute communication externe engageante reste sous validation humaine.
- Les données de clients et les traces de traitement doivent être protégées et explicables.

## Workflows métier actuels

### Traiter un incident entrant

**Déclencheur → acteurs → informations consultées → décisions → actions → résultat attendu**  
Nouveau ticket → agent support, client → contenu du ticket, profil client, version déclarée, engagements de service → qualifier la gravité et décider si une réponse immédiate ou une escalade est nécessaire → préparer une réponse et créer les actions de suivi → client informé dans le délai adapté.

Frottements et risques observables : informations incomplètes, mauvaise qualification, dépassement de SLA, réponse externe non vérifiée.

### Vérifier si le problème est connu

**Déclencheur → acteurs → informations consultées → décisions → actions → résultat attendu**  
Incident qualifié → agent support, expert produit → historique de tickets, problèmes connus, guides et notes de version → déterminer si le symptôme correspond à un cas connu et si un contournement est applicable → proposer une marche à suivre ou solliciter l'expert → résolution documentée et cohérente avec la version concernée.

Frottements et risques observables : vocabulaire différent entre le ticket et les documents, consignes périmées, confusion entre versions.

### Escalader un incident sensible

**Déclencheur → acteurs → informations consultées → décisions → actions → résultat attendu**  
Risque élevé ou délai critique → agent support, responsable support, expert produit → ticket, client, historique, engagements de service et incidents similaires → décider du niveau d'escalade et du message à transmettre → le responsable humain valide la communication et l'escalade → incident pris en charge avec une trace des décisions.

Frottements et risques observables : urgence, informations contradictoires, promesse inappropriée au client, absence de trace.

## Votre cadrage

À partir de ces éléments, choisissez un objectif prioritaire et formulez un MVP observable. Quel problème précis mérite d'être traité en premier, pour quel utilisateur, et pourquoi ? Définissez une baseline, une métrique de succès et les sources réellement utiles. Précisez le niveau d'automatisation retenu, les risques, les garde-fous et les non-objectifs. Quelle décision doit rester humaine ? Quelle preuve vous ferait conclure que le MVP aide réellement sans accroître le risque ?

Justifiez explicitement pourquoi un **traitement LLM simple (chat)**, un **Workflow**, un **RAG** ou un **Agent** sont retenus ou écartés pour votre périmètre — la solution la plus simple qui fait la preuve de la valeur est un choix légitime. Votre décision doit être proportionnée aux utilisateurs, aux risques et aux preuves que vous pouvez produire.

## Démarrer

La progression, les livrables et les pratiques attendues sont décrits dans le module `Méthodologie Projet AI Eng (FR)` sur la plateforme Learn.

Documentez vos décisions importantes dans des ADR et conservez les preuves demandées à chaque phase : contrat, baseline, tests, résultats d'évaluation, traces et démonstrations de fonctionnement ou d'échec maîtrisé.

Le jeu de 5 à 10 cas demandé dès le cadrage peut partir des cas fournis dans `donnees/jeux_evaluation/` ; complétez-les par vos propres cas ambigus et d'erreur, en documentant ce que vous ajoutez et pourquoi.
