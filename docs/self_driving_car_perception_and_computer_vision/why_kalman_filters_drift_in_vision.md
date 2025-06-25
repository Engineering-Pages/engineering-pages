# Why Kalman Filters Drift in Vision

Why Kalman Filters Drift in Vision

The Kalman filter, a cornerstone of modern tracking systems, exhibits peculiar behavior when applied to computer vision tasks that often goes unnoticed until systems fail in production. While these filters excel at tracking objects with well-defined motion models, their performance in vision applications can deteriorate due to several interconnected factors that create cumulative drift.

The primary culprit is the assumption of Gaussian noise in measurements. In vision systems, measurement errors are rarely Gaussian. Consider a feature tracker following corner points across frames. The measurement uncertainty is heavily influenced by illumination changes, motion blur, and perspective distortions. When these non-Gaussian errors are fed into a Kalman filter, the state estimates begin to drift.

[figure]
A split-screen visualization showing feature point tracking across video frames. The left side shows ideal Gaussian measurement noise as assumed by the Kalman filter, represented by symmetric uncertainty ellipses around tracked points. The right side shows actual vision-based measurements, where uncertainty regions are irregularly shaped and vary with lighting conditions. Arrows indicate how the estimated position (red dot) drifts from ground truth (green dot) over time, with the drift increasing non-linearly.
[/figure]

Another significant issue arises from the linear motion model assumption. Real-world objects rarely move linearly, especially when projected onto the image plane. A person walking parallel to the camera plane appears to move faster when closer to the camera and slower when farther away. The Kalman filter's linear prediction model struggles with this perspective effect, leading to systematic bias in state estimates.

[figure]
Three graphs showing tracking error over time for different scenarios. The top graph shows error for linear motion parallel to the image plane (stable). The middle graph shows error for motion with varying depth (increasing drift). The bottom graph shows error under rapid perspective changes (exponential drift). Each graph plots ground truth (green), Kalman estimate (red), and uncertainty bounds (gray).
[/figure]

Process noise estimation presents another challenge. Vision systems often struggle to differentiate between measurement noise and actual motion changes. When a tracked object temporarily disappears behind an obstacle, should the filter increase its uncertainty estimate or maintain its prediction? Most implementations choose conservative uncertainty growth, leading to drift when objects reappear in unexpected locations.

The solution often lies in hybrid approaches. Modern systems combine Kalman filtering with visual odometry or deep learning-based motion prediction. Some implementations use adaptive noise models that adjust based on visual quality metrics. Others employ multiple hypothesis tracking, maintaining several Kalman filters with different motion models and selecting the best performer.

[figure]
Architecture diagram showing a hybrid tracking system. The central Kalman filter (blue) receives inputs from traditional measurements (green), visual odometry (yellow), and deep learning prediction (purple). Confidence weights dynamically adjust the influence of each source based on visual quality metrics. Error feedback loops (red) allow for adaptive noise model updates.
[/figure]

Practitioners should be particularly cautious when tracking objects through extended occlusions or rapid camera motion. The drift becomes most apparent in augmented reality applications, where virtual overlays gradually misalign with real-world features. Regular re-initialization using robust visual features or external sensors remains essential for long-term stability.

Understanding these limitations doesn't diminish the Kalman filter's utility in vision applications. Rather, it emphasizes the importance of careful system design that accounts for vision-specific challenges. The most successful implementations treat the Kalman filter as one component in a larger visual tracking ecosystem, rather than relying on it as a complete solution.