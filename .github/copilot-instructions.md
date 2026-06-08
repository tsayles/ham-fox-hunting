# Ham Fox Hunting — Copilot Instructions

## Project Overview

A Python + web application for organizing amateur radio fox hunting
(ARDF — Amateur Radio Direction Finding) events. Covers equipment
builds, practice hunts, local (in-park) hunts, regional (car-based)
hunts, and social gatherings.

## Architecture

Mixed Python backend + TypeScript web frontend:

```
ham-fox-hunting/
├── backend/          # Python: API server, data models, business logic
│   ├── src/          # Application source
│   ├── tests/        # pytest unit tests
│   │   └── sample_results/  # Reference outputs per unit under test
│   ├── logs/         # Runtime log files (gitignored)
│   └── benchmarks/   # Performance benchmarks
├── frontend/         # TypeScript web UI
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   ├── types/
│   │   └── utils/
│   └── tests/
├── docs/             # Design decisions, architecture notes
└── .github/
```

## Build, Test & Lint Commands

These will be established as the project grows. Expected patterns:

```bash
# Python backend
pytest                        # full test suite
pytest tests/test_<module>.py # single test file
pytest -k "test_name"         # single test by name
python -m mypy src/           # type checking
flake8 src/                   # linting

# TypeScript frontend
npm run build
npm test
npm run test -- --testPathPattern=<file>
npx eslint src/
```

## Code Style

### Global

- **80 column line length limit** — applies to all languages and
  docstrings/comments.
- Avoid trailing whitespace. Explicit imports only (no wildcards).
- Follow SOLID principles; favor composition over inheritance.
- Include `main()` functions in modules where standalone execution
  is useful.

### Python

- 4 spaces per indent level. Follow PEP 8 (except where overridden
  here).
- **Type hints required** on all function signatures (parameters and
  return values). Use `typing` module for complex types.
- **PEP 257 docstrings** for all public modules, classes, methods,
  and functions. Wrap at 80 columns.
- Logging: `logger = logging.getLogger(__name__)` at module level.
  Log to `logs/` directory. Never log passwords, API keys, or PII.
- Testing: prefer `pytest`. Reference outputs in
  `tests/sample_results/<unit_name>/`.
- Error handling: use specific exception types; always clean up
  resources with `with` or `try/finally`.
- Dependencies: pin versions in `requirements.txt`; document why
  each dependency is needed.

### TypeScript / Web Frontend

- **TypeScript over JavaScript** for all new code (`.ts`/`.tsx`).
- 2 spaces per indent. Semicolons required. Single quotes for strings.
- Enable strict mode in `tsconfig.json`
  (`"strict": true, "noImplicitAny": true, "strictNullChecks": true`).
- Avoid `any`; use `unknown` with type guards if truly unknown.
- Named exports over default exports.
- Prefer `async`/`await` over Promise chains.
- Logging: Winston (Node.js) or Pino; configure via `LOG_LEVEL`
  environment variable.
- Testing: Vitest or Jest; Playwright for E2E.
- Import order: built-ins → external packages → internal (`@/`) →
  relative → type-only imports.
- File/directory names: kebab-case.

## Security

- Validate and sanitize all external inputs.
- Never hardcode secrets; use environment variables or a config file.
- Avoid `eval()` / `exec()`.
- Scan with CodeQL or `npm audit` before requesting PR review.

## Versioning & Branching

- Semantic versioning (MAJOR.MINOR.PATCH).
- Feature branches from `main`. Draft PRs titled `[WIP] ...` opened
  early. Remove `[WIP]` and mark ready when complete.

## Domain Vocabulary

- **Fox** — the hidden transmitter participants search for.
- **Hunt** — a single ARDF event (practice, local/park, or
  regional/car-based).
- **Hound** — a participant searching for the fox.
- **RDF** — Radio Direction Finding; using signal bearing to locate
  the fox.
- **Hide** — the physical location where the fox transmitter is
  placed.
