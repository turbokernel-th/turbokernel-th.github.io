---
title: "Coding Agent for Everyone — Preface: What If You Could Just Ask?"
date: 2026-04-25
draft: true
post_type: "Blog Post"
tags: ["Introduction", "AI", "Coding Agent", "OpenCode", "Claude Code", "Gemini", "Productivity", "Fun", "Python", "Gradio"]
summary: "You don't have to be an engineer to use a coding agent. This preface shows you what's possible — a photo editing app, an 8-slide PDF deck, and a live data dashboard — all built by just asking."
---

You've probably heard the buzzwords: *Coding Agent*, *Agentic AI*, *Vibe Coding*. Let's ignore those for a second.

Here's the honest pitch: **what if you could just tell your computer what you wanted, and it built it for you?**

Not in a chatbot window. Not with you copying code and praying it works. A real, local agent sitting in your terminal — reading your files, writing code, running it, fixing the errors, and handing you the finished thing. All while you watch.

That's what this series is about.

---

## Who This Is For

This series is called **Coding Agent for Everyone** — and I mean *everyone*. Not just engineers. Not just people who know what a `for` loop is.

- You're a business analyst who wants to crunch a messy Excel file and get a chart, without waiting two weeks for IT.
- You're a student who needs a quick demo app for a presentation tomorrow.
- You're a developer who's tired of Googling the same Stack Overflow answers.
- You're just curious, and you want to build something fun on a Sunday afternoon.

All of you belong here.

---

## Free vs. Paid — You Have Options

You don't need to spend money to start. **[OpenCode](https://opencode.ai)** backed by Gemini's free tier lets you run a capable coding agent at zero cost. If you want more power, paid tools like **Claude Code** go significantly further — but this series will show you what's achievable with the free path too.

All three demos below were built with Gemini CLI. Free.

---

## Demo 1 — A Photo Editing App, Running on Your Machine

> *Sorry — no voice on this one. Just ASMR. 🎧*

{{< gdrive id="1c2j2QGwdd9nTNAx5pVncbVRNs302_cUz" >}}

We asked the agent to build a photo editing web app. It wrote the entire thing in one shot using **Gradio** and **Pillow** — the kind of stack a senior Python developer would reach for.

The app it built includes:
- **Resize, rotate, flip** — basic transforms with sliders
- **Brightness, contrast, color, sharpness** — live enhancement controls
- **Filters** — Blur, Contour, Emboss, Edge Enhance, Sharpen, and more

All running locally in your browser. No upload to anyone's server. No subscription.

The agent didn't just write the code — it installed the dependencies, ran the app, and told you where to open it. You typed a sentence. You got a working app.

> *Sorry — no narration on this one. Just the peaceful sounds of a coding agent doing its thing. Consider it ASMR. 🎧*

---

## Demo 2 — An 8-Slide Presentation, Built in Under 3 Minutes

> *Still no voice — pure ASMR. But stick around, Demo 3 is where I actually talk you through what's happening.*

{{< gdrive id="1rBa8NJbeSvrHI_qD0uiMQOcnG0OV2_Xt" >}}

We gave the agent a PDF report — a financial analysis on the economic impact of the US-Iran conflict — and told it to turn it into a presentation.

It read the document, designed eight slides, and generated both a **`.pptx`** and a **`.pdf`** version. The slides covered:
- An executive summary with key findings
- Oil & gas price surge analysis (Brent crude peaked at $126/bbl)
- Country-level GDP impact comparisons
- Strait of Hormuz traffic disruption
- Suspicious pre-conflict trading activity
- Forward scenarios for global markets

The kind of deck you'd normally spend an afternoon on. Built in minutes — ready to walk into a meeting with.

---

## Demo 3 — Dataset Analysis + Live Dashboard + Slide Deck, Combined

{{< gdrive id="1RSV1plXwxuLvmv_x6uSMV293ryk1Z9tI" >}}

This one builds on Demo 2. We dropped in a folder of **9 CSV files** — the raw data behind that same conflict analysis — and asked the agent to do two things:

1. Build an **interactive data dashboard** (a Gradio web app) that tells the story through charts: oil price volatility, GDP growth deltas by country, Hormuz traffic disruption, suspicious trades, forward scenarios.
2. Generate the **slide deck** from the same data, so the presentation matches the dashboard.

It installed **pandas**, **matplotlib**, **seaborn**, and **gradio** — then wrote both the app and the presentation generator. One prompt. Two outputs. The dashboard and the deck tell the same story, from the same data, in two different formats.

This is the one that makes analysts stop and stare.

---

## The Series Roadmap

Here's where we're headed after this:

| # | Title | What you'll learn |
|---|---|---|
| **0** | **Preface: What If You Could Just Ask?** *(you are here)* | What's possible, demo reel, series overview |
| **1** | **The Boring-but-Worth-It Part** | Shell basics, Python, Node.js, and a dead-simple mental model of how LLMs and agents work |
| **2** | **Your First Coding Agent** | OpenCode + Gemini (free) and Claude Code (paid), side by side from zero |
| **3** | **Making It Yours** | Custom prompts, tools, skills, and sub-agents *(likely two posts)* |
| **4** | **Ship It** | Deploying to Vercel, GCP, and beyond |

You can read in order, or jump to whatever's relevant to you.

---

## A Word on the "Boring" Part

Part 1 is the one most people want to skip. I'd ask you not to.

You don't need to become a programmer. But understanding *just enough* — what a terminal is, roughly how an LLM decides what to do next — means you can unstick yourself when something goes sideways. And it will, occasionally. Even for engineers.

I'll keep it short. I'll keep it visual. I'll trade depth for clarity everywhere I can.

Trust me on this one. Then go build something.
