# AI Readability of Documents

Currently, there is a buzz around a development tool called GitHub Copilot, which has AI autocomplete features.
There seems to be a misconception that this tool is for engineers only.
It could be said that this is half true and half false.
Indeed, GitHub Copilot has an amazing ability to change the way engineers work.
However, as the way engineers work changes, they themselves are inevitably changing as well.
If you are in a position of a PM or PO, this is an important issue for you too.
This is because your team is expected to have engineers working at their maximum performance, implementing the requirements you defined as quickly as possible.
From now on, even if you are not an engineer, you will need to create documents with **AI readability** so that the engineers on your team can collaborate with AI.

## Documentation Culture and AI Development

In recent years, AI technology has developed rapidly, and models such as LLM (Language Model) have attracted attention.
The development platform for OSS, GitHub, has also ventured into the field of AI development.
A prime example is "GitHub Copilot".
Interestingly, there are similarities between the AI-driven development style and the OSS development style in terms of collaboration.
Specifically, both are primarily document-based, and the documents are often represented in formats like Markdown.
Formats like Markdown are designed for representing structured information and have features that make them easier for AI to analyze than PowerPoint or Excel files.
As a result, they can also contribute to improving the quality of AI-generated code.

AI prefers simple csv files over complex Excel tables filled with metadata.
Suppose you, as a PM, compile customer requirements into a list and gather the necessary information for the database.
If the requirements are written in code in a csv file or expressed in Markdown, engineers can easily convert them into code.
However, if you compile them in an Excel document that is easy for you to read, the engineer will first have to copy, format, and convert it into code.
Which would be better?

Furthermore, in OSS development, the quality of documentation can directly affect the success or failure of a project.
Since OSS is open to anyone, proper documentation can facilitate the smooth participation of new developers.
Therefore, documentation is highly valued in OSS development.
In AI development as well, it is believed that the establishment of a documentation culture will enable more efficient and high-quality development.
Even if you are not an engineer, your natural language written in Markdown can significantly contribute to the final output, which is the code.

## Creating Context-Rich Documentation

As OSS development matures, cross-border and cross-time-zone collaboration emerges.
However, geographical distance and time dispersion can make synchronous communication difficult.
For example, noon in New York is night in Tokyo, and you would want to avoid waking up Japanese committers at night or interrupting their family time.
As a result, document-based documentation is generally preferred.
This may be something like RFCs or design documents, or comments written in GitHub Issues.
These Issue comments are also called passive documentation and are a form of documentation.

What is important here is to properly document, including the context.
It is difficult to convey non-verbal communication, nuances, and atmosphere that are transmitted through Zoom or face-to-face conversations across time zones and asynchronously.

Let's think about AI-assisted development.
For example, will GitHub Copilot attend Zoom meetings? Will it be in the team room saying, "Hey, I'm GitHub Copilot, let's have a quick check-in meeting"?
The answer is probably no.
You need to convey all context to AI in writing.
Even when communicating asynchronously, like in OSS development, it is necessary to create proper documentation.

Of course, there are differences in the granularity of documentation between OSS development and AI-assisted development.
If you write "I want to fix this bug" in GitHub Issues, someone might come up with a solution, but AI cannot handle that level of complexity.
However, there are definitely areas where AI excels.
For example, if you want to express cloud architecture as Infrastructure as Code, it is better to write it in Mermaid or describe it in natural language, rather than drawing it in PowerPoint.

What is being said here is not that all communication needs to be documented.
You and your team need to consider at what level of documentation, how, and where to leave it.

## Interactive Documentation

With features like GitHub Copilot for Docs included in GitHub Copilot X, AI can create the perfect document for you.
The document you create can also serve as onboarding material for the next person.

Previously, you might have had to gather the necessary information and create onboarding materials for new engineers, but in the future, AI will take on this role.
You can embed all the knowledge you have in the documentation as a single, reliable source of information.

This approach can be seen explicitly in Atlassian's documentation.
If you read their documentation with AI in mind, you might discover something new.
The documents you write can seem as if they have a personality.

With GitHub Copilot for Docs, you can virtually create an "engineer who knows the entire codebase and history."
However, this requires sufficient documentation as mentioned earlier.
https://www.atlassian.com/ja/work-management/knowledge-sharing/documentation/importance-of-documentation

## The Gap Between Natural Language and Implementation is Closing

As you may have noticed by now, the distance between natural language and implementation is getting much closer.
As mentioned earlier, from an educational perspective, writing prompts and code in one place could eventually lead to the creation of a single-file document.
This kind of change is very intriguing.

## Checklist

- [ ] Does your team currently have a documentation culture? If so, what is it like? If not, what is preventing it?
- [ ] Consider what kind of documentation your team needs to collaborate with AI.
- [ ] There's no need to document everything. Start by writing documentation in Markdown within your capabilities.
