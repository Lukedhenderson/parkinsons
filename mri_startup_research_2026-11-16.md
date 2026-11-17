# MRI startups: initial research brief

Prepared November 16, 2026. Audience: an advanced MRI research lab, particularly acquisition and reconstruction researchers. Talk length: 10 minutes. Subtle Medical is familiar to the lab and should be a brief reference only.

## Recommended framing

**From MRI physics to a funded company: three different bets on making MRI more useful.**

My recommended main examples are Adialante (encoding), Chipiron (detection), and NVision (polarization). These are editorial selections for this audience, not rankings of scientific quality or investment prospects. Investor backing provides context; the experiments establish what has been demonstrated.

For each company, answer four questions: What bottleneck is it tackling? What technical idea does it use? What evidence supports it? What remains to be proved before the business works?

Funding amounts below refer to specifically dated announcements I verified, not an assertion that no subsequent private round exists. A company paper, conference abstract, patent, and independent clinical study provide different kinds of evidence.

## 1. Adialante — strongest audience fit

**Hook:** Can RF fields perform spatial encoding that normally requires switched B0 gradients?

Adialante is listed in **Y Combinator's Spring 2026 batch**. Its current business pitch is an owned-and-operated mobile MRI service, initially targeting prostate imaging, charging clinics per scan. Treat this as the company's commercial plan. Its letters of intent are prospective customer interest, not investment capital or completed sales. [YC company profile and founder launch](https://www.ycombinator.com/companies/adialante)

The Great Lakes I-Corps Hub reported a **$1.18 million NSF SBIR Phase II award on June 19, 2025** and identifies the company as an I-Corps alumnus. This gives you a concrete bridge from research commercialization training to grants to accelerator backing. Do not label the grant as a venture round. [I-Corps announcement](https://www.greatlakesicorps.org/press/)

**Research lineage:** Torres et al., *B1-gradient–based MRI using frequency-modulated Rabi-encoded echoes*, Magnetic Resonance in Medicine, DOI **10.1002/mrm.29002**. Published online September 2021; volume 87(2), 2022. FREE uses adiabatic RF pulses and spatial variation in B1 to create spatially dependent phase. The human-brain experiment replaced the y-direction B0 phase-encoding gradient; it did not eliminate every conventional gradient in that experiment. Nonlinear B1 fields caused distortion. [Foundational paper](https://onlinelibrary.wiley.com/doi/10.1002/mrm.29002)

**More recent result:** Pizetta et al., ISMRM 2025 abstract **2612**, reports 2D phantom details at 0.2 mm resolution in an inhomogeneous 0.5 T magnet with no B0 gradient hardware, using two-channel RF encoding and FFT/model-based reconstruction. This is a conference demonstration, not evidence of equivalent clinical whole-body performance. [2025 abstract](https://archive.ismrm.org/2025/2612.html)

The company explicitly lists the FREE papers on its [publications page](https://adialante.com/publications), making the company-to-research connection unusually direct. A useful follow-on is Froelich et al., *Fast spin-echo approach for accelerated B1 gradient–based MRI* (2023), DOI **10.1002/mrm.29592**. [Follow-on paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10050123/)

**Discussion prompts:** How does nonlinear encoding affect conditioning and resolution across the field of view? What B1 mapping and calibration are needed? What happens to SAR, sequence flexibility, acquisition time, and contrast as the approach scales? Which published experiments actually match the proposed product?

**Potential slide:** Conventional gradient encoding beside RF encoding, followed by one clearly labeled experimental image from the research. Verify the figure's acquisition parameters before using it.

## 2. Chipiron — an unusually clear detector-physics story

**Hook:** Can very sensitive detection make MRI useful at much lower magnetic fields?

Chipiron announced a **$17 million Series A on April 30, 2025**. Funding coverage names Blast as lead, with EIC Fund and iXcore participation. [Company announcement](https://www.chipiron.co/2025/04/30/successful-closing-of-17m-series-a/), [funding coverage](https://www.mobihealthnews.com/news/chipiron-raises-17m-miniature-mri-prototype)

The technical approach uses superconducting quantum interference devices (SQUIDs) for sensitive signal detection. An October 2025 presentation by cofounder Dimitri Labat at ETH describes a **10 mT** system, a SQUID volume gradiometer, and EDITER interference cancellation, with wrist and garlic images. This is later work than the initial 1 mT prototype. [ETH seminar abstract](https://qc.ethz.ch/news-events/seminars---colloquia/seminars/visions-seminars/chipiron.html)

**Research to read:** Saniour et al., *Proof of concept for the integration of a low-Tc SQUID in MRI detection at 1 mT*, ISMRM 2024, abstract **1416**. The early phantom result required four hours at 15 × 12.5 mm² resolution. It is valuable as a development baseline, not as a description of the current system's performance. [ISMRM abstract](https://archive.ismrm.org/2024/1416_MDWEVRQ2q.html)

The company's newer [2026 white paper, High-quality 0.01 T breast MRI](https://www.chipiron.co/wp-content/uploads/2026/04/Chipiron-White-Paper-2026.pdf) is an additional technical lead. Searchable excerpts describe cooled detection and a breast-imaging focus. I did not fully inspect the large PDF in this pass, so do not take its figures or current performance claims as verified here. It is a company white paper, not a journal validation study.

**Discussion prompts:** Which noise sources dominate at 10 mT? What does detector sensitivity recover, and what limitations remain from polarization, voxel size, bandwidth, and scan duration? How much infrastructure remains for the cooled detector? What breast-imaging task would justify the system clinically?

**Potential slide:** Signal/noise budget and detector schematic. Avoid describing the device as entirely cryogen-free: a low-field main magnet does not imply that the SQUID detector operates at room temperature.

## 3. NVision — MRI of metabolism, with a commercialization bottleneck

**Hook:** Make hyperpolarized metabolic imaging easier to perform repeatedly and reproducibly.

NVision announced **$55 million in Series B financing on May 13, 2026**, anchored by **Abbott**, with participants including **Playground Global**. The announced package **includes a $17 million European Investment Bank venture loan**. Thus, $55 million is not all newly raised equity. The company also announced a quantum-computing expansion; the MRI story here is its POLARIS hyperpolarization platform. [Financing announcement](https://www.nvision-quantum.com/blog/series-b-piqc)

**Research foundation:** Nagel et al., *Parahydrogen-Polarized [1-13C]Pyruvate for Reliable and Fast Preclinical Metabolic Magnetic Resonance Imaging*, Advanced Science (2023), DOI **10.1002/advs.202303441**. NVision scientists are coauthors. The paper describes automated parahydrogen-induced polarization via side-arm hydrogenation (PHIP-SAH), preparing pyruvate for metabolic MRI and comparing preclinical results with dissolution DNP. [Peer-reviewed paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10602543/)

**Recent evidence:** *First worldwide multicenter validation of the POLARIS preclinical polarizer across biological models and imaging paradigms*, July 2026, DOI **10.21203/rs.3.rs-9996713/v1**. This is explicitly a **preprint**. It reports four devices across eight centers, over 400 doses, and sample production as short as 90 seconds. The discussion reports roughly 20-minute inter-dose times; do not turn “90-second preparation” into a claim of one complete examination every 90 seconds. [Preprint](https://pmc.ncbi.nlm.nih.gov/articles/PMC13345529/)

**Discussion prompts:** How reproducible are polarization, concentration, purity, and delivery timing? What would multi-site quantitative metabolic imaging require? Which clinical decisions would these signals improve? Compatible MRI acquisition still needs the appropriate 13C hardware and sequences; the polarizer is not a universal software upgrade to any scanner.

**Potential slide:** Hyperpolarize labeled pyruvate → administer → acquire dynamic 13C data → observe labeled metabolic products. Clearly label preclinical versus human evidence.

## Alternatives and brief references

| Company | Verified funding or backing | Technical reading and reason to include |
|---|---|---|
| AIRS Medical / SwiftMR | $20M Series C, July 10, 2024, led by BSK Investment and Shinyoung Securities. [Announcement](https://airsmed.com/news/series-c-funding/) | Strong software alternative, although conceptually closer to Subtle. *All-in-One Deep Learning Framework for MR Image Reconstruction*, arXiv:2405.03684, explicitly identifies itself as SwiftMR's core algorithm. [Preprint](https://arxiv.org/abs/2405.03684) |
| Synex Medical | $21.8M Series A, September 22, 2024; Khosla Ventures, Accomplice, Radical Ventures and others. [Company announcement](https://synex.substack.com/p/announcing-synexs-series-a) | Miniaturized MRS for non-invasive metabolite monitoring. ISMRM 2025 abstract 0900 demonstrates imaging, spectroscopy, and in-vivo methylsulfonylmethane detection. It does not establish a clinically validated glucose monitor. More MRS-adjacent than conventional MRI. [Abstract](https://archive.ismrm.org/2025/0900.html) |
| Corsmed | $3.5M announced December 18, 2024, from Luminar Ventures and Big Pi Ventures. [Announcement](https://www.corsmed.com/en-us/news/corsmed-raises-3-5m-from-luminar-and-big-pi-ventures-to-save-100m-lives) | Physics simulation and quantitative/synthetic MRI research. Its research page explicitly labels roughly three-minute acquisition claims as internal phantom testing, without clinical validation or benchmarking against a specific clinical protocol. A useful ambitious early-stage alternative. [Research page and papers](https://www.corsmed.com/en-us/research) |
| Subtle Medical | $33M growth financing, June 2, 2026, led by Morgan Stanley Expansion Capital. [Investor announcement](https://www.morganstanley.com/im/en-la/intermediary-investor/insights/press-release/morgan-stanley-expansion-capital-leads-33m-growth-financing-for-subtle-medical.html) | Familiar reference only. Bash et al. studied 60% accelerated 3D T1 brain MRI in 40 subjects across six scanners/five institutions. [AJNR study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8805755/) |

For AIRS, the algorithm uses degraded raw k-space to generate training pairs but processes reconstructed DICOM images at inference. That distinction is worth making for a reconstruction audience. [Methods](https://arxiv.org/html/2405.03684v2)

A prospective SwiftMR study in 150 participants, using three vendors' 3 T scanners, reported a mean 39.4% reduction in acquisition time for the tested sequences. It excluded major structural lesions such as acute hemorrhage, infarction, and tumors, limiting generalization. [Choi et al., Korean Journal of Radiology, 2025](https://www.kjronline.org/DOIx.php?id=10.3348%2Fkjr.2024.0653)

For balance, an independent small SubtleMR study in 33 patients with brain tumors reported lower subjective image quality and task-dependent lesion-detection sensitivity after acceleration. This illustrates why a clean-looking image is not a sufficient validation endpoint. [2024 study](https://pubmed.ncbi.nlm.nih.gov/38866650/)

## Funding routes worth understanding

These are fit-based suggestions, not an objective ranking of “top” funds. A fund investing in therapeutics may have little appetite for MRI hardware; identify the partner and portfolio relevant to the actual business.

| Route | Why it may fit |
|---|---|
| [1517 Fund](https://www.1517fund.com/) | Explicit focus on students, unconventional founders, and deep-tech scientists at early stages. Its [Medici Project](https://www.1517fund.com/medici) describes grants starting at $1,000, with no equity/IP claim, for eligible North American teams; applicants send a short Loom video. Useful for beginning an experiment, not financing a whole scanner. |
| [SOSV / HAX](https://hax.co/faq/) | Hardware-focused early investment plus engineering and prototype support. Its FAQ advertises initial pre-seed capital up to $550k. Investment terms and cash versus services should be checked in the actual offer. |
| [Creative Destruction Lab, Biomedical Engineering](https://creativedestructionlab.com/streams/health/biomedical-engineering/) | Mentoring for science/engineering ventures with at least proof of concept, including some pre-incorporation projects. No program fees or equity; participation is not a guaranteed investment. |
| [MedTech Innovator](https://medtechinnovator.org/apply/) | Clinical, regulatory, commercial, and investor connections for device, diagnostic, and digital-health companies. The 2027 application deadline is December 1, 2026. Applying is free, but participation fees exist; do not repeat older blanket “free accelerator” descriptions. [October 2026 applicant briefing](https://assets.medtechinnovator.org/f/293764240441569/b1e2d6d078/mti-2027-info-session-1-summary.pdf) |
| [Y Combinator](https://www.ycombinator.com/companies/adialante) | Adialante is a direct MRI example. Best discussed as company-building capital and network, with specialized clinical/regulatory expertise still needed. |
| Khosla Ventures | A relevant research target because it invested in Synex's disclosed round. The thesis fit is inferred from that investment, not a claim it will fund any MRI idea. [Evidence](https://synex.substack.com/p/announcing-synexs-series-a) |
| Playground Global | A relevant deep-tech target with direct NVision backing. [Evidence](https://www.nvision-quantum.com/blog/series-b-piqc) |
| [a16z Bio + Health](https://a16z.com/bio-health/) | A major health/technology investor to examine for software, diagnostics, and scalable healthcare businesses; match a specific partner's interests. |
| [OrbiMed](https://www.orbimed.com/about/) | Broad healthcare investment from seed onward; its [portfolio](https://www.orbimed.com/portfolio/) includes devices, diagnostics, and tools. |
| [ARCH Venture Partners](https://www.archventure.com/portfolio/) | Useful life-sciences landscape context, particularly scientific company creation and therapeutics/tools. My assessment: less obvious as a first target for a small standalone MRI enhancement product. |

For a UT Austin team, [Discovery to Impact](https://discoverytoimpact.utexas.edu/startups/) is a practical starting point for technology licensing, market fit, business planning, and investor connections.

[NSF I-Corps National Teams](https://www.nsf.gov/funding/initiatives/i-corps/national-teams-applicants) offers eligible accepted teams up to $50,000 for customer-discovery participation. This is not unrestricted prototype money; the published program includes a $10,000 participation fee paid from award funds.

[NIH SEED](https://seed.nih.gov/) is a route to investigate for SBIR/STTR and commercialization support. Check the specific current notice, eligibility, and deadlines through [NIH's funding-opportunity search](https://www.grants.nih.gov/funding/explore-nih-opportunities); this initial brief does not identify an open MRI-specific solicitation.

## A practical explanation of raising money

My suggested sequence for the talk:

1. **Choose a specific use case and buyer.** “Improve MRI” is too broad. Examples: preserve detection of a defined lesion type while reducing a particular scan's duration, or make a specified examination viable in a clinic.
2. **Discuss university IP with the PI and technology-transfer office.** Establish what can be licensed and who can commercialize it.
3. **Interview users and purchasers.** A radiologist, technologist, department administrator, and scanner manufacturer can have different needs. I-Corps is designed around this discovery work.
4. **Fund the next decisive experiment.** Define the milestone, pass/fail criteria, cost, and time: phantom feasibility, cross-scanner validation, a prospective reader study, or a pilot deployment.
5. **Match the money to the milestone.** Small grants and university support for initial uncertainty; SBIR/STTR and appropriate accelerators for translation; sector-matched equity investors for building and scaling the company. This is a possible sequence, not a universal requirement.
6. **Pitch the whole product.** Explain clinical value, evidence, competing approaches, deployment, regulatory strategy, buyer economics, team, IP position, and what the requested capital enables. A better reconstruction metric is only one part of that story.

For investor outreach, prepare a short deck, an evidence-backed one-page technical summary, and a budget linked to milestones. Approach partners with relevant investments; introductions through collaborators, technology transfer, and founders can help, but well-targeted direct outreach is also possible.

## Suggested 10-minute structure

| Time | Content |
|---|---|
| 0:00–0:45 | Introduce the question: which MRI bottlenecks are becoming companies? Mention Subtle briefly as a familiar example. |
| 0:45–3:15 | Adialante: RF encoding, founding papers, YC and NSF route, central technical uncertainty. |
| 3:15–5:30 | Chipiron: SQUID detection, low-field tradeoffs, prototype evidence, funding. |
| 5:30–7:45 | NVision: hyperpolarized metabolic imaging, published evidence, reproducibility and workflow. |
| 7:45–9:30 | Lab idea → customer discovery → milestone → suitable funding. Use Adialante's history as the example; keep investor names to a few. |
| 9:30–10:00 | Close with a discussion prompt: “Which of these bets would we want to test, and what experiment would convince us?” |

This assumes questions follow the ten minutes. If questions are included, reduce to two main companies.

## What to verify before making slides

- Inspect original figures, scan parameters, sample types, and reuse terms; do not present phantom images as patient validation.
- Fully read Chipiron's 2026 white paper and check whether planned human studies have produced public results.
- Check Adialante's current system configuration against the published research lineage, and verify any current clinical or regulatory claims separately.
- Check whether the POLARIS preprint has a later peer-reviewed version and separate human-translation evidence from animal studies.
- Recheck round announcements and accelerator deadlines if the presentation is substantially later than this brief.
