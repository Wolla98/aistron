export AISTRON_DATASETS=../data/datasets/
output_dir=/home/winston/projects/AmodalSegmentation/data/asbu_viz # directory to output the visualize images 
dataset_name=coco_2017 # kins2020_train, d2sa_train, or your_custom_datasets_name
segm_type=amodal # amodal or visible (the mode of the visualized masks)

python tools/visualize_data.py \
    --output-dir ${output_dir} \
    --dataset-name ${dataset_name} \
    --segm_type ${segm_type} \
    --source "annotation" \