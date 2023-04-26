# AI Native Documentation

## Description

Creating documentation in a format that can be understood by AI, not just engineers who write code, can improve team productivity overall.
For example, instead of writing database table definitions in PowerPoint, they can be written in Markdown and managed in Git as documentation.

## Problem

Various documents are necessary for product development, such as requirement definitions, design documents, architecture overview diagrams, infrastructure configuration specifications, and test case documents.
Generally, formats such as PowerPoint and Excel are preferred, but AI cannot read those documents.
Additionally, managing binary files in a Git repository is not a best practice.

## Story

Your team has introduced GitHub Copilot for Business.
Engineers are happy that their working time is being reduced.
The team feels like they have doubled in size with the help of AI.
However, the problem is that AI can only do what the engineer instructs it to do.
Furthermore, since AI does not understand the context that the engineer possesses, the engineer must input a large amount of natural language to convey the context to the AI.
As a result, there has been an increase in tasks such as copying and pasting text provided by the PM or converting PowerPoint slides and complexly formatted Excel files created by superiors into Markdown or CSV format that AI can read.

"It would be great if they were written in CSV or Markdown from the beginning!"

## Context

In many projects, documentation is managed in formats such as PowerPoint and Excel.
People other than engineers communicate in places other than GitHub, and the final decision is not saved in the repository.
The documents are summarized in a form that is easy for AI to read, but they are not centrally managed.

## Solution

The team strives to create text-based documents such as Markdown and CSV.
The documents that should ultimately be given to engineers and AI containing the context are saved in a Git repository.
Engineers provide context to AI by calling that repository in the current workspace using mechanisms such as git submodule and opening the file with a tab.

## Known Instance

* Prepare table definition files in CSV or Markdown format and associate them with migration files or interface creation.
* Convert infrastructure definitions summarized in natural language to configuration files for Infrastructure as Code such as Terraform.
* Convert test case documents to test files.
This is more effective for those that have certain patterns such as API tests.
This makes test-driven development easier.

## Resulting Context

* Engineers can create more code with less effort, resulting in reduced man-hours.
* Project owners and product managers can receive deliverables from engineers faster.
* Even members who do not usually write code can become accustomed to determining the context required by engineers and AI by collaborating using GitHub, enabling appropriate development using AI.
* Since change histories are recorded in documents, tracking for everything other than code, such as who made what changes at what time and when decisions were made, becomes possible overall.
* The gap between documents and implementation is eliminated.

## Note

* Currently, the files that GitHub Copilot can read are limited.
It is desirable that if you are writing Python, it is Python code.
Therefore, copying a Markdown file and making it a commented-out Python document and using it as a hit is a good idea.
* This pattern is not effective for all documents.
If you make a mistake in deciding the structure of the repository or which documents to store, a large number of unnecessary documents may be generated in the repository, and search performance may deteriorate.
* The number of tokens that can be passed to AI is limited.
Try to keep each section of each sentence concise so that it does not have too many dependencies on the surrounding sentences.
