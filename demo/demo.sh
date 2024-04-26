python demo/demo.py \
  --config-file projects/AISFormer/configs/COCO/aisformer_R50_FPN_coco_asbu_8ep_bs2.yaml \
  --input /home/winston/projects/AmodalSegmentation/data/datasets/coco/val2017/*.jpg \
  --output /home/winston/projects/AmodalSegmentation/data/asbu_viz/coco_asbu_demo_test_asbu_amodal/demo \
  --segm_type amodal \
  --opts MODEL.WEIGHTS /home/winston/projects/AmodalSegmentation/data/aisformer_model_outputs/coco_asbu_test_asbu/model_final.pth \