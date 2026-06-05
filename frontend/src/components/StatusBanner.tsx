import type { HealthStatus } from "../types/consensus";

type StatusBannerProps = {
  health: HealthStatus | null;
  error: string;
  isChecking: boolean;
};

function StatusBanner({ health, error, isChecking }: StatusBannerProps) {
  if (isChecking) {
    return <div className="status-banner neutral">Checking backend health...</div>;
  }

  if (error) {
    return <div className="status-banner error">{error}</div>;
  }

  if (health) {
    return (
      <div className="status-banner success">
        Backend status: {health.status} ({health.service})
      </div>
    );
  }

  return <div className="status-banner neutral">Backend status not checked.</div>;
}

export default StatusBanner;
