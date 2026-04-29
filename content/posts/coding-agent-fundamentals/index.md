---
title: "Coding Agent for Everyone — Part 1: How Agents Actually Think"
date: 2026-04-29
draft: false
post_type: "Blog Post"
tags: ["AI", "Coding Agent", "LLM", "ReAct", "Fundamentals", "Tools", "Beginners"]
summary: "Open the hood on Claude Code, Gemini CLI, and OpenCode. What's actually happening when you ask an agent for help? A guided tour of the Think-Act-Observe loop — no engineering background required."
cover:
    image: "images/coder_robot_agent.jpeg"
    alt: "Anime coder opening the hood on a coding agent"
    relative: true
    responsiveImages: false
---

Last time we said a coding agent is like a personal assistant: Jarvis from *Iron Man*. Today we open the hood.

We're not going to write any code, and we're not going to install anything yet. The goal is to understand what's happening behind the screen when you type a request. Once you can picture the loop, agents stop feeling like magic and start feeling like a tool you can steer.

Three questions, in order:

1. What is an LLM, really?
2. Why does an LLM by itself fall short?
3. What turns an LLM into an *agent*?

![Anime coder opening the chest panel of a friendly robot to reveal glowing circuitry inside](images/investigate_inside.jpeg)

## The brain: what's a Large Language Model?

A Large Language Model (LLM — the family that includes GPT, Claude, and Gemini) is, at its core, a very sophisticated **autocomplete**. You give it text, and it predicts what should come next. Then the next. Then the next. Until it stops.

That's it. There's no thinking, no understanding, no consciousness. Just a statistical guess at the next chunk of text, run a few thousand times in a row.

That sounds underwhelming. But the model has read a sizeable fraction of the internet, so its "guess at the next word" is shockingly good. Good enough that the output looks like reasoning, like writing, like knowledge. Most of the time it *is* useful, but it's still autocomplete underneath.

> The model sees your text in tiny chunks called *tokens* — usually parts of a word rather than whole words. Want to go deeper? See [What Is a Token, Exactly?](../what-is-token-exactly/).

This shape has consequences. The model only knows what it read during training, so anything newer than the training cutoff (yesterday's news, the weather, your private notes) is invisible to it. And the model can't *do* anything. It can describe how to send an email; it can't actually send one. Text goes in, text comes out, and that's the whole job.

## A brain in a jar

That second point is the big one. Picture a brilliant assistant who has read every book ever written, locked in a sealed room with no door, no phone, and no internet. You can slide a question under the door, and they slide back an answer. That's a chatbot.

![A glowing brain floating in a glass jar on a desk, surrounded by sticky notes with questions pressed against the glass](images/brain_in_jar.jpeg)

Useful! But limited. The brain in the jar can't:

- Look up today's weather.
- Read a file from your computer.
- Run a calculation that's too large to do in its head.
- Send your email, draft your slides, or build your photo editor.

To do any of that, the brain needs **hands**.

## Adding hands: from LLM to agent

An **agent** is an LLM that's been given a set of *tools* it can call. A tool is anything the agent can do that goes beyond producing text: searching the web, reading a file, running a script, talking to another app's servers.

> **Agent = LLM + Tools + a loop that lets it use them.**

That loop is the secret ingredient. When you ask a chatbot a question, the answer comes out in one step. When you ask an agent, it can take a *series* of steps: think a little, use a tool, look at what came back, think some more, use another tool, and finally answer you.

To see why that matters, watch the difference yourself.

{{< chatbot-vs-agent >}}

Same question. Two completely different machines.

## A tour through one task

Let's slow down and watch an agent work, step by step. You ask:

> *Did Le Sserafim just release a new song?*

The agent's training data has a cutoff months ago. It has no idea. So it can't answer from memory, but it doesn't have to.

Click through the loop below. Each step is one move the agent makes.

{{< react-loop >}}

Notice the rhythm: **think a little, do a little, look at what happened, think again.** The agent doesn't write the whole answer in one go. It alternates between reasoning (in its head) and acting (calling a tool). Every loop, it has more information than the loop before.

That rhythm is so common in agent systems that it has a name.

## The loop, named

What you just watched is called the **Think → Act → Observe** loop, sometimes written as ReAct ("Reason + Act").[^react] Every modern coding agent — Claude Code, Gemini CLI, OpenCode, Codex — uses some variation of it.

<div class="loop-diagram" role="img" aria-label="A circular diagram showing three phases — Think, Act, Observe — connected by arrows in a clockwise loop, with a final arrow exiting to Answer.">
<svg viewBox="0 0 480 280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="loop-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" marker-end="url(#loop-arrow)">
    <path d="M 160 90 Q 240 50 320 90"/>
    <path d="M 350 130 Q 350 200 280 220"/>
    <path d="M 200 220 Q 130 200 130 130"/>
  </g>
  <g>
    <circle cx="120" cy="100" r="46" fill="var(--role-think-tint)" stroke="var(--role-think)" stroke-width="2"/>
    <text x="120" y="96" text-anchor="middle" font-size="15" font-weight="600" fill="currentColor">Think</text>
    <text x="120" y="116" text-anchor="middle" font-size="11" fill="currentColor" opacity="0.7">reason</text>
  </g>
  <g>
    <circle cx="360" cy="100" r="46" fill="var(--role-act-tint)" stroke="var(--role-act)" stroke-width="2"/>
    <text x="360" y="96" text-anchor="middle" font-size="15" font-weight="600" fill="currentColor">Act</text>
    <text x="360" y="116" text-anchor="middle" font-size="11" fill="currentColor" opacity="0.7">call a tool</text>
  </g>
  <g>
    <circle cx="240" cy="230" r="46" fill="var(--role-observe-tint)" stroke="var(--role-observe)" stroke-width="2"/>
    <text x="240" y="226" text-anchor="middle" font-size="15" font-weight="600" fill="currentColor">Observe</text>
    <text x="240" y="246" text-anchor="middle" font-size="11" fill="currentColor" opacity="0.7">read result</text>
  </g>
  <g>
    <path d="M 240 184 L 240 150" stroke="currentColor" stroke-width="2" stroke-dasharray="4 4" fill="none"/>
    <text x="252" y="170" font-size="11" fill="currentColor" opacity="0.6">…or answer</text>
  </g>
</svg>
</div>

The **think** phase is where the LLM decides what to do next; it's the part that looks like reasoning. In the **act** phase, the LLM picks a tool and calls it. In the **observe** phase, the result of that tool comes back and the LLM reads it — even if the result is a failure (a broken link, a site that's down). The agent observes the error, thinks about a different approach, and tries again. Then the loop repeats, and keeps repeating until the agent has enough information to answer you, or realizes it's stuck and asks for help.

That's almost the entire trick.

## What counts as a tool?

A tool, from the agent's perspective, is anything it can call by name and get a result back. The most common ones for coding agents:

<div class="tool-grid">
  <div class="tool-tile">
    <div class="tool-icon" aria-hidden="true">
      <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.5" y2="16.5"/></svg>
    </div>
    <div class="tool-name">Web search</div>
    <div class="tool-desc">Type a query, get back results, just like you would.</div>
  </div>
  <div class="tool-tile">
    <div class="tool-icon" aria-hidden="true">
      <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="8" y1="13" x2="16" y2="13"/><line x1="8" y1="17" x2="14" y2="17"/></svg>
    </div>
    <div class="tool-name">Files</div>
    <div class="tool-desc">Open files in your project, edit them, or create new ones.</div>
  </div>
  <div class="tool-tile">
    <div class="tool-icon" aria-hidden="true">
      <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg>
    </div>
    <div class="tool-name">Shell</div>
    <div class="tool-desc">Run commands to organize your computer — move files, check what changed, install software.</div>
  </div>
  <div class="tool-tile">
    <div class="tool-icon" aria-hidden="true">
      <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
    </div>
    <div class="tool-name">Run code</div>
    <div class="tool-desc">Write a small Python or JavaScript program and execute it.</div>
  </div>
</div>

If you can do it on your computer — open a folder, run a search, install a program — the agent can probably do it too. That's why coding agents are so much more powerful than chatbots: they have your whole machine as their playground. We'll cover the specific tools (shells, Python, JavaScript) properly in a later post.

## A note on context (and what the agent "remembers")

One last piece of the puzzle: how does the agent know what to do? It can't see your screen or read your mind. Everything it does is based on a single bundle of text called the **context**.

<div class="context-stack" role="img" aria-label="A diagram showing context as three stacked layers — system prompt, your message, and conversation so far — bracketed together as the input to the LLM.">
<svg viewBox="0 0 520 260" xmlns="http://www.w3.org/2000/svg">
  <g font-family="inherit" fill="currentColor">
    <g>
      <rect x="40" y="30" width="380" height="48" rx="8" fill="var(--role-think-tint)" stroke="var(--role-think)" stroke-width="1.5"/>
      <text x="56" y="52" font-size="13" font-weight="600">System prompt</text>
      <text x="56" y="68" font-size="11" opacity="0.7">"You are a coding assistant. Tools available: search, read_file, run_shell…"</text>
    </g>
    <g>
      <rect x="40" y="92" width="380" height="48" rx="8" fill="var(--role-observe-tint)" stroke="var(--role-observe)" stroke-width="1.5"/>
      <text x="56" y="114" font-size="13" font-weight="600">Your message</text>
      <text x="56" y="130" font-size="11" opacity="0.7">"Did Le Sserafim just release a new song?"</text>
    </g>
    <g>
      <rect x="40" y="154" width="380" height="64" rx="8" fill="var(--role-act-tint)" stroke="var(--role-act)" stroke-width="1.5"/>
      <text x="56" y="176" font-size="13" font-weight="600">Conversation so far</text>
      <text x="56" y="192" font-size="11" opacity="0.7">prior thoughts, tool calls,</text>
      <text x="56" y="206" font-size="11" opacity="0.7">and tool results from this session</text>
    </g>
    <path d="M 430 30 Q 460 30 460 124 Q 460 218 430 218" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.6"/>
    <text x="472" y="118" font-size="13" font-weight="600">=</text>
    <text x="472" y="138" font-size="13" font-weight="600">Context</text>
  </g>
</svg>
</div>

The context contains, in order:

1. **System prompt** — instructions written by the agent's developers ("you are a helpful coding assistant, here are the tools you can use, here's how to use them"). You usually don't see or edit this part; it ships with the agent.
2. **Your message** — the request you typed.
3. **The conversation so far** — every previous message and every tool result from this session.

Each turn of the loop, the entire context gets re-sent to the LLM, and the LLM produces the next chunk of output. When the agent searched for Le Sserafim a moment ago, the result didn't disappear; it got appended to the *conversation so far*, where the next pass through the loop could read it. That's how the agent "remembers" something it looked up seconds earlier, even though it has no real memory of its own.

That memory ends when the session does. Close the terminal and the agent forgets you exist. (Some agents support persistent memory through files like `CLAUDE.md`; that's a Part 3 topic.) The context is also finite, so long conversations eventually run out of room. And what's in the context is everything: if you didn't tell the agent something, it doesn't know.

Knowing this changes how you talk to agents. The skill of "prompting" is largely the skill of putting the right things into the context, clearly, in the right order, without burying the important parts.

## The takeaway

> An **agent** is a language model + a set of **tools** + a **Think → Act → Observe** loop. Everything it knows about your task lives in its **context**.

That's the whole shape. The rest is details: which model, which tools, which loop variation, how the context is built. You can swap any one of those parts and still have an agent.

In **Part 2**, we'll stop reading and start installing. You'll pick an agent (free options first), get it running, and run your first real prompt through it.

## Where to go deeper

We covered the spine. Each rib has its own deep-dive coming:

- **What is a token, exactly?** — How LLMs actually see your text. *([Available now](../what-is-token-exactly/).)*
- **What is AI, really?** — Beyond the hype: what's a neural network, what's training, what's a model? *(Coming soon.)*
- **LLMs vs Agents in depth** — A closer look at the loop, prompts, and what makes one agent different from another. *(Coming soon.)*
- **Shells and programming languages** — Bash, PowerShell, Python, JavaScript: a friendly tour for non-programmers. *(Coming soon.)*

## Useful links

- **The ReAct paper**: Yao et al., *ReAct: Synergizing Reasoning and Acting in Language Models* (2022) — [arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629). The original write-up of the loop.
- **Anthropic — Building effective agents**: [anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents). A clear, current overview of how production agents are designed.
- **Coding agents** (preview for Part 2): [Claude Code](https://claude.ai/code), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [OpenCode](https://opencode.ai), [Codex CLI](https://github.com/openai/codex).

## References

[^react]: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao. *ReAct: Synergizing Reasoning and Acting in Language Models.* ICLR 2023. [arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629). The paper that named the Think-Act-Observe loop and showed it works better than reasoning or acting alone.
