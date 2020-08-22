# Thunder-Detr
(unofficial) - customized fork of DETR, optimized and tuned for intelligent obj detection on 'real world' custom datasets

This is a customized framework based on FB AI's DETR, but with a number of improvements/modifications to optimize it for obj detection on your own datasets.
I had started a colab to show how to do this, but with more and more customizations piling up requiring more and more code modifications to DETR core...</br>it became clear building a codebase focused on handling custom datasets would be better and faster for all.
Thus, Thunder-Detr was born, 8/1/2020.

Updates:
8/22/20 - add thunder_file_utils.py.  </br>
Adds a coco_compressor to remap category_ids to contiguous values and rebase to zero.  </br>
Adds a show_catids to view the categories in a json file and shows the proper "num_classes" value for training DETR with. </br>
Usage:</br>
![](https://github.com/lessw2020/Thunder-Detr/blob/master/images/thunder_compress_view.PNG)

</br>
Various changes to improve results built into Thunder-Detr:</br>
1 - recommend LaProp optimizer vs AdamW.  </br>
2 - recommend bs of 4 (vs default 2 in DETR) </br>
3 - recommend ciou over giou default of DETR </br>
4 - recommend additional augmentations esp colorjitter </br>






