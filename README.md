# Focus Flow | مسار التركيز

Action-first AI responses in English, Modern Standard Arabic, or Egyptian Arabic.

## Quick install

### Codex

Run:

```bash
codex plugin marketplace add ahmed3bead/focus-flow --ref main
codex plugin add focus-flow@focus-flow
```

Start a new conversation, then activate it with:

```text
$focus-flow
```

Verify the installation at any time:

```bash
codex plugin list
```

### Claude Code

Run:

```bash
claude plugin marketplace add ahmed3bead/focus-flow
claude plugin install focus-flow@focus-flow
```

Restart Claude Code, then type:

```text
/focus-flow
```

Verify the installation at any time:

```bash
claude plugin list
```

## Quick test

After activation, try:

```text
أنا محتار بين كذا حاجة ومش عارف أبدأ منين. ساعدني أختار أول خطوة.
```

The response should use natural Egyptian Arabic, lead with one clear action, and avoid unnecessary tangents.

## What it does

Focus Flow shapes AI responses so the next useful action is easy to see and execute. It automatically mirrors:

- English
- Modern Standard Arabic (العربية الفصحى)
- Egyptian Arabic (العامية المصرية)

It is an output style, not an ADHD diagnosis or medical tool.

## What changes

Focus Flow leads with the answer or next action, numbers real sequences, limits the visible working set, preserves progress across turns, removes tangents, and reports errors directly.

Arabic is not handled as a literal translation. The skill detects the user's current register, respects explicit language requests, preserves technical identifiers, and avoids exaggerated or artificial slang.

## Always-on mode for Claude Code

To load Focus Flow at the start of every Claude Code session, create this opt-in flag:

```bash
touch ~/.claude/.focus-flow-always
```

Remove that file to disable always-on loading.

## Update or remove

Codex:

```bash
codex plugin marketplace upgrade focus-flow
codex plugin remove focus-flow
codex plugin add focus-flow@focus-flow
```

Claude Code:

```bash
claude plugin marketplace update focus-flow
claude plugin uninstall focus-flow
claude plugin install focus-flow@focus-flow
```

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
