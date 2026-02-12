import typer
from pathlib import Path

from score_core.domain.entities.garment import Garment
from score_core.application.use_cases.recommend_outfit import recommend_outfits

app = typer.Typer(help="SCORE CLI")

# =========================================================
# OPTION A: SIMPLE TOP-LEVEL TASK COMMANDS (team-friendly)
# =========================================================

@app.command("recommend")
def recommend(
    context: str = typer.Option("university", help="Occasion/context"),
):
    """Recommend outfit combinations given a context."""
    current = [
        Garment(kind="top", color_primary="orange"),
        Garment(kind="bottom", color_primary="green"),
    ]
    recs = recommend_outfits(current=current, context=context)
    for r in recs:
        typer.echo(f"- score={r.score} | {r.explanation}")

@app.command("detect")
def detect(
    image: Path = typer.Option(..., exists=False, help="Path to input image (stub)"),
):
    """Detect garments/colors from an image (stub for now)."""
    typer.echo(f"[stub] detect: would process image at: {image}")

@app.command("train")
def train(
    data_dir: Path = typer.Option(..., exists=False, help="Dataset directory (training-only)"),
    epochs: int = typer.Option(1, help="Epochs (stub)"),
):
    """Train the model (stub for now)."""
    typer.echo(f"[stub] train: data_dir={data_dir}, epochs={epochs}")

@app.command("eval")
def eval_cmd(
    data_dir: Path = typer.Option(..., exists=False, help="Dataset directory (evaluation-only)"),
):
    """Evaluate the model (stub for now)."""
    typer.echo(f"[stub] eval: data_dir={data_dir}")

# =========================================================
# OPTION B: ARCHITECTURE-ALIGNED DEV NAMESPACE
# =========================================================

dev_app = typer.Typer(help="Developer commands (architecture-aligned)")
app.add_typer(dev_app, name="dev")

# --- dev perception ---
perception_app = typer.Typer(help="Perception subsystem (stub)")
dev_app.add_typer(perception_app, name="perception")

@perception_app.command("detect")
def dev_perception_detect(
    image: Path = typer.Option(..., exists=False, help="Path to input image (stub)"),
):
    typer.echo(f"[stub] dev perception.detect: {image}")

# --- dev wardrobe ---
wardrobe_app = typer.Typer(help="Wardrobe subsystem (stub)")
dev_app.add_typer(wardrobe_app, name="wardrobe")

@wardrobe_app.command("list")
def dev_wardrobe_list():
    typer.echo("[stub] dev wardrobe.list")

@wardrobe_app.command("add")
def dev_wardrobe_add(
    kind: str = typer.Option(...),
    color: str = typer.Option(...),
    material: str = typer.Option("", help="optional"),
):
    typer.echo(f"[stub] dev wardrobe.add: kind={kind}, color={color}, material={material}")

@wardrobe_app.command("remove")
def dev_wardrobe_remove(
    item_id: str = typer.Option(...),
):
    typer.echo(f"[stub] dev wardrobe.remove: id={item_id}")

# --- dev scoring ---
scoring_app = typer.Typer(help="Scoring subsystem (stub)")
dev_app.add_typer(scoring_app, name="scoring")

@scoring_app.command("test")
def dev_scoring_test(
    context: str = typer.Option("university"),
):
    typer.echo(f"[stub] dev scoring.test: context={context}")

# --- dev learning ---
learning_app = typer.Typer(help="Learning subsystem (stub)")
dev_app.add_typer(learning_app, name="learning")

@learning_app.command("update")
def dev_learning_update(
    reward: int = typer.Option(..., help="1 like, 0 neutral, -1 dislike"),
):
    typer.echo(f"[stub] dev learning.update: reward={reward}")

def main():
    app()

if __name__ == "__main__":
    main()
