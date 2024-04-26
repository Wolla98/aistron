export CUDA_VISIBLE_DEVICES=0
export AISTRON_DATASETS=../data/datasets/

# KINS
#python projects/AISFormer/train_net.py --config-file projects/AISFormer/configs/KINS2020/aisformer_R50_FPN_kins2020_6ep_bs1.yaml --num-gpus 1 \
#python projects/AISFormer/train_net.py --config-file projects/AISFormer/configs/KINS2020/aisformer_R101_FPN_kins2020_6ep_bs1.yaml --num-gpus 1 \

# COCOA
# python projects/AISFormer/train_net.py --config-file projects/AISFormer/configs/COCOA/aisformer_R50_FPN_cocoa_8ep_bs2.yaml --num-gpus 1 \
#python projects/AISFormer/train_net.py --config-file projects/AISFormer/configs/COCOA/aisformer_R101_FPN_cocoa_8ep_bs2.yaml --num-gpus 1 \

# COCOA-cls
# python projects/AISFormer/train_net.py --config-file projects/AISFormer/configs/COCOA-cls/aisformer_R50_FPN_cocoa_cls_8ep_bs2.yaml --num-gpus 1 \

# D2SA
#python projects/AISFormer/train_net.py --config-file projects/AISFormer/configs/D2SA/aisformer_R50_FPN_d2sa_18ep_bs2.yaml --num-gpus 1 \

# COCO
python projects/AISFormer/train_net.py --config-file projects/AISFormer/configs/COCO/aisformer_R50_FPN_coco_asbu_8ep_bs2.yaml --num-gpus 1 \


## Eval
# python projects/AISFormer/train_net.py \
#     --config-file projects/AISFormer/configs/COCO/aisformer_R50_FPN_coco_asbu_8ep_bs2.yaml \
#     --num-gpus 1 \
#     --eval-only MODEL.WEIGHTS /home/winston/projects/AmodalSegmentation/data/aisformer_model_outputs/coco_asbu_test_asbu/model_final.pth \

# ## Cocoa_cls modified test
# python projects/AISFormer/train_net.py --config-file projects/AISFormer/configs/COCOA-cls/cocoa_cls_modified_TEST.yaml --num-gpus 1 \