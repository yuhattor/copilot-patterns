# PROMPT知识共享

{%hint style="info"%}
本文档仍在验证中。我们期望通过[Github问题](https://github.com/AI-Native-Development/patterns/issues/8)进行积极讨论。
{%endhint%}

## 描述

共享生成代码的提示很重要，作为团队成员学习的资源。

## 问题

通过与像GitHub Copilot这样的AI一起开发，您可以编写高质量的代码，但对于高级工程师来说，优秀的代码或性能良好的代码是否适合作为代码阅读的良好代码是不同的。如果以过度缩写的代码或用语特定的高级表达来表示程序，则可能会使在特定领域中的工程师协作变得困难。

## 故事

您正在探索编写哪些提示以精通GitHub Copilot。作为高级工程师，您在实现某个功能时通过尝试和错误，与GitHub Copilot合作产生了出色的代码。同时，您旁边的团队工程师说： “您总是以这种方式编写代码！我现在感觉了解了您是如何始终产生优秀的代码的。”

您意识到，当您通过试验和错误达到最佳输出时的提示或试验和错误的过程本身是团队成员学习的重要资源。同时，您发现文件中的提示问题是它们不包括在成果物中，因此您开始思考如何共享。

## 背景

引入了GitHub Copilot，但各工程师只是单独使用，没有共享用法。此外，每个工程师在GitHub Copilot中编写的提示也没有共享。

## 解决方案

考虑提示的共享方法和评论的编写方式，并制定规则。为了不使提示成为噪音，最好将其作为文件的评论，也可以作为文件本身的文档。

以下是共享提示的模式：

*直接写入文件
通过在文件中留下提示，团队可以从其他成员的提示中学习。为了避免提示成为噪音，保留适当的提示平衡是很重要的。此外，可以考虑将部分提示转换为文档或解释评论而不是提示形式。此外，可以在代码审查时一起审查提示，促进工程师的成长。

*被动文档
将一些提示包含在拉取请求或问题的评论中。这将提高包含代码的文件的可读性，但不能在编辑器中引用参考提示。

*模拟编程
在不将提示留在文件或PR/问题中的同时，组织模拟编程会议以体验高级工程师的开发场景。将此处学到的内容单独共享为文档是很重要的。

## 结果上下文

整个团队的技能得到提高，通过共享提示促进有效学习。
代码的可读性得到提高，通过作为文档而不是提示级别的评论，代码的理解变得更加容易。
