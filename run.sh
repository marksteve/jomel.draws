#!/usr/bin/bash

mkdir -p output
for image in $(find style_images -iname "*.jpg")
do
  output=output/$(basename $image)
  if [ -f $output ]; then
    echo $output already exists
  else
    python neural_style.py \
      -style_image $image \
      -content_image content.jpg \
      -output_image $output \
      -gpu 0 \
      -backend cudnn \
      -original_colors 0 \
      -num_iterations 800 \
      -save_iter 0
  fi
done