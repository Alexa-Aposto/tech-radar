---
layout: default
title: "Tech Radar: 2026-05-22"
date: 2026-05-22
lang: en
---

> From 52 items, 11 important content pieces were selected

---

1. [CODA Rewrites Transformer Blocks for Optimized LLM Kernel Performance](#item-1) ⭐️ 8.0/10
2. [Hugging Face Transformers v5.9.0 Adds Cohere2Moe and HRM-Text Models](#item-2) ⭐️ 7.0/10
3. [MLflow 3.13.0rc0 Enhances RBAC, AI Gateway, and Kubernetes Deployment](#item-3) ⭐️ 7.0/10
4. [CrewAI 1.14.6a1 Adds Skills Repository and Enhances Agent Orchestration](#item-4) ⭐️ 7.0/10
5. [FTC Fines Cox Media Group $1M for Deceptive AI Marketing Claims](#item-5) ⭐️ 7.0/10
6. [Datasette Agent: AI Assistant for Conversational Data Querying and Chart Generation](#item-6) ⭐️ 7.0/10
7. [SpaceX's S-1 Filing Reveals $1.25B/Month Anthropic Cloud Deal](#item-7) ⭐️ 7.0/10
8. [Google I/O: Gemini Spark AI Agent and Antigravity Tooling](#item-8) ⭐️ 7.0/10
9. [llm-gemini Tool Updates to 0.32 with Gemini 3.5 Flash Support](#item-9) ⭐️ 7.0/10
10. [Specialized AI Models Can Outperform Large General Models](#item-10) ⭐️ 7.0/10
11. [Hugging Face Releases Ettin Reranker Family for Enhanced RAG](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [CODA Rewrites Transformer Blocks for Optimized LLM Kernel Performance](https://arxiv.org/abs/2605.19269) ⭐️ 8.0/10

Researchers have introduced CODA, a system that rewrites Transformer blocks into GEMM-epilogue programs, enabling LLM-driven code generation for enhanced kernel performance. This development is significant for LLM serving and inference optimization, potentially leading to faster execution of large language models. It highlights a shift towards LLM-driven code generation for complex computational tasks. CODA focuses on rewriting Transformer blocks by fusing operations into GEMM-epilogue programs, a technique that can eliminate global memory round-trips. The system demonstrates that LLMs can author these specialized kernels, though the challenge lies in low-level hardware optimization.

hackernews · matt_d · May 22, 04:54

**Relevance**: This research is highly relevant as it explores LLM-driven code generation for optimizing low-level hardware performance, a key aspect for efficient AI model deployment on Kubernetes. It informs decisions on how LLMs can be leveraged to create optimized kernels for our platform.

**Background**: Transformer blocks are fundamental components of large language models. GEMM (General Matrix Multiply) is a core operation in deep learning, and epilogue programs refer to operations that run after the main computation. Optimizing these kernels is crucial for efficient LLM inference.

**Discussion**: Community members note that while epilogue fusion is not entirely new, the significant takeaway is the design shift towards LLM-driven code generation rather than manual kernel crafting. There's discussion on LLMs' strengths in high-level composition and the potential for feedback loops to improve low-level optimization.

**Tags**: `#LLM serving`, `#inference optimization`, `#transformers`, `#AI-driven codegen`

---

<a id="item-2"></a>
## [Hugging Face Transformers v5.9.0 Adds Cohere2Moe and HRM-Text Models](https://github.com/huggingface/transformers/releases/tag/v5.9.0) ⭐️ 7.0/10

Hugging Face Transformers library has released version 5.9.0, introducing support for new models including Cohere2Moe, a Mixture-of-Experts model with hybrid attention, and HRM-Text, a hierarchical recurrent language model variant. This release expands the library's capabilities with advanced model architectures relevant to efficient LLM serving and complex reasoning tasks, potentially impacting the development of more sophisticated AI applications. Cohere2Moe utilizes a hybrid attention pattern and supports large context windows, while HRM-Text employs a hierarchical recurrent forward pass with two transformer stacks and PrefixLM attention. Breaking changes include an update to `text_embeds` input expectations for SAM3 models.

github · Cyrilvallez · May 20, 14:12

**Relevance**: The inclusion of Mixture-of-Experts (MoE) and Hierarchical Reasoning Models (HRM) is highly relevant for our AI-powered K8s platform, as MoE models offer scalability and efficiency for LLM serving, while HRM's hierarchical approach could inform new approaches to complex query understanding or code generation.

**Background**: Mixture-of-Experts (MoE) models enhance performance by sparsely activating parameters, increasing model size without a proportional rise in computational cost. Hierarchical Reasoning Models (HRM) are inspired by human brain processing, aiming to overcome limitations of token-based reasoning in conventional LLMs by using a hierarchical structure for planning and computation. PrefixLM attention is a variant of transformer attention where instruction tokens attend bidirectionally and response tokens attend causally.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2507.11181">[2507.11181] Mixture of Experts in Large Language Models</a></li>
<li><a href="https://arxiv.org/abs/2506.21734">[2506.21734] Hierarchical Reasoning Model</a></li>

</ul>
</details>

**Tags**: `#transformers`, `#LLM`, `#NLP`, `#model deployment`

---

<a id="item-3"></a>
## [MLflow 3.13.0rc0 Enhances RBAC, AI Gateway, and Kubernetes Deployment](https://github.com/mlflow/mlflow/releases/tag/v3.13.0rc0) ⭐️ 7.0/10

MLflow v3.13.0rc0 introduces Phase 2 of Role-Based Access Control (RBAC) with a new Admin UI, integrates coding agents like Claude Code and OpenAI Codex as plugins within the AI Gateway, and provides first-class Helm charts for Kubernetes deployment. These updates significantly improve security, manageability, and deployment flexibility for MLflow, making it more robust for enterprise use cases and simplifying the integration of AI models within MLOps workflows. The release includes a major RBAC overhaul with unified APIs and a new Admin UI, expanded AI Gateway support for multiple coding agents via plugins, and production-ready Helm charts for easier Kubernetes deployment.

github · kriscon-db · May 22, 07:41

**Relevance**: The enhanced RBAC and AI Gateway plugins are directly relevant to building a secure and integrated AI-powered Kubernetes platform, enabling fine-grained access control and seamless integration of various LLM providers.

**Background**: MLflow is an open-source platform for managing the end-to-end machine learning lifecycle, including experimentation, reproducibility, and deployment. RBAC is a security mechanism that controls user access to resources based on their roles, while the AI Gateway aims to centralize and manage interactions with various large language models.

<details><summary>References</summary>
<ul>
<li><a href="https://mlflow.org/docs/latest/llms/deployments/index.html">MLflow AI Gateway (Experimental)</a></li>
<li><a href="https://mlflow.org/ai-gateway">AI Gateway for LLMs & Agents | MLflow AI Platform</a></li>

</ul>
</details>

**Discussion**: The release notes highlight significant community contributions, with multiple contributors credited for the RBAC overhaul and AI Gateway features, indicating active development and community engagement.

**Tags**: `#MLOps`, `#experiment tracking`, `#RBAC`, `#AI Gateway`

---

<a id="item-4"></a>
## [CrewAI 1.14.6a1 Adds Skills Repository and Enhances Agent Orchestration](https://github.com/crewAIInc/crewAI/releases/tag/1.14.6a1) ⭐️ 7.0/10

CrewAI has released version 1.14.6a1, introducing a new Skills Repository with registry, cache, CLI, and SDK integration, alongside bug fixes and documentation updates. This release also deprecates `CrewAgentExecutor` in favor of the default `AgentExecutor` and improves Daytona sandbox tools. The addition of a Skills Repository standardizes how AI agents can acquire and utilize tools, which is crucial for building more robust and interoperable AI-powered platforms. This advancement in agent orchestration directly impacts the development of complex AI systems that require modular and reusable capabilities. The release addresses a security issue by bumping `idna` to 3.15 and includes fixes for runtime state serialization and JSX rendering. It also refactors the CLI into a standalone `crewai-cli` package.

github · greysonlalonde · May 21, 13:28

**Relevance**: The Skills Repository feature in CrewAI is highly relevant to an AI-powered K8s platform, as it provides a framework for managing and discovering agent capabilities, akin to how Kubernetes manages containerized applications. This could inform decisions on how to implement a similar registry for AI tools and services within our platform.

**Background**: CrewAI is a framework designed for orchestrating role-playing, autonomous AI agents that work together to tackle complex tasks. The Daytona sandbox is a secure infrastructure for running AI-generated code, enabling programmatic interaction with sandboxes for various operations.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.crewai.com/en/skills">Skills - CrewAI</a></li>
<li><a href="https://github.com/daytonaio/daytona">GitHub - daytonaio/daytona: Daytona is a Secure and Elastic Infrastructure for Running AI-Generated Code · GitHub</a></li>

</ul>
</details>

**Discussion**: No community discussion was provided for this release.

**Tags**: `#AI agent orchestration`, `#tool use`, `#CrewAI`, `#platform engineering`

---

<a id="item-5"></a>
## [FTC Fines Cox Media Group $1M for Deceptive AI Marketing Claims](https://simonwillison.net/2026/May/22/ftc-active-listening/#atom-everything) ⭐️ 7.0/10

The FTC has ordered Cox Media Group, MindSift, and 1010 Digital Works to pay nearly $1 million to settle charges of deceiving customers about an AI-powered marketing service called 'Active Listening'. These companies falsely claimed the service used smart devices to listen to conversations for real-time intent data, when in reality, it resold data lists at a markup. This case highlights the increasing regulatory scrutiny on AI marketing practices and underscores the importance of transparency and truthful claims in AI services. It serves as a warning to companies using AI to ensure their marketing accurately reflects the technology's capabilities and respects consumer privacy. The 'Active Listening' service did not actually listen to consumer conversations or use voice data; instead, it involved reselling existing email lists. The FTC also clarified that deceptively hiding consent for such invasive data collection within terms of service is not acceptable.

rss · Simon Willison · May 22, 04:48

**Relevance**: This incident is relevant to building trustworthy AI platforms by demonstrating the potential legal and reputational risks associated with misleading AI capabilities. It informs decisions about how AI features are marketed and how user consent is managed, particularly concerning data privacy and the perception of 'listening' technologies.

**Background**: The 'Active Listening' marketing service was pitched to advertisers with claims that smart devices captured real-time intent data by listening to conversations, which could then be paired with behavioral data for targeted advertising. This marketing tactic played into existing consumer concerns and conspiracy theories about devices listening to private conversations for ad targeting purposes.

**Discussion**: The author of the original post expressed satisfaction that the FTC's action validated his theory that the 'active listening' claims were a fancy metaphor for existing ad targeting methods, rather than actual voice data harvesting. He also noted this provides new ammunition against the persistent 'microphone ads conspiracy' theory.

**Tags**: `#AI governance`, `#AI regulation`, `#deceptive AI`, `#consumer protection`

---

<a id="item-6"></a>
## [Datasette Agent: AI Assistant for Conversational Data Querying and Chart Generation](https://simonwillison.net/2026/May/21/datasette-agent/#atom-everything) ⭐️ 7.0/10

Datasette Agent, an extensible AI assistant for Datasette, has been released, integrating LLM capabilities with the Datasette data store. It provides a conversational interface for querying data and, with the datasette-agent-charts plugin, can generate visualizations. This development is significant as it showcases an AI agent's ability to directly interact with and interpret data stored in a database, a crucial step towards more intelligent data analysis tools. It demonstrates a practical application of AI agents for data exploration and reporting. The live demo instance utilizes Gemini 3.1 Flash-Lite for its speed and cost-effectiveness in generating SQLite queries. Datasette Agent is designed to be extensible through plugins, with initial plugins supporting chart generation and image generation.

rss · Simon Willison · May 21, 19:52

**Relevance**: This is highly relevant to building an AI-powered K8s platform, as it demonstrates how an AI agent can be orchestrated to interact with data stores and generate outputs like queries and charts. This pattern can be adapted for analyzing Kubernetes cluster data or application logs.

**Background**: Datasette is a tool for exploring and publishing data, often used for SQLite databases. LLMs (Large Language Models) are AI models trained on vast amounts of text data, capable of understanding and generating human-like text, and are foundational to many modern AI applications. AI agents are systems that can perceive their environment, make decisions, and take actions to achieve goals.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent</a></li>
<li><a href="https://en.wikipedia.org/wiki/LLM">LLM</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#data querying`, `#tool use`, `#visualization`

---

<a id="item-7"></a>
## [SpaceX's S-1 Filing Reveals $1.25B/Month Anthropic Cloud Deal](https://simonwillison.net/2026/May/20/spacex-s1/#atom-everything) ⭐️ 7.0/10

SpaceX's S-1 filing disclosed a significant cloud services agreement with Anthropic, commencing in May 2026, wherein Anthropic will pay $1.25 billion per month for access to compute capacity on SpaceX's COLOSSUS and COLOSSUS II infrastructure. This agreement signifies a major shift in AI infrastructure provisioning, with a non-traditional cloud provider like SpaceX leveraging its substantial compute resources to support a leading AI research company. It highlights a growing trend of specialized hardware providers entering the AI cloud services market, potentially impacting established cloud giants and offering new options for AI development. The contract is set to run through May 2029, with capacity ramping up in May and June 2026 at a reduced initial fee, and either party can terminate the agreement with 90 days' notice. SpaceX also mentions using its COLOSSUS II infrastructure for training its own AI models, such as Grok 5.

rss · Simon Willison · May 20, 22:26

**Relevance**: This development is highly relevant as it demonstrates a large-scale compute-as-a-service offering from a company with significant infrastructure, mirroring potential capabilities for an AI-powered K8s platform. It informs decisions about building or integrating with specialized compute providers and highlights the competitive landscape for AI infrastructure.

**Background**: COLOSSUS is a supercomputer developed by xAI, Elon Musk's artificial intelligence company, designed for large-scale AI training. SpaceX, also led by Elon Musk, is a space exploration company that is now leveraging its infrastructure for AI compute services. The S-1 filing is a document required by the U.S. Securities and Exchange Commission (SEC) for companies planning to go public through an Initial Public Offering (IPO).

<details><summary>References</summary>
<ul>
<li><a href="https://x.ai/colossus">Colossus: The World's Largest AI Supercomputer | xAI</a></li>
<li><a href="https://www.cnbc.com/video/2026/05/21/spacexs-ipo-and-the-most-ambitious-ai-bet-ever-attempted.html">SpaceX's S-1 and the most ambitious AI bet ever attempted - CNBC</a></li>

</ul>
</details>

**Discussion**: The news has generated discussion around the sheer scale of the deal, the potential disruption to traditional cloud providers, and the strategic implications of SpaceX's move into AI infrastructure. Some view it as a validation of specialized AI hardware providers, while others question the long-term sustainability and competitive positioning.

**Tags**: `#AI infrastructure`, `#compute capacity`, `#cloud services`, `#AI models`

---

<a id="item-8"></a>
## [Google I/O: Gemini Spark AI Agent and Antigravity Tooling](https://simonwillison.net/2026/May/20/google-io/#atom-everything) ⭐️ 7.0/10

Google announced Gemini Spark, a new personal AI agent designed to integrate with Google apps, and mentioned it runs on Gemini 3.5 Flash and a system called Antigravity. The Antigravity project includes a CLI tool, an SDK, and a VS Code fork, with the Gemini CLI transitioning to the Antigravity CLI. This announcement is significant as it signals Google's push towards more integrated and proactive AI agents that can interact with user data and applications, potentially setting new standards for personal AI assistance and automation. Gemini Spark is described as a 24/7 personal AI agent that connects natively with Google apps like Gmail and Drive, and it operates on a secure runtime with isolated VMs and an Agent Gateway for DLP policy enforcement. The Antigravity SDK is an open-source Python wrapper around a closed-source Go binary, and the Gemini CLI is being replaced by a closed-source Antigravity CLI.

rss · Simon Willison · May 20, 15:32

**Relevance**: Gemini Spark's integration capabilities and its underlying Antigravity tooling are highly relevant to building an AI-powered K8s platform, particularly for agent orchestration and enabling agents to interact with various services and APIs. The security measures for Gemini Spark also offer insights into handling sensitive data within agent environments.

**Background**: Gemini is a family of multimodal large language models developed by Google DeepMind, succeeding models like LaMDA and PaLM 2. Gemini 3.5 Flash is positioned as a high-performance model for agents and coding tasks. Antigravity appears to be a collection of tools and infrastructure developed by Google to support AI agents and developer tooling.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/">The Gemini app becomes more agentic, delivering proactive, 24/7 help</a></li>

</ul>
</details>

**Discussion**: The author expresses a preference for writing about generally available products rather than upcoming announcements due to past discrepancies between previews and final releases. There is also a notable concern raised about the potential for prompt injection vulnerabilities in Gemini Spark, given the sensitive data it will handle.

**Tags**: `#AI agents`, `#agent orchestration`, `#tool use`, `#Google Gemini`

---

<a id="item-9"></a>
## [llm-gemini Tool Updates to 0.32 with Gemini 3.5 Flash Support](https://simonwillison.net/2026/May/19/llm-gemini-2/#atom-everything) ⭐️ 7.0/10

The llm-gemini tool has been updated to version 0.32, introducing support for Google's new Gemini 3.5 Flash model. This release enables users to leverage the capabilities of this latest addition to the Gemini family through the llm-gemini plugin. This update is significant as Gemini 3.5 Flash is positioned as a cost-effective and performant model, potentially impacting LLM serving and inference optimization strategies. Organizations deploying AI models may consider this new model for its balance of intelligence and speed, influencing their model selection and deployment architectures. Gemini 3.5 Flash is highlighted for its 'frontier performance for agents and coding' and its ability to deliver intelligence rivaling larger models at Flash series speeds. It also claims to advance the 'frontier for intelligence per dollar,' suggesting a competitive cost-performance ratio.

rss · Simon Willison · May 19, 23:46

**Relevance**: The integration of Gemini 3.5 Flash into the llm-gemini tool is relevant for our AI-powered Kubernetes platform by providing a new, potentially more efficient model option for inference. This could inform decisions about which LLMs to support and optimize for deployment within our platform's serving infrastructure.

**Background**: Google's Gemini models are a family of multimodal AI models designed for various applications, from creative assistance to complex reasoning. The Gemini 3.5 series represents an advancement in their AI capabilities, with different versions like 'Flash' optimized for specific use cases such as speed and cost-efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/models/gemini/">Gemini 3 . 5 — Google DeepMind</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/">Gemini 3 . 5 : frontier intelligence with action</a></li>

</ul>
</details>

**Discussion**: The provided content does not include community discussions. However, the release notes mention a humorous anecdote about drawing a pelican using the plugin, indicating a lighthearted engagement with the tool's capabilities.

**Tags**: `#llm`, `#gemini`, `#inference optimization`, `#model deployment`

---

<a id="item-10"></a>
## [Specialized AI Models Can Outperform Large General Models](https://huggingface.co/blog/Dharma-AI/specialization-beats-scale) ⭐️ 7.0/10

A recent article argues that for specific tasks, specialized AI models often achieve better performance than large-scale, general-purpose models. This suggests a strategic shift in AI procurement decisions away from solely prioritizing scale. This insight is significant because it challenges the prevailing notion that bigger is always better in AI development. It could lead to more efficient and cost-effective AI solutions by focusing on tailored models that meet specific needs, impacting various industries and AI deployment strategies. The article posits that specialized models can match or even exceed the performance of generalist models on narrow tasks. Smaller models also tend to be less expensive to serve, which is a critical factor in operational costs.

rss · Hugging Face Blog · May 22, 15:25

**Relevance**: This directly informs our AI-powered K8s platform by suggesting that we should consider specialized models for specific platform functionalities rather than relying solely on massive, general LLMs. This could lead to optimized resource utilization and improved performance for targeted tasks within the platform.

**Background**: LLM serving refers to the deployment and operation of large language models to handle requests efficiently, impacting latency, throughput, and cost. Specialized AI models are AI systems designed and trained for a particular task or domain, as opposed to general-purpose models that aim for broad applicability.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reddit.com/r/learnmachinelearning/comments/1mqtrb9/big_ai_models_vs_smaller_specialized_models_whats/">Big AI models vs smaller specialized models — what's the real future? - Reddit</a></li>
<li><a href="https://community.openai.com/t/question-about-specialized-ai-models/777249">Question About Specialized AI Models - API - OpenAI Developer Community</a></li>

</ul>
</details>

**Discussion**: Discussions around specialized AI models often highlight their potential to enhance performance in multi-agent systems and their cost-effectiveness compared to larger models. There is also a question about why more 'specialized' LLMs or SLMs are not readily available.

**Tags**: `#LLM serving`, `#model deployment`, `#AI strategy`, `#specialized models`

---

<a id="item-11"></a>
## [Hugging Face Releases Ettin Reranker Family for Enhanced RAG](https://huggingface.co/blog/ettin-reranker) ⭐️ 7.0/10

Hugging Face has introduced the Ettin Reranker family, a new set of six models designed to improve the relevance of search results within retrieval-augmented generation (RAG) pipelines. These models are released under the Apache 2.0 license, consistent with the Ettin encoders. This development is significant for AI systems that rely on external knowledge, as improved reranking directly enhances the accuracy and usefulness of LLM outputs by ensuring more relevant information is retrieved. This impacts the quality of AI agents and applications built on RAG architectures. The Ettin rerankers are cross-encoder models fine-tuned on datasets like MS MARCO, designed to compute scores for text pairs to facilitate reranking and semantic search. They were evaluated on the MTEB (eng, v2) Retrieval benchmark, paired with various embedding models.

rss · Hugging Face Blog · May 19, 00:00

**Relevance**: The Ettin Reranker family is directly relevant to building an AI-powered K8s platform by enhancing the RAG capabilities essential for intelligent agents and automated workflows. This could inform decisions on integrating advanced reranking models to improve the platform's ability to understand and act on external data.

**Background**: Retrieval-Augmented Generation (RAG) is a technique that allows Large Language Models (LLMs) to access and incorporate information from external data sources before generating a response. This process involves retrieving relevant documents and then using that information to augment the LLM's generation capabilities, thereby improving accuracy and reducing hallucinations.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/ettin-reranker">Introducing the Ettin Reranker Family</a></li>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval - augmented generation - Wikipedia</a></li>
<li><a href="https://huggingface.co/tomaarsen/ms-marco-ettin-32m-reranker">tomaarsen/ms-marco-ettin-32m-reranker · Hugging Face</a></li>

</ul>
</details>

**Discussion**: The announcement has been met with positive reception, highlighting the importance of rerankers in optimizing RAG pipelines and the value of open-source contributions to the LLM ecosystem.

**Tags**: `#LLM serving`, `#inference optimization`, `#RAG`, `#NLP research`

---