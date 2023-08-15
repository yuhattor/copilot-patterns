---
name: "AI friendly documentation"
description: "Be friendly to AI by writing text-based documentation. AI can read text-based documentation, but cannot read image-based  or over-complex documentation such as complex excel and powerpoint files."
authors: [yuhattor] 
category: "general"
level: 100
---

## AI-friendly documentation

Be friendly to AI by writing text-based documentation. AI can read text-based documentation, but cannot read image-based  or over-complex documentation such as complex excel and powerpoint files.

### Description

In the age of AI-powered tools like GitHub Copilot, having documentation that is text-based and easily accessible by AI is essential. This pattern ensures that your infrastructure definitions, database table specifications, and test requirements are readable by AI, rather than being hidden in complex Excel, PowerPoint files, or image formats. This approach can enhance collaboration with AI tools and make information quickly available.

#### Samples

Checking if the following files are text-based:

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

- How can I ensure all team members are adhering to the text-based documentation standard?
- What tools can I use to automatically convert non-text-based documents to text-based formats?
- How can the adoption of text-based documentation improve the integration with AI tools like GitHub Copilot?
