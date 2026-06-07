import type { ConsensusResponse } from "../types/consensus";
import {
  buildConsensusMarkdown,
  buildMarkdownFilename,
  downloadMarkdown,
} from "../utils/markdownExport";

type ExportButtonProps = {
  result: ConsensusResponse | null;
};

function ExportButton({ result }: ExportButtonProps) {
  const isDisabled = !result;

  function handleExport() {
    if (!result) {
      return;
    }

    const generatedAt = new Date();
    const markdown = buildConsensusMarkdown(result, generatedAt);
    const filename = buildMarkdownFilename(generatedAt);
    downloadMarkdown(filename, markdown);
  }

  return (
    <button
      className="secondary-button"
      type="button"
      disabled={isDisabled}
      onClick={handleExport}
    >
      Export Markdown
    </button>
  );
}

export default ExportButton;
