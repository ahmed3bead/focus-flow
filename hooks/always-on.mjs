import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

try {
  const configDir = process.env.CLAUDE_CONFIG_DIR || path.join(os.homedir(), ".claude");
  const flagPath = path.join(configDir, ".focus-flow-always");
  if (!fs.existsSync(flagPath)) process.exit(0);
  const scriptDir = path.dirname(fileURLToPath(import.meta.url));
  const skillPath = path.join(scriptDir, "..", "skills", "focus-flow", "SKILL.md");
  if (!fs.existsSync(skillPath)) process.exit(0);
  const body = fs.readFileSync(skillPath, "utf8")
    .replace(/^---[^\S\r\n]*\r?\n[\s\S]*?\r?\n---[^\S\r\n]*(?:\r?\n|$)/, "")
    .replace(/(?:\r?\n)+$/, "");
  process.stdout.write(
    "FOCUS FLOW ACTIVE (always-on). Match the user's language and Arabic register. " +
    '"stop focus mode" or "اقفل وضع التركيز" disables it for this session.\n\n' + body + "\n",
  );
} catch {
  process.exit(0);
}
