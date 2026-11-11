# User stories

Tickets of the current backlog. Ids match `data/tabular_data/tickets.csv`. Criterion ids are written `AC-<ticket>-<n>`. The expected behaviour behind each criterion is detailed in `docs/FUNCTIONAL_SPEC.md` of the platform repository (section given in brackets).

## TX-101: Prediction input contract [§5.1, §5.2]

As an API client, I want invalid inputs to be rejected clearly so that I can fix my request.

- AC-101-1: Values at the bounds of every field are accepted.
- AC-101-2: A value outside a bound, or of the wrong type, returns 422 and names the faulty fields, sorted.
- AC-101-3: An empty body is valid: every field has a default.
- AC-101-4: An invalid request returns 422 even when no model is loaded.
- AC-101-5: The API accepts exactly the ranges that the training data validation accepts.

## TX-102: Prediction responses [§5.2]

As an API client, I want a predictable answer in every situation.

- AC-102-1: A valid request returns the fare rounded to the cent and the model version, computed from the 9 model features.
- AC-102-2: Without a model the API returns 503 and never loads a model during the request.
- AC-102-3: An error raised by the model returns 500 without exposing internal details.
- AC-102-4: Logs name the faulty fields of a rejected request, never their values.

## TX-103: Readiness [§5.3]

As an operator, I want `/health` to tell whether the service can really predict.

- AC-103-1: Without a model, `/health` returns 503.
- AC-103-2: With a model that cannot predict, `/health` returns 503.
- AC-103-3: With a working model, `/health` returns 200 with the version and a smoke fare.

## TX-104: Serving the champion [§5.4]

As a data scientist, I want the API to serve the latest champion without a restart.

- AC-104-1: When no champion exists, nothing changes and the API keeps answering 503.
- AC-104-2: A new champion version is loaded and its version is reported.
- AC-104-3: The same version is not loaded twice.

## TX-105: Data preparation [§1]

As a data engineer, I want raw trips to become clean features.

- AC-105-1: Source columns are renamed and the output has the 9 features then the target, in order.
- AC-105-2: A missing required column fails and names every missing column.
- AC-105-3: `pickup_weekday` is 1 from Monday to Friday and 0 at the weekend.
- AC-105-4: `total_fare` adds the optional components, counting absent ones as 0.

## TX-106: Data validation and quarantine [§2]

As a data engineer, I want bad rows set aside, never lost, and a broken source to stop the pipeline.

- AC-106-1: Rows outside the valid ranges are quarantined with a reason naming the column.
- AC-106-2: Missing, infinite and non-numeric values are quarantined.
- AC-106-3: More than 20% invalid rows fails the preparation; exactly 20% passes.
- AC-106-4: Fewer than 100 valid rows fails the preparation; exactly 100 passes.
- AC-106-5: The limits come from the configuration file, not from the code.

## TX-107: Ingestion [§3]

As a data engineer, I want ingestion to be safe to retry.

- AC-107-1: An invalid month or a limit under 100 fails before anything is downloaded.
- AC-107-2: Ingesting the same source twice does not duplicate valid or quarantined rows.
- AC-107-3: Quarantined rows are stored with their reason.

## TX-108: Training and promotion [§4]

As a data scientist, I want a new model to replace the champion only when it is better.

- AC-108-1: Candidate and champion are scored on the same validation data.
- AC-108-2: The candidate is promoted only if there is no champion or if its error is strictly lower; a tie keeps the champion.
- AC-108-3: Every candidate is registered as a new version, promoted or not, with its metrics, parameters and training sample.
- AC-108-4: The champion alias moves only after the model and its artifacts are stored.

## TX-109: Fast enough API

As a product owner, I want the API to be fast enough for our users.

- AC-109-1: The API responds fast enough.

## TX-110: Retrain when data changes

As a product owner, I want the model to be retrained when the data changes a lot.

- AC-110-1: A significant data change triggers a retraining.

## TX-111: Better model quality

As a product owner, I want the predictions to be more accurate.

- AC-111-1: The model is more accurate than today.
