---
name: "Copilot Snnipet Handling"
description: "GitHub Copilot uses LLM to generate code. And LLM has a token limitation. You need to know that GitHub Copilot doesn't see all of your code."
category: "editor"
authors: [yuhattor] 
platforms: [copilot]
level: 100
---

## Token Handling

### Description

GitHub Copilot, which utilizes OpenAI's Large Language Models (LLM) to generate code, has a limitation on the number of tokens it can process. As of 2023, it doesn't see all of the code that's open in the editor and doesn't receive every token. This means that users must carefully limit the context provided to GitHub Copilot. Notably, Copilot doesn't have access to external repositories or source code placed in GitHub Enterprise Cloud.

The files that GitHub Copilot uses for suggestions are primarily the currently open file and other tab files adjacent to it (basically with the same file extension). To make accurate suggestions, it's essential to have only the relevant files open. The following is a checklist as of August 2023. The types of files that GitHub Copilot includes as snippets may change in the future, but practices such as "closing unnecessary files" will likely have a positive impact on your coding even if you were not using GitHub Copilot.

- Open the files you need to refer to
- Close unnecessary files
- If there is an .md file you want to refer to, copy it and comment it out

If your first language is not English, it's worth noting that English is a very token-efficient language. Expressing the same concept in Japanese or other languages might consume more tokens. Writing comments in English could save tokens, but be mindful of your team's language preferences as it might hinder development speed.  Then it's putting the cart before the horse.

### Exercise

- **Exercise 1**: Experiment with reducing the code context sent to Copilot in a complex project. Observe how this affects the suggestions provided.
- **Exercise 2**: Discuss with your team the best practice for commenting based on language efficiency and understanding within the team.

### Checklist for Further Learning

- What strategies can be employed to provide the necessary context to Copilot without exceeding token limitations?
- How does the choice of language in comments affect collaboration within a diverse team?