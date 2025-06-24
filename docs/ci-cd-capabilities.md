# CI/CD Capabilities with iPaaS CLI Tool

This document outlines what **can and cannot** be achieved using the CLI tool provided by our iPaaS partner within our CI/CD pipeline.

---

## ✅ Supported Actions (What We Can Do)

The CLI tool enables us to **pull**, **update**, and **delete** various integration components. The typical workflow involves pulling existing configurations from a workspace, updating them locally (e.g., in a Git repository), and pushing changes back to the workspace.

The following resources are supported:

* **Actions** – update, delete
* **App Data Schemes** – update, delete
* **App Events** – update, delete
* **Data Sources** – update, delete
* **Field Mappings** – update, delete
* **Flows** – update, delete
* **Integrations** – update connector versions, delete
* **Workspace Management** – ability to push/pull configurations across multiple workspaces

### Multi-Workspace Support

The CLI supports a multi-workspace configuration, enabling CI/CD pipelines for environments like:

* `dev`
* `staging`
* `production`

Each workspace can be targeted independently, using a shared configuration setup.

---

## ❌ Unsupported Actions (What We Cannot Do)

The CLI tool has some limitations. Specifically, it **does not support creating new entities** or managing certain aspects of the platform.

### Not Supported:

* ❌ **Creation of entities** (e.g., new flows, actions, integrations, etc.)
* ❌ **Managing users** (e.g., adding or removing users)
* ❌ **Adding custom fields to workspaces**
* ❌ **Changing workspace settings**
* ❌ **Configuring integrations** (configuring authentication methods, etc.)
* ❌ **Managing connections**
* ❌ **Managing organizations**

---

## Summary

| Capability                     | Supported |
| ------------------------------ | --------- |
| Pull existing workspace config | ✅         |
| Update/delete components       | ✅         |
| Push changes to workspace      | ✅         |
| Create new components          | ❌         |
| Manage users/connections/orgs  | ❌         |
| Multi-workspace configuration  | ✅         |

---

Let me know if you'd like this converted into a Markdown file or need sections on how to structure Git repos or example commands.
