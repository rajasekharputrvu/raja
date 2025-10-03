import matplotlib.pyplot as plt
import matplotlib as venn

# Create figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Addition Rule (Union)
venn.venn2(subsets=(1, 1, 1), set_labels=('A', 'B'), ax=axes[0])
axes[0].set_title("Addition Rule (A ∪ B) = A OR B")

# Multiplication Rule (Intersection)
venn.venn2(subsets=(1, 1, 1), set_labels=('A', 'B'), ax=axes[1])
# Highlight only the intersection
venn.venn2_circles(subsets=(1, 1, 1), ax=axes[1])
axes[1].set_title("Multiplication Rule (A ∩ B) = A AND B")

plt.show()
