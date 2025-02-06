# Planventure

# Development Environment Setup using Dev Containers

This guide will help you set up your development environment using **Dev Containers** for both the **Frontend** and **Backend** applications. Utilizing Dev Containers ensures a consistent and isolated environment, making it easier for new contributors to get started without worrying about system-specific configurations.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Setting Up Dev Containers](#setting-up-dev-containers)
  - [Frontend Dev Container](#frontend-dev-container)
  - [Backend Dev Container](#backend-dev-container)
- [Running the Applications](#running-the-applications)
- [Accessing the Applications](#accessing-the-applications)
- [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

1. **Docker Desktop**  
   - [Download Docker Desktop](https://www.docker.com/products/docker-desktop/)
   - Ensure Docker is running.

2. **Visual Studio Code (VS Code)**  
   - [Download VS Code](https://code.visualstudio.com/)

3. **VS Code Extensions**  
   - **Remote - Containers**  
     Install from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

4. **Git**  
   - [Download Git](https://git-scm.com/downloads)
   - Ensure Git is available in your system's PATH.

---
## Getting Started

1. **Clone the Repository**

   Open your terminal and run:

   ```bash
   git clone https://github.com/github-samples/planventure.git
   
   cd planventure

   code .
   ```

2. **Setting Up Dev Containers**
   
   There are 2 separate Dev Containers for the Frontend and Backend applications for this project. Each container will run in its own VS Code window with distinct color themes to differentiate between them.

   **Frontend Dev Container**
   
   Color Theme: Blue

   1. From the VS Code window open to the root of this project repo, run `Dev Containers: Reopen in Container` from the Command Palette (F1) and select `Planventure Frontend`.

   2. VS Code will then start up both containers, reload the current window and connect to the selected container.

  **Backend Dev Container
  
  Color Theme: Purple

  1. From the open VS Code instance for the Frontend app, open a new window using File > New Window.

  2. Open this project at root level in the current window. (This should be the same folder you opened when you first cloned the repo)

  3. Run `Dev Containers: Reopen in Container` from the Command Palette (F1) and select `Planventure Backend`.

  4. VS Code will then start up both containers, reload the current window and connect to the selected container.

  You can now interact with both containers from separate windows.

---

## Running the Applications

With both Dev Containers set up, your development environment is ready. Here's how to run and interact with both the frontend and backend applications.

### Frontend
1. Development Server
   - The frontend Dev Container automatically runs the development server using npm run dev.
   - Port: 5173 (forwarded to your host machine).

2. Accessing the Frontend

   - Open your browser and navigate to:
http://localhost:5173

3. Hot Reloading
   - Any changes made to the frontend code within the Dev Container will automatically reflect in the browser without needing a manual refresh.

### Backend
1. Development Server
   - The backend Dev Container automatically runs the Flask development server.
   - Port: 5000 (forwarded to your host machine).

2. Accessing the Backend API
   - Open your browser or API client (e.g., Bruno) and navigate to:
http://localhost:5000

3. Hot Reloading
   - Any changes made to the frontend code within the Dev Container will automatically reflect in the browser without needing a manual refresh.

---

## Troubleshooting

If you encounter issues while setting up or running the Dev Containers, consider the following steps:

1. Docker Not Running
   - Ensure Docker Desktop is installed and running.
   - Verify Docker's status by running docker info in your terminal.

2. Port Conflicts
   - Ensure that ports 5173, 5000, and 5432 are not being used by other applications.
   - If conflicts exist, adjust the docker-compose.yml and devcontainer.json to use different ports.

3. Dependency Issues
   - Check the postCreateCommand in each devcontainer.json to ensure dependencies are installing correctly.
   - View the integrated terminal in VS Code for any installation errors.

4. Environment Variables
   - Verify that all necessary environment variables are correctly set in docker-compose.yml.
   Ensure that the frontend's `BASE_API_URL` points to the correct backend service (http://localhost:5000).

5. File Permissions
   - Ensure that your user has the necessary permissions to read and write to the project directories.
   - On Unix-based systems, you might need to adjust permissions using chmod or chown.

6. Rebuilding Containers
   - If changes are made to `Dockerfile` or `docker-compose.yml`, rebuild the containers:
   ```sh
   docker-compose up --build
   ```

7. Clearing Docker Cache
   Sometimes, cached layers can cause issues. To rebuild without cache:
   ```sh
   docker-compose build --no-cache
   ```

8. Check Logs
   - Use Docker logs to identify issues:
   ```sh
   docker logs planventure-frontend-1
   docker logs planventure-backend-1
   ```