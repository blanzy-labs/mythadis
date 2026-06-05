import type { HealthStatus } from "../types/consensus";

const backendUrl = import.meta.env.VITE_BACKEND_URL ?? "http://localhost:8000";

export async function getBackendHealth(): Promise<HealthStatus> {
  const response = await fetch(`${backendUrl}/health`);

  if (!response.ok) {
    throw new Error(`Backend health check failed with ${response.status}`);
  }

  return response.json();
}
