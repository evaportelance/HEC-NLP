import torch
import torch.nn as nn
import numpy as np


def test_layer_norm(your_layer_norm_class):
    # Set random seed for reproducibility
    torch.manual_seed(42)

    # Test parameters
    batch_size = 2
    seq_len = 3
    hidden_size = 4
    eps = 1e-12

    # Create random input tensor
    x = torch.randn(batch_size, seq_len, hidden_size)

    # Create our custom LayerNorm
    custom_ln = your_layer_norm_class(hidden_size, eps=eps)

    # Create PyTorch's built-in LayerNorm
    torch_ln = nn.LayerNorm(hidden_size, eps=eps)

    # Initialize the weights and biases to be the same
    with torch.no_grad():
        torch_ln.weight.copy_(custom_ln.weight_D)
        torch_ln.bias.copy_(custom_ln.bias_D)

    # Forward pass
    custom_output = custom_ln(x)
    torch_output = torch_ln(x)

    # Check if outputs are close
    is_close = torch.allclose(custom_output, torch_output, rtol=1e-5, atol=1e-5)

    # Print results
    print(f"Input shape: {x.shape}")
    print(f"Custom output shape: {custom_output.shape}")
    print(f"PyTorch output shape: {torch_output.shape}")
    print(f"Outputs match: {is_close}")

    if is_close:
        print("✅ Test passed! Custom LayerNorm matches PyTorch's implementation.")
    else:
        print("❌ Test failed! Outputs don't match.")
        # Print the maximum absolute difference
        max_diff = torch.max(torch.abs(custom_output - torch_output))
        print(f"Maximum absolute difference: {max_diff.item()}")

        # Print a sample of the outputs
        print("\nSample outputs (first element):")
        print(f"Custom: {custom_output[0, 0]}")
        print(f"PyTorch: {torch_output[0, 0]}")

        # Check if the means and variances match
        custom_mean = custom_output.mean(dim=-1)
        torch_mean = torch_output.mean(dim=-1)
        custom_var = custom_output.var(dim=-1)
        torch_var = torch_output.var(dim=-1)

        print(
            "\nMeans close:",
            torch.allclose(custom_mean, torch_mean, rtol=1e-5, atol=1e-5),
        )
        print(
            "Variances close:",
            torch.allclose(custom_var, torch_var, rtol=1e-5, atol=1e-5),
        )


def test_mlp(your_mlp_class):
    # Set random seed for reproducibility
    torch.manual_seed(42)

    # Test parameters
    batch_size = 2
    seq_len = 3
    hidden_size = 4
    intermediate_size = 8
    dropout_prob = 0.0  # Set to 0 for deterministic testing

    # Create random input tensor
    x = torch.randn(batch_size, seq_len, hidden_size)

    # Create our MLP
    mlp = your_mlp_class(hidden_size, intermediate_size, dropout=dropout_prob)

    # Set to eval mode to disable dropout for deterministic results
    mlp.eval()

    # Forward pass
    output = mlp(x)

    # Check output shape
    expected_shape = (batch_size, seq_len, hidden_size)
    shape_correct = output.shape == expected_shape

    # Create a reference implementation for comparison
    class ReferenceMLP(nn.Module):
        def __init__(self, hidden_size, intermediate_size, dropout=0.0):
            super().__init__()
            self.linear1 = nn.Linear(hidden_size, intermediate_size)
            self.linear2 = nn.Linear(intermediate_size, hidden_size)
            self.activation = nn.GELU()
            self.dropout = nn.Dropout(dropout)

        def forward(self, x):
            x = self.activation(self.linear1(x))
            x = self.dropout(x)
            x = self.linear2(x)
            return x

    # Create reference MLP with same weights
    ref_mlp = ReferenceMLP(hidden_size, intermediate_size, dropout_prob)
    with torch.no_grad():
        ref_mlp.linear1.weight.copy_(mlp.W_in_DF.weight)
        ref_mlp.linear1.bias.copy_(mlp.W_in_DF.bias)
        ref_mlp.linear2.weight.copy_(mlp.W_out_FD.weight)
        ref_mlp.linear2.bias.copy_(mlp.W_out_FD.bias)

    ref_mlp.eval()
    ref_output = ref_mlp(x)

    # Check if outputs match
    outputs_match = torch.allclose(output, ref_output, rtol=1e-5, atol=1e-5)

    # Print results
    print(f"Input shape: {x.shape}")
    print(f"Output shape: {output.shape}")
    print(f"Expected shape: {expected_shape}")
    print(f"Shape is correct: {shape_correct}")
    print(f"Outputs match reference implementation: {outputs_match}")

    # Test activation function
    # Extract intermediate activations
    with torch.no_grad():
        intermediate = mlp.activation_function(mlp.W_in_DF(x))
        ref_intermediate = ref_mlp.activation(ref_mlp.linear1(x))

    activations_match = torch.allclose(
        intermediate, ref_intermediate, rtol=1e-5, atol=1e-5
    )
    print(f"Activations match: {activations_match}")

    # Overall test result
    if shape_correct and outputs_match and activations_match:
        print("✅ Test passed! MLP implementation is correct.")
    else:
        print("❌ Test failed!")
        if not shape_correct:
            print("  - Output shape is incorrect")
        if not outputs_match:
            print("  - Output values don't match reference implementation")
            max_diff = torch.max(torch.abs(output - ref_output))
            print(f"  - Maximum absolute difference: {max_diff.item()}")
        if not activations_match:
            print("  - Activation function output doesn't match reference")


def test_self_attention_outputs(your_self_attention_class):
    """Test that specifically checks the output tensor and attention weights from SelfAttention."""
    # Set random seed for reproducibility
    torch.manual_seed(42)

    # Test parameters
    batch_size = 2
    seq_len = 4
    hidden_size = 12
    num_heads = 3
    dropout_prob = 0.0  # Set to 0 for deterministic testing

    # Create random input tensor
    x = torch.randn(batch_size, seq_len, hidden_size)

    # print("Testing SelfAttention outputs...")

    # Test both regular and causal attention
    for causal in [False, True]:
        print(f"\n--- {'Causal' if causal else 'Regular'} Self-Attention ---")

        # Create our SelfAttention module
        attn = your_self_attention_class(
            hidden_size, num_heads, dropout=dropout_prob, causal=causal
        )

        # Set to eval mode to disable dropout for deterministic results
        attn.eval()

        # Forward pass
        out_BLD, attn_BHLL = attn(x)

        # 1. Check output shape
        expected_out_shape = (batch_size, seq_len, hidden_size)
        expected_attn_shape = (batch_size, num_heads, seq_len, seq_len)

        print(f"Output shape: {out_BLD.shape}, Expected: {expected_out_shape}")
        print(
            f"Attention weights shape: {attn_BHLL.shape}, Expected: {expected_attn_shape}"
        )

        shape_correct = (
            out_BLD.shape == expected_out_shape
            and attn_BHLL.shape == expected_attn_shape
        )

        # 2. Check attention weights sum to 1 along the last dimension
        attn_sum = attn_BHLL.sum(dim=-1)
        attn_sum_correct = torch.allclose(
            attn_sum, torch.ones_like(attn_sum), rtol=1e-5, atol=1e-5
        )
        print(f"Attention weights sum to 1: {attn_sum_correct}")

        # 3. Check attention weights are non-negative (after softmax)
        attn_non_negative = torch.all(attn_BHLL >= 0)
        print(f"Attention weights are non-negative: {attn_non_negative}")

        # 4. Check causal masking if applicable
        if causal:
            # Upper triangular part should be 0 (future tokens masked)
            mask = torch.triu(torch.ones(seq_len, seq_len), diagonal=1).bool()
            upper_tri_zero = torch.all(attn_BHLL[:, :, mask] < 1e-6)
            print(
                f"Future tokens properly masked (upper triangular is ~0): {upper_tri_zero}"
            )

            # Check that the diagonal and lower triangular have non-zero values
            lower_tri_mask = ~mask
            lower_tri_nonzero = torch.any(attn_BHLL[:, :, lower_tri_mask] > 1e-6)
            print(
                f"Present/past tokens have attention (lower triangular has non-zeros): {lower_tri_nonzero}"
            )

            causal_correct = upper_tri_zero and lower_tri_nonzero
        else:
            # For non-causal attention, check that attention is distributed across all positions
            # (this is a bit of a heuristic check)
            attn_distributed = torch.all(torch.any(attn_BHLL > 0.1, dim=-1))
            print(f"Attention is distributed across positions: {attn_distributed}")
            causal_correct = attn_distributed

        # 5. Check output values are reasonable (not NaN or Inf)
        output_valid = torch.all(torch.isfinite(out_BLD))
        print(f"Output values are finite (no NaN/Inf): {output_valid}")

        # Overall test result
        all_correct = (
            shape_correct
            and attn_sum_correct
            and attn_non_negative
            and causal_correct
            and output_valid
        )

        if all_correct:
            print(
                f"✅ All checks passed for {'Causal' if causal else 'Regular'} Self-Attention!"
            )
        else:
            print(
                f"❌ Some checks failed for {'Causal' if causal else 'Regular'} Self-Attention!"
            )
            if not shape_correct:
                print("  - Output shapes are incorrect")
            if not attn_sum_correct:
                print("  - Attention weights don't sum to 1")
            if not attn_non_negative:
                print("  - Attention weights contain negative values")
            if causal and not upper_tri_zero:
                print("  - Future tokens are not properly masked")
            if causal and not lower_tri_nonzero:
                print("  - Present/past tokens don't have attention")
            if not causal and not attn_distributed:
                print("  - Attention is not well distributed")
            if not output_valid:
                print("  - Output contains NaN or Inf values")
