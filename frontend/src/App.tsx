import { useState } from "react";

import { getBackendHealth } from "./api/client";
import StatusBanner from "./components/StatusBanner";
import type { HealthStatus } from "./types/consensus";

function App() {
  const [health, setHealth] = useState<HealthStatus | null>(null);
  const [isChecking, setIsChecking] = useState(false);
  const [error, setError] = useState("");

  async function handleHealthCheck() {
    setIsChecking(true);
    setError("");

    try {
      const result = await getBackendHealth();
      setHealth(result);
    } catch {
      setHealth(null);
      setError("Backend is unavailable. Start the backend and try again.");
    } finally {
      setIsChecking(false);
    }
  }

  return (
    <main className="app-shell">
      <section className="intro">
        <p className="eyebrow">Mythadis Labs</p>
        <h1>Mythadis Consensus Engine</h1>
        <p className="tagline">The books are fiction. The questions are real.</p>
      </section>

      <section className="workspace" aria-label="Application status">
        <StatusBanner health={health} error={error} isChecking={isChecking} />
        <button type="button" onClick={handleHealthCheck} disabled={isChecking}>
          {isChecking ? "Checking..." : "Check backend health"}
        </button>
      </section>

      <p className="placeholder">
        Consensus workflow will be added in a later slice.
      </p>
    </main>
  );
}

export default App;
