# Contexte de l'équipe

## Le produit et l'équipe

TaxiFare prédit le prix d'une course de taxi new-yorkaise avant son départ. La plateforme comprend un pipeline d'entraînement (ingestion, validation, entraînement, promotion dans un registre de modèles) et une API de prédiction qui sert le modèle promu. Son code est dans le dépôt `DataScientest/AI_ENGINEERING_QA_ASSISTANT_TAXI_PLATFORM` (tag `v1.0`) ; son comportement attendu est décrit dans `docs/FUNCTIONAL_SPEC.md` de ce dépôt.

L'équipe compte sept personnes : six développeurs et une personne chargée de la QA. Depuis que les développeurs utilisent des assistants IA pour coder, ils livrent environ deux fois plus de changements, et la QA, seule à concevoir les tests et à maintenir la suite, est devenue le goulot d'étranglement.

## Le cheminement actuel d'un changement

1. Un ticket avec des critères d'acceptation est rédigé dans l'outil de suivi.
2. Un développeur l'implémente et ouvre une pull request. La CI lance les tests existants.
3. La QA conçoit les cas de test (nominal, limite, erreur), puis automatise ceux qui valent la peine d'être gardés, au bon niveau : unitaire, intégration ou bout en bout.
4. Le changement est fusionné quand la suite est verte et que la QA est d'accord.

La suite n'a pas suivi : 4 tests unitaires, 2 tests de bout en bout, aucun test d'intégration, et 43 % de couverture de branches des services. L'entraînement et la promotion ne sont pas testés du tout.

## Contraintes

- Aucun recrutement QA supplémentaire n'est prévu.
- Rien de ce qu'un outil génère n'est fusionné sans relecture humaine.
- Les fixtures existantes doivent être réutilisées plutôt que réécrites.
- Les tests de bout en bout demandent la plateforme lancée (environ huit conteneurs et un premier entraînement). Ils sont lents ; on les réserve à ce que les niveaux inférieurs ne peuvent pas vérifier.
- Les tickets sont écrits par plusieurs personnes et ne sont pas toujours précis.
