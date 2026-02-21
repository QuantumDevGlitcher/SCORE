#!/usr/bin/env bash
set -euo pipefail

ROOT="packages/core/src/score_core"

mkdir -p "$ROOT"/{domain/{entities,value_objects},ports/{context,feedback,perception,preferences,recommender,scoring,storage},application/{use_cases,services},scoring/{rules,fuzzy,nn},adapters/{context,feedback,persistence},infrastructure/{logging,perception,preferences,recommender,scoring,storage},utils}

touch \
  "$ROOT/__init__.py" \
  "$ROOT/domain/__init__.py" \
  "$ROOT/domain/entities/__init__.py" \
  "$ROOT/domain/value_objects/__init__.py" \
  "$ROOT/ports/__init__.py" \
  "$ROOT/application/__init__.py" \
  "$ROOT/application/use_cases/__init__.py" \
  "$ROOT/application/services/__init__.py" \
  "$ROOT/scoring/__init__.py" \
  "$ROOT/scoring/rules/__init__.py" \
  "$ROOT/scoring/fuzzy/__init__.py" \
  "$ROOT/scoring/nn/__init__.py" \
  "$ROOT/adapters/__init__.py" \
  "$ROOT/adapters/context/__init__.py" \
  "$ROOT/adapters/feedback/__init__.py" \
  "$ROOT/adapters/persistence/__init__.py" \
  "$ROOT/infrastructure/__init__.py" \
  "$ROOT/infrastructure/logging/__init__.py" \
  "$ROOT/infrastructure/perception/__init__.py" \
  "$ROOT/infrastructure/preferences/__init__.py" \
  "$ROOT/infrastructure/recommender/__init__.py" \
  "$ROOT/infrastructure/scoring/__init__.py" \
  "$ROOT/infrastructure/storage/__init__.py" \
  "$ROOT/utils/__init__.py"

# Domain files
touch \
  "$ROOT/domain/entities/garment.py" \
  "$ROOT/domain/entities/outfit.py" \
  "$ROOT/domain/entities/user_profile.py" \
  "$ROOT/domain/value_objects/context.py" \
  "$ROOT/domain/value_objects/color.py" \
  "$ROOT/domain/value_objects/score.py" \
  "$ROOT/domain/value_objects/explanation.py" \
  "$ROOT/domain/errors.py"

# Ports files
touch \
  "$ROOT/ports/storage/wardrobe_repository_port.py" \
  "$ROOT/ports/preferences/preferences_port.py" \
  "$ROOT/ports/perception/perception_port.py" \
  "$ROOT/ports/context/context_provider_port.py" \
  "$ROOT/ports/scoring/scoring_engine_port.py" \
  "$ROOT/ports/recommender/recommender_port.py"

# Use cases
touch \
  "$ROOT/application/use_cases/uc01_outfit_completion.py" \
  "$ROOT/application/use_cases/uc02_garment_comparison.py" \
  "$ROOT/application/use_cases/uc03_full_recommendation.py" \
  "$ROOT/application/use_cases/uc04_photo_analysis.py"

# Services
touch \
  "$ROOT/application/services/outfit_generator_service.py" \
  "$ROOT/application/services/filter_service.py" \
  "$ROOT/application/services/explainability_service.py" \
  "$ROOT/application/services/feedback_service.py"

# Scoring layer
touch \
  "$ROOT/scoring/scoring_engine.py" \
  "$ROOT/scoring/rules/hard_constraints.py" \
  "$ROOT/scoring/rules/color_harmony.py" \
  "$ROOT/scoring/rules/formality.py" \
  "$ROOT/scoring/rules/warmth_weather.py" \
  "$ROOT/scoring/rules/style_coherence.py" \
  "$ROOT/scoring/rules/weights.py" \
  "$ROOT/scoring/fuzzy/membership.py" \
  "$ROOT/scoring/fuzzy/rule_base.py" \
  "$ROOT/scoring/fuzzy/fuzzy_engine.py" \
  "$ROOT/scoring/nn/features.py" \
  "$ROOT/scoring/nn/compatibility_model.py" \
  "$ROOT/scoring/nn/inference.py"

# Adapters
touch \
  "$ROOT/adapters/persistence/dto_mapper.py" \
  "$ROOT/adapters/context/context_normalizer.py" \
  "$ROOT/adapters/context/weather_labels.py" \
  "$ROOT/adapters/feedback/feedback_mapper.py"

# Infrastructure implementations
touch \
  "$ROOT/infrastructure/storage/json_wardrobe_repository.py" \
  "$ROOT/infrastructure/storage/sqlite_wardrobe_repository.py" \
  "$ROOT/infrastructure/preferences/sqlite_preferences_repository.py" \
  "$ROOT/infrastructure/perception/cnn_classifier_runtime.py" \
  "$ROOT/infrastructure/perception/segmentation_runtime.py" \
  "$ROOT/infrastructure/perception/color_extractor.py" \
  "$ROOT/infrastructure/context_weather_api_adapter.py" \
  "$ROOT/infrastructure/scoring/nn_runtime.py" \
  "$ROOT/infrastructure/logging/logger.py"

echo "✅ Created SCORE core structure under: $ROOT"