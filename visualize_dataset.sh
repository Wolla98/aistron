export AISTRON_DATASETS=../data/datasets/
output_dir=/home/winston/projects/AmodalSegmentation/data/asbu_viz/coco_asbu_test_visible # directory to output the visualize images 
dataset_name=coco_asbu_train # kins2020_train, d2sa_train, or your_custom_datasets_name
segm_type=visible # amodal or visible (the mode of the visualized masks)

python tools/visualize_data.py \
    --output-dir ${output_dir} \
    --dataset-name ${dataset_name} \
    --segm_type ${segm_type} \
    --source "annotation" \