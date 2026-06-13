# Multi-Fidelity Deep Learning Surrogate for Vadose Zone Uncertainty Quantification at Hanford





Technical Task Plan



Mission Need Statement:

The vadose zone at Hanford's Central Plateau is not merely a pathway—it is the **rate-limiting control** on remediation timelines and the **dominant source of uncertainty** in long-term risk predictions. Over 450 billion liters of liquid waste were discharged to the subsurface across 800+ waste sites, with contaminants currently residing in the vadose zone that will continue migrating to the groundwater for **centuries to millennia**. 

**The vadose zone determines:**
- **When** contaminants reach the aquifer (travel time: decades to thousands of years)
- **How much** mass reaches the aquifer (retardation, decay, lateral spreading)
- **Where** contamination emerges at the water table (spatial distribution from commingling)
- **How long** remediation must continue (source depletion timescales)

Unlike the groundwater, where pump-and-treat systems can actively intervene, **the vadose zone cannot be directly remediated at scale**. Once contaminants are in the subsurface, their fate is governed by slow, complex physical and chemical processes that we can only observe indirectly and model with significant uncertainty.

---

## The Uncertainty Crisis: Why Current Approaches Fall Short

### Vadose Zone Uncertainty Dominates Risk Predictions

The Hanford vadose zone models incorporate **massive uncertainty** across multiple dimensions:

**1. Hydraulic Properties (Orders of Magnitude)**
- Unsaturated hydraulic conductivity varies by 3-5 orders of magnitude
- Anisotropy ratios (horizontal/vertical flow) range from 1 to >100
- Moisture-dependent behavior creates non-linear, coupled uncertainties
- Stratified sediments cause preferential lateral spreading—difficult to characterize

**2. Geochemical Parameters (Factor of 10-1000)**
- Distribution coefficients (Kd) for key contaminants:
  - Tc-99: 0-0.1 mL/g (highly mobile)
  - I-129: 0-15 mL/g (variable sorption)
  - U-238: 0.2-4.0 mL/g (redox-dependent)
- Small changes in Kd → **orders of magnitude change in travel time**

**3. Source Term Uncertainty (Factor of 2-10)**
- Historical discharge volumes poorly documented
- Contaminant inventories estimated from process knowledge
- Spatial distribution of sources unknown (commingling potential)
- Temporal release patterns uncertain (episodic vs. continuous)

**4. Recharge Uncertainty (Factor of 2-5)**
- Natural recharge: 0.5-100 mm/yr depending on surface conditions
- Anthropogenic sources: pipeline leaks, surface runoff, irrigation
- Climate change impacts on future recharge rates
- Surface barrier performance and longevity

### The Computational Bottleneck

**Current state:** Each of the 26 Central Plateau vadose zone models requires **weeks to months** for a single STOMP simulation running from 1943 to 10,000 years.

**What's needed for uncertainty quantification:**
- Monte Carlo analysis: 1,000-10,000 realizations
- Sensitivity analysis: 100s of parameter combinations
- Scenario evaluation: 10s-100s of alternative futures

**The gap:** To properly quantify uncertainty requires **millions of CPU-hours** that are simply not available. As a result, **current risk assessments rely on single deterministic runs** that cannot capture the true range of possible outcomes.

**Consequence:** Decision-makers lack the uncertainty bounds needed to:
- Design robust remediation strategies
- Prioritize high-risk areas
- Optimize resource allocation
- Defend regulatory decisions

---

## How Vadose Zone Uncertainty Controls Remediation Timelines

### The Timeline Paradox

Hanford's groundwater pump-and-treat systems (like the 200 West P&T optimized by OPTIMA) can only address contamination **after it reaches the aquifer**. But the vadose zone acts as a **long-term source** that continuously recharges groundwater contamination for centuries.

**Example from the document:**
- Peak groundwater concentrations may not occur until **1,000-10,000 years** in the future
- Vadose zone travel times range from decades (shallow, high-recharge areas) to millennia (deep, low-recharge areas)
- Remediation cannot be declared "complete" until vadose zone sources are depleted

### Uncertainty Compounds Over Time

**Small uncertainties in vadose zone parameters → Large uncertainties in remediation timelines:**

| Parameter | Uncertainty Range | Impact on Timeline |
|-----------|------------------|-------------------|
| Kd (Tc-99) | 0 vs. 0.1 mL/g | 2-10× difference in travel time |
| Recharge | 1 vs. 10 mm/yr | 5-20× difference in flux rate |
| Anisotropy | 1:1 vs. 100:1 | Lateral spreading → commingling → extended plume |
| Source inventory | 0.5× vs. 2× | Proportional change in cleanup duration |

**Combined effect:** Uncertainty in remediation timeline spans **centuries to millennia**—making it impossible to plan, budget, or commit to cleanup endpoints without quantifying vadose zone uncertainty.

### The Optimization Dilemma

**OPTIMA optimizes groundwater pump-and-treat systems**, but its effectiveness depends critically on **vadose zone source terms**:

- **Underestimate vadose flux** → P&T system undersized → containment failure
- **Overestimate vadose flux** → P&T system oversized → wasted resources
- **Ignore uncertainty** → brittle designs that fail under unexpected conditions

**Current approach:** OPTIMA uses **deterministic vadose zone predictions** (single STOMP run per model) as fixed boundary conditions.

**Problem:** Without vadose zone uncertainty quantification, OPTIMA cannot perform **robust optimization**—designs that perform well across the full range of plausible futures.

---

## Mission Impact: Why This Work Matters

### 1. **Enables Risk-Informed Decision Making**

**Current:** Decisions based on single deterministic predictions (best guess)

**With this work:** Decisions based on uncertainty-bounded predictions (confidence intervals)

**Impact:**
- Regulators can assess probability of exceeding cleanup standards
- Stakeholders can understand range of possible outcomes
- Managers can prioritize high-risk, high-uncertainty areas
- Budgets can account for uncertainty in timeline and cost

### 2. **Accelerates Remediation Planning**

**Current:** Each scenario evaluation requires weeks-months (STOMP run)

**With this work:** Each scenario evaluation requires seconds (DL surrogate)

**Impact:**
- Rapid "what-if" analysis for adaptive management
- Real-time exploration of alternative strategies
- Faster response to new data (monitoring, characterization)
- Iterative optimization instead of one-shot planning

### 3. **Optimizes Resource Allocation**

**Current:** Cannot explore full parameter space → suboptimal designs

**With this work:** Monte Carlo optimization across uncertainty space → robust designs

**Impact:**
- **Cost savings:** Avoid over-design of P&T systems (millions of dollars)
- **Risk reduction:** Avoid under-design that leads to containment failure
- **Timeline compression:** Identify strategies that reduce cleanup duration
- **Prioritization:** Focus characterization efforts on high-impact uncertainties

### 4. **Integrates Vadose Zone and Groundwater Remediation**

**Current:** Vadose zone and groundwater modeled separately, loosely coupled

**With this work:** Fast vadose surrogate enables **end-to-end optimization**

**Impact:**
- **Vadose UQ → OPTIMA:** Uncertainty-informed groundwater optimization
- **Coupled analysis:** Evaluate vadose-aquifer system as integrated whole
- **Source control:** Identify where vadose zone interventions (barriers, recharge reduction) are most effective
- **Holistic strategy:** Optimize across both vadose and saturated zones simultaneously

### 5. **Advances DOE-EM Mission**

**Hanford Central Plateau is DOE's largest, most complex cleanup challenge:**
- $100+ billion lifecycle cost
- Multi-century timeline
- 800+ waste sites
- Regulatory scrutiny and stakeholder engagement

**This work directly supports DOE-EM priorities:**
- **Accelerate cleanup:** Faster scenario evaluation → faster decisions
- **Reduce cost:** Optimize remediation strategies → avoid waste
- **Reduce risk:** Quantify uncertainty → risk-informed decisions
- **Improve stewardship:** Long-term predictions with confidence bounds

### 6. **Scalable to Other DOE Sites**

**The vadose zone uncertainty problem is not unique to Hanford:**
- Savannah River Site (South Carolina)
- Idaho National Laboratory (INTEC)
- Los Alamos National Laboratory (chromium plumes)
- Nevada National Security Site (underground test areas)

**This work establishes a framework** that can be adapted to any site where:
- Vadose zone transport controls long-term risk
- Computational cost prevents uncertainty quantification
- Remediation decisions require fast scenario evaluation

---

## The Bottom Line

**The vadose zone is the pacing item for Hanford remediation.** Its uncertainties dominate risk predictions, control cleanup timelines, and determine the effectiveness of groundwater remediation systems. Yet current computational limitations prevent us from quantifying these uncertainties or exploring the full range of possible futures.

**This work breaks the computational bottleneck** by developing a multi-fidelity deep learning surrogate that enables:
- **Fast uncertainty quantification** (seconds instead of weeks)
- **Robust optimization** (designs that work across uncertainty space)
- **Integrated vadose-groundwater analysis** (end-to-end system optimization)

**The result:** Risk-informed, uncertainty-bounded decisions that accelerate cleanup, reduce cost, and improve long-term stewardship of the Hanford Site—with a framework scalable to the broader DOE complex.

**Without this capability, we are flying blind.** With it, we can finally see the full landscape of possibilities and chart the optimal path forward.
