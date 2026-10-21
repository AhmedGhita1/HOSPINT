"""Local video perception for hospint."""

from __future__ import annotations

from hospint.qwen import get_qwen


def describe_video(video_path: str) -> str:
    """Produce the factual description consumed by HORUS extraction."""

    if not video_path:
        raise ValueError("A video path is required.")
    return get_qwen().describe_video(video_path)
