# KOA GUEST SENTIMENT ANALYSIS PROJECT
## CIS 8396 - AI for Business Innovation Experience

---

## PROJECT OVERVIEW

**Client:** KOA (Kampgrounds of America) + AIRIA.AI  
**Team:** Team 2 (Maxwell, Beza, Jyoti, Nandini, Dylan)  
**Client Contacts:** Nathan, Hannah  
**Timeline:** March 2 - April 27, 2026  
**Platform:** AIRIA.AI agent-based system

**Classification:**
- Type: Extend + External  
- Function: Front Office / Customer Experience  
- Data Sources: RYS, SMS, Help Desk Tickets, Guest Surveys

---

## WHAT WE'RE BUILDING

**Mission:**  
AI agent system that analyzes guest feedback → detects sentiment trends → surfaces dissatisfaction drivers → alerts stakeholders with action plans

**Success Criteria:**

| Level | Requirements |
|-------|-------------|
| **MVP** | Agent that tracks sentiment over time (days/weeks/months) with periodic email to campgrounds on guest sentiment from all 4 data sources |
| **Value Add** | Agent that ties sentiment to specific campground issues with action plans |
| **Exceeds** | System-wide sentiment aggregation to provide KOA focus areas for guest experience improvement + reputation monitoring |

---

## SYSTEM ARCHITECTURE (8 Agents)

1. **Data Loader** - Ingests RYS, SMS, tickets, surveys
2. **Text Cleaner** - Normalizes/preprocesses feedback
3. **Sentiment Scorer** - Classifies sentiment (Very Positive → Very Negative)
4. **Theme Extractor** - Identifies complaint categories (cleanliness, maintenance, staff, etc.)
5. **Aggregator** - Rolls up trends by campground/region/time
6. **Report Generator** - Creates stakeholder dashboards
7. **Notification & Messaging Agent** ← **MAXWELL'S PRIMARY ROLE**
8. **Orchestration Agent** ← **MAXWELL'S SECONDARY OWNERSHIP**

---

## MAXWELL'S ROLE

### Primary: Notification & Messaging Agent
**Responsibilities:**
- Auto-respond to guests based on sentiment scores
- Route alerts to internal department POCs (campground managers, regional ops, customer service)
- Generate action plan recommendations for stakeholders
- Define escalation thresholds and response templates

**Key Decisions to Make:**
- What sentiment score triggers auto-response?
- What tone/template for each severity level?
- Who gets alerted and when? (real-time vs digest)
- What context goes in alerts? (theme tags, sentiment score, recommended actions)

**Inputs:** Sentiment score + theme tags (from upstream agents)  
**Outputs:** Guest message drafts + internal alerts with action plans

### Secondary: Orchestration Agent
**Responsibilities:**
- Control workflow between all 8 agents
- Manage data flow and agent sequencing
- End-to-end system conductor

**Why Maxwell Owns This:**  
Gives end-to-end visibility and ensures Notification Agent integrates properly

---

## DELIVERABLES & GRADING

| Deliverable | Weight | Due Date |
|------------|--------|----------|
| Working Prototype + PowerPoint | 70% | April 27 |
| Mid-semester Status Check | 15% | March 30 |
| Student Contribution Form | 15% | April 27 |

**Presentation Requirements (20 min):**
- Problem clearly understood
- Client-defined success criteria respected
- AIRIA agent behavior demonstrated
- Testing insights (MVP / Value Add / Exceeds?)
- Strategic value articulated
- Success metrics shown
- Risks acknowledged

---

## CURRENT STATE

**Team Progress:**
- Dylan sent proactive data request to Hannah/Nathan
- Team has access to 49+ KOA documents in AIRIA.AI library (data strategy, analytics, operational guides)
- Hannah confirmed team can use synthetic/fake data to start building
- Need to create sample reviews as ground truth for testing

**Immediate Next Steps:**
1. Write sample reviews (4 per team member = 20 total)
2. Define sentiment classification scale
3. Build dissatisfaction taxonomy (cleanliness, maintenance, staff, etc.)
4. Start building agents in AIRIA.AI using synthetic data
5. Test with sample reviews before real data arrives

**Resources Available:**
- AIRIA.AI platform with 49-doc KOA library
- Client contacts for questions (Nathan, Hannah)
- Team members for collaboration
- Weekly Monday sessions (5:30-9:45 PM) - attendance mandatory

---

## KEY CONSTRAINTS

**Must Have to Pass:**
- Working prototype
- All required materials
- Attend all classes (no absences)
- Stay for entire final presentation (April 27)

**No Class:** March 16 (Spring Break)

**Final Deadline:** April 27, 5 PM ET - NO EXCEPTIONS

---

## CONTACT INFO

**Instructor:** Dr. McCurdy (dmccurdy1@gsu.edu)  
**GRA:** Lami Latinwo (olatinwo3@student.gsu.edu)  
**Client Contacts:** Nathan, Hannah (KOA/AIRIA)

---

*Last Updated: March 25, 2026*
