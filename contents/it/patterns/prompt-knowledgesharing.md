# Prompt Knowledge Sharing

## Description

Sharing prompts and utilizing them as resources for team members to learn is important.

## Problem

While working with AI like GitHub Copilot can help in writing high-quality code, for senior engineers, whether great or highly-performant code is good code for code reading is a different story.
Overly condensed code or programs expressed in highly specific language expressions can make it difficult for engineers to collaborate on specific areas.

## Story

As you explore what kind of prompts you should write to master GitHub Copilot, you, as a senior engineer, work on implementing a certain feature and eventually come up with great code by working with GitHub Copilot through trial and error.
Another engineer on the same team who was watching you from the next seat said, "So that's how you always come up with great code! I think I understand now how you do it."

You realize that the prompts you created when you arrived at the best output through trial and error, as well as the trial and error process itself, are important resources for team members to learn.
At the same time, you discover the problem that the output file does not contain the prompt and start thinking about how to share it.

## Context

GitHub Copilot has been introduced, but its usage has not been shared among individual engineers.
Additionally, the prompts written by each engineer in GitHub Copilot are not shared.

## Solution

The team should consider how to share prompts and write comments, and establish rules. It is desirable to make the comment function as a document as well so that the prompt does not become noise.

The following patterns can be considered for prompt sharing:

* Directly Writing to the File
  By leaving prompts in a file for the team to learn, they can learn from other members' prompts. It is important to leave prompts in a proper balance so that they do not become noise. Additionally, some prompts can be converted into documentation or explanatory comments rather than in prompt form. Also, by reviewing the prompts along with the code review, engineers can be further developed.
* Passive Documentation
  Include some prompts as comments in pull requests or issues. The readability of files containing code is improved, but reference to the prompts cannot be made within the editor.
* Mob Programming
  While not leaving prompts in files or PR/Issues, hold mob programming sessions for senior engineers to experience the development environment. It is important to share what is learned here as documentation.

## Resulting Context

The team's overall skills are improved, and effective learning is promoted through prompt sharing.
By functioning as both a prompt and document, the readability of the code is improved, making it easier to understand.
