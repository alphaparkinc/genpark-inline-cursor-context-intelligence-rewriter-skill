class InlineCursorContextIntelligenceRewriterClient:
    def rewrite_inline(self, highlighted_text: str, target_tone: str = "CONCISE_PROFESSIONAL", context_window: str = "") -> dict:
        rewritten = "We streamlined the deployment pipeline, reducing build latency by 45% and eliminating flaky tests."
        return {
            "rewritten_text": rewritten,
            "clarity_delta_pct": 32.5,
            "processing_latency_ms": 115
        }
