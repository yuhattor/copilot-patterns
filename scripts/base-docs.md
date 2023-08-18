---
marp: true
theme: default
class: invert
paginate: true
footer: "GitHub Copilot Patterns & Exercises"
allowlocalfiles: true
html: true
style: |
  footer {
    font-family: Arial, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    width:90%;
    font-size: 14px;
    color: #666;
  } 
  header {
    font-family: Arial, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  }
  .center-hubber > p {
    display: flex;
    align-items: center;
    vertical-align: center
  }
  img[alt~="full"] {
    padding-top:72px;
    border-radius:48px;
  }
  img[alt~="fit"] {
    padding-top:72px;
    border-radius:48px;
    margin: 0% 8%;
    width: 84%;
  }
  li {
    font-size: 22px;
    line-height:28px;
    list-style: none;
    background-size: 22px;
    background-image: url("./assets/icons/circle.png");
    background-repeat: no-repeat;
    margin-left: -48px;
    margin-top: -10px;
    margin-bottom: 20px;
    padding: 0px 0px 12px 52px;
  }
  pre {
    font-size: 18px;
    background-color: #232029; 
    border: 0px;
    width:60%;
  }
  h1, h2, h3, h4{
    background: -webkit-linear-gradient(-70deg, #8250df 0%, #d42a32 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: rgba(0,0,0,0);
    -webkit-box-decoration-break: clone;
  }
  h1 {
    font-size: 64px;
    margin-bottom: 0px;
    line-height: 64px;
    clip-path: inset(6px);
    padding-bottom: 0px;
  }
  h2 {
    position: absolute;
    left: 60px; 
    top: 40px;
    font-size: 44px;
    padding: 20px;
    padding-bottom: 40px;
    clip-path: inset(2px);
  }
  h3 {
    padding-bottom: 20px;
    padding-left:2px;
    clip-path: inset(0px);
  }
  code {
    padding:2px;
  }
  p {
    font-size: 28px;
    margin-top: 20px;
    margin-left: 2px;
    color: #ccc;
  }
  section {
    font-family: Arial, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    background-color: #0d1116;
    color: #ccc;
  }
  section::after {
    font-size:14px;
  }

  /* Title Section */
  section.title{
  }
  section.title h2{
    position: relative !important;
    left:0px;
    margin-top:100px;
    margin-left:0px;
    padding-left:2px;
    clip-path: inset(2px) !important;
    font-size: 64px;
  }
  section.title p{
    margin-top:0px;
    font-size: 28px;
    position: relative !important;
    margin-left:0px;
    padding-left:0px;
    left:0;
  }
  section.title blockquote {
    border-left: 6px solid #555;
    line-height:24px;
    padding-left: 10px;
  }
  section.title blockquote p {
    font-size: 24px;
    color: #555;
  }
  /* Description Section */
  section.list {
    justify-content: start;
  }
  section.list li{
    position: relative;
    top: 100px;
    left: 0px;
    font-size: 28px;
    margin-top: -10px;
    line-height:28px;
    margin-bottom: 28px;
  }

  /* Description Section */
  section.description{
    justify-content: start;
  }
  section.description h3{
    margin-top: 70px;
    font-size: 28px;
    background: -webkit-linear-gradient(-70deg, #ddd, #ccc 100%);
    -webkit-background-clip: text;
    background-clip: text;
    font-weight: 800;
    margin-bottom: -20px;
  }
  section.description p{
    font-size: 22px;
  }

  /* Exercise Section */
  section.exercise{
    justify-content: start;
  }
  section.exercise h3{
    margin-top: 60px;
    font-size: 28px;
    background: -webkit-linear-gradient(-70deg, #ddd, #ccc 100%);
    -webkit-background-clip: text;
    background-clip: text;
    font-weight: 800;
  }
  section.exercise p{
    font-size: 20px;
  }

  /* Example Section */
  section.example{
    justify-content: start;
  }
  section.example h3{
    margin-top: 60px;
    font-size: 28px;
    background: -webkit-linear-gradient(-70deg, #ddd, #ccc 100%);
    -webkit-background-clip: text;
    background-clip: text;
    font-weight: 800;
    margin-bottom: -20px;
  }

  section.example p{
    font-size: 22px;
  }

  /* Checklist Section */
  section.checklist {
    justify-content: start;
  }
  section.checklist h3{
    margin-top: 60px;
    font-size: 28px;
    background: -webkit-linear-gradient(-70deg, #ddd, #ccc 100%);
    -webkit-background-clip: text;
    background-clip: text;
    font-weight: 800;
  }

  section.checklist p{
    font-size: 22px;
  }
---
<!--
_paginate: false
_footer: ""
class: invert
-->

# GitHub Copilot 
# Patterns & Exercise

![bg right:40%](./assets/copilot/copilot.png)

Getting Started with GitHub Copilot

---
<!--
_class: list
-->

## Table of Contents

- **About GitHub Copilot**
- **GitHub Copilot Patterns** - Let's Use GitHub Copilot Effectively

---

# About GitHub Copilot

---
<!--
_class: list
-->


## What is GitHub Copilot?

- AI-powered paired programming assistant
- Developed by GitHub and OpenAI
- Uses machine learning models to suggest code snippets

![bg right:50% 85%](./assets/copilot/copilot-suggestion.png)

---
<!-- class: invert -->

## How GitHub Copilot works

![full](./assets/copilot/how-copilot-works.png)

---
<!--
_class: list
-->

## Benefits of using GitHub Copilot

![bg right:36%](./assets/copilot/copilot.png)

- Faster coding
- Improved accuracy
- Learning tool
- Less time writing the simple stuff

---

## GitHub Copilot Benefit

![bg fit 84%](./assets/copilot/copilot-result.png)

---

## GitHub Copilot Today and Tomorrow

![fit](./assets/copilot/copilot-value-prop.png)

---

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
