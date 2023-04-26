# Reinventing the Wheel

## Description

"Reinventing the wheel" is often seen as inefficient and it's important to use open-source resources or increase shared resources across an organization. 
However, depending on code hosted by someone unknown can cause maintenance issues. In cases where reliance on a large dependency like a library or framework is necessary, reinventing the wheel may be preferred.

This pattern is inspired by a blog post by Matt Rickard on [having a GitHub Copilot](https://matt-rickard.com/having-a-GitHub Copilot).

> Prefer a little copying over a little dependency
> Instead of vendoring in left-pad as a dependency, use GitHub Copilot to generate the function. There are benefits to using battle-tested generic libraries but also benefits to bringing simple code in-tree.

## Problem

Have you heard of the left-pad problem? In 2016, a library called left-pad was unpublished from npm causing famous libraries that depend on it to break. 
Left-pad is a simple JavaScript library that pads the left side of a string with a specified number of characters, or spaces if no characters are specified. 
It is a simple implementation with only around 10 lines of code excluding blank lines.

There are many approaches to avoid reinventing the wheel, such as inner sourcing and code sharing ownership in XP. However, it's also important to consider external code that has a significant impact.
When the scope of provided code is very limited, it may be better to keep it internal rather than relying on external dependencies.

## Context

GitHub Copilot is skilled at generating simple code. While some argue that it's better to avoid dependencies altogether, that applies to dependencies that have interdependent relationships in business logic and implementation. 
For stateless functions or ones that are only depended on from one side, using GitHub Copilot to create them is possible.

## Solution

The size of dependencies can determine whether reinventing the wheel is necessary.
If a dependency is small and has a narrow impact, reinventing the wheel may be beneficial.
The left-pad problem is an example of this.
