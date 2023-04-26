# AI-Native Development

The adoption of AI technologies like GitHub Copilot can potentially impact the architecture of projects as the work of engineers within development teams changes.
This document discusses the possible implications that AI-Native development methods may have.

## Context is Everything

AI technologies, represented by GitHub Copilot, can enter development environments and processes in various ways.
Development teams need to be more aware of the context in order to achieve greater development speed.
One thing to keep in mind is the technical and business context included in your program.
While this is not a new topic and has been discussed before, it is worth considering these two contexts again in light of the boost that developers are now receiving through AI cooperation.
These contexts will affect architecture and the careers of engineers.

Also, there are high-context and low-context areas for each context. 
For example, in coding, simply pressing the tab key to accept GitHub Copilot's suggestions may be sufficient for repetitive tasks or writing processes that would ultimately lead to the same result regardless of who wrote them. 
On the other hand, nothing will come from just pressing the tab key in areas where high context is required. 
These areas require experience and knowledge of specific technical domains, which cannot be easily acquired.

### Technical Context

To consider technical context, let's think about some programming languages.
Some languages, like Python, have a certain degree of commonality in how they express things, while others, like Ruby, allow for diverse expressions for the same task.
The scope width is also an issue.
There are languages like BASIC where global scope is the default, and many languages with narrower scopes.
Rust's reference and borrowing mechanism, for example, is a typical case that involves high technical context.
At the framework level, the context can be stacked in multiple layers.

### Business Context

The same is true for the business domain.
Consider SQL, a database language.
AI excels at simple tasks and is well-suited for implementing SQL's standard expressions.
If you're defining database access for a simple application implementation, you can get by with less context.
However, when dealing with a complex, intertwined, large database, it's difficult to be confident that the AI-generated code won't affect other processes.
Understanding the overall architecture and having some knowledge of the actual logic may be required.
The same applies to testing: AI is good at writing tests along given scenarios, but it's difficult to come up with comprehensive test scenarios.
AI can easily write API tests for a REST API with simple CRUD features, but writing perfect tests for an application with complex authorization conditions might be challenging for AI.

## AI-Native Architecture

How much context exists in the architecture of the features/applications you manage?
If there is a lot of context in the architecture, the development speed utilizing AI might decrease.
This is because LLMs can understand only a limited amount of context, and it is not possible to provide a large amount of context to AI at the same time.
This is partly due to the upper limit of tokens that can be given, but it is also because humans generally cannot provide all the information in a form that is AI-readable.
In a sense, AI can work indefinitely as long as prompts are continuously provided.
On the other hand, humans have limited time to provide prompts to AI.
In that case, the bottleneck in development becomes human.
Therefore, it is worth considering reducing the context of the features or applications so that AI can write the correct program even without humans providing as much context as possible.

Dividing services into smaller levels and making them loosely related is a good idea.
However, what I am referring to is not necessarily using microservices in the context of Kubernetes.
Any design you can think of, including SOA and library-level separation, is fine.
What's important is to divide the components into simple and testable units.
The more context an application has, the harder it is to get AI support.

There are sometimes religious wars about the appropriate size of programs to handle, and AI-assisted development is just beginning, so there is no exact answer.
However, considering maximizing engineer productivity and growing products in the shortest time possible, it might be a good idea for your team to consider development methods and architecture based on GitHub Copilot.

However, on the other hand, it should not be mistaken that IT architecture should be considered with the purpose of "maximizing engineer production." 
Engineering exists as a means to ultimately achieve something.

I look forward to everyone actively participating in the discussions in this field.

## Career Prospects as an Engineer

So far, I have touched on the potential for AI to bring about changes in architecture and development culture.
It is also important to look at the career of engineering.
This is a point to consider not only for engineers themselves but also for managers and those in positions to build organizations.

In the end, engineers need to consider whether to aim for engineers with a wide range of business and product insights or highly technical engineers.
However, the problem is that there are low-context and high-context areas in both.

For example, in coding, simply pressing the Tab key for what GitHub Copilot suggests may be enough for simple repetitive tasks or writing processes that ultimately reach the same processing, no matter who writes them.
On the other hand, the areas specified in the technical context and business context sections require a high context.
This area is a field where experience and knowledge of specific technology areas are required, so it is not something that can be easily acquired.
If it is knowledge available on the Internet, there is still a way to catch up, but on the other hand, if it is a closed knowledge area in a specific organization, and it is not documented or the cost of obtaining information is extremely high, it is difficult to catch up.

This is not limited to coding, but AI tends to strengthen humans with rich knowledge and experience.
This means that senior members will lose the jobs of newcomers.
If left unchecked, newcomers will not be able to do important work in the organization and will not be able to expect skill growth.
Senior skills will further increase, making it difficult for the organization to maintain them, and it will also be difficult to keep newcomers who are only doing boring work that seniors cannot do due to time constraints.

So, what should be done? One answer is to compile technical and business information in products and organizations into documents containing context and nurture them internally.
As more people participate in creating these documentations and co-creation occurs, a knowledge database for the company is formed.
Now is the time to create an atmosphere of internal collaboration similar to open-source.

## Checklist

- [ ] What context does your project or product have? Try organizing the context.
- [ ] Is the context exclusive to a few individuals? Is it shared within the team?
- [ ] In your project or product, is there a lot of code that AI can understand even with low context? If there is a lot of high-context code, how do you plan to convert it into AI-friendly code?
- [ ] Are you promoting internal collaboration? If not, consider actions to improve communication and knowledge sharing within and between teams.
- [ ] Have you discussed the career paths of your team's engineers in the AI era? Let's talk about whether they want to strengthen their technical and business areas.
