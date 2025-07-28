---
name: Bug report
about: Create a report to help us improve
title: 'Issue default title: [BUG] Module/Layer - Short summary'
labels: bug
assignees: aionet-protocol

---

name: Bug Report
description: Report a technical issue or malfunction
title: "[BUG] - "
labels: [bug]
body:
  - type: textarea
    attributes:
      label: Describe the issue
      placeholder: What happened? What did you expect?

  - type: input
    attributes:
      label: Affected module or repo (optional)
      placeholder: governance, sdk, layer2 bridge...

  - type: dropdown
    attributes:
      label: Severity
      options:
        - Minor (cosmetic, doesn’t affect function)
        - Moderate (feature partially broken)
        - Critical (consensus or validator failure)

  - type: textarea
    attributes:
      label: Steps to Reproduce (optional)
      placeholder: 1. Go to X… 2. Click Y… 3. Error appears

  - type: textarea
    attributes:
      label: Suggested fix or workaround (optional)
      placeholder: If known, include a temporary fix idea or file reference.
