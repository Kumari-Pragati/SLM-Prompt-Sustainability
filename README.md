# SLM-Prompt-Sustainability

This repository contains the complete experimental artifacts supporting the paper  
**“Sustainability-aware evaluation of prompt strategies for SLM-based automated test generation.”**

The repository is designed to support transparency, reproducibility, and inspection of prompt strategies, execution behavior, sustainability measurements, and test quality outcomes across multiple small language models (SLMs).

---

## Repository Structure

- **Code Carbon Files/**  
  CodeCarbon logs generated for all experimental runs, capturing execution duration, energy consumption (CPU, GPU, RAM), and carbon emissions for each prompt strategy–model combination.

- **Code Files/**  
  Representative implementation files for each prompt strategy. Each file demonstrates how the corresponding prompt is constructed and integrated into the test-generation pipeline. The same pipeline is used across all SLMs, with only the model identifier changed.

- **Coverage Report/**  
  Coverage reports for generated test scripts, provided for all prompt strategies and models as plain-text outputs.

- **TOKEN/**  
  Token usage logs used for token-level analysis. This folder includes both fine-grained generation logs and batch-level merged summaries used to compute token-normalized metrics.

- **Test Script Files/**  
  Generated unit test scripts produced by each prompt strategy across all evaluated models.

- **All Results MasterSheet.xlsx**  
  Consolidated results used in the paper, including raw measurements and derived metrics such as energy per 1K tokens, carbon emissions per 1K tokens, quality per 1K tokens, and sustainability–quality scores. The sheet also contains the plots reported in the paper.

---

## Purpose

This repository is intended to:
- Provide reference implementations of prompt strategies used in the study  
- Enable verification of sustainability and quality measurements  
- Support reproducibility of reported results and derived metrics  


