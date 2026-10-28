# Local archive metadata

Source: https://docs.google.com/document/d/12-GdNg6z-2ZeDpKYXhYgxxO4hUPzBcWfheKwtkye0bw
Document ID: 12-GdNg6z-2ZeDpKYXhYgxxO4hUPzBcWfheKwtkye0bw
Title: Meeting started 2026/10/05 15:41 MDT - Notes by Gemini
Meeting start: 2026-10-05 15:41 America/Denver

All source text follows; rich links use Markdown. Embedded images are linked to the original tab, not downloaded. Transcript elapsed time is not a verified meeting duration.

---

# Source tab: Quick notes

Please rate the new Quick notes tab by taking a short survey.

Meeting Oct 5, 2026 at 15:41 MDT

Oct 5, 2026

Linux setup evaluation and robot book retrieval assignment planning via technical review

Linux system setup and OS preferences
Linux Mint recommended as a user-friendly operating system alternative to Windows.
Linux environments demonstrated significantly lower memory usage than Windows during multitasking.

Robotics assignment and BST cost model analysis
Evaluated robot retrieval costs encompassing rotation, distance movement, and title scanning.
Explored mapping a flat bin array to a BST structure for optimal search routing.
Calculated an optimal cost of 10 for the first test case based on expected bin frequencies.

Next steps
[Harry Cook] Review assignment: Study the optimal Binary Search Tree material to gain a deeper understanding of the robot pathing costs.
[The group] Schedule meeting: Coordinate a follow-up session for tomorrow to continue discussing the task requirements.
[Samuel Schuetz] Confirm schedule: Notify Harry in advance to confirm the specific time for the tomorrow meeting.


Want to see more? View the full notesTip: You can always access your full notes from the left sidebar.



You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes

# Source tab: Full notes

Oct 5, 2026
Meeting Oct 5, 2026 at 15:41 MDT
Meeting records [Transcript](https://docs.google.com/document/d/12-GdNg6z-2ZeDpKYXhYgxxO4hUPzBcWfheKwtkye0bw/edit?usp=drive_web&tab=t.ej6jn0wiwvqz) 


Summary
Linux setup evaluation and robot book retrieval assignment planning via technical reviewLinux Setup and EfficiencyDiscussion highlighted Linux memory efficiency and resource management benefits compared to Windows.Robot Assignment SetupParticipants established a GitHub repository and reviewed cost models for the book retrieval robot task.Test Cases and CostsAnalysis of test cases revealed optimal calculation methods based on rotation, movement, and scan frequencies.


Next steps
[Harry Cook] Review assignment: Study the optimal Binary Search Tree material to gain a deeper understanding of the robot pathing costs.
[The group] Schedule meeting: Coordinate a follow-up session for tomorrow to continue discussing the task requirements.
[Samuel Schuetz] Confirm schedule: Notify Harry in advance to confirm the specific time for the tomorrow meeting.


Details
Linux Setup and Resource Efficiency: Harry Cook and Samuel Schuetz discussed the initial setup friction of Linux compared to Windows, with Harry Cook noting that the long-term benefits and resource management of Linux make the transition worthwhile. Later, Harry Cook demonstrated Linux's superior memory and CPU efficiency by pointing out that running multiple applications—including two VS Code instances, Firefox, K9s, Spotify, Discord, and Steam—only consumed 16 gigabytes of memory (00:01:44).
Linux Distributions and Robotics Interest: Samuel Schuetz expressed interest in getting into robotics and embedded systems using Nix and flakes, though they admitted not feeling fully ready yet. Harry Cook recommended starting with a friendlier distribution like Mint for beginners, noting that Nix might not be the ideal first choice based on personal experience (00:00:51).
Housing Situation: Amidst their discussion, Harry Cook inquired about Samuel Schuetz's recent housing move, and Samuel Schuetz confirmed they were happy with their new location where Professor Bradshaw's mother-in-law acts as their landlord for a rented house (00:01:44).
Robot Book Retrieval Assignment Setup and GitHub Repository: Harry Cook and Samuel Schuetz began working on a class assignment involving a robot tasked with retrieving a book from a bookshelf (00:03:16). Harry Cook outlined the problem's cost model, which includes a cost to rotate, a move cost per distance, and a title cost per scan, with the ultimate goal of minimizing total distance, locations, and scans (00:04:37). To collaborate, Harry Cook created a private GitHub repository for the assignment and added Samuel Schuetz (username Schuetz77) as a collaborator via an invite sent through the Google Meet chat (00:06:28).

[Embedded image kix.tsh0tdv1dqz2; view in original source](https://docs.google.com/document/d/12-GdNg6z-2ZeDpKYXhYgxxO4hUPzBcWfheKwtkye0bw?tab=t.8sz20yiu68pj)

Bin Searching and Tree Structure Mechanics: Samuel Schuetz and Harry Cook reviewed how the bookshelf functions as a flat list or array of bins while a binary search tree is built over it to determine the optimal search route for the robot. Harry Cook explained that when scans are expensive, the robot may perform greedy jumps across layers to avoid scanning every single book, though it must ultimately scan the QR code on the bin at the tree root and at the target bin (00:11:01) (00:20:10).

[Embedded image kix.93niextiwqdk; view in original source](https://docs.google.com/document/d/12-GdNg6z-2ZeDpKYXhYgxxO4hUPzBcWfheKwtkye0bw?tab=t.8sz20yiu68pj)

Directional Facing and Returning to Index Zero: The participants reviewed the physical movements of the robot, noting that it always starts at bin zero and must ensure it faces the correct negative or positive direction when navigating and scanning (00:13:47). Harry Cook clarified that once the robot discovers the target ISBN, it ensures it is facing the negative direction before moving back to index zero to deliver the book (00:17:48).
Analyzing Test Cases and Frequency Costs: Harry Cook and Samuel Schuetz examined the assignment's first three test cases, which provide expected daily bin frequencies alongside rotation, move, and scan costs (00:24:43) (00:31:51). Analyzing the first test case with a frequency of 5, rotation cost of 3, move cost of 1, and scan cost of 2, Harry Cook explained that the optimal cost of 10 is calculated because the robot starts at root zero and incurs no movement or rotation costs, only requiring 5 scans multiplied by a scan cost of 2 (00:31:01) (00:34:41). They also decoded the tree structure format used in the test cases, identifying it as root, left, and right nested tuples (00:29:36) (00:33:52).

[Embedded image kix.xy4kqh5u42u5; view in original source](https://docs.google.com/document/d/12-GdNg6z-2ZeDpKYXhYgxxO4hUPzBcWfheKwtkye0bw?tab=t.8sz20yiu68pj)

Meeting Wrap-Up and Scheduling Next Steps: Due to an upcoming office hours meeting in 20 minutes, Harry Cook ended the session with Samuel Schuetz. The pair agreed to review the material independently and schedule their next meeting for the following day, as Harry Cook was tied up until 9 o'clock later that day (00:36:49).


You should review Gemini's notes to make sure they're accurate. Get tips and learn how Gemini takes notes
How is the quality of these specific notes? Take a short survey to let us know your feedback, including how helpful the notes were for your needs.

