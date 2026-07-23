## Variant: Sonar Bunker

### Design stance
Radial/circular composition — a large sonar-scope screen at the center with a rotating sweep and "contacts" (flagged items) as blips, switches rendered as submarine levers, gauges arranged as a vertical readout stack. Leans into "detection/contact" as the operating metaphor rather than "terminal read-out."

### Key choices
- Layout: circular center screen dominates, side panels are narrower vertical stacks (levers+sliders left, gauge list right)
- Typography: Orbitron (geometric, sci-fi display) for headers, Share Tech Mono for body — cooler and more "systems" than "typewriter"
- Color: monochrome green phosphor, single red accent reserved for a flagged/at-risk blip or gauge
- Interaction: levers toggle, amplitude sliders (not knobs) tune Perspective intensity per row, radar sweep animates continuously to keep the screen feeling "live"

### Trade-offs
- Strong at: visually the most distinctive/ownable of the three — nothing else in PM software looks like this; the "blips as flagged items" metaphor could genuinely extend to represent open issues/gaps spatially
- Weak at: circular screen wastes rectangular space for dense dialogue/text; sliders are a more generic web-UI control than the amber variant's knobs, slightly undercutting the console feel

### Best for
A portfolio-level view where you're scanning multiple projects/contacts at once rather than reading one project's detail — the radar metaphor scales naturally to "many blips."
