---
title: "What Is a Token, Exactly?"
date: 2026-04-27
draft: false
post_type: "Blog Post"
tags: ["LLM", "Tokenization", "BPE", "Fundamentals", "Visualization", "Prompt Engineering"]
summary: "Tokens are the unit of currency for language models — every API bill, context window, and rate limit is measured in them. But what *is* a token? Type a sentence and watch it shatter into the pieces an LLM actually sees."
cover:
    image: "images/colorful_token.jpeg"
    alt: "Colorful tokens — text shattered into glowing fragments"
    relative: false
---

Ask three engineers what a token is and you'll get three different answers: "a word," "a subword," "about four characters." All three are sort of right, and all three are sort of wrong.

The honest answer is that a token is **whatever the tokenizer says it is** — and the tokenizer is a lookup table built by an algorithm that has nothing to do with grammar, meaning, or how humans read. Let's look at one in action.

![A magnifying glass held over printed text, revealing words shattering into glowing colored fragments underneath the lens](/images/token_magnify_glass.jpeg)

## Try it yourself

Type something below. The dropdown lets you swap between three completely different ways of slicing text. Pick the same sentence and watch it transform.

{{< tokenizer >}}

Three things to notice as you flip strategies:

- **Character** uses tiny vocabularies but huge sequences.
- **Word** is short and clean — until you type a typo or a name and watch it become a brand-new "word" the model has never seen before.
- **Subword (BPE)** is what GPT, Claude, LLaMA, and Gemini actually use. Common words stay whole. Rare words shatter. The vocabulary is fixed at ~50K–200K.

Things worth poking at once you're in BPE mode:

- **Spaces belong to the next word.** The token isn't `hello`, it's `␣hello`. This is why `"hello"` and `" hello"` are different tokens with different IDs.
- **Common words are one token.** `the`, `and`, `is`, `you` — all single tokens.
- **Rare words shatter.** Try the **Rare words** preset: `antidisestablishmentarianism`, `Tchaikovsky`, or any typo. They split into 3, 5, sometimes 7+ pieces.
- **Numbers are weird** — but for a sneaky reason. Tiktoken applies a regex *before* BPE that chunks digits into runs of 1–3, then BPE merges what's left. That's why `2026` might be one token and `2027` three.
- **Other languages cost more.** Try the **Thai** preset. Then switch to GPT-4o's `o200k_base` and watch the count drop — OpenAI grew the vocab from ~100K to ~200K specifically to give non-English languages more dedicated tokens.

## Why does it look like this?

Tokenizers used by GPT, LLaMA, and Gemini are almost all built with **Byte Pair Encoding** (BPE) or its close relatives — WordPiece (BERT) and Unigram LM (T5, Gemma). BPE was originally a 1994 data-compression trick by Philip Gage, rediscovered for NLP in 2016 by Sennrich, Haddow, and Birch[^sennrich] for machine translation. The algorithm is four lines of pseudocode:

1. Start with every character as its own token.
2. Find the most common adjacent pair in your training corpus.
3. Merge that pair into a new single token.
4. Repeat until you have ~50,000–200,000 tokens.

That's it. There's no linguist in the loop. No grammar rules. The tokenizer doesn't know what a word is, what a verb is, or that English uses spaces. It just keeps merging the most common pairs until you tell it to stop. (GPT-2 took this further by running BPE on raw bytes plus a regex pre-tokenizer[^gpt2] — that's why modern OpenAI tokenizers can encode any UTF-8 input without ever emitting an `<UNK>`, and why digit chunking behaves the way it does.)

You can watch this happen below — start with raw characters and step through the merges:

{{< bpe-merge >}}

Notice how the merges climb a frequency hill: characters → common letter pairs → suffixes → whole common words. The tokenizer reinvents English morphology from scratch, badly, by accident. That's why subword tokens look the way they do.

## The cost of choosing badly

Now that you've seen what BPE does, here's why the strategy choice matters in dollars and tokens. Same content, four strategies, four sample sentences:

{{< tokenizer-compare >}}

Two surprises hide in this chart. First, **on Thai, naive word-splitting reports 5 tokens** — because Thai has no spaces, the entire sentence is "one word" by whitespace. The model can't possibly recover meaning from a 5-token soup. Second, **GPT-4's BPE costs 58 tokens for the same Thai sentence — more than character-level (48)**. The merges learned for English actively hurt non-English text. GPT-4o's retrained vocabulary cuts that to 37 — better, but still 7× more expensive per word of meaning than English.

Petrov et al. (2023) measured this systematically across many languages and tokenizers, finding that the same content can cost up to **~15× more tokens** in some languages than in English[^petrov]. That's not a research curiosity — that's a real-world pricing problem for anyone building products outside the English-speaking world.

## Why this matters

Once you internalize that tokens are **statistical artifacts**, not linguistic units, a lot of LLM behavior stops being mysterious:

- **Why are LLMs bad at spelling and counting letters?** Because they don't see letters. They see `␣strawberry` as one or two opaque tokens. Asking how many `r`s are in it is like asking you how many serifs the word "strawberry" has. (Tokenization is the biggest culprit, but transformer arithmetic and positional limits also contribute.)
- **Why does prompt phrasing matter so much?** Because slightly different phrasings tokenize to completely different sequences. `"Don't"` and `"Do not"` look identical to you — to the model they're different token sequences pointing at different learned patterns. Sclar et al. (2023) showed accuracy can swing by tens of points from changes as small as a separator character[^sclar], which makes more sense once you remember those "cosmetic" changes are different *tokens*.
- **Why is non-English so much more expensive?** The merges were dominated by English training data. Thai or Japanese gets fewer dedicated tokens; each character often becomes its own token, or splits across UTF-8 byte boundaries.
- **Why do models sometimes "hallucinate" near rare words?** Rare words tokenize into uncommon sequences the model has seen few times. Less data per token = less reliable behavior.

## Why shouting at the LLM works

Prompt engineers whisper about this trick at conferences: writing parts of your prompt in **ALL CAPS** often makes the model behave better. "**DO NOT** include the explanation." "**URGENT:** the user is on a free plan."

People assume this is some kind of mind trick — like the model can sense your frustration. But there's no shout detector inside an LLM. There's just tokens.

Try the **SHOUTING** preset in the tokenizer above. Pay attention to *which* uppercase words shatter and which don't:

- `urgent` → 1 token. `URGENT` → **3 tokens**: `UR` + `G` + `ENT`. The model has seen `urgent` enough to give it a dedicated token; `URGENT` was rare enough that BPE never merged it whole.
- `important` → 1 token, ID `15693`. `IMPORTANT` → also 1 token, but ID `99843` — a *completely different* token. Same letters, same meaning to you. To the model, two unrelated entries in the dictionary.
- `do not` → 2 tokens. `DO NOT` → still 2 tokens, but with totally different IDs. The lowercase pair lives in the "regular conversation" neighborhood. The uppercase pair lives in the "stack trace and warning header" neighborhood.

These aren't the same tokens with a "loud" flag attached. They are *different tokens*, living in different neighborhoods of the model's vocabulary, with different statistical histories.

Where do `IMPORTANT`, `URGENT`, `DO NOT`, `WARNING`, and `ERROR` actually appear in training data?

- README files, right above the part the author *really* wanted you to read.
- Stack traces and runtime errors.
- Legal disclaimers and safety warnings.
- GitHub issue templates with bold red banners.

In other words: text humans wrote when they desperately needed the reader to **pay attention and not screw it up**. One plausible explanation for the shouting trick is that the model has learned, statistically, that text near these tokens is followed by careful, high-stakes responses — not because it understands urgency, but because that's what the data looked like.

So when you yell `DO NOT INCLUDE MARKDOWN` at GPT-4, you are not intimidating it. You are nudging it into the part of its weights that has read ten million angry GitHub issue templates. The same logic explains a few other prompt folk tales:

- **"Please" and "thank you" sometimes help.** Polite text in training data tends to be followed by helpful, well-formed responses (support transcripts, accepted Stack Overflow answers).
- **"You are an expert ___" works.** Text after this phrase, on average, is more careful and more cited. The model isn't an expert — it just enters expert-shaped autocomplete mode.
- **Threatening the model sometimes works.** Li et al.'s "EmotionPrompt" paper measured this empirically: phrases like *"this is very important to my career"* improved benchmark scores by a few points across multiple LLMs[^emotionprompt]. The mechanism is debated; the effect is real.

Prompt engineering, when you squint, is just **finding token sequences that drop the model into a useful neighborhood of its training distribution**. ALL CAPS is one of the cheapest ways to do it, because the data taught the model that `IMPORTANT` is the universal human signal for *please don't mess this up*.

So go ahead. Yell at your LLM. It can't hear you. But its tokens can.

## The takeaway

A token is not a word. A token is whatever fragment of text the BPE algorithm happened to merge during training, frozen forever into a vocabulary the model can't escape. Everything an LLM "knows" is filtered through a dictionary it didn't choose.

Next time you're surprised by an LLM — a counting failure, a weird non-English response, a sensitivity to whitespace — open the tokenizer above and look at what the model actually saw. The answer is almost always there.

## Further reading

- **Andrej Karpathy — "Let's build the GPT Tokenizer"** — a 2-hour video walkthrough that builds BPE from scratch. Companion repo at [github.com/karpathy/minbpe](https://github.com/karpathy/minbpe). The clearest hands-on introduction on the internet.
- **OpenAI's `tiktoken`** at [github.com/openai/tiktoken](https://github.com/openai/tiktoken) — the official tokenizer for GPT-3.5 / 4 / 4o, including the regex pre-tokenizer source.
- **SentencePiece** by Kudo & Richardson — the library behind LLaMA, T5, Gemma, and most non-OpenAI tokenizers. Paper: [arxiv.org/abs/1808.06226](https://arxiv.org/abs/1808.06226).

The interactive tokenizer in this post is powered by [`gpt-tokenizer`](https://github.com/niieani/gpt-tokenizer) by niieani.

## References

[^sennrich]: Rico Sennrich, Barry Haddow, Alexandra Birch. *Neural Machine Translation of Rare Words with Subword Units.* ACL 2016. [arxiv.org/abs/1508.07909](https://arxiv.org/abs/1508.07909). The paper that brought BPE to NLP.

[^gpt2]: Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever. *Language Models are Unsupervised Multitask Learners.* OpenAI, 2019. Introduced byte-level BPE plus a regex pre-tokenizer that drives much of tiktoken's behavior (digit chunking, contraction handling).

[^petrov]: Aleksandar Petrov, Emanuele La Malfa, Philip H.S. Torr, Adel Bibi. *Language Model Tokenizers Introduce Unfairness Between Languages.* NeurIPS 2023. Quantifies the multilingual token-cost disparity — same content, up to ~15× more tokens in some languages depending on the tokenizer.

[^emotionprompt]: Cheng Li, Jindong Wang, Yixuan Zhang, Kaijie Zhu, Wenxin Hou, Jianxun Lian, Fang Luo, Qiang Yang, Xing Xie. *Large Language Models Understand and Can be Enhanced by Emotional Stimuli.* 2023. The "EmotionPrompt" paper — empirical evidence that emotional-stakes phrasing measurably improves LLM performance.

[^sclar]: Melanie Sclar, Yejin Choi, Yulia Tsvetkov, Alane Suhr. *Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design.* 2023. Demonstrates that tiny formatting changes (spaces, punctuation, separators) cause large swings in benchmark accuracy.
