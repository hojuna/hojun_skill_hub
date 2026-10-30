---
name: build-api
description: Build or modify a small REST or HTTP backend with endpoints, request validation, persistence, status codes, and repeatable tests. Use for FastAPI, Flask, Express, Node, or an existing server project.
---

# Implement the API contract with minimal changes

1. Read task API examples/OpenAPI/README and the existing server's routing/storage style. Preserve framework, dependencies, package scripts and conventions.
2. Create an endpoint table: method + path, request fields, response schema, success status, and failure status. Follow the task's exact contract over personal preferences.
3. Implement a complete endpoint first, including input validation, business logic, storage interaction and error handling. Add the remaining required routes.
4. Cover IDs not found, malformed/empty payload, duplicate/conflicting writes and invalid state transitions when applicable. Don't return success for an operation that failed.
5. Test actual HTTP behavior (provided tests, framework test client, curl to local server) for at least one success and one failure per critical endpoint.
6. Confirm application startup command and declared port. Handle environment configuration without embedding credentials or logging secrets.
7. If frontend is part of the assignment, integrate only after a minimal API response works.

## Useful evidence

- Endpoint and expected schema.
- The exact command/test run and results.
- Actual error status and response for a negative case.
- Which persistence mechanism was used and what it guarantees.

Do not add authentication, cloud deployment, microservices or a large ORM unless required. Never export the assignment or results to an external backend.
