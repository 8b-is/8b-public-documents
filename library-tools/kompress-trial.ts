// Run the local, pure rewriter only: no pipeline, hosted API, or persistence.
// Usage: bun kompress-trial.ts REPOSITORY INPUT OUTPUT LEVEL
import { pathToFileURL } from "node:url";
import { resolve } from "node:path";
const [repository, input, output, level] = Bun.argv.slice(2);
if (!repository || !input || !output || !["0", "1", "2"].includes(level)) {
  throw new Error("Expected REPOSITORY INPUT OUTPUT LEVEL (0, 1, or 2)");
}
const module = await import(pathToFileURL(resolve(repository, "src/rewriter.ts")).href);
const original = await Bun.file(input).text();
await Bun.write(output, module.compressMessage(original, Number(level)));
