# AI Friendly Documentation

## Description

Creating documentation in a format that can be understood by AI, not just engineers who write code, can improve team productivity as a whole. For example, database table definitions can be written in Markdown and managed as documentation in Git, rather than in PowerPoint or Excel.

## Problem

Various documents are necessary for product development, including requirement definitions, design documents, architecture overviews, infrastructure configuration specifications, and test case documents. While formats like PowerPoint and Excel are commonly preferred, AI cannot read those documents. Additionally, managing binary files in Git repositories is not a best practice.

## Story

Your team has introduced GitHub Copilot for Business, and the engineers are pleased with the shortened work time. The team feels like it has doubled in size with the help of AI. However, the problem is that AI can only do what the engineers instruct it to do, and it does not understand the context that the engineers have. Therefore, the engineers need to input a lot of natural language to convey context to the AI. As a result, there has been an increase in copying and pasting text from articles provided by the PM or converting PowerPoint slides and complex Excel files created by bosses to Markdown or CSV format that AI can read.

"If it were written in CSV or Markdown from the beginning, it would be much better!"

## Context

Many projects are managed with documentation in formats like PowerPoint or Excel. People other than engineers are communicating outside of GitHub, and final decisions are not being saved in the repository. While the documents are summarized in a way that is easy for AI to read, they are not being managed centrally.

## Solution

The team should strive to create text-based documents, such as Markdown or CSV. Documents containing context that should ultimately be passed on to the engineer and AI should be stored in Git repositories. The repository should be easy to call from outside the workspace, using Git Submodule and other methods. If necessary, copy the text of the file to the comments section and pass it on to AI as a prompt.

## Known Instance

* Prepare a table definition file in CSV or Markdown format and associate it with the creation of migration files and interfaces.
* Convert infrastructure definitions summarized in natural language into configuration files for Infrastructure as Code, such as Terraform.
* Convert test case documents to test files. This works more effectively for certain patterns, such as API tests. This makes test-driven development easier.

## Resulting Context

* Engineers can create more code with less effort, leading to reduced workload.
* Project owners and product managers can obtain results from engineers more quickly.
* Members who do not normally write code can use GitHub to collaborate and become accustomed to judging the context that engineers need and the context that should be provided to AI, allowing for appropriate development using AI.
* Since changes to documents are tracked, it is possible to track everything, including when decisions were made, beyond just the code.
* There will be no discrepancy between documents and implementation.

## Note

* Currently, GitHub Copilot has limited capabilities for reading files. If you are writing in Python, only the Python code in the open tab will be read and passed on to the prompt. Therefore, copy the necessary text from AI-friendly documents and paste it into the comments section of the ```.py``` file.
* This pattern is not effective for all documents. Misjudging which documents should be stored can result in a large amount of unnecessary documents in the repository, reducing search performance. Try to prioritize writing implementation-related text in Markdown.
* There is a limit to the number of tokens that can be passed to AI. Try to make each section of the text concise and with as few dependencies as possible between previous and subsequent sentences.
