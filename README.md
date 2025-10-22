# 🩺 USF-MAE: Ultrasound Self-Supervised Foundation Model with Masked Autoencoding

This repository accompanies the paper:

> **USF-MAE: Ultrasound Self-Supervised Foundation Model with Masked Autoencoding for Cross-Task Generalization**  
> Youssef [Your Last Name], et al., 2025  
> Submitted to *Intelligent Medicine* Journal

---

## 🧠 Overview

**USF-MAE** is the first large-scale, self-supervised transformer foundation model trained exclusively on ultrasound (US) data.  
The model leverages a **Vision Transformer (ViT)**–based masked autoencoder (MAE) architecture to learn rich, modality-specific representations directly from unlabeled ultrasound scans.

USF-MAE was pretrained on **370,000 2D and 3D ultrasound images** curated from **46 open-source datasets**, collectively named **OpenUS-46**.  
This repository provides:
- The **USF-MAE pretrained checkpoint**
- Access links and references for **OpenUS-46**
- Scripts for preprocessing and fine-tuning
- Example code for integrating USF-MAE into downstream tasks

---

## 📦 Model Highlights

- **Architecture:** Vision Transformer (ViT) encoder–decoder MAE  
- **Pretraining strategy:** Self-supervised masked patch reconstruction  
- **Pretraining data:** 370K unlabeled ultrasound images from 46 datasets  
- **Downstream tasks:**  
  - Breast cancer classification (BUS-BRA)  
  - Ovarian tumor subtype classification (MMOTU-2D)  
  - Gastrointestinal stromal tumor detection (GIST514-DB)  
- **Key results:**  
  - F1-scores of 81.6 %, 79.6 %, and 82.4 % on the above tasks  
  - Outperformed CNN and ViT baselines  
  - Comparable to the supervised UltraSam model while using no labels

---

## 🌍 OpenUS-46 Dataset Collection

**OpenUS-46** is a large, unified compilation of 46 publicly available ultrasound datasets from multiple anatomical regions and clinical tasks.  
All datasets remain under their original licenses. We provide direct access links for research reproducibility and transparency.

| Dataset Name | Anatomy / Target Region | Access Link |
|---------------|------------------------|--------------|
| 105US | Liver | [Link](#) |
| AbdomenUS | Abdomen | [Link](#) |
| ACOUSLIC | Abdomen | [Link](#) |
| AUL | Liver | [Link](#) |
| BLUES | Lung | [Link](#) |
| BP | Neck | [Link](#) |
| Brachial Plexus | Neck | [Link](#) |
| BrEaST | Breast | [Link](#) |
| BUS (Dataset B) | Breast | [Link](#) |
| BUS_UC | Breast | [Link](#) |
| BUS_UCML | Breast | [Link](#) |
| BUS-BRA | Breast | [Link](#) |
| Cactus Dataset | Heart | [Link](#) |
| CAMUS_public | Echocardiography | [Link](#) |
| CardiacUDC | Heart | [Link](#) |
| CCAUI | Common Carotid Artery | [Link](#) |
| DFHI | Fetal Head | [Link](#) |
| EchoCP | Heart | [Link](#) |
| EchoNet-Dynamic | Heart | [Link](#) |
| EchoNet-Pediatric | Heart | [Link](#) |
| FALLMUD | Leg Muscle | [Link](#) |
| FASS | Fetal Abdominal | [Link](#) |
| Fast-U-Net | Fetal Abdominal | [Link](#) |
| FEFT | Fetal Echocardiography | [Link](#) |
| FETAL_PLANES_DB | Fetal Anatomy | [Link](#) |
| FH-PS-AOP | Fetal Head | [Link](#) |
| GIST514-DB | Gastrointestinal | [Link](#) |
| HC | Fetal Head Circumference | [Link](#) |
| JNU-IFM | Pelvis and Fetal Head | [Link](#) |
| kidneyUS | Kidney | [Link](#) |
| LUSS_phantom | Lung | [Link](#) |
| MicroSeg | Prostate | [Link](#) |
| MMOTU-2D | Ovarian Tumor | [Link](#) |
| MMOTU-3D | Ovarian Tumor | [Link](#) |
| Pocus | Lung | [Link](#) |
| Porcine | Spinal Cord | [Link](#) |
| PSFHS | Pelvis and Fetal Head | [Link](#) |
| regPro | Prostate | [Link](#) |
| S1 | Breast | [Link](#) |
| Segthy | Thyroid and Neck | [Link](#) |
| STMUS_NDA | Musculoskeletal | [Link](#) |
| STU-Hospital | N/A | [Link](#) |
| Thyroid Dataset | Head and Neck | [Link](#) |
| Thyroid US Cineclip | Thyroid | [Link](#) |
| Ultrasound Fetus Dataset | Fetal | [Link](#) |
| UPBD | Brachial Plexus | [Link](#) |

> 📘 *Note:* Replace each “[Link](#)” with the corresponding dataset URL or DOI. All datasets retain their original licenses and should be cited appropriately.

---

## 🧩 Checkpoints

| Model | Pretraining Data | Epochs | Download |
|--------|------------------|---------|-----------|
| **USF-MAE (100 epochs)** | OpenUS-46 (370K images) | 100 | [Download](#) |
| **USF-MAE (500 epochs)** | OpenUS-46 (370K images) | 500 | [Download](#) |

---

## 🧪 Usage

```bash
# Clone repository
git clone https://github.com/yourusername/USF-MAE.git
cd USF-MAE

# Example: load pretrained model
python scripts/load_usfmae.py --checkpoint checkpoints/usfmae_100ep.pth
