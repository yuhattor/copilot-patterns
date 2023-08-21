---
name: "AI friendly documentation"
description: "Be friendly to AI by writing text-based documentation. AI can read text-based documentation, but cannot read image-based  or over-complex documentation such as complex excel and powerpoint files."
authors: [yuhattor] 
category: collaboration
level: lv1
---

## AI-friendly documentation

[<img src="https://img.shields.io/badge/Lv1-Early_Stage_Pattern-blue">](https://github.com/orgs/AI-Native-Development/projects/1/)

### Description

In the era of GitHub Copilot, an AI powered coding assistance tool, having easily accessible documents in text format becomes crucial. In the AI era, files such as Infrastructure as Code, database table specifications, test requirements, and more have the potential to be instantly transformed into actual code. Rather than dealing with complex Excel, PowerPoint files, PDFs, or image formats, AI will be able to assist your coding efforts collaboratively through text-based documents.

Let's check if the following files are text-based or AI friendly:

- Infrastructure definitions
- Database table definitions
- Test specifications

#### Example

- Infrastructure Definitions
- Database Table Definitions
- Test Specifications

For example, if you have a table written in markdown like below, GitHub Copilot can use it as a base for migration files and interface files.

```rb
# | No. | Item Name            | Type                        | Length | Decimal | Required | Primary Key | Remarks                |
# | --- | -------------------- | --------------------------- | ------ | ------- | -------- | ----------- | ---------------------- |
# | 1   | pass_document_id     | integer                     |        |         | Y        | Y           | Document ID            |
# | 2   | checkout_id          | integer                     |        |         | Y        | Y           | Unique Serial Number   |
# | ... | ...                  | ...                         | ...    | ...     | ...      | ...         | ...                    |
# | 15  | update_datetime      | timestamp-without-time-zone |        |         |          |             | Update Timestamp       |

# Create migration file of cooperation_pass public

class CreateGovernmentPass < ActiveRecord::Migration[7.0]
  def change
    # <Copilot Suggestion Here>

```

### Exercise

- **Exercise 1**: Check your existing documentation and list the files that are not in text-based formats.
- **Exercise 2**: Convert one of the non-text-based files into a markdown or plaintext file and compare its accessibility with the previous format.
- **Exercise 3**: Write a script that scans your repository and alerts you if non-text-based documentation is committed.

### Checklist for Further Learning

- How can you ensure that team members are adhering to text-based documentation standards?
- What other team/project documentation could be written in text to speed up development?
- How can the adoption of text-based documentation improve development using the AI tool GitHub Copilot?
