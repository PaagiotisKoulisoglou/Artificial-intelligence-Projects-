# Transformer from Scratch (PyTorch)

This project is a minimal implementation of the **Transformer** architecture using PyTorch. It follows the original paper [Attention Is All You Need](https://arxiv.abs/1706.03762) but is written with clarity in mind so that newcomers can understand how the model works under the hood.

## What is a Transformer?

A Transformer is a neural network architecture designed to handle sequential data (like text) without relying on recurrence (RNNs) or convolution (CNNs). It is built on the concept of **self-attention**, which allows the model to weigh the importance of different tokens in a sequence when encoding or generating text.

## Project Structure

The project contains the following key components:

- `SelfAttention`: Computes scaled dot-product attention across multiple heads. Each head captures different relationships in the sequence.
- `TransformerBlock`: Combines multi-head attention, residual connections, normalization, and a feed-forward network.
- `Encoder`: Stacks multiple transformer blocks. Adds word embeddings and positional embeddings to preserve order.
- `DecoderBlock`: A block with masked self-attention and encoder-decoder attention.
- `Decoder`: Stacks multiple decoder blocks to generate outputs.
- `Transformer`: The full model combining encoder and decoder. Handles masking to ignore padding and enforce causal order.

## How the Pipeline Works

1.  **Input Tokens** (source and target) are converted into **embeddings**.
2.  **Positional Embeddings** are added to capture sequence order.
3.  **Encoder** processes the source sequence with self-attention layers to create context-rich representations.
4.  **Decoder** processes the target sequence using:
    -   **Masked self-attention** (to prevent looking ahead).
    -   **Attention over encoder outputs** (to use source context).
5.  **Linear Layer + Softmax** projects decoder outputs to vocabulary size for prediction.

## Key Concepts to Know

-   **Embedding**: Turns tokens into dense vectors.
-   **Attention**: Mechanism to decide which tokens to focus on.
-   **Multi-Head Attention**: Runs multiple attentions in parallel.
-   **Masking**: Prevents attending to padding tokens or future tokens.
-   **Residual Connections**: Helps gradients flow by adding input back to output.

## Notes

-   This implementation is meant for learning and clarity, not production training.
-   You can extend it with optimizers, loss functions, and datasets to train it on tasks like translation or text generation.

## Example Run

The included `main` section runs a small test with toy data:

```python
import torch

# ... (assuming the classes are defined)

x = torch.tensor([[1,5,6,4,3,9,5,2,0],[1,8,7,3,4,5,6,7,2]]).to(device)
trg = torch.tensor([[1,7,4,3,5,9,2,0],[1,5,6,2,4,3,9,2]]).to(device)

model = Transformer(src_vocab_size=10, trg_vocab_size=10, src_pad_idx=0, trg_pad_idx=0, device=device).to(device)
out = model(x, trg[:, :-1])
print(out.shape) # torch.Size([batch_size, target_len, trg_vocab_size])



