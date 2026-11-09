# Handoff: autonomous systems research rebrand (website and GitHub profiles)

status: done, in review (draft PRs)
date: 2026-11-09

## State
Owner directive 2026-11-09: stop quantum-first branding; present Rowan as an autonomous
AI systems researcher (not a software engineer). Career thread: network
modeling since the first transportation job, FHWA national Tour-Based Model System,
Deloitte analytics and ML, AARP Livability Index, QNFO autonomous research system.

Changed on branch `claude/project-thread-parcv4` in:
- rwnq8.github.io: index.html, papers/, ai/, ai/declaration.md, llms.txt, github-profile-README.md
- rwnq8/rwnq8: README.md (profile page)
- rwnq8/.github: README.md (replaced stale quantum copy, removed patent and publication-count claims)
- rwnq8/agent-operating-system and rwnq8/AIOS: research-context note in README.md

## Decisions
- Every factual claim comes from rwnq8/resume RESUME.md; nothing new invented.
- Quantum papers kept on the publications page and AI page only as one application of the JPCUB metric, removed from home and profile.
- Skills badges for programming languages removed; replaced with focus areas.

## Next
- Align copy with the brand source-of-truth doc from the positioning thread when it lands.
- Repository descriptions (About field) are not editable through this session's tools;
  rwnq8/resume still says "Quantum Computing" there.

## Verify
- `curl -s https://rwnq8.github.io/ | grep -c "Autonomous AI systems researcher"` returns 1 or more after merge.
- `curl -s https://rwnq8.github.io/llms.txt | grep -c "Autonomous AI systems researcher"` returns 1 or more.
