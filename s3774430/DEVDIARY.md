---
Name: Myeonghoon Sun
Student ID: s3774430
---

# Week 7

## SC1: Sercurity Assessment and Testing
### Participaration Activity
[here](week7_pa.png)

## SC2: Security Assessment and Testing
### Fagan Inspection
1. Planning
2. Overview
3. Preparation
4. Meeting
5. Rework (can back to Planning)
6. Follow up

Software code is one of the most common sources of security vulnerabilities. Developers write billions of lines of code each year, and there are thousands of security issues buried in the complexity of that code, just waiting to be discovered. Code reviews are one of the most important software testing techniques. During a code review, developers have their work reviewed by other developers who examine the code to ensure that it doesn't contain obvious or subtle security issueshis process may be totally informal, completely formal, or something in between. The most formal code review process is known as the Fagan inspection. Fagan inspections follow a six-step process. During the first step, planning, developers perform the prework required to get the code review underway. This includes preparing the materials required for the review, identifying the participants, and scheduling the review. Next, the review moves on to the overview phase where the leader of the code review assigns roles to different participants and provides the team with an overview of the software being reviewed. During the preparation phase, the participants review the code and any supporting materials on their own to get ready for the review session. They look for any potential issues and make notes that they can refer back to later. Once everyone is prepared, the formal inspection meeting takes place. During this meeting, developers raise any issues they discovered during the preparation phase and discuss them with the team. The meeting is where the team formally identifies any defects in the software that require correction. After the inspection meeting, the developers who created the code correct any defects identified during the review in the rework phase. If there were no defects, the developers can then move on to the next phase. If the defects were significant, the process returns to the planning phase for another code review. Once the code no longer requires rework, the Fagan inspection concludes with the follow-up phase. During this follow-up phase, the leader of the review confirms that all defects were successfully corrected and completes the documentation of the review. 


# Week 8
## 26/10/2021
### Software Platforms
Software security depends on secure application platforms.
### Development methodologies

1. Waterfall Model
  * Waterfall The waterfall methodology is a linear project management approach, where stakeholder and customer requirements are gathered at the beginning of the project, and then a sequential project plan is created to accommodate those requirements. The waterfall model is so named because each phase of the project cascades into the next, following steadily down like a waterfall.
2. Spiral Model
  * The spiral model is a risk-driven software development process model. Based on the unique risk patterns of a given project, the spiral model guides a team to adopt elements of one or more process models, such as incremental, waterfall, or evolutionary prototyping.
3. Agile Model
  * Agile is an iterative approach to project management and software development that helps teams deliver value to their customers faster and with fewer headaches. Instead of betting everything on a "big bang" launch, an agile team delivers work in small, but consumable, increments. Requirements, plans, and results are evaluated continuously so teams have a natural mechanism for responding to change quickly.

### Maturity Models
Maturity Models help assess an organisation's process maturity

1. The Capability Maturity Model Integration
  - Initial
    * Work gets done but is subject to delays and budget overruns.
  - Managed
    * Various types of mangement (Configuration management, Process and Product quality assurance)
  - Defined
    * Decision analysis and resolution, Organisationsal training
  - Quantitively Manged
    * Organisational process performance
  - Optimising

2. IDEAL Model
  - Initiating
  - Diagnosing
  - Establishing 
  - Action
  - Learning 

3. Software Assurance Maturity Model
  * SAMM seeks to provide a framework for integrating security activitives into the software development and maintenance process, as well as offer organisations the ability to access their maturity levels in these areas  

### Change Mangement
1. Request Control
  * manages, evaluates, and prioritizes inbound requests from customers. 
2. Change Control
  * grants permission for developers to make changes to application code.
3. Release Control
  * moves the code from the developement environment into production

## 27/10/2021
### SC1:Participation Activitiy
|Scenario|Type of Threat|Mitigation Techniques|Issues related to the threat|
|---|---|---|---|
|The attacker attempts to guess passwords|Elevation of privilege, Information Disclosure, Tampering with Data, Denial of Service|Enforce the strong password policy|The attacker can set a foothold into the network to wage a more sophisticated attack|
|The attacker spoofs a server|Spoofing Identity, Tampering with Data, Repudation, DoS |Monitoring netwroks for atypical activity|Confidential information can be leaked|
|Attacker posts HTML or script to your site|Denial of Service, Tampering with Data|Do not allow any dynamic code exeuction in the application|Your website can be made unavailable for users|
|Access to or modification of confidential HTTP data|Tampering with data, Information Disclosure|Use a secure protocol like HTTPS|Data integrity is at risk|
|Flood service with too many connections|Denial of service|Overprovision Bandwidth|Your website can be down for an extended period of time|

### OWASP top ten
- The Open Web Application Security Project maintains a list of common web security issues.
1. Injection Flaws (insert unwanted transaction code)
2. Broken Authentication (Exploits session management)
3. Sensitive Data Exposure (Discloses confidential information)
4. XML External Entities (Allow remote code execution)
5. Broken Access Control (Allow unauthorised access)
6. Security Misconfigurations (Occur in many possible locations)
7. Cross-site scripting
8. Insecure Deserialisation (Allows API exploitation)

### Understanding cross-site scripting
- Dont allow <script> tags in user inputs

### Session hijacking
- Secure Cookies by using encryption

### Code execution attacks
1. Limit administrative access
2. Patch systems and applications

### Privilege escalation
1. Perform input validation
2. Patch operating systems, platfomts, and applications
3. Enforce the least privilege principle

## 29/10/2021
### SC2: Participation activity: SQL Injection Attack

The example code is vulnerable to SQL injection attacks to extract sensitive information, inject malicious code, and worse yet, delete data. 

## Week 8 - Workshop
