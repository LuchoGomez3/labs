# labs

> **Repo de aprendizaje en progreso.** Esto no es un portfolio de proyectos
> terminados: son ejercicios cortos y spikes que voy armando mientras estudio.
> Muchas carpetas todavía están vacías y otras van a cambiar a medida que avance.

## Qué es esto

Vengo del desarrollo Full Stack y estoy encarando un plan de upskilling hacia
AI Engineering. Este repo junta los experimentos chicos de ese camino: cada
carpeta es un ejercicio autocontenido que responde una pregunta concreta.

La idea es simple: trabajar con sistemas que usan LLMs en producción exige
bastante más que saber llamar a una API. Hace falta backend sólido, infra que
se pueda reproducir, observabilidad y una forma de medir si los cambios de
prompt mejoran o rompen algo. Acá practico cada una de esas piezas por separado.

Los proyectos más grandes (un notetaker con RAG, un agente con MCP) van a vivir
en sus propios repos. Acá quedan solo los ejercicios cortos.

## Cómo está organizado

Cada carpeta lleva un número de dos dígitos. El primero indica el bloque:

| Bloque | Área |
|--------|------|
| `1x` | Backend |
| `2x` | Infra y cloud |
| `3x` | IA |
| `4x` | Prácticas del rol de AI Engineer |

## Índice

| # | Tema | Qué problema resuelve | Estado |
|---|------|-----------------------|--------|
| 11 | [pytest + FastAPI](./11-pytest-fastapi) | Testear endpoints contra un Postgres real | En curso |
| 12 | [Seguridad web](./12-seguridad-web) | CORS, rate limiting y checklist OWASP | Pendiente |
| 13 | [Colas con Celery](./13-colas-celery) | Procesar webhooks de forma asíncrona | Pendiente |
| 21 | [Docker avanzado](./21-docker-avanzado) | Multi-stage builds, healthchecks y networks | Pendiente |
| 22 | [Terraform: S3 + IAM](./22-terraform-s3-iam) | IaC básico: un bucket y un rol con permisos mínimos | Pendiente |
| 23 | [GitHub Actions + OIDC](./23-github-actions-oidc) | CI/CD a AWS sin credenciales de larga vida | Pendiente |
| 31 | [OpenTelemetry + Tempo](./31-otel-tempo) | Seguir el trace de un request que cruza microservicios | Pendiente |
| 32 | [Chunking y embeddings](./32-chunking-embeddings) | Comparar estrategias de chunking y su impacto en el retrieval | Pendiente |
| 33 | [Agente con tools](./33-agente-tools) | Armar un loop de agente con tool calling | Pendiente |
| 34 | [Servidor MCP](./34-mcp-server) | Escribir un servidor MCP propio | Pendiente |
| 41 | [Evals de prompts](./41-evals-prompts) | Regression testing de prompts | Pendiente |
| 42 | [Tracing con Langfuse](./42-langfuse-tracing) | Observabilidad de cadenas LLM | Pendiente |

## Convención de trabajo

Cada carpeta tiene su propio `README.md` con tres secciones:

1. **Pregunta de partida**: qué quiero averiguar o resolver con el ejercicio.
2. **Cómo correrlo**: los pasos para levantarlo y probarlo.
3. **Qué me llevé**: lo que aprendí, lo que me sorprendió y lo que haría distinto.

Todo levanta con Docker Compose: entrás a la carpeta, corrés
`docker compose up` y no hace falta instalar nada más en la máquina.
