# Thunder-Detr
(unofficial) - customized fork of DETR, optimized and tuned for intelligent obj detection on 'real world' custom datasets

This is a customized framework based on FB AI's DETR, but with a number of improvements/modifications to optimize it for obj detection on your own datasets.
I had started a colab to show how to do this, but with more and more customizations piling up requiring more and more code modifications to DETR core...it became clear building a codebase focused on handling custom datasets would be better and faster for all.
Thus, Thunder-Detr was born, 8/1/2020.

Various changes to improve results built into Thunder-Detr:
1 - recommend LaProp optimizer vs AdamW.  
2 - recommend bs of 4 (vs default 2 in DETR)
3 - recommend ciou over giou default of DETR
4 - recommend additional augmentations esp colorjitter






