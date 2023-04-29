# Prompt Knowledge Sharing

{% hint style="info" %}
This document is still under review. We welcome active discussion on the [GitHub issue](https://github.com/AI-Native-Development/docs/issues/8).
{% endhint %}

## Description

Sharing prompts for generating code and using them as learning resources for team members is important.

## Problem

Working with AI such as GitHub Copilot can help write high-quality code, but for senior engineers, whether great code or high-performance code is good code for code reading is a different story. When programs are represented by excessively abbreviated code or language-specific advanced expressions, collaboration among engineers in a specific area may become difficult.

## Story

You are exploring what prompts to write to master GitHub Copilot. As a senior engineer, you collaborate with GitHub Copilot to produce great code through trial and error in implementing a certain feature. Another engineer on the same team who was watching you next to you said, "So you always write like that! I feel like I understand a little now how you always come up with great code."

You realize that the prompts you used to reach the best output through trial and error, as well as the process of trial and error itself, are important resources for team members to learn. At the same time, you discover the problem that prompts are not included in the output files, and you begin to think about how to share them.

## Context

GitHub Copilot has been introduced, but how to use it has not been shared as each engineer uses it individually. In addition, the prompts written by each engineer in GitHub Copilot are not shared.

## Solution

Discuss how to share prompts and write comments as a team and establish rules. It is desirable to make comments that also function as a document so that the prompts do not become noise.

The following patterns can be considered for sharing prompts:

* Directly write in the file
  By leaving the prompts in the file for the team to learn, team members can learn from each other's prompts. It is important to leave prompts in an appropriate balance so that they do not become noise. Additionally, some prompts can be converted into document or explanatory comments rather than in prompt form. Furthermore, prompts can be reviewed along with code reviews, promoting the development of engineers.
* Passive documentation
  Include some prompts in comments in pull requests or issues. This improves the readability of files containing code, but prompts cannot be referenced in the editor.
* Mob programming
  Host mob programming sessions to experience the development environment of senior engineers without leaving prompts in files or PR/issues. It is important to share what is learned here as a separate document.

## Resulting Context

The skills of the entire team will improve, and effective learning will be promoted through prompt sharing. The readability of the code will improve, and understanding of the code will be facilitated by comments that function not only as prompts but also as documents.
