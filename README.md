# DairyTwinOS

DairyTwinOS is an enterprise roadmap and reference architecture for a dairy plant digital twin platform. It describes the path from a foundation release through an ultimate enterprise deployment that combines a 3D digital twin, SCADA, MES, analytics, AI assistance, and production-grade deployment patterns.

## Documentation

- [Enterprise master architecture](docs/architecture.md) - the full Mermaid architecture map for product versions, platform modules, dairy equipment, backend services, data stores, AI models, users, and deployment targets.
- [Project changelog](CHANGELOG.md) - notable repository updates and documentation changes.

## Architecture at a glance

DairyTwinOS is organized around four major delivery layers:

1. **Experience layer**: React + Three.js for immersive plant visualization and Streamlit for dashboards, analytics, reports, maintenance, production, and Power BI-style views.
2. **Service layer**: FastAPI services for REST, WebSocket, OPC UA, MQTT, authentication, notifications, Redis, and Celery workloads.
3. **Data layer**: PostgreSQL domains for users, equipment, telemetry, production, maintenance, recipes, inventory, energy, quality, alarms, and audits.
4. **Enterprise layer**: Docker, Docker Compose, Kubernetes, GitHub, GitHub Actions, and Nginx packaging toward a production enterprise system.

## Version roadmap

| Version | Focus | Outcome |
| --- | --- | --- |
| V1 | Foundation | Establish the baseline architecture, documentation, and initial platform boundaries. |
| V2 | Professional 3D | Introduce a professional 3D dairy plant visualization layer. |
| V3 | Interactive Digital Twin | Add equipment selection, metadata, labels, animations, process flows, and plant interactions. |
| V4 | SCADA | Add alarms, trends, historian data, events, notifications, tag browsing, and real-time dashboards. |
| V5 | Enterprise MES | Add production orders, batch management, recipes, inventory, dispatch, reporting, and cleaning schedules. |
| V6 | AI Platform | Add AI assistance, predictive maintenance, root cause analysis, anomaly detection, and recommendations. |
| V7 | Smart Factory | Connect operational intelligence across production, maintenance, quality, energy, and utilities. |
| V8 | Ultimate Enterprise | Package the full production enterprise system and final deliverable. |

## Repository structure

```text
.
├── README.md
├── CHANGELOG.md
└── docs/
    └── architecture.md
```

## Suggested next implementation steps

- Convert the architecture roadmap into tracked implementation milestones.
- Scaffold the React, Streamlit, backend, shared, and deployment directories shown in the architecture.
- Add validation for Mermaid diagrams in CI so documentation changes remain renderable.
- Define API and database contracts for telemetry, equipment, production, maintenance, quality, and alarm history.
