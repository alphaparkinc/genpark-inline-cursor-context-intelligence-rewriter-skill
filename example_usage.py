from client import InlineCursorContextIntelligenceRewriterClient

def main():
    client = InlineCursorContextIntelligenceRewriterClient()
    raw = "So basically what we did is we made the pipeline way faster and tests don't fail anymore."
    res = client.rewrite_inline(raw, "CONCISE_PROFESSIONAL")
    print(f"Latency: {res['processing_latency_ms']}ms")
    print(f"Clarity Improvement: +{res['clarity_delta_pct']}%")
    print("Rewritten Text:", res["rewritten_text"])

if __name__ == "__main__":
    main()
