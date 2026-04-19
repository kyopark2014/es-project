claude_4_7_opus_models = {
    "model_type": "claude",
    "model_id": "global.anthropic.claude-opus-4-7"
}

claude_4_6_opus_models = {
    "model_type": "claude",
    "model_id": "global.anthropic.claude-opus-4-6-v1"
}

claude_4_6_sonnet_models = {
    "model_type": "claude",
    "model_id": "global.anthropic.claude-sonnet-4-6"
}

claude_4_5_haiku_models = {
    "model_type": "claude",
    "model_id": "global.anthropic.claude-haiku-4-5-20251001-v1:0"
}

claude_4_5_opus_models = {
    "model_type": "claude",
    "model_id": "global.anthropic.claude-opus-4-5-20251101-v1:0"
}

claude_4_5_sonnet_models = {
    "model_type": "claude",
    "model_id": "global.anthropic.claude-sonnet-4-5-20250929-v1:0"
}
    
def get_model_info(model_name):
    models = []

    if model_name == "Claude 4.5 Opus":
        models = claude_4_5_opus_models
    elif model_name == "Claude 4.5 Sonnet":
        models = claude_4_5_sonnet_models
    elif model_name == "Claude 4.5 Haiku":
        models = claude_4_5_haiku_models
    elif model_name == "Claude 4.6 Sonnet":
        models = claude_4_6_sonnet_models
    elif model_name == "Claude 4.6 Opus":
        models = claude_4_6_opus_models
    elif model_name == "Claude 4.7 Opus":
        models = claude_4_7_opus_models
    else:
        models = claude_4_6_sonnet_models

    return models
