### Participation activity 19-10-2021

Activity can be found in file [An Internal Link](\FrequentFlyerSystemAnalysis.png)

## Reccomended Reading / video notes

#### What is vulnerability management?
Modern software is huge.
Coders will make mistakes.
When we learn of a vulnerability we have a processes. Patching, which is then implemented by everyone running the software.
Requirments of vulnerability management program, why do you need one?
A variety of regulations may force organisations to do vulnerability scanning regularily.
Network scans probe any devices connecte to your network. While software scans, scan the applications running on these devices.
Make sure you design your program to ssatisify the requirments.

#### Identify scan targets
Turn requirments into a specific set of assest that you want to scan.
The organisation may already have a complete inventory.
First run a lightweight scan to find systems on the local network before doing a deeper scan.
Once you have an assest inventory you can priorities the importance.
3 factors:
Impact: what is the highest data classification handled by the system.
Likelihood: what is the network exposure. What type of services are exposed.
Critical: what impact does the system have on business operations.
These targets are also helpful when prioritising remediation.

#### Penetration testing
Executing an attack is the best way to test security.
penetration tests place security personal as attackers.
If the attackers are successful they defeat the system.
Before the test it is important to seek out the permited scope of the tests.
The ROE document (rules of engagement) is a document that tells everyone what the scope will be.
White bopx attacks:
Attackers have full access to information beforehand.
Gray box:
Attackers have limited knowledge beforehand.
Commonly use
Black box:
Attacker has no knowledge. Simulates an external attack.
Penetration test process.
loop back and forth between discovery phase and attack phase.
The discovery phase may use many different strategies.
Some strategys may even use drones to find exposed wires.
Attack phase involves:
Gaining access. Escalating privileges. Then browse for new targets in the system.
They may even install more tools.
Pivoting:
After exploiting an initial vulnerability attackers use the system to target other systems in that network.
Essentially they attack a system that isnt the target but use that system to get another system.
Persistence:
Setting up backdoors in the system by installing software.
After the Penetration test the attackers should help restore all the systems to their pre attack state. IE cleanup.
Penetration testing is labor intesnive and costly. So they are not done often.
BAS systems seek to automate the penetration testing. They inject threat indicators into systems.
In a well functioning system existing security controls should detect the BAS attack.

#### Ethical discolsure.
Vulnerability researchers may find previously unknown vulnerability.
It is important to use this information ethically.
Best practice is to notify the organisation in question with the vulnerability. And to set a date that you will release this vulnerability publically to put pressure on them to fix the issue.

#### Bug bounty.
Formal process to open network to security researchers which incourages researchers to report the responsible fashion. Organisations who are deploying this process normally do so with a vendor. Attackers will constantly probe networks with attacks.
The fast majority of attacks are automated scans looking for vulnerability. Bug bounty programs attract attackers who will then profit legally.
Operataion of bug bountys is a highly specilised task.
Organisations who have adopted bug bounties have reported good results.

#### Cybersecurity exercises.
Pits a team of attackers against a team of defenders.
Helps identify issues. Provides individuals in the organisation with attacking and defending opportunity, which improves the skills of the group.
Two teams and a group of judges.
All the members of the team share a common purpose of improving the system. after each phase the teams can be brought together to share strategies.
Capture the flag is a common style of game. The exercise is scored by the number of objectives the attacking team accomplishes and defending team defends.

#### Logging Security Information.
System monitoring produces massive amounts of data.
Monitoring technology can be somewhat automated.
Network or netflow data tells us which systems communicated and the amount of data the exchanged.
DNS logs tell us which systems may have communicated with external systems.
System logs let us know about the inner workings of the operating system.
Application logs tell us similar information about application level workings.
Authentication logs let us know who may have used the central authentication center, and what internal and external locations they accessed through this server.
VoIP lets you know about traffic on the network using SIP.
Dump traffic may also be used.
Syslog is very important.
Syslog standard is a simple format.
Each message has 4 components:
Header. (timestamp, souce address)
Facility. 24 bit code that describes where the message came from.
Severity. importance of the message.
Message. system that creates the log entry can include information that explains the purpose of the message.
Severity. 0 is an emergency. 7 is a debug.
Syslog is supported by all linux servers.
Syslog forms the core of many security systems.
syslog-ng added encryption.
Rsyslog added further enhancments.

Journalctl another system of logs that uses binary.
Decisions have to be made on how long to keep logs.
Tagging is also used to hold more information such as the user, and other metadata.
NXlog is a central log management tool.

#### Security information and even management

Log files are an important secruity system. But their are too many for humans to do the work. So it needs to be automated to computers.
AI is used to solve security log analysis.
SIEM:
Act as a central secure collection point. Stores them security.
Applys artificial intellegence to find patterns of attack.
SIEM has access to files from all across the network, so can see the big picture.
Does something called log coorilation which recognises combinations of activity which indicates a security incident.
Intrusion detection system:
A suspicious event which may be an attack triggers the inital event within the SIEM. Then it pulls together other information.
SIEM consolidates information into a dashboard, which provides admin with a view of the network.
Soar platforms is a greatly enhanced version of a siem