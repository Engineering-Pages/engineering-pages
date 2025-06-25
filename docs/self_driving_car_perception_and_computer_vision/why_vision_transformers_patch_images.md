# Why Vision Transformers Patch Images

Why Vision Transformers Patch Images

The Vision Transformer (ViT) architecture introduced a paradigm shift in computer vision by treating images not as continuous 2D grids but as sequences of discrete patches. This seemingly counterintuitive approach - chopping up images into a grid of non-overlapping squares - actually reveals deep insights about how we can process visual information more efficiently.

[figure]
A diagram showing how a 224x224 pixel RGB image is divided into 16x16 patches, creating a 14x14 grid. The patches are color-coded to show their sequential ordering. Below this, each patch is flattened into a 768-dimensional vector (16x16x3=768). These vectors are arranged in a sequence, with a special [CLS] token prepended at the start. A positional encoding is added to each vector, visualized as a heatmap overlay showing how spatial information is preserved despite the sequential arrangement.
[/figure]

Traditional convolutional networks process images through hierarchical sliding windows, gradually building up feature representations. This approach mimics biological vision but comes with computational overhead - each pixel needs to be processed multiple times as different convolution kernels slide across it. The patching approach of Vision Transformers takes a different route - it immediately transforms the image into a sequence of independent tokens that can be processed in parallel.

The engineering brilliance of this approach becomes apparent when we examine the implementation. By converting the image into fixed-size patches (typically 16x16 pixels), we create a sequence length that scales quadratically with image resolution rather than the quartic scaling of attention over individual pixels. This makes attention computationally feasible for high-resolution images.

[figure]
A performance comparison graph showing throughput (images/second) versus accuracy on ImageNet for three architectures: CNN (blue line), ViT with 32x32 patches (green line), and ViT with 16x16 patches (red line). The graph demonstrates how smaller patch sizes achieve higher accuracy but with lower throughput, while larger patches enable faster processing at a slight cost to performance. The axes are logarithmic, highlighting the efficiency-accuracy tradeoff.
[/figure]

However, this patching strategy introduces its own challenges. The hard boundaries between patches can create artifacts - the model might miss features that span patch boundaries. Modern implementations address this through overlapping patches or by using convolutional stem layers before the transformer blocks. The patch size itself becomes a critical hyperparameter: smaller patches preserve more fine-grained detail but increase computational cost, while larger patches process faster but might miss important local structure.

The patch embedding layer, which projects each patch into a high-dimensional feature space, plays a crucial role. Unlike CNNs that learn hierarchical features naturally through their architecture, Vision Transformers must encode all spatial relationships through this initial embedding combined with positional encodings. This makes the design of the patch embedding particularly important for model performance.

[figure]
An attention visualization showing how different patches attend to each other in the first few layers of a Vision Transformer. The figure uses a 7x7 grid of patches from a face image, with bright lines connecting patches that have strong attention weights between them. Early layers show mostly local attention patterns (connecting adjacent patches), while deeper layers develop more global attention patterns (connecting distant but semantically related patches).
[/figure]

Recent architectural innovations have started exploring adaptive patching strategies, where patch sizes vary based on image content or task requirements. Some models dynamically merge or split patches during processing, allowing them to allocate computational resources more efficiently. These developments suggest that while fixed patching was the breakthrough that enabled Vision Transformers, the future might lie in more flexible approaches to image tokenization.

The success of patch-based processing has implications beyond just Vision Transformers. It challenges our assumptions about how visual information should be processed and suggests that the continuous nature of images, while intuitive to humans, might not be the optimal representation for machine learning systems. This insight has sparked new research directions in discrete visual representations and efficient image processing architectures.