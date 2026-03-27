# Project Detail Pages Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add two PDF-backed project detail pages, wire homepage project actions, and preserve the site's existing visual language.

**Architecture:** Keep the site as static HTML. Update the homepage buttons to point to either new internal detail pages or the required Feishu link. Add two standalone detail pages that reuse the current cyber visual system, embed local PDF assets, and provide floating contact and proposal actions.

**Tech Stack:** Static HTML, Tailwind CDN classes already present in the project, vanilla JavaScript, local PDF/image assets

---

## Chunk 1: Test Coverage And Asset Wiring

### Task 1: Add regression test for required project-detail behavior

**Files:**
- Create: `tests/test_project_detail_pages.py`
- Modify: none
- Test: `tests/test_project_detail_pages.py`

- [ ] **Step 1: Write the failing test**
- [ ] **Step 2: Run `python -m unittest tests.test_project_detail_pages -v` and confirm failure because files/links are missing**
- [ ] **Step 3: Implement the minimal site changes and static assets needed to satisfy the assertions**
- [ ] **Step 4: Re-run `python -m unittest tests.test_project_detail_pages -v` and confirm pass**

## Chunk 2: Static Page Implementation

### Task 2: Update homepage project entry points

**Files:**
- Modify: `site/index.html`
- Test: `tests/test_project_detail_pages.py`

- [ ] **Step 1: Replace the relevant `查看项目` buttons with anchors for two internal detail pages and one external Feishu page**
- [ ] **Step 2: Preserve current card styling and hover behavior**
- [ ] **Step 3: Re-run the regression test**

### Task 3: Create reusable detail-page experience for the two PDF projects

**Files:**
- Create: `site/project-consult-agent.html`
- Create: `site/project-sales-training.html`
- Create: `site/assets/docs/AI_Consulting_Agent_Matrix_(2).pdf`
- Create: `site/assets/docs/AI_Sales_Traning.pdf`
- Test: `tests/test_project_detail_pages.py`

- [ ] **Step 1: Create two detail pages that match the site's style direction**
- [ ] **Step 2: Embed the corresponding PDF in each page and provide a fallback open/download link**
- [ ] **Step 3: Add floating `联系我` and `查看产品方案文档` actions**
- [ ] **Step 4: Re-run the regression test**

## Chunk 3: Verification

### Task 4: Final verification

**Files:**
- Modify: none
- Test: `tests/test_project_detail_pages.py`

- [ ] **Step 1: Run `python -m unittest tests.test_project_detail_pages -v`**
- [ ] **Step 2: Inspect `git diff -- site tests docs/superpowers/plans` for scope accuracy**
