# E1: DFA of filtered rank sequences, original vs FGN

Estimator of the FGN-matching step: `dfa_exponent`, L = 100 .. min(10000, n/4), 10 scales; ranks of the original frequency table. orig/fgn = alpha of the original / FGN rank sequence; diff = fgn - orig.

| file | genre | N | M | alpha0 | unfilt orig | unfilt FGN | filt orig | filt FGN | traj orig | traj FGN | diff traj | shuf traj |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| analysis_of_mind | nonfiction | 88,221 | 30,515 | 0.758 | 0.752 | 0.752 | 0.635 | 0.630 | 0.628 | 0.630 | +0.001 | 0.501 |
| david_copperfield | fiction | 351,160 | 128,534 | 0.758 | 0.719 | 0.710 | 0.717 | 0.618 | 0.715 | 0.621 | -0.094 | 0.520 |
| don_quixote | fiction | 404,384 | 147,764 | 0.758 | 0.716 | 0.712 | 0.686 | 0.609 | 0.680 | 0.610 | -0.070 | 0.519 |
| dorian_gray | fiction | 79,257 | 25,728 | 0.874 | 0.844 | 0.850 | 0.693 | 0.751 | 0.693 | 0.749 | +0.057 | 0.542 |
| dracula | fiction | 161,221 | 55,315 | 0.828 | 0.768 | 0.771 | 0.725 | 0.683 | 0.715 | 0.681 | -0.034 | 0.468 |
| frankenstein | fiction | 75,080 | 24,533 | 0.712 | 0.708 | 0.714 | 0.607 | 0.535 | 0.600 | 0.527 | -0.072 | 0.458 |
| great_expectations | fiction | 186,170 | 62,754 | 0.758 | 0.703 | 0.712 | 0.621 | 0.602 | 0.616 | 0.607 | -0.010 | 0.470 |
| huckleberry_finn | fiction | 111,380 | 34,640 | 0.781 | 0.736 | 0.744 | 0.646 | 0.620 | 0.642 | 0.611 | -0.030 | 0.487 |
| island_life | nonfiction | 130,882 | 50,061 | 0.919 | 0.861 | 0.851 | 0.700 | 0.790 | 0.692 | 0.783 | +0.091 | 0.461 |
| jane_eyre | fiction | 187,243 | 68,221 | 0.712 | 0.682 | 0.673 | 0.631 | 0.557 | 0.631 | 0.555 | -0.077 | 0.533 |
| life_on_the_mississippi | nonfiction | 130,313 | 45,856 | 0.781 | 0.742 | 0.743 | 0.699 | 0.655 | 0.700 | 0.650 | -0.050 | 0.440 |
| middlemarch | fiction | 319,788 | 119,568 | 0.781 | 0.725 | 0.733 | 0.707 | 0.650 | 0.696 | 0.646 | -0.050 | 0.476 |
| moby_dick | fiction | 211,867 | 80,978 | 0.735 | 0.698 | 0.695 | 0.698 | 0.563 | 0.694 | 0.561 | -0.133 | 0.469 |
| oliver_twist | fiction | 158,505 | 58,014 | 0.758 | 0.721 | 0.719 | 0.589 | 0.610 | 0.569 | 0.613 | +0.044 | 0.470 |
| origin_of_species | nonfiction | 150,812 | 58,583 | 0.804 | 0.772 | 0.765 | 0.774 | 0.681 | 0.775 | 0.684 | -0.091 | 0.511 |
| pride_and_prejudice | fiction | 122,219 | 42,366 | 0.666 | 0.642 | 0.636 | 0.644 | 0.557 | 0.640 | 0.553 | -0.087 | 0.484 |
| psychology_briefer_course | nonfiction | 150,453 | 55,898 | 0.735 | 0.695 | 0.702 | 0.648 | 0.607 | 0.653 | 0.604 | -0.049 | 0.496 |
| system_of_logic | nonfiction | 371,981 | 142,532 | 0.828 | 0.772 | 0.779 | 0.744 | 0.701 | 0.743 | 0.715 | -0.028 | 0.496 |
| tess_of_the_durbervilles | fiction | 150,506 | 51,546 | 0.712 | 0.685 | 0.679 | 0.606 | 0.563 | 0.605 | 0.564 | -0.040 | 0.492 |
| the_jungle | fiction | 151,114 | 49,524 | 0.828 | 0.773 | 0.778 | 0.666 | 0.694 | 0.662 | 0.698 | +0.037 | 0.481 |
| the_rainbow | fiction | 187,449 | 67,032 | 0.758 | 0.715 | 0.714 | 0.647 | 0.613 | 0.653 | 0.617 | -0.035 | 0.489 |
| theory_of_moral_sentiments | nonfiction | 105,956 | 35,602 | 0.735 | 0.713 | 0.710 | 0.704 | 0.598 | 0.707 | 0.602 | -0.105 | 0.478 |
| tom_sawyer | fiction | 70,817 | 21,855 | 0.804 | 0.792 | 0.792 | 0.649 | 0.649 | 0.656 | 0.645 | -0.011 | 0.506 |
| ulysses | fiction | 263,007 | 100,539 | 0.804 | 0.778 | 0.771 | 0.816 | 0.640 | 0.801 | 0.642 | -0.159 | 0.489 |
| vanity_fair | fiction | 305,028 | 120,171 | 0.758 | 0.717 | 0.717 | 0.666 | 0.624 | 0.666 | 0.620 | -0.046 | 0.496 |
| voyage_of_the_beagle | nonfiction | 196,103 | 79,752 | 0.689 | 0.646 | 0.652 | 0.568 | 0.578 | 0.574 | 0.568 | -0.006 | 0.476 |
| war_and_peace | fiction | 564,609 | 235,426 | 0.758 | 0.724 | 0.721 | 0.750 | 0.649 | 0.727 | 0.640 | -0.088 | 0.487 |
| wuthering_heights | fiction | 116,810 | 40,331 | 0.747 | 0.721 | 0.720 | 0.627 | 0.631 | 0.616 | 0.625 | +0.010 | 0.495 |

## Summary over texts (paired)

- unfilt: orig 0.733 ± 0.050, FGN 0.733 ± 0.050; diff mean -0.000 (sd 0.006, range [-0.010, +0.009]), FGN < orig in 15/28; paired t = -0.11, P = 0.91; Wilcoxon P = 0.81
- filt: orig 0.674 ± 0.058, FGN 0.631 ± 0.058; diff mean -0.043 (sd 0.058, range [-0.176, +0.090]), FGN < orig in 22/28; paired t = -3.93, P = 0.00054; Wilcoxon P = 0.00058
- traj: orig 0.670 ± 0.056, FGN 0.629 ± 0.059; diff mean -0.040 (sd 0.057, range [-0.159, +0.091]), FGN < orig in 22/28; paired t = -3.74, P = 0.00087; Wilcoxon P = 0.0014
- drop from unfilt to traj: orig -0.063, FGN -0.103
- shuffled traj: 0.489 ± 0.023
- check: alpha_match_target == orig_unfilt to 1e-9: True; |alpha_match_fgn - fgn_unfilt| max 0

By genre (traj):

- fiction: n = 20, orig 0.664, FGN 0.619, diff -0.044 ± 0.013 (s.e.)
- nonfiction: n = 8, orig 0.684, FGN 0.654, diff -0.030 ± 0.022 (s.e.)
