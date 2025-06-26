# Why Photometric Stereo Needs Three Lights

Why Photometric Stereo Needs Three Lights

Photometric stereo, a technique for recovering surface normals from multiple images taken under different lighting conditions, fundamentally requires at least three non-coplanar light sources. This requirement isn't arbitrary - it emerges from the physical constraints of how light interacts with surfaces and our need to solve for three unknown components of surface orientation.

Consider what happens with just one light source. When we illuminate an object from a single direction, we capture the interaction between the surface normal and that specific light vector. This gives us one equation, but we're trying to solve for three unknowns (the x, y, and z components of the surface normal). With two lights, we get two equations - still insufficient for a unique solution.

```
[figure]
A 3D visualization showing a gray spherical surface illuminated sequentially by three light sources positioned at different angles. The first panel shows a single light from the left, creating strong shadows on the right. The second panel adds a light from the right, reducing but not eliminating ambiguity. The third panel shows all three lights (left, right, top), enabling full normal reconstruction. Overlaid vectors show how surface normals can only be uniquely determined with three light directions forming a non-coplanar set.
[/figure]
```

The fundamental ambiguity with one or two lights manifests in practical ways. With a single light, any surface normal lying on a cone around the light direction produces identical brightness - we can't distinguish between these possibilities. Two lights narrow down the possibilities but still leave us with two potential normal directions that would produce the same pair of intensity measurements.

This ambiguity becomes particularly problematic when building real photometric stereo systems. Engineers often try to minimize the number of lights to reduce system complexity and cost, but going below three lights invariably leads to unstable reconstructions. The surface normal estimates become highly sensitive to noise and often exhibit systematic biases that no amount of calibration can fully eliminate.

The three-light minimum assumes we're working with a Lambertian surface (matte, not shiny) and known light directions. In practice, most implementations use four or more lights to handle non-Lambertian effects and provide redundancy for error reduction. Some modern systems use ring lights with continuous illumination variation, but they still fundamentally sample at least three independent lighting directions.

```
[figure]
A plot showing reconstruction error versus number of light sources. The x-axis ranges from 1 to 6 lights, while the y-axis shows RMS error in surface normal estimation. A sharp knee in the curve occurs at 3 lights, where error drops dramatically. Additional lights beyond 3 show diminishing returns in error reduction. Different colored lines represent varying levels of surface specularity.
[/figure]
```

When building a photometric stereo system, the positioning of these three lights is crucial. They should be roughly equidistant from the subject and spaced to maximize the conditioning of the reconstruction problem. The classic configuration places lights in a triangular pattern above the subject, each about 120 degrees apart when viewed from above.

The necessity for three lights has driven interesting engineering solutions. Some systems use rotating light sources to sequentially capture three or more images. Others employ color multiplexing, using red, green, and blue LEDs to capture three lighting conditions simultaneously. These approaches trade off between capture speed, system complexity, and reconstruction accuracy.

The three-light requirement extends beyond basic surface normal recovery. When attempting to reconstruct full 3D geometry through integration of normal fields, having accurate normal estimates becomes even more critical. Errors in normal estimation propagate and accumulate during the integration process, making the three-light minimum a practical necessity rather than just a theoretical constraint.

Modern deep learning approaches to photometric stereo haven't eliminated the need for three lights - they've simply gotten better at handling non-ideal conditions like shadows, specularities, and interreflections. The fundamental physics of light transport still requires sampling at least three independent lighting directions to reliably recover surface orientation.

Human Nature Note: Engineers frequently attempt to bypass this requirement through clever tricks or additional assumptions about surface properties. While such approaches can work in constrained scenarios, they invariably break down when confronted with real-world complexity. The three-light minimum represents one of those rare cases where physics gives us a clear lower bound that no amount of algorithmic sophistication can circumvent.