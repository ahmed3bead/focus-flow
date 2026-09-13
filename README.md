# Focus Flow | مسار التركيز

Focus Flow shapes AI responses so the next useful action is easy to see and execute. It automatically mirrors:

- English
- Modern Standard Arabic (العربية الفصحى)
- Egyptian Arabic (العامية المصرية)

It is an output style, not an ADHD diagnosis or medical tool.

## What changes

Focus Flow leads with the answer or next action, numbers real sequences, limits the visible working set, preserves progress across turns, removes tangents, and reports errors directly.

Arabic is not handled as a literal translation. The skill detects the user's current register, respects explicit language requests, preserves technical identifiers, and avoids exaggerated or artificial slang.

## Install in Codex

Install this repository as a plugin, then invoke:

```text
/focus-flow
```

Or ask:

```text
Use $focus-flow and match my language and Arabic register automatically.
```

## Install in Claude Code

Add the repository as a marketplace and install `focus-flow`, then restart Claude Code and invoke `/focus-flow`.

To make Claude Code load the mode at session start, create this opt-in flag:

```bash
touch ~/.claude/.focus-flow-always
```

Remove that file to disable always-on loading.

## Development

Run the structural tests:

```bash
python3 -m unittest discover -s tests -v
```

Behavioral cases for English, formal Arabic, Egyptian Arabic, mixed technical language, safety, and explicit overrides live in `evals/cases.jsonl`.

## Credits

Inspired by [i-have-adhd](https://github.com/ayghri/i-have-adhd) by Ayoub G. Focus Flow has its own bilingual language policy, wording, tests, and identity.

## License

MIT. See `LICENSE` and `NOTICE`.
