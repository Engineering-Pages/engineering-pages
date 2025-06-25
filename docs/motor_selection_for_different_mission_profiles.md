# Motor Selection for Different Mission Profiles

Motor Selection for Different Mission Profiles

The selection of a rocket motor represents one of the most critical decisions in sounding rocket design, yet many builders fall into the trap of simply choosing the highest total impulse motor that fits their airframe. This approach overlooks the subtle interplay between thrust curves, mission objectives, and aerodynamic constraints that ultimately determines flight success.

Consider a typical altitude-focused mission profile. While total impulse correlates strongly with maximum altitude potential, the thrust curve shape plays an equally important role. A motor with a high initial thrust-to-weight ratio (typically >10:1) helps minimize off-rail velocity requirements but often results in higher drag losses during the transonic region. In contrast, motors with longer, more gradual thrust curves can achieve higher overall efficiency despite lower initial thrust.

[figure]
Graph comparing three representative thrust curves: "Fast burn" (steep initial spike, rapid decay), "Dual thrust" (initial spike followed by sustained lower thrust), and "Long burn" (gradual bell curve). X-axis shows time in seconds (0-10), Y-axis shows thrust in Newtons (0-1000). Overlaid efficiency curves demonstrate altitude achieved per unit of total impulse, showing the dual-thrust profile achieving optimal results for most altitude missions. Drag losses are indicated by shaded regions under each curve, with the fast-burn profile showing significantly higher losses in the transonic region.
[/figure]

For payload-focused missions, motor selection criteria shift dramatically. Here, acceleration limits often dictate motor choice more than absolute performance. A 10-pound camera payload might limit acceptable acceleration to 15Gs, immediately excluding many high-thrust motors that would otherwise be suitable for the airframe. The relationship between payload mass and acceptable G-loading creates a narrow band of suitable thrust curves.

Staging introduces additional complexity to motor selection. The booster motor must provide sufficient velocity at burnout to maintain stability through coast phase, while the sustainer requires reliable ignition conditions. Analysis of hundreds of successful staged flights reveals a consistent pattern: successful staging typically occurs at velocities between 300 and 600 fps, with sustainer ignition delayed until dynamic pressure drops below 15 PSF.

[figure]
Scatter plot showing successful staging events across various flight profiles. X-axis shows staging velocity (200-700 fps), Y-axis shows dynamic pressure at ignition (0-30 PSF). Data points are color-coded by sustainer success rate, revealing a clear "sweet spot" centered around 450 fps and 10 PSF. Overlaid contours show theoretical stability margins during transition.
[/figure]

The clustering of motors presents unique selection criteria. While total thrust remains additive, the statistical probability of simultaneous ignition becomes a dominant factor. Field data suggests that synchronization within 100ms becomes increasingly difficult with more motors, leading to a practical limit of four motors for most amateur applications. The thrust curve must account for potential asymmetric thrust during startup and shutdown phases.

Modern composite motors offer unprecedented variety in thrust curves through variations in grain geometry. The traditional BATES grain design provides reliable performance but limited flexibility. More sophisticated configurations like C-slot and finocyl grains enable custom thrust profiles optimized for specific mission requirements. However, this flexibility comes with increased cost and reduced commercial availability.

[figure]
Cross-sectional diagrams of four common grain geometries (BATES, C-slot, finocyl, and moon burner), with corresponding thrust curves below each. Annotations highlight key characteristics of each design including burn surface progression, regression rate stability, and typical applications. Cost vs. performance trade-off data shown in adjacent table.
[/figure]

Recent developments in hybrid motors have introduced new considerations in motor selection. While offering theoretical advantages in specific impulse and throttleability, operational complexity often outweighs these benefits for typical sounding rocket applications. The exception comes in research missions where payload requirements mandate restart capability or precise thrust control.

Experience shows that successful motor selection requires systematic evaluation of at least seven key parameters: total impulse, thrust-to-weight ratio, burn time, thrust curve shape, physical dimensions, availability, and cost. These parameters must be weighted according to mission priorities and practical constraints. A scoring matrix approach helps quantify these trade-offs and avoid subjective decision-making.