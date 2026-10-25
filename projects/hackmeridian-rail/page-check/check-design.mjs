// Design fidelity: every colour, font and radius in the page comes from the Radox Signal tokens.
// Usage: node check-design.mjs <rio-miami-rail page dir> <radox-internal frontend/src/index.css>
// Reads only the token values from the Radox file. Exit 0 when clean; the last line is the number of violations.
import { readFileSync } from "node:fs";
import { join } from "node:path";

const [page, tokensFile] = process.argv.slice(2);
const radox = readFileSync(tokensFile, "utf8");
const dark = radox.slice(radox.indexOf(".dark {"), radox.indexOf("}", radox.indexOf(".dark {")));
const norm = (v) => v.replace(/\s+/g, " ").trim();
const tokens = Object.fromEntries([...dark.matchAll(/(--[\w-]+):\s*([\d.]+ [\d.]+% [\d.]+%)/g)].map((m) => [m[1], norm(m[2])]));
const radius = /--radius:\s*([^;]+);/.exec(radox)[1].trim();
const fonts = new Set(["Inter", "'Inter'", "system-ui", "sans-serif", "var(--font-body)"]);
const NAMED = /\b(white|black|red|green|blue|gray|grey|silver|yellow|orange|purple|pink|navy|teal|lime|olive|maroon|aqua|fuchsia)\b/;

const bad = [];
const html = readFileSync(join(page, "index.html"), "utf8");
const css = [...html.matchAll(/<style>([\s\S]*?)<\/style>/g)].map((m) => m[1]).join("\n") + "\n" + [...html.matchAll(/style="([^"]*)"/g)].map((m) => m[1]).join("\n");
const js = ["app.js", "globe.js"].map((f) => [f, readFileSync(join(page, f), "utf8")]);

// :root values must equal the .dark token of the same name (radius and font from the same file)
const root = /:root\s*{([^}]*)}/.exec(css)?.[1] ?? "";
const local = {};
for (const m of root.matchAll(/(--[\w-]+):\s*([^;]+);/g)) {
  const [n, v] = [m[1], norm(m[2])];
  local[n] = v;
  if (n === "--radius") { if (v !== radius) bad.push(`:root ${n} ${v} (Radox ${radius})`); }
  else if (n === "--font-body") { if (!/^'Inter', system-ui, sans-serif$/.test(v)) bad.push(`:root ${n} ${v}`); }
  else if (tokens[n] !== v) bad.push(`:root ${n} ${v} (Radox .dark ${tokens[n] ?? "no such token"})`);
}
const scan = (where, text) => {
  for (const m of text.matchAll(/#[0-9a-fA-F]{3,8}\b(?![-\w])/g)) bad.push(`${where}: hex ${m[0]}`);
  for (const m of text.matchAll(/\b(rgba?|hsla?|oklch|lab|lch|hwb)\(\s*((?:[^()]|\([^()]*\))*)\)/g)) {
    const arg = m[2];
    const v = /^var\((--[\w-]+)\)(\s*\/\s*[\d.]+)?$/.exec(arg.trim());
    if (m[1] === "hsl" && v && (local[v[1]] ?? tokens[v[1]])) continue;
    if (m[1] === "hsl" && /^\$\{/.test(arg.trim())) continue; // JS reads the CSS token at run time
    bad.push(`${where}: colour ${m[0]}`);
  }
  for (const m of text.matchAll(/(?:^|[;{\s])(color|background(?:-color)?|border(?:-\w+)?|outline|fill|stroke)\s*:\s*([^;}]+)/g))
    if (NAMED.test(m[2].replace(/var\([^)]*\)/g, ""))) bad.push(`${where}: named colour in ${m[1]}: ${m[2].trim()}`);
  for (const m of text.matchAll(/font-family\s*:\s*([^;}]+)/g))
    for (const f of m[1].split(",").map((x) => x.trim())) if (!fonts.has(f)) bad.push(`${where}: font ${f}`);
  for (const m of text.matchAll(/(?:^|[;{\s])font\s*:\s*([^;}]+)/g)) {
    const fam = m[1].replace(/^.*?\d+(px|rem|em)(\/[\d.]+)?\s+/, "");
    for (const f of fam.split(",").map((x) => x.trim())) if (!fonts.has(f)) bad.push(`${where}: font ${f}`);
  }
  for (const m of text.matchAll(/border-radius\s*:\s*([^;}]+)/g)) if (m[1].trim() !== "var(--radius)") bad.push(`${where}: radius ${m[1].trim()}`);
};
scan("index.html css", css);
for (const [f, t] of js) {
  scan(f, t.replace(/"#[\w-]+"/g, "")); // element ids such as "#verify" are selectors, not colours
  for (const m of t.matchAll(/["'`](\d{3} [\w ]*?\d+px )?([^"'`]*?), system-ui, sans-serif["'`]/g)) if (!/(^|\s)Inter$/.test(m[2])) bad.push(`${f}: canvas font ${m[0]}`);
  for (const m of t.matchAll(/tok\("(--[\w-]+)"/g)) if (!tokens[m[1]]) bad.push(`${f}: canvas colour ${m[1]} is not a Radox token`);
}
for (const b of bad) console.log("FAIL", b);
console.log(`tokens ${Object.keys(tokens).length}, page :root ${Object.keys(local).length}, js ${js.length} files`);
console.log(bad.length);
process.exit(bad.length ? 1 : 0);
