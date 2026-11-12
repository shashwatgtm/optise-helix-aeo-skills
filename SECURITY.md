# Security policy: AEO and GEO Toolkit for B2B Websites

Please report security problems privately by email to shashwat@gtmhelix.com with the subject "Security report: optise-helix-aeo-toolkit". Include the file and line, what could go wrong, and how to reproduce it. We aim to reply within 5 working days.

Please do not open a public GitHub issue for a security problem.

What this plugin contains: Claude skills (Markdown) and reference files. It contains no scripts or other program files. The FITq and RACE audits fetch the http or https address the user gives, with Claude's own tools, following `references/page-fetch-method.md` in each of those two skills, and follow up to 5 redirects. Before every connection (the first address and each redirect) the method looks up the host name once and refuses the request unless every address found is a public internet address, so loopback, private network, link-local, cloud metadata and other reserved addresses are refused, and it then connects to that checked address. It also refuses addresses written as integers, octal or hex numbers, web addresses with a user name or password, ports other than 80 and 443, and responses that are not HTML. Each refusal is reported as an error and nothing is fetched. The plugin has no server, no hooks and no MCP server, and it stores no data.
