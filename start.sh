#!/usr/bin/env bash
set -e

# สร้างโฟลเดอร์ตามโครงสร้าง
mkdir -p ckpt/densepose
mkdir -p ckpt/humanparsing
mkdir -p ckpt/image_encoder
mkdir -p ckpt/openpose/ckpts

# ดาวน์โหลดแต่ละไฟล์
wget -O ckpt/densepose/model_final_162be9.pkl \
  "https://huggingface.co/yisol/IDM-VTON/resolve/main/densepose/model_final_162be9.pkl"

wget -O ckpt/humanparsing/parsing_atr.onnx \
  "https://huggingface.co/yisol/IDM-VTON/resolve/main/humanparsing/parsing_atr.onnx"

wget -O ckpt/humanparsing/parsing_lip.onnx \
  "https://huggingface.co/yisol/IDM-VTON/resolve/main/humanparsing/parsing_lip.onnx"

wget -O ckpt/openpose/ckpts/body_pose_model.pth \
  "https://huggingface.co/yisol/IDM-VTON/resolve/main/openpose/ckpts/body_pose_model.pth"

wget -O ckpt/image_encoder/model.safetensors \
  "https://huggingface.co/yisol/IDM-VTON/resolve/main/image_encoder/model.safetensors"  
