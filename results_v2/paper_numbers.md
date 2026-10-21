# Numbers for the paper (regenerated)

## 1. Four showcase texts (Table tab:single_text_summary and per-text sections)

| text | N | M | OOV (old) | alpha (old) | alpha0 (old) | r(lambda,B), P (old) | rho, P | B2 (old) | LaTeX |
|---|---|---|---|---|---|---|---|---|---|
| War and Peace | 564,609 | 235,426 | 1.6% (1.6%) | 0.724 (0.721) | 0.76 (0.76) | 0.708, P=0.0046 (0.702, 0.0006) | 0.847, P=0.0000 | 1.875 (1.855) | 0.708$^{**}$ |
| Origin of Species | 150,812 | 58,583 | 0.4% (0.4%) | 0.772 (0.771) | 0.80 (0.8) | 0.393, P=0.0894 (0.295, 0.207) | 0.678, P=0.0015 | 1.876 (1.888) | 0.393 |
| Great Expectations | 186,170 | 62,754 | 1.3% (1.3%) | 0.703 (0.689) | 0.76 (0.74) | 0.421, P=0.0641 (0.511, 0.021) | 0.611, P=0.0053 | 1.217 (1.209) | 0.421 |
| Ulysses | 263,007 | 100,539 | 0.7% (0.7%) | 0.778 (0.763) | 0.80 (0.8) | 0.664, P=0.0149 (0.571, 0.009) | 0.887, P=0.0000 | 1.470 (1.495) | 0.664$^{*}$ |

### War and Peace
- EVR PC1 7.00% (old 6.98), PC2 4.21% (old 4.21), PC3 2.97%, first ten 27.2% (old 27.2)
- q=0.95: B1=1.637, B2=1.875, B3=2.019; largest at PC3 (B=2.019); null at that k: surr 0.973, FGN 0.988
- mean over k=1..20: B_orig 1.366 (old Bbar 1.36), B_surr 0.974, B_FGN 0.977; null range surr [0.969,0.976], FGN [0.960,1.001]
- ordering B_orig > B_FGN and > B_surr at q=0.95: 20/20
- quantile sweep, full ordering: q=0.6: 20/20, q=0.7: 20/20, q=0.8: 20/20, q=0.9: 20/20, q=0.95: 20/20, q=0.99: 20/20

### Origin of Species
- EVR PC1 6.64% (old 6.61), PC2 3.61% (old 3.58), PC3 3.00%, first ten 26.4% (old 26.4)
- q=0.95: B1=1.250, B2=1.876, B3=1.740; largest at PC2 (B=1.876); null at that k: surr 0.965, FGN 1.030
- mean over k=1..20: B_orig 1.315 (old Bbar 1.35), B_surr 0.974, B_FGN 0.979; null range surr [0.963,0.984], FGN [0.943,1.030]
- ordering B_orig > B_FGN and > B_surr at q=0.95: 20/20
- quantile sweep, full ordering: q=0.6: 20/20, q=0.7: 20/20, q=0.8: 20/20, q=0.9: 20/20, q=0.95: 20/20, q=0.99: 20/20

### Great Expectations
- EVR PC1 6.22% (old 6.54), PC2 4.46% (old 4.34), PC3 3.02%, first ten 27.1% (old 27.2)
- q=0.95: B1=1.189, B2=1.217, B3=1.249; largest at PC3 (B=1.249); null at that k: surr 0.971, FGN 0.985
- mean over k=1..20: B_orig 1.171 (old Bbar 1.18), B_surr 0.974, B_FGN 0.980; null range surr [0.964,0.983], FGN [0.962,1.003]
- ordering B_orig > B_FGN and > B_surr at q=0.95: 20/20
- quantile sweep, full ordering: q=0.6: 20/20, q=0.7: 20/20, q=0.8: 20/20, q=0.9: 20/20, q=0.95: 20/20, q=0.99: 20/20

### Ulysses
- EVR PC1 6.83% (old None), PC2 3.43% (old None), PC3 3.10%, first ten 25.1% (old 25.0)
- q=0.95: B1=1.299, B2=1.470, B3=1.324; largest at PC2 (B=1.470); null at that k: surr 0.973, FGN 0.964
- mean over k=1..20: B_orig 1.212 (old Bbar 1.23), B_surr 0.973, B_FGN 0.978; null range surr [0.965,0.980], FGN [0.950,1.017]
- ordering B_orig > B_FGN and > B_surr at q=0.95: 20/20
- quantile sweep, full ordering: q=0.6: 20/20, q=0.7: 20/20, q=0.8: 20/20, q=0.9: 20/20, q=0.95: 20/20, q=0.99: 20/20

## 2. Corpus table (tab:corpus) — 28 texts, from corpus_burstiness.csv

| file | N | M | alpha | alpha0 |
|---|---|---|---|---|
| analysis_of_mind.txt | 88,221 | 30,515 | 0.752 | 0.76 |
| david_copperfield.txt | 351,160 | 128,534 | 0.720 | 0.76 |
| don_quixote.txt | 404,384 | 147,764 | 0.716 | 0.76 |
| dorian_gray.txt | 79,257 | 25,728 | 0.844 | 0.87 |
| dracula.txt | 161,221 | 55,315 | 0.768 | 0.83 |
| frankenstein.txt | 75,080 | 24,533 | 0.709 | 0.71 |
| great_expectations.txt | 186,170 | 62,754 | 0.703 | 0.76 |
| huckleberry_finn.txt | 111,380 | 34,640 | 0.736 | 0.78 |
| island_life.txt | 130,882 | 50,061 | 0.861 | 0.92 |
| jane_eyre.txt | 187,243 | 68,221 | 0.682 | 0.71 |
| life_on_the_mississippi.txt | 130,313 | 45,856 | 0.742 | 0.78 |
| middlemarch.txt | 319,788 | 119,568 | 0.725 | 0.78 |
| moby_dick.txt | 211,867 | 80,978 | 0.698 | 0.73 |
| oliver_twist.txt | 158,505 | 58,014 | 0.721 | 0.76 |
| origin_of_species.txt | 150,812 | 58,583 | 0.772 | 0.80 |
| pride_and_prejudice.txt | 122,219 | 42,366 | 0.642 | 0.67 |
| psychology_briefer_course.txt | 150,453 | 55,898 | 0.695 | 0.73 |
| system_of_logic.txt | 371,981 | 142,532 | 0.772 | 0.83 |
| tess_of_the_durbervilles.txt | 150,506 | 51,546 | 0.685 | 0.71 |
| the_jungle.txt | 151,114 | 49,524 | 0.773 | 0.83 |
| the_rainbow.txt | 187,449 | 67,032 | 0.715 | 0.76 |
| theory_of_moral_sentiments.txt | 105,956 | 35,602 | 0.713 | 0.73 |
| tom_sawyer.txt | 70,817 | 21,855 | 0.792 | 0.80 |
| ulysses.txt | 263,007 | 100,539 | 0.778 | 0.80 |
| vanity_fair.txt | 305,028 | 120,171 | 0.717 | 0.76 |
| voyage_of_the_beagle.txt | 196,103 | 79,752 | 0.646 | 0.69 |
| war_and_peace.txt | 564,609 | 235,426 | 0.724 | 0.76 |
| wuthering_heights.txt | 116,810 | 40,331 | 0.721 | 0.75 |

N range [70,817, 564,609]; M range [21,855, 235,426] (old: 27,000–565,000 and 12,000–321,000, with Alice); alpha range [0.64, 0.86] (old [0.61, 0.85])

## 3. Corpus-level burstiness (sec. Component-resolved ... corpus-wide, Robustness, Distribution)

- <B_k^orig>_texts over k: range [1.15, 1.39], mean 1.22 (old [1.12,1.37], 1.22)
- <B_k^surr>_texts: [0.973, 0.975] (old [0.972,0.978]); <B_k^FGN>_texts: [0.968, 0.983] (old [0.970,0.992])
- pairs (text,k) at q=0.95: 560; B_orig > B_surr in 100.0% (old 100%); B_orig > B_FGN in 100.0% (old 99.4%); |B_FGN/B_surr - 1| < 0.05 in 97.7% (old 95.9%)
- ratio orig/surr: mean over pairs 1.2574 ± s.e. 0.0059 (sd 0.140), range [1.03, 2.08]; per-text means: mean 1.257, sd 0.075, range [1.15, 1.44]; t-test vs 1: t=43.52, p=1.15e-181   (old 1.248±0.011, texts [1.14,1.30] sd 0.044)
- ratio orig/FGN: mean over pairs 1.2566 ± s.e. 0.0059 (sd 0.139), range [1.03, 2.04]; per-text means: mean 1.257, sd 0.073, range [1.15, 1.43]; t-test vs 1: t=43.58, p=6.6e-182   (old 1.244±0.010)
- ratio FGN/surr: mean over pairs 1.0009 ± s.e. 0.0009 (sd 0.021), range [0.93, 1.11]; per-text means: mean 1.001, sd 0.004, range [0.99, 1.01]; t-test vs 1: t=1.02, p=0.309   (old 1.0035±0.0012, range [0.94,1.11], t=2.88 p=0.011)

Per-text mean ratios at q=0.95 (definition of eq. ratio_corpus):

| file | orig/surr | orig/FGN | FGN/surr |
|---|---|---|---|
| wuthering_heights.txt | 1.146 | 1.152 | 0.9950 |
| pride_and_prejudice.txt | 1.150 | 1.163 | 0.9891 |
| middlemarch.txt | 1.170 | 1.165 | 1.0043 |
| tess_of_the_durbervilles.txt | 1.192 | 1.191 | 1.0010 |
| david_copperfield.txt | 1.195 | 1.198 | 0.9979 |
| jane_eyre.txt | 1.196 | 1.193 | 1.0031 |
| vanity_fair.txt | 1.197 | 1.198 | 0.9995 |
| oliver_twist.txt | 1.199 | 1.198 | 1.0020 |
| great_expectations.txt | 1.202 | 1.195 | 1.0062 |
| dorian_gray.txt | 1.204 | 1.207 | 0.9976 |
| don_quixote.txt | 1.218 | 1.219 | 0.9994 |
| frankenstein.txt | 1.225 | 1.230 | 0.9959 |
| tom_sawyer.txt | 1.230 | 1.233 | 0.9999 |
| theory_of_moral_sentiments.txt | 1.231 | 1.235 | 0.9974 |
| ulysses.txt | 1.245 | 1.239 | 1.0049 |
| dracula.txt | 1.246 | 1.246 | 0.9996 |
| moby_dick.txt | 1.277 | 1.275 | 1.0024 |
| the_jungle.txt | 1.283 | 1.283 | 1.0013 |
| huckleberry_finn.txt | 1.288 | 1.286 | 1.0019 |
| the_rainbow.txt | 1.290 | 1.288 | 1.0025 |
| psychology_briefer_course.txt | 1.293 | 1.286 | 1.0062 |
| life_on_the_mississippi.txt | 1.297 | 1.296 | 1.0010 |
| analysis_of_mind.txt | 1.340 | 1.340 | 1.0015 |
| voyage_of_the_beagle.txt | 1.344 | 1.349 | 0.9977 |
| origin_of_species.txt | 1.350 | 1.342 | 1.0045 |
| system_of_logic.txt | 1.355 | 1.347 | 1.0057 |
| war_and_peace.txt | 1.403 | 1.397 | 1.0038 |
| island_life.txt | 1.440 | 1.434 | 1.0035 |
- orig/surr: mean over 28 texts 1.2574 ± s.e. 0.0143 (sd 0.0754), range [1.146, 1.440], t=18.06, p=1.3e-16
- orig/FGN: mean over 28 texts 1.2566 ± s.e. 0.0138 (sd 0.0731), range [1.152, 1.434], t=18.58, p=6.5e-17
- FGN/surr: mean over 28 texts 1.0009 ± s.e. 0.0007 (sd 0.0038), range [0.989, 1.006], t=1.22, p=0.23

By q (fraction of pairs):

| q | orig>surr | orig>FGN | full ordering | \|FGN/surr-1\|<0.05 |
|---|---|---|---|---|
| 0.6 | 100.0% | 100.0% | 100.0% | 100.0% |
| 0.7 | 100.0% | 100.0% | 100.0% | 100.0% |
| 0.8 | 100.0% | 100.0% | 100.0% | 100.0% |
| 0.9 | 100.0% | 100.0% | 100.0% | 99.1% |
| 0.95 | 100.0% | 100.0% | 100.0% | 97.7% |
| 0.99 | 99.5% | 98.8% | 98.8% | 77.0% |

(old: orig>FGN >= 99.4% for q<=0.95 and 98.7% at 0.99; |FGN/surr-1|<0.05 >98% for q<=0.90, 85% at 0.99)

## 4. ACF (sec. Empirical results, Corpus-level ACF results)

### Great Expectations (alpha=0.703, old 0.688; M=62,754; ci95=0.008)
- rho_k(1) orig range [0.050, 0.209] (old [0.042,0.179]); FGN: all < 0.025? True, max |rho_FGN(1)| 0.009, inside band 18/20 (old 19/20); rho_1^FGN(1)=0.009 (old 0.023)

Table tab:acf_summary (k=1..10):

| k | rho(1) orig | rho(1) FGN | rho(100) orig | rho(100) FGN |
|---|---|---|---|---|
| 1 | 0.067 | 0.009 | 0.009 | -0.000 |
| 2 | 0.209 | 0.003 | 0.022 | 0.004 |
| 3 | 0.142 | 0.008 | 0.021 | 0.004 |
| 4 | 0.127 | 0.002 | 0.008 | -0.001 |
| 5 | 0.081 | 0.009 | 0.007 | 0.001 |
| 6 | 0.118 | 0.003 | 0.006 | -0.001 |
| 7 | 0.130 | 0.002 | 0.000 | -0.002 |
| 8 | 0.093 | -0.006 | 0.008 | -0.010 |
| 9 | 0.090 | -0.004 | 0.011 | -0.012 |
| 10 | 0.084 | -0.001 | 0.010 | 0.004 |

k=11..20: max |rho_FGN(1)| = 0.007 (old 'all < 0.007'); bold = |rho| > ci95 = 0.008

### Corpus (28 texts, 560 (text,k) pairs)
- lag 1: rho_orig 0.099 ± 0.042; rho_FGN 0.001 ± 0.005; rho_surr -0.000 ± 0.004
- lag 10: rho_orig 0.030 ± 0.019; rho_FGN 0.000 ± 0.004; rho_surr -0.000 ± 0.004
- lag 100: rho_orig 0.011 ± 0.011; rho_FGN 0.000 ± 0.005; rho_surr 0.000 ± 0.004
  (old: orig 0.096±0.044 / 0.026±0.017 / 0.010±0.009; FGN(1) 0.003±0.009; surr(1) 0.000±0.004)

| lag | orig sig | FGN sig | surr sig |
|---|---|---|---|
| 1 | 100.0% | 9.5% | 3.8% |
| 2 | 99.8% | 5.9% | 4.5% |
| 5 | 98.6% | 5.9% | 2.7% |
| 10 | 94.5% | 3.8% | 4.3% |
| 20 | 86.4% | 5.7% | 5.2% |
| 50 | 70.9% | 5.7% | 3.6% |
| 100 | 53.8% | 5.0% | 6.4% |
| 200 | 40.5% | 5.5% | 5.9% |
| 300 | 32.1% | 5.7% | 4.5% |

'original significant and FGN not' by lag: 1: 90.5%, 2: 93.9%, 5: 92.9%, 10: 90.7%, 20: 81.8%, 50: 67.0%, 100: 51.4%, 200: 38.9%, 300: 30.4% (old: peak 89.7% at lag 2, >56% up to 100)

(old lag 1: 100% / 17.2% / 4.7%; lag 2: 89.7% orig; 'above 56% up to lag ...')
- rho_k(1) orig range [0.027, 0.249] (old [0.020,0.282]); FGN range [-0.014, 0.027] (old [-0.015,0.058]); t-test FGN rho(1) vs 0: t=5.94, p=5.04e-09 (old t=5.83); orig-null gap 0.097 (old 0.093)
- fraction of FGN pairs with rho(1) > 0.007: 11.1%

## 5. DFA of projections (sec. DFA of projected series)

### Great Expectations, table tab:dfa_proj

| k | orig | FGN | surr |
|---|---|---|---|
| 1 | 0.607 | 0.530 | 0.505 |
| 2 | 0.683 | 0.497 | 0.499 |
| 3 | 0.696 | 0.514 | 0.500 |
| 4 | 0.640 | 0.481 | 0.500 |
| 5 | 0.642 | 0.500 | 0.499 |
| 6 | 0.634 | 0.482 | 0.500 |
| 7 | 0.644 | 0.513 | 0.497 |
| 8 | 0.634 | 0.483 | 0.502 |
| 9 | 0.656 | 0.483 | 0.501 |
| 10 | 0.640 | 0.517 | 0.500 |
| 11 | 0.581 | 0.510 | 0.502 |
| 12 | 0.621 | 0.490 | 0.497 |
| 13 | 0.583 | 0.495 | 0.501 |
| 14 | 0.583 | 0.513 | 0.492 |
| 15 | 0.605 | 0.494 | 0.500 |
| 16 | 0.615 | 0.520 | 0.499 |
| 17 | 0.598 | 0.518 | 0.488 |
| 18 | 0.631 | 0.476 | 0.502 |
| 19 | 0.610 | 0.479 | 0.500 |
| 20 | 0.591 | 0.500 | 0.498 |

means ± sd: orig 0.625 ± 0.032 (old 0.637±0.032); FGN 0.500 ± 0.016 (old 0.502±0.015); surr 0.499 ± 0.004 (old 0.499±0.002)
- orig > 0.5: 20/20; |FGN-0.5|<0.05: 20/20; orig range [0.581, 0.696] (old [0.575,0.698]); max orig at PC3=0.696, min at PC11=0.581

### Corpus
- mean ± sd over 560 pairs: orig 0.663 ± 0.053; FGN 0.504 ± 0.019; surr 0.499 ± 0.005; orig>0.5 in 99.8%, |FGN-0.5|<0.05 in 97.3%

## 6. Verification: does the frequency filter preserve rank-level scaling?

Calibration column: `a(rank,unfilt)` is `projection_alpha` applied to the
unfiltered rank sequence, to be compared with `alpha_text` computed by the
pipeline. If the two disagree, the remaining columns are not comparable.

| text | M | M_FGN | M_FGN/M | a(rank,unfilt) | alpha_text | a(rank orig,filt) | a(rank FGN,filt) |
|---|---|---|---|---|---|---|---|
| War and Peace | 235,426 | 235,426 | 1.0000 | 0.694 | 0.724 | 0.674 | 0.632 |
| Origin of Species | 58,583 | 58,583 | 1.0000 | 0.726 | 0.772 | 0.694 | 0.643 |
| Great Expectations | 62,754 | 62,754 | 1.0000 | 0.673 | 0.703 | 0.605 | 0.599 |
| Ulysses | 100,539 | 100,539 | 1.0000 | 0.804 | 0.778 | 0.777 | 0.628 |
  - multiset identical to original: True

### Multiset identity vs the high-frequency cutoff R

| text | unfiltered | R=100 | R=150 | R=200 |
|---|---|---|---|---|
| War and Peace | True | True (239,219/239,219) | True (209,719/209,719) | True (188,275/188,275) |
| Origin of Species | True | True (58,843/58,843) | True (50,743/50,743) | True (45,106/45,106) |
| Great Expectations | True | True (63,606/63,606) | True (52,741/52,741) | True (45,195/45,195) |
| Ulysses | True | True (101,286/101,286) | True (90,304/90,304) | True (82,487/82,487) |
- PCA components retained: 300
- eigenvalues 300, proj (100539, 20), attrs ['K', 'components', 'eigenvalues', 'explained_variance_ratio', 'mean', 'proj']

### Burstiness beyond the retained K=20 (PCA refitted with K=50)

| text | cum.var 20 | 50 | 100 | mean B 1..20 | 21..50 | min B 21..50 | all > geom | refit err |
|---|---|---|---|---|---|---|---|---|
| War and Peace | 37.9% | 57.2% | 76.5% | 1.366 | 1.140 | 1.086 | True | 1.4e-06 |
| Origin of Species | 38.2% | 59.1% | 78.7% | 1.315 | 1.191 | 1.101 | True | 9.5e-07 |
| Great Expectations | 38.6% | 59.2% | 78.8% | 1.171 | 1.121 | 1.037 | True | 7.2e-07 |
| Ulysses | 35.0% | 53.2% | 72.7% | 1.212 | 1.120 | 1.059 | True | 9.5e-07 |
