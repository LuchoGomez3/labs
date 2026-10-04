# CLAUDE.md

Contexto para sesiones de Claude Code en este repo.

## Qué es este repo

`labs` junta los ejercicios y spikes de un plan de upskilling personal, de
Full Stack Developer a AI Engineer. No tiene un producto final: es un repo de
aprendizaje donde cada carpeta es un experimento autocontenido que se va
desarrollando con el tiempo.

- Los proyectos grandes (notetaker con RAG, agente con MCP) viven en repos
  propios, no acá. Acá van solo los ejercicios cortos.
- El README raíz es público. Tiene que dejar claro de entrada que es un repo de
  aprendizaje en progreso, no un portfolio de proyectos terminados.
- La documentación habla solo de qué se está aprendiendo y por qué.

## Estructura

Numeración de carpetas por bloque:

- `1x`: backend
- `2x`: infra y cloud
- `3x`: IA
- `4x`: prácticas del rol de AI Engineer

Las carpetas vacías llevan un `.gitkeep` para que git las versione.

Cuando cambie el estado de un tema (Pendiente, En curso, Terminado), hay que
actualizar la tabla índice del `README.md` raíz.

## Convenciones

- Cada carpeta tiene un `README.md` con tres secciones: **Pregunta de partida**,
  **Cómo correrlo** y **Qué me llevé**.
- Todo levanta con Docker Compose desde la carpeta del ejercicio.
- Cada ejercicio es autocontenido: no comparte código ni dependencias con otras
  carpetas.
- Documentación en español rioplatense, sin emojis en los títulos.

## Ramas

Se trabaja siempre desde `develop`: cualquier rama nueva sale de ahí. A `main`
no se commitea directo; solo recibe lo que viene de `develop`.

- Cada ejercicio tiene su rama `ejercicio/NN-nombre` (por ejemplo
  `ejercicio/11-pytest-fastapi`), creada desde `develop`. Ahí van los commits
  chicos e intermedios.
- Al terminar el ejercicio se mergea a `develop` con `--no-ff`. Ese merge
  commit agrupa el aprendizaje: el mensaje lleva la pregunta de partida y un
  resumen de qué me llevé.
- `develop` se mergea a `main` también con `--no-ff`.
- Nunca squash ni rebase de ramas ya mergeadas: `main` y `develop` tienen que
  compartir historia.
- Para ver un aprendizaje por línea: `git log --first-parent --oneline develop`.

## Skills y plugins

Si hace falta instalar skills, plugins o cualquier configuración de Claude Code,
se instalan **siempre a nivel de proyecto** (dentro de `.claude/` en este repo),
nunca a nivel global ni de usuario. La configuración global no se toca.
