# AI-Native Documentation: AI Readability of Documents

Currently, there is a lot of buzz around a development tool called GitHub Copilot, which comes with AI-assisted functionality.
There seems to be a misconception that this tool is only for engineers.
While this is partially true, it's also partially incorrect.
Indeed, GitHub Copilot has an incredible ability to transform the way engineers work.
However, as engineers' work methods change, organizations must also adapt.
If you are in a PM or PO position, this is an important issue for you as well. 
Since your team's engineers are expected to perform at their best, implementing your defined requirements as quickly as possible.
Going forward, even if you are not an engineer, you will need to create **AI-readable** documentation to enable your team's engineers to collaborate with AI.

## Documentation Culture and AI Development

In recent years, AI technology has advanced rapidly, with models like LLM (Large Language Model) gaining attention.
GitHub, an open-source development platform, has also ventured into the field of AI development.
A prime example of this is "GitHub Copilot." 
Interestingly, AI-assisted development and open-source development share common ground in terms of collaboration.
Specifically, both methods involve working with document-based formats like Markdown.
Formats such as Markdown are designed to represent structured information and are easier for AI to analyze than PowerPoint or Excel files.
Consequently, they contribute to the improvement of AI-generated code quality.

AI prefers simple CSV files over complex Excel spreadsheets filled with metadata.
Suppose you, as a PM, list customer requirements and gather necessary information for a database.
If the requirements are written in a CSV file or summarized in Markdown, engineers can easily convert them into code.
However, if you compile the information in an Excel document tailored to your preferences, engineers must first copy, format, and then convert it into code.
Which approach is better?

Moreover, in open-source development, the quality of documentation can be directly related to the success of a project.
Open-source projects are open to anyone, and properly maintained documentation allows new developers to join more smoothly.
Therefore, documentation is highly valued in open-source development.
Similarly, in AI development, a well-established documentation culture can lead to more efficient and higher-quality development.
Even if you are not an engineer, your natural language written in Markdown can significantly contribute to the final output, which is the code.
This could be code representing business logic, table definitions, or even test scenarios.
Is your development team ready to include AI.
Are AI-readable documents prepared.
If the answer is no, you must start creating a development team that is comfortable for AI to participate in.

## AI-Native Development and InnerSource Strategy

We've been discussing open-source development, but there's also a similar concept called inner source.
InnerSource is an approach that adopts the best practices of open-source software development within organizations that develop non-open-source or proprietary software.
It aims to promote collaboration across organizational boundaries and break down organizational silos.

InnerSource is becoming increasingly important for companies to avoid reinventing the wheel, streamline development to reduce costs, and create new value through collaboration.

As mentioned on the AI-Native development page, AI tends to augment experienced humans.
Senior or experienced individuals within an organization who understand the architecture are boosted, while others are assigned simpler tasks.

However, since AI is primarily trained on knowledge from the internet, it cannot access proprietary domains, closed knowledge within organizations, or unpublished information.
Therefore, if this information is not documented or properly shared within the organization, it poses a problem.
This issue means that not only can engineers not access the information, but AI like GitHub Copilot also cannot access it.

Knowledge that cannot be obtained from the internet is currently becoming more important and a core competency of businesses.
There is a quote from an InnerSource introductory book ["Getting Started with InnerSource"](https://innersourcecommons.org/learn/books/getting-started-with-innersource/) by O'Reilly :

> InnerSource differs from classic open source by remaining within the view and control of a single organization. The “openness” of the project extends across many teams within the organization. This allows the organization to embed differentiating trade secrets into the code without fear that they will be revealed to outsiders, while benefitting from the creativity and diverse perspectives contributed by people throughout the organization.

Many businesses are faced with the choice of either collaborating with AI or being replaced by AI.
It is essential to aggregate the internal information that is the source of an organization's competitive advantage and have it utilized by AI.
To achieve this, documentation with AI readability is indispensable.

Regarding InnerSource, there is already a mature community where methods for realizing co-creation within organizations and creating documentation are shared.
Access this community and leverage InnerSource initiatives.
By doing so, you can effectively utilize internal knowledge and information and make the most of collaboration with AI.

### InnerSource References

- [InnerSource Commons](https://innersourcecommons.org/): InnerSource Commons Foundation page
- [InnerSource Patterns](https://patterns.innersourcecommons.org/): Collection of InnerSource best practices
- [Getting Started with InnerSource](https://innersourcecommons.org/learn/books/getting-started-with-innersource/): O'Reilly's InnerSource introductory book
- [Understanding the InnerSource Checklist](https://innersourcecommons.org/learn/books/understanding-the-innersource-checklist/): O'Reilly's InnerSource practical guide

## Creating Context-Rich Documentation

As open source development matures, collaboration across countries and time zones emerges.
However, geographical distance and time differences can sometimes make synchronous communication difficult.
For example, daytime in New York is nighttime in Tokyo, and it's undesirable to disturb Japanese-based committers at night or interfere with family time.
Therefore, documentation based on written documents is generally preferred.
This could be something like RFCs or design documents, or comments written in GitHub Issues.
Documents formed by comments in Issues and the like are also called [passive documentation](https://www.oreilly.com/library/view/understanding-the-innersource/9781491986899/ch04.html).
These are also forms of documentation.

There is a passage in [Understanding the InnerSource Checklist](https://innersourcecommons.org/ja/learn/books/getting-started-with-innersource/) published by O'Reilly that goes like this:

> Passive documentation is the record of the documentation we create every day while communicating openly. It is a great way to get tribal knowledge out of silos and into a format that is archival and findable. As an added bonus, it is typically kept with the project or the code that it documents, thus it is in an easy-to-find, context-relevant location.

What's important here is to properly put it into words, including the context.
It's difficult to convey nonverbal communication, nuances, and atmosphere that are communicated through Zoom or face-to-face conversations asynchronously across time zones.

Consider developing with AI.
For example, will GitHub Copilot participate in Zoom meetings.
Will it be in the team room saying, "Hey, I'm GitHub Copilot, let's have a quick check-in meeting".
The answer is no.
All context must be conveyed to AI in writing.
This is also necessary when creating appropriate documentation for asynchronous communication, like in open source development.

Of course, there are differences in the granularity of documentation between open source development and AI-assisted development.
Writing "I want to fix this bug" in GitHub Issues might prompt someone to think of a solution, but AI cannot go that far.
However, there are definitely areas where AI excels.
If you want to express cloud architecture as Infrastructure as Code, it's better to write it in Mermaid or express it in natural language rather than drawing it in PowerPoint.

The point here is not that all communication needs to be documented.
You and your team need to consider what level of documentation to leave, how and where to leave it.

## AI Coordinating Organizational Knowledge

With features like GitHub Copilot for Docs included in GitHub Copilot X, AI can create the perfect documentation for you.
The documents you write can also become onboarding materials for the next person.

In the past, gathering information and creating onboarding materials for new engineers was a common task, but in the future, AI will likely take on that role.
You can embed all the knowledge you possess in documents as the only reliable source of information.

This approach can also be seen explicitly in [Atlassian](https://www.atlassian.com/ja/work-management/knowledge-sharing/documentation/importance-of-documentation) documentation.
Reading their documentation with AI-Native development in mind might lead to new discoveries.
The documents you write will feel as if they have a personality through AI.
However, this requires sufficient documentation, as mentioned earlier.

## The Distance Between Natural Language and Implementation Becomes Closer

As you may have noticed by now, the distance between natural language and implementation is getting much closer.
As mentioned earlier, from an educational perspective, if writing prompts and code in one place continues, it may be possible to create documentation in a single file.
This kind of change is fascinating.

## Checklist

- [ ] Does your team currently have a documentation culture. If so, what is it like. If not, what is preventing it?
- [ ] Consider what kind of documentation is needed for your team to collaborate with AI.
- [ ] Is there a culture of open source or inner source in your team?
- [ ] Start by creating a documentation culture within your scope.  What areas can you begin writing documentation in Markdown.  Think about it.
