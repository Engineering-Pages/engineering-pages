#!/usr/bin/env python3

import os
import time
import re
from pathlib import Path
from typing import List, Optional
import anthropic
from tqdm import tqdm

class ContentGenerator:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the content generator with Anthropic API key"""
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("Anthropic API key required. Set ANTHROPIC_API_KEY environment variable or pass as parameter.")
        
        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.output_dir = Path("generated_files")
        self.output_dir.mkdir(exist_ok=True)
        
        # Rate limiting: pause between requests
        self.request_delay = 2.0  # seconds
        
    def get_topics(self) -> List[str]:
        return [
            "The Invisible Cyclist Problem",
            "Why Cameras Lie About Distances",
            "Moravec's Paradox in Pixel Space",
            "The Aperture Problem Dilemma",
            "When Convolutional Kernels Hallucinate",
            "Epipolar Geometry's Hidden Symmetries",
            "The Correspondence Problem's Combinatorial Explosion",
            "Aliasing: The Nyquist Frequency's Revenge",
            "Why Deep Networks Fear Adversarial Patches",
            "The Vanishing Point Theorem",
            "Optical Flow's Aperture Ambiguity",
            "When SIFT Descriptors Fail",
            "The Harris Corner Detector's Blind Spots",
            "Why Neural Networks Can't Count Cars",
            "Homography Estimation Under Noise",
            "The Eight-Point Algorithm's Degeneracies",
            "When Stereo Vision Goes Cross-Eyed",
            "The Fundamental Matrix's Rank Deficiency",
            "Why Depth from Focus Never Quite Works",
            "Texture Synthesis and the Markov Property",
            "The Lucas-Kanade Method's Convergence Basin",
            "When Histograms of Gradients Lose Direction",
            "The Curse of Illumination Invariance",
            "Why Background Subtraction Breaks",
            "The Non-Maximum Suppression Paradox",
            "Edge Detection's Scale-Space Journey",
            "When Hough Transforms Miss Lines",
            "Why Kalman Filters Drift in Vision",
            "Template Matching's Correlation Catastrophe",
            "The Moravec Interest Point Operator",
            "The Chamfer Distance Transform",
            "Why Superpixels Aren't Super",
            "The Watershed Algorithm's Dam Problem",
            "Belief Propagation on Pixel Grids",
            "The Mumford-Shah Functional's Minimization",
            "Why Optical Character Recognition Stutters",
            "The Viola-Jones Cascade's Training Secrets",
            "When Deformable Part Models Deform Too Much",
            "The Grabcut Algorithm's Graph Cuts",
            "Why Motion Blur Destroys Everything",
            "The Canny Edge Detector's Hysteresis",
            "The RANSAC Algorithm's Inlier Count",
            "Why Photometric Stereo Needs Three Lights",
            "The Structured Light Scanner's Stripe Patterns",
            "The Retinex Theory's Illumination Estimation",
            "Why Histogram Equalization Isn't Equal",
            "The Bilateral Filter's Edge Preservation",
            "When JPEG Compression Artifacts Attack",
            "The Laplacian of Gaussian's Zero Crossings",
            "Why Morphological Operations Erode Precision",
            "The Distance Transform's Medial Axis",
            "When Alpha Matting Meets Natural Images",
            "The Seam Carving Algorithm's Content Awareness",
            "Why Poisson Image Editing Works",
            "The Variational Approach to Optical Flow",
            "When Graph Cuts Solve Vision Problems",
            "The Mean Shift Algorithm's Mode Seeking",
            "The Non-Local Means Denoising Method",
            "The Feature Pyramid Network's Multi-Scale Magic",
            "Why Object Detection Boxes Never Fit",
            "The Focal Loss Function's Hard Example Mining",
            "Why Vision Transformers Patch Images",
            "The Differentiable Rendering Revolution",
            "Why 3D Convolutions See Through Time",
            "The Point Cloud's Permutation Invariance",
            "When NeRFs Render New Views",
            "The Implicit Neural Representation's Coordinate Magic",
            "Why CLIP Connects Images and Text",
            "The Vision-Language Model's Modal Bridge",
            "The Embodied AI's Visual Navigation",
            "Why Knowledge Graphs Ground Visual Understanding",
            "The Causal Inference in Computer Vision",
            "When Fairness Meets Face Recognition",
            "The Explainable AI's Saliency Maps"
        ]
    
    def create_prompt(self, topic: str) -> str:
        """Create a prompt for generating content about a specific topic"""
        return f"""There is a site called MathPages.com which is a personal website offering in-depth, informal explorations of mathematical concepts, historical insights, and theoretical physics, written in a conversational yet rigorous style. Here are the high level subject areas on the site:

```
Number Theory
Combinatorics
Geometry
Algebra
Calculus & Diff Eqs
Probability & Statistics
Reflections on Relativity
Set Theory & Foundations
History
Physics
Combined List of Articles
Quotations
```

These subjects have a list of topics. For example, here are the topics under Number Theory:
```
Symmetric Pseudoprimes
Is e Normal?
The Half-Totient Tree
Limit Cycles of xy (mod x+y)
A Knot of Congruences
Fermat's Last Theorem for Cubes
Digit Reversal Sums Leading to Palindromes
Self-Similar Reverse-Sum Sequences
The Sum of the Prime Factors of N
Sequence Partitionable Into Powers of 2 or 3
Iterated Sum-of-Digits Function
If ab+1, ac+1, bc+1 are squares,...
Zeisel Numbers
Quadratic Reciprocity
Highly Wilsonian Primes
Quadratic Congruences
Squares in Arithmetic Progression (mod p)
Numeri Idonei
Sequences With No Arithmetic Progressions
A Primality Criterion
Can n Divide !n ?
Periods of Fibonacci Sequences mod m
Diophantine Walk-a-thon
Barlow's Observation
Divisors of an n-term Geometric Series
More Results on the Form xy (mod x+y)
Sums of Three Cubes
Congruences Involving the Totient Function
Infinitely Many Rhondas
Why z Is Not a Prime Power in z^p = x^p + y^p
Evidence for Goldbach
Perrin's Sequence
Miscellaneous Diophantine Equations
No Four Squares In Arithmetic Progression
Gauss' Lemma Without Divisibility Arguments
Product Divisible By Sum of Squares
Lucas and Perrin Pseudoprimes
Pseudoprimes For x^2 - 4x - 9
Primitive Roots and Exponential Iterations
Pythagorean Graphs
On Case 1 of Fermat's Last Theorem
Coprime Partitions
The 450 Pound Problem (x^3 + y^3 = 6z^3)
Rational Triangles in Spacetime
Reverse Greed for Unit Fractions
The Amanda Arrangement
Sum of Divisors Equals a Power of 2
Sublime Numbers
On x^2 + y^3 = z^6
A Method Of Factoring Based On 1/N
The Distribution of Perfection
Square Triangular Numbers
Fermat's Last Theorem for Quadratic Integers
Tetrahedra with Edges in Arithmetic Progression
Diophantine n-tuples and their Duals
Differences Between Powers
Recurrences and Pell Equations
In Defense of Base-Related Problems
On x^3 - x + y^3 - y = z^3 - z
On the Density of Some Exceptional Primes
Double Equations from Triangles in Squares
Differently Perfect
A Special Property of 151
Simple Complex Quadratic Fields
The Euclidean Algorithm
Casting Out Nines
Detecting Squares
Numbers Expressible As (a^2 - 1)(b^2 - 1)
Concordant Forms
Summations and Recurrences
Solving Magic Squares
Unit Fractions and Fibonacci
The 2 Ohm Problem
Reflective and Cyclic Sets of Primes
Unit Fraction Partitions
Squares Close to Cubes
N = (x^2 + y^2)/(1+xy) Is A Square
Proof of Generalized Little Theorem of Fermat
Minimizing the Denominators in Unit Fraction Expansions
On General Palindromic Numbers
Series Within Parallel Resistor Circuits
Sums of Consecutive Nth Powers Equal to an Nth Power
Integer Sequences Related to PI
Smallest Quadrilateral With Distinct Integer Sides
Mock-Rational Numbers
Coherent Arrays of Squares
Magic Square of Squares
Orthomagic Square of Squares
Automedian Triangles and Magic Squares
Continued Fractions and Characteristic Recurrences
One In The Chamber
The Greedy Algorithm for Unit Fractions
Average of Sigma(n)/n
Lucas's Primality Test With Factored N-1
Highly Heronian Ellipses
How Leibniz Might Have Anticipated Euler
Odd Greedy Unit Fraction Expansions
Factoring Zeta
Triangles and Diophantine n-Tuples
Accidental Melodies
Some Properties of the Lucas Sequence
Four Squares From Three Numbers
Meandering Convergence of a Dirichlet Series
Geodesic Diophantine Boxes
Least Significant Non-Zero Digit of n!
Discordance Impedes Square Magic
No Progression of Four Rectangles On A Conic?
Whole Permutation Fractions
A Unique Intersection Pattern for Plane Curves
```

Each topic has a page dedicated to it with the content. Here is the content for `Is e Normal?`:
```
A number is called "normal" with respect to a given base if, when the number is expressed in that base, the asymptotic frequencies of occurrence of each distinct string of k digits are equal, and this applies to every positive integer k. For example, if a number is normal in the base 10, the asymptotic frequency of occurrence of each of the decimal numerals 0, 1, …, 9 is precisely 1/10, and the asymptotic frequency of each two-digit strings 00, 01, 02, ..., 99 is exactly 1/100, and so on. By the same token, the asymptotic frequency of occurrence of each 10-digit string must be exactly 1/1010. Now, of the distinct 10-digit strings, exactly 10! contain each numeral just once, i.e., there are 10! permutations of the 10 decimal numerals 0, 1, ..., 9. Therefore, if a number is normal in the base 10, the asymptotic frequency of 10-digit strings comprising permutations of all 10 numerals must be 10!/1010, which equals roughly 1/2755.73.
It’s widely believed that the two most naturally occurring transcendental numbers, π and e, are both normal in the base 10 (although it has never even been proven that the individual numerals of these numbers have equal asymptotic frequencies), and indeed if we examine the occurrences of complete permutation strings in the first million digits of π we find very good agreement with the expected frequency, i.e., if p(n) denotes the numbers of complete permutation strings in the first n digits, then n/p(n) apparently converges on 2755, and it does so fairly rapidly. However, somewhat surprisingly, if we examine the first million decimal digits of the number e, we find that the ratio n/p(n) seems to settle at a value around 2520, as shown in the figure below.
 [figure]
This result is confirmed by continuing to check the next million digits, which show no very significant upward trend in this ratio, leaving it at 2568. (See the note on The e in Petersburg for a plot covering the first two million digits.) Hence the frequency of complete permutation strings is more than 6% greater than what would be predicted for a "normal" number. This suggestion of non-normality seems quite implausible, so I checked digits of e computed independently by two different sources, but in both cases the results were identical. Also, the fact that the digits of π yield the expected frequency using my counting program tends to support the validity of the program - which, after all, is just a simple counting routine. Could there be some systematic error in this assessment?
To provide another check of these results I acquired a set of 1 million pseudo-random digits generated by the Rand Corporation in 1955 based on work begun in 1947. According to the documentation accompanying these digits, the basic table was produced during May and June of 1947 by means of an "electronic roulette wheel". This device consisted of a random frequency pulse source, providing on the average about 100,000 pulses per second, gated about once per second by a constant frequency pulse. The pulses were then passed through a 5-place binary counter. There were about 3000 revolutions per "trial", leading to the output of one number per second. A binary-to-decimal converter was then used to convert 20 of the 32 numbers (the other twelve were discarded), and it retained only the final digit of two-digit numbers. Interestingly, the documentation notes that "production from the original machine showed statistically significant biases, and the engineers had to make several modifications and refinements of the circuits before production of apparently satisfactory numbers was achieved". Even after these modifications, some statistical biases remained. The final step in producing the table of "random digits" was to transform the table by adding pairs of digits modulo 10. This was done "in order to improve the distribution of the digits". There were 20,000 punched cards with 50 digits per card; each digit on a given card was added modulo 10 to the corresponding digit of the preceding card to yield a re-randomized digit. It is this transformed table which is published..."
This is an interesting "re-randomization" technique, since it represents something like a convolution of the data sequence. In other words, if the string of digits is in an array D[i] of length 1 million, the process consisted of applying the transformation
[figure]
Presumably for completeness we would stipulate that the digits "wrap around", e.g., D'[1] would equal the sum of D[1] and D[999951]. Iterations of this transformation don't seem to degenerate into an orderly sequence, given a sufficiently disordered initial sequence.
In any case, results for the Rand sequence are also plotted on the figure above, labeled as "synthesized". This sequence behaves very differently than the digits of π or e. It starts out quite high, meaning that there is a scarcity of complete permutation sequences. Eventually it settles down in the vicinity of the theoretical value, but it seems to converge on a slightly higher value. Is there a systematic bias in the Rand data, or does it simply require far more digits to establish the asymptotic density of complete permutation sequences?
To study this further, I acquired the first two million decimal digits of the square root of 2, as computed by Nemiroff & Bonnell. The rate of occurrence of complete permutation strings is shown in the figure below.
[figure] 
This seems to show a systematic upward bias, i.e., a scarcity of complete permutation strings relative to the expected frequency based on the assumption of normality. I also acquired the first million decimal digits of the square root of 7, and of Euler's constant g = 0.577...  The behaviors of n/p(n) for the digits of these two numbers are shown below.
[figure]
The digits of the square root of 7 seem to converge fairly well on the predicted frequency, but the digits of gamma seem to be consistently richer in complete permutations, i.e., n/p(n) is low, at least out to one million digits.
It may be worth noting that of all these numbers, the digits of π are the most thoroughly checked and verified, and those are the digits that converge most satisfactorily to the theoretical value. For the digits of the other constants (e, γ, √2, √7), Nemiroff & Bonnell are careful to point out that they do not guarantee their accuracy, and they invite other people to check them.
For another check, I acquired the first five million decimal digits of the square root of 5 as computed by Dawson Merrill. He has actually computed 10 million digits, but says only the first five million have been checked, and he is confident of their correctness. The average interval between complete permutation strings, plotted below, seems to converge fairly well on the predicted theoretical value.
[figure]
These mixed results lead to the question of how many digits would need to be checked in order to reasonably expect the overall frequency of complete permutation strings to be within, say, 1% of the theoretical asymptotic value. Also, does the speed of convergence for the digits of a particular number have any significance? Is the prompt convergence for the decimal digits of π on the asymptotic value just an accident?
One possible way of trying to answer these questions would be to treat the occurrence of Complete Permutation Strings (CPSs) as a Poisson process. Of course, since the digits of overlapping strings are not independent, this isn't exactly correct, because a Poisson model assumes a memoryless process, i.e., it assumes that the expected distance to the next occurrence is independent of any prior occurrences. With CPSs this is not the case, because the string immediately following a CPS has a probability of about 1/10 of also being a CPS (since the new digit simply needs to equal the digit being discarded). This is roughly born out in the case of the digits of e, because of the 778 CPSs there are 67 cases of consecutive CPSs. There are also 6 cases of two CPSs at a distance of 2 digits. On the other hand, it's also true that non-CPSs are disproportionately likely to have non-CPS neighbors, because pairs of duplicate digits are likely to be contained in the overlap of neighboring strings.
Nevertheless, we can use the Poisson model to give a rough estimate of the probability that the observed frequency over a given interval differs from the asymptotic frequency by various amounts. As discussed in Poisson Processes and Queues, the probability of exactly k occurrences of an (exponentially distributed) event with rate L in time (or number of trials) T is
[figure]
For large k we can use Stirling's formula for k! to write this in the more easily computed form
[figure]
We examined the first T = 2,000,000 strings in the decimal expansion of e, and found k = 778 complete permutation strings. The theoretical rate is L = 1/2755.73, so the expected number of CPSs in this range is LT = 725.76. The probability of finding exactly k complete strings in the first 2 million decimal digits is shown below for k ranging from 600 to 900.
[figure]
We've also marked on this figure the value 778, which is the number of CPSs found in the first 2,000,000 decimal digits of e. The probability that k would be equal to or greater than 778 is only about 2.8% based on this Poisson model.
A better method of evaluation would be to examine the digits in disjoint blocks of 10, because these blocks would (presumably) be statistically independent. On this basis our 2 million digits of e represent only 200,000 independent samples, among which we would expect to find 72.57 complete permutation strings. Now, we can split up the digits in essentially 10 different ways, depending on how we choose to frame the blocks. This amounts to partitioning the 778 CPSs according to the least significant digit of their index. Doing this, we find the following results
[figure]
On this basis the Poisson model is actually valid, so we can plot these results on top of the predicted distribution as shown below.
[figure]
The average of our ten "samples" is 77.8 (although these samples are not independent), and we can compute that the probability of this being 78 or higher is about 27.8%. Hence it is not terribly improbable that we would find this deviation from the expected number of CPSs over this number of digits. It would evidently be necessary to examine about 20 million digits to give a valid basis for drawing a conclusion about the actual density of CPSs in the decimal digits of e.
It's interesting that the block indices seem to bifurcate into the odds and the evens. In fact, if we just focused on the odd blocks, we find a mean of 72.6 CPSs per 200,000 samples, in excellent agreement with the expected number (72.57). In contrast, the even-indexed blocks have an average of 83 CPSs per 200,000 samples. The probability of finding 83 or more CPSs in this range is only 12.3%.
Postscript:  In November 2013 I received an email from Dan Corson informing me that, using digits of e computed by a program called “y-cruncher”, he had checked the number of CPSs up to 100 million digits, and found that it does finally approach the expected value, although even by this point it has not quite ever reached the expected value. Below is a plot of the rate of CPSs versus the number of digits for both e and π, based on tabulations provided by Corson (at ten samples per decade).
[figure]
Our previous considerations indicated that “it would evidently be necessary to examine about 20 million digits to give a valid basis for drawing a conclusion about the actual density of CPSs in the decimal digits of e”. This seems to be at least partially confirmed by the data, since by 20 million digits the observed rate is about 2720, which is significantly closer to the predicted asymptote than the observed rate in the first 2 million digits (which, we recall, was only about 2568). The most abrupt rise occurs between 4 million and 7 million digits, during which the rate rises from 2563 to 2707. It's somewhat re-assuring that the rate does eventually approach the predicted asymptote, but nevertheless it’s still interesting that it stays low for so long, especially in comparison with how quickly the digits of some other irrational numbers (such as π) approach the long-term expectation. Is it conceivable that different irrational numbers have different "frequencies", such that high-frequency numbers exhibit their expected averages very quickly, whereas low-frequency numbers may require billions of digits to exhibit the expected averages?
```

I am building a similar site for various subject areas related to practical, hands-on engineering. Here are the list of topics I'm planning:

```
The Invisible Cyclist Problem
Why Cameras Lie About Distances
Moravec's Paradox in Pixel Space
The Aperture Problem Dilemma
When Convolutional Kernels Hallucinate
Epipolar Geometry's Hidden Symmetries
The Correspondence Problem's Combinatorial Explosion
Aliasing: The Nyquist Frequency's Revenge
Why Deep Networks Fear Adversarial Patches
The Vanishing Point Theorem
Optical Flow's Aperture Ambiguity
When SIFT Descriptors Fail
The Harris Corner Detector's Blind Spots
Why Neural Networks Can't Count Cars
Homography Estimation Under Noise
The Eight-Point Algorithm's Degeneracies
When Stereo Vision Goes Cross-Eyed
The Fundamental Matrix's Rank Deficiency
Why Depth from Focus Never Quite Works
Texture Synthesis and the Markov Property
The Lucas-Kanade Method's Convergence Basin
When Histograms of Gradients Lose Direction
The Curse of Illumination Invariance
Why Background Subtraction Breaks
The Non-Maximum Suppression Paradox
Edge Detection's Scale-Space Journey
When Hough Transforms Miss Lines
Why Kalman Filters Drift in Vision
Template Matching's Correlation Catastrophe
The Moravec Interest Point Operator
The Chamfer Distance Transform
Why Superpixels Aren't Super
The Watershed Algorithm's Dam Problem
Belief Propagation on Pixel Grids
The Mumford-Shah Functional's Minimization
Why Optical Character Recognition Stutters
The Viola-Jones Cascade's Training Secrets
When Deformable Part Models Deform Too Much
The Grabcut Algorithm's Graph Cuts
Why Motion Blur Destroys Everything
The Canny Edge Detector's Hysteresis
The RANSAC Algorithm's Inlier Count
Why Photometric Stereo Needs Three Lights
The Structured Light Scanner's Stripe Patterns
The Retinex Theory's Illumination Estimation
Why Histogram Equalization Isn't Equal
The Bilateral Filter's Edge Preservation
When JPEG Compression Artifacts Attack
The Laplacian of Gaussian's Zero Crossings
Why Morphological Operations Erode Precision
The Distance Transform's Medial Axis
When Alpha Matting Meets Natural Images
The Seam Carving Algorithm's Content Awareness
Why Poisson Image Editing Works
The Variational Approach to Optical Flow
When Graph Cuts Solve Vision Problems
The Mean Shift Algorithm's Mode Seeking
The Non-Local Means Denoising Method
The Feature Pyramid Network's Multi-Scale Magic
Why Object Detection Boxes Never Fit
The Focal Loss Function's Hard Example Mining
Why Vision Transformers Patch Images
The Differentiable Rendering Revolution
Why 3D Convolutions See Through Time
The Point Cloud's Permutation Invariance
When NeRFs Render New Views
The Implicit Neural Representation's Coordinate Magic
Why CLIP Connects Images and Text
The Vision-Language Model's Modal Bridge
The Embodied AI's Visual Navigation
Why Knowledge Graphs Ground Visual Understanding
The Causal Inference in Computer Vision
When Fairness Meets Face Recognition
The Explainable AI's Saliency Maps
```

Please write the content for the topic: "{topic}"

1. Use the sample content provided for mathpages.com as a reference for the nature of content. But note that I am not interested in making it mathematical like mathpages.com, but focus more on engineering and building side of the subject.

2. Mention [figure] where there's supposed to be a figure, in a way that we will be able to recreate a figure based on the description (keep within 200 words). Keep the description between [figure] and [/figure]. Eg.

```
[figure]
This graph shows mathematical data related to the square root of 2 (≈1.414), as indicated by the red text at the top. The plot uses a black background with a y-axis ranging from 0 to 4000 and an x-axis labeled "Thousands of Digits" extending from 0 to 2000.

The main feature is a reddish-orange curve that begins at approximately 3500-3600 on the y-axis when the digit count is near zero. As the number of digits increases, this curve exhibits a steady downward trend, gradually declining and appearing to converge toward a horizontal reference line positioned around the 2800-3000 level.

A dotted horizontal line runs across the graph at roughly the 2800-3000 mark, likely representing a theoretical limit or expected value that the main curve is approaching. The convergence behavior suggests this graph is demonstrating how some mathematical property or calculation related to the square root of 2 stabilizes as more digits are considered.

The overall pattern shows typical mathematical convergence, where initial values start significantly above the target and gradually approach a stable limit as precision increases. This type of visualization is common in numerical analysis studies examining how mathematical constants or computed values behave as computational precision grows.
[/figure]

3. As for the length of the content, keep it to roughly the same size as the content provided above (from mathpages.com) not including the content within `[figure]...[/figure]`

4. Do not mention anything related to mathpages anywhere.

5. Keep it to the topic. Do not write anything fluffy like: `Here's my attempt at writing content for ...`. That's just noise.
```
"""

    def sanitize_filename(self, topic: str) -> str:
        """Convert topic title to a safe filename"""
        # Remove special characters and replace spaces with underscores
        safe_name = re.sub(r'[^\w\s-]', '', topic)
        safe_name = re.sub(r'[-\s]+', '_', safe_name)
        return safe_name.lower() + '.md'
    
    def generate_content(self, topic: str) -> str:
        """Generate content for a specific topic using Anthropic's API"""
        prompt = self.create_prompt(topic)
        
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=8000,
                temperature=0.7,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.content[0].text
        except Exception as e:
            print(f"Error generating content for '{topic}': {e}")
            return f"# {topic}\n\nError generating content: {e}"
    
    def save_article(self, topic: str, content: str) -> Path:
        """Save article content to a markdown file"""
        filename = self.sanitize_filename(topic)
        filepath = self.output_dir / filename
        
        # Add title header if not present
        if not content.startswith('#'):
            content = f"# {topic}\n\n{content}"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return filepath
    
    def generate_all_articles(self, topics: Optional[List[str]] = None, start_from: int = 0):
        """Generate articles for all topics"""
        if topics is None:
            topics = self.get_topics()
        
        # Filter topics based on start_from index
        topics_to_process = topics[start_from:]
        
        print(f"Generating {len(topics_to_process)} articles...")
        print(f"Output directory: {self.output_dir.absolute()}")
        
        successful = 0
        failed = 0
        
        for i, topic in enumerate(tqdm(topics_to_process, desc="Generating articles")):
            try:
                print(f"\nProcessing: {topic}")
                content = self.generate_content(topic)
                filepath = self.save_article(topic, content)
                print(f"Saved: {filepath}")
                successful += 1
                
                # Rate limiting
                if i < len(topics_to_process) - 1:  # Don't delay after the last request
                    time.sleep(self.request_delay)
                    
            except Exception as e:
                print(f"Failed to process '{topic}': {e}")
                failed += 1
                continue
        
        print(f"\nGeneration complete!")
        print(f"Successful: {successful}")
        print(f"Failed: {failed}")
        print(f"Articles saved in: {self.output_dir.absolute()}")
    
    def generate_index(self, topics: Optional[List[str]] = None):
        """Generate an index.md file listing all topics"""
        if topics is None:
            topics = self.get_topics()
        
        index_content = "# Engineering Pages\n\n"
        index_content += "## Topics\n\n"
        
        for topic in topics:
            filename = self.sanitize_filename(topic)
            index_content += f"- [{topic}]({filename})\n"
        
        index_path = self.output_dir / "index.md"
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        
        print(f"Index saved: {index_path}")


def main():
    """Main function to run the content generator"""
    # Example usage
    generator = ContentGenerator()
    
    # Generate index file first
    generator.generate_index()
    
    # Get all topics
    topics = generator.get_topics()
    
    print(f"Found {len(topics)} topics to generate")
    
    # Option to generate specific topics or all topics
    choice = input("Generate all articles? (y/n/partial): ").lower().strip()
    
    if choice == 'y':
        generator.generate_all_articles()
    elif choice == 'partial':
        start_idx = int(input(f"Start from topic index (0-{len(topics)-1}): "))
        end_idx = int(input(f"End at topic index (0-{len(topics)-1}): "))
        selected_topics = topics[start_idx:end_idx+1]
        generator.generate_all_articles(selected_topics)
    else:
        # Interactive selection
        print("\nAvailable topics:")
        for i, topic in enumerate(topics):
            print(f"{i:2d}: {topic}")
        
        indices = input("\nEnter topic indices (comma-separated): ").split(',')
        selected_topics = [topics[int(i.strip())] for i in indices if i.strip().isdigit()]
        generator.generate_all_articles(selected_topics)


if __name__ == "__main__":
    main()
