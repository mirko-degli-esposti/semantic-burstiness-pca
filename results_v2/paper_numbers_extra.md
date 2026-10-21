# Additional paper numbers

## Per-text ratio <B_orig/B_surr>_k at q = 0.95

- vs M: Pearson r = 0.220 (P = 0.26), Spearman rho = 0.063 (P = 0.75), n = 28
- fiction: n = 20, mean 1.228 ± s.e. 0.013 (sd 0.059), range [1.146, 1.403]
- nonfiction: n = 8, mean 1.331 ± s.e. 0.021 (sd 0.061), range [1.231, 1.440]
- nonfiction - fiction: 0.103; Welch t = 4.11, P = 0.0013; Mann-Whitney U = 147, P = 0.00022
- ranks of the nonfiction texts (1 = highest of 28): [1, 3, 4, 5, 6, 7, 8, 15]
- fiction only, vs M: Pearson r = 0.441 (P = 0.05)

## Event counts and estimator error, n = (1-q) M, relative error ~ 1/sqrt(n)

- median M = 56,956: q=0.95: n=2,848, 1/sqrt(n)=1.9%, q=0.99: n=570, 1/sqrt(n)=4.2%
- shortest M = 21,855: q=0.95: n=1,093, 1/sqrt(n)=3.0%, q=0.99: n=219, 1/sqrt(n)=6.8%
- longest M = 235,426: q=0.95: n=11,771, 1/sqrt(n)=0.9%, q=0.99: n=2,354, 1/sqrt(n)=2.1%
  (shortest: tom_sawyer.txt; longest: war_and_peace.txt)

## Full-ordering failures

- q=0.6: 0 of 560 pairs
- q=0.7: 0 of 560 pairs
- q=0.8: 0 of 560 pairs
- q=0.9: 0 of 560 pairs
- q=0.95: 0 of 560 pairs
- q=0.99: 7 of 560 pairs: frankenstein k=1, tom_sawyer k=16, wuthering_heights k=5, wuthering_heights k=11, wuthering_heights k=15, wuthering_heights k=16, wuthering_heights k=17

## Semantic poles of the showcase texts (scripts/poles.py format, n = 6)

### war_and_peace.txt: B_max = 2.019 at PC3

```latex
PC1 & $+$ & 1.637 &
  \emph{gerasim} (26), \emph{maidservant} (5), \emph{irritably} (6), \emph{piteously} (7), \emph{nikolaevich} (6), \emph{andreevich} (8)
  & INTERPRETATION \\
PC1 & $-$ & &
  \emph{any} (466), \emph{government} (64), \emph{than} (533), \emph{its} (568), \emph{people} (557), \emph{us} (423)
  & INTERPRETATION \\
\midrule
PC2 & $+$ & 1.875 &
  \emph{regiment} (227), \emph{infantry} (82), \emph{cavalry} (77), \emph{battalion} (44), \emph{squadron} (64), \emph{brigade} (5)
  & INTERPRETATION \\
PC2 & $-$ & &
  \emph{really} (203), \emph{yourself} (117), \emph{feel} (133), \emph{myself} (148), \emph{laugh} (60), \emph{everybody} (119)
  & INTERPRETATION \\
\midrule
PC3 & $+$ & \textbf{2.019} &
  \emph{walked} (70), \emph{sat} (345), \emph{feet} (112), \emph{screaming} (6), \emph{yards} (20), \emph{clutching} (12)
  & INTERPRETATION \\
PC3 & $-$ & &
  \emph{principles} (7), \emph{undertake} (10), \emph{utmost} (12), \emph{renounce} (8), \emph{justification} (11), \emph{obligations} (7)
  & INTERPRETATION \\
```

### origin_of_species.txt: B_max = 1.876 at PC2

```latex
PC1 & $+$ & 1.250 &
  \emph{sessile} (11), \emph{faunas} (14), \emph{ovules} (6), \emph{plumage} (9), \emph{polymorphic} (9), \emph{insectivorous} (6)
  & INTERPRETATION \\
PC1 & $-$ & &
  \emph{he} (163), \emph{him} (17), \emph{said} (47), \emph{us} (104), \emph{she} (24), \emph{his} (90)
  & INTERPRETATION \\
\midrule
PC2 & $+$ & \textbf{1.876} &
  \emph{northern} (37), \emph{islands} (131), \emph{sea} (100), \emph{southern} (43), \emph{island} (60), \emph{eastern} (13)
  & INTERPRETATION \\
PC2 & $-$ & &
  \emph{innate} (7), \emph{slightest} (7), \emph{understand} (74), \emph{infer} (31), \emph{absolutely} (25), \emph{judgment} (12)
  & INTERPRETATION \\
\midrule
PC3 & $+$ & 1.740 &
  \emph{me} (153), \emph{eat} (5), \emph{squirrels} (5), \emph{beaks} (10), \emph{legs} (37), \emph{rabbit} (5)
  & INTERPRETATION \\
PC3 & $-$ & &
  \emph{geographical} (42), \emph{reduction} (5), \emph{increased} (27), \emph{proportional} (16), \emph{increase} (66), \emph{increases} (6)
  & INTERPRETATION \\
```

### great_expectations.txt: B_max = 1.249 at PC3

```latex
PC1 & $+$ & 1.189 &
  \emph{jaggers} (242), \emph{townsman} (6), \emph{biddy} (231), \emph{peeped} (5), \emph{stammered} (6), \emph{provis} (70)
  & INTERPRETATION \\
PC1 & $-$ & &
  \emph{will} (174), \emph{government} (5), \emph{its} (151), \emph{year} (26), \emph{states} (6), \emph{their} (175)
  & INTERPRETATION \\
\midrule
PC2 & $+$ & 1.217 &
  \emph{river} (59), \emph{near} (66), \emph{opened} (41), \emph{fell} (55), \emph{port} (7), \emph{centre} (5)
  & INTERPRETATION \\
PC2 & $-$ & &
  \emph{really} (41), \emph{understand} (53), \emph{think} (241), \emph{anybody} (30), \emph{myself} (236), \emph{yourself} (51)
  & INTERPRETATION \\
\midrule
PC3 & $+$ & \textbf{1.249} &
  \emph{walked} (45), \emph{legs} (35), \emph{feet} (34), \emph{staring} (26), \emph{crying} (15), \emph{bed} (72)
  & INTERPRETATION \\
PC3 & $-$ & &
  \emph{concerning} (13), \emph{regarding} (8), \emph{recognised} (14), \emph{expressly} (5), \emph{derived} (13), \emph{relation} (12)
  & INTERPRETATION \\
```

### ulysses.txt: B_max = 1.470 at PC2

```latex
PC1 & $+$ & 1.299 &
  \emph{wonderworker} (6), \emph{dedalus} (174), \emph{maggy} (9), \emph{purefoy} (20), \emph{dignam} (83), \emph{voglio} (9)
  & INTERPRETATION \\
PC1 & $-$ & &
  \emph{government} (14), \emph{any} (191), \emph{than} (169), \emph{people} (78), \emph{because} (219), \emph{year} (71)
  & INTERPRETATION \\
\midrule
PC2 & $+$ & \textbf{1.470} &
  \emph{st} (6), \emph{william} (40), \emph{edward} (17), \emph{sir} (219), \emph{attended} (7), \emph{frederick} (10)
  & INTERPRETATION \\
PC2 & $-$ & &
  \emph{yourself} (38), \emph{really} (49), \emph{feel} (104), \emph{stuff} (24), \emph{stupid} (11), \emph{ourselves} (10)
  & INTERPRETATION \\
\midrule
PC3 & $+$ & 1.324 &
  \emph{thick} (24), \emph{inches} (7), \emph{surface} (10), \emph{tail} (24), \emph{mud} (6), \emph{sloping} (9)
  & INTERPRETATION \\
PC3 & $-$ & &
  \emph{married} (56), \emph{marry} (10), \emph{poet} (29), \emph{sir} (219), \emph{son} (113), \emph{brother} (66)
  & INTERPRETATION \\
```

