---
marp: true
theme: default
class: invert
paginate: true
footer: "GitHub Copilot Patterns & Exercises"
allowlocalfiles: true
html: true
style: |
  /* Shared Style Sheet*/
  footer {
    font-family: Arial, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    width:90%;
    font-size: 14px;
    color: #666;
  } 
  header {
    font-family: Arial, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    text-align: right;
    width: 95%;
  }
  section {
    font-family: Arial, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    background-color: #0d1116;
    color: #ccc;
  }
  section::after {
    font-size:14px;
  }
  img[alt~="full"] {
    padding-top:72px;
    border-radius:48px;
    background-color: #0d1116;
  }
  img[alt~="fit"] {
    padding-top: -40px !important;
    margin: 0% 8%;
    margin-top: -48px;
    width: 80%;
    background-color: #0d1116;
  }
  section.badge img{
    width: 50px !important;
  }

  /* Shared Style Markup */
  h1, h2 {
    /* Title Gradient */
    background: -webkit-linear-gradient(-70deg, #8250df 0%, #d42a32 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: rgba(0,0,0,0);
    -webkit-box-decoration-break: clone;
    -moz-background-clip: text;
    -moz-text-fill-color: transparent;
  }
  h1 {
    font-size: 64px;
    padding-bottom: 0px;
    margin: 0px;
    clip-path: inset(2px);
  }
  h2 {
    font-size: 44px;
    margin-left: -4px;
  }
  h3 {
    margin-top: -16px !important;
    margin-bottom: 4px !important;
  }
  li {
    font-size: 22px;
    line-height:28px;
    list-style: none;
    background-size: 22px;
    background-image: url("./assets/icons/circle.png");
    background-repeat: no-repeat;
    margin-left: -60px;
    margin-top: -10px;
    margin-bottom: 20px;
    padding: 0px 0px 12px 52px;
  }
  li li{
    font-size: 18px;
    line-height:28px;
    background-size: 18px;
    margin-bottom: -18px;
    margin-top: 20px;
  }
  pre {
    font-size: 18px;
    background-color: #232029; 
    margin-top: 8px;
    padding:8px;
    border: 0px;
    max-width:80%;
  }
  code {
    padding: 1px;
  }
  p {
    font-size: 28px;
    margin-top: 20px;
    margin-left: 2px;
    color: #ccc;
  }

  /* Specific Section */
  section.list li{
    font-size: 28px;
  }
  section.list h2{
    margin-bottom: 36px;
  }
  section.only-image img{
    background-color: #0d1116;
    margin: 0px;
    padding: 0px;
    border-radius: 0px;
  }

  /* Title Section */
  section.title h2{
    clip-path: inset(2px) !important;
    font-size: 64px;
  }
  section.title p{
    margin-top: -20px !important;
    font-size: 22px;
    position: relative !important;
    margin-left:0px;
    padding-left:0px;
    left:0;
  }
  section.title img {
    margin-top: 30px !important;
    margin-left: 4px;
  }
  section.title blockquote {
    border-left: 6px solid #555;
    padding-left: 10px;
  }
  section.title blockquote p {
    padding-top:23px;
    font-size: 20px;
    color: #555;
  }

  /* Description, Example, Exercise, Checklist Section */
  section.description, section.exercise, section.checklist, section.example, section.list {
    justify-content: start;
  }
  section.description p, section.exercise p, section.example p, section.checklist p{
    font-size: 20px;
    line-height:28px;
  }
  section.example p, section.example li{
    font-size: 18px !important;
    margin-bottom: 0px;
    margin-top: 8px;
  }
  section.description li,section.example li, section.exercise li, section.checklist li, {
    line-height: 20px;
    margin-bottom: -18px !important;

  }
  section.example pre, section.example code, section.exercise pre, section.exercise code{
    font-size: 10px !important;
    line-height: 10px;
  }
  section.description li, section.exercise li, section.example li, section.checklist li{
    font-size: 20px;
    margin-top: 20px;
    line-height:28px;
  }
  section.only-image img{
    background-color: #0d1116;
    margin: 0px;
    padding: 0px;
    border-radius: 0px;
  }

---
<!--
_paginate: false
_footer: "Last updated: "
class: invert
-->

# GitHub Copilot

# Patterns & Exercise

![bg right:40%](./assets/copilot/copilot.png)

Getting Started with GitHub Copilot

---
<!-- _class: list -->

## Table of Contents

- **About GitHub Copilot**
- **GitHub Copilot Patterns and Exercises**
  - General
  - Client Tips
  - Collaboration
  - Design Pattern
  - Refactoring
  - Testing

---

# About GitHub Copilot

---
<!-- _class: list -->

## What is GitHub Copilot?

- AI-powered paired programming assistant
- Developed by GitHub and OpenAI
- Uses machine learning models to suggest code snippets

![bg right:40% 85%](./assets/copilot/copilot-suggestion.png)

---
<!-- _class: invert, only-image -->

## How GitHub Copilot works

![full](./assets/copilot/how-copilot-works.png)

---
<!-- _class: list -->

## Benefits of using GitHub Copilot

![bg right:30%](./assets/copilot/copilot.png)

- Faster coding
- Improved accuracy
- Learning tool
- Less time writing the simple stuff

---
<!-- _class: list -->

## GitHub Copilot Benefit

![bg fit 84%](./assets/copilot/copilot-result.png)

---

## GitHub Copilot Today and Tomorrow

![fit](./assets/copilot/copilot-value-prop.png)

---
<!-- _class: list -->

## Reactions on GitHub Copilot

![fit](./assets/copilot/sns-feedback.png)

---

# GitHub Copilot Patterns

---
<!--
footer: "GitHub Copilot Patterns"
class: description
-->

## What is GitHub Copilot Patterns

### **Patterns are a way of describing a repeatable, proven solution to a problem within a context.** This document helps any engineer get along with GitHub Copilot by summarizing each engineer's abstract know-how as a pattern

---
